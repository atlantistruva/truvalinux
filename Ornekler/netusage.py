#!/usr/bin/env python

# REDHAT USERS PLEASE CHANGE 'python' ABOVE TO 'python2'

# Customise these parameters to your needs

# location of your sendmail binary
sendmail = "/usr/sbin/sendmail -t"

# your username
username = "atlantis"

# file to store usage data
usagefile = "/home/" + username + "/.netusage"

# day of the month when your billing cycle resets
myBillingDay = 11

# number of bytes traffic allowed each month
myMonthlyQuota = 10485760000

# ethernet interface to measure
myInterface = "eth0"

# END OF CUSTOMISATION SECTION
#
# ----------------------------------------------------

"""
Program to extract network usage from /proc/net/dev

Best to cron this prog to run once a day.

Each time it runs, it sends you an email letting you know
how much data you've used, and how much traffic you have
left for the month without incurring excess traffic charges.

"""


import re, os, time, commands, popen2

from pdb import set_trace as trace

class netUsage:

    IDX_TIME = 0
    IDX_RX = 1
    IDX_TX = 2
    IDX_RXTOTAL = 3
    IDX_TXTOTAL = 4

    def __init__(self, interface=myInterface):
        """
        """
        self.reWhite = re.compile("\\s+")
        self.interface = "eth0"
        self.usagefile = usagefile
        self.getAllData()
    
    def getRawNetUsage(self):
        """
        Determines total network traffic on a given interface,
        default eth0
        
        Returns as a tuple (rx, tx)
        """

        # grab the full bulk dump
        fd = file("/proc/net/dev")
        all = fd.readlines()
        fd.close()

        # find the line with the interface we're interested in
        # print all
        # return
        for line in all:
            # print line
            bits = line.strip().split(self.interface+":", 1)
            # print bits
            if bits and len(bits) == 2:
                # print bits
                fields = self.reWhite.split(bits[1].strip())
                # print fields
                rx = int(fields[0])
                tx = int(fields[8])
                return (rx, tx)

    def logUsageNow(self):
        rx, tx = self.getRawNetUsage()
        
        # fetch last inserted record
        numrows = len(self.data)
        if numrows > 0:
            row = self.data[-1]

        # compare present levels with previous
        if numrows == 0:

            # this is the first reading
            self.rxInc = 0
            self.rxTotal = rx
            self.txInc = 0
            self.txTotal = tx

        elif rx < row[self.IDX_RXTOTAL]:

            # we've rebooted since last time
            self.rxInc = self.rxTotal = rx
            self.txInc = self.txTotal = rx

        else:
            self.rxTotal, self.txTotal = rx, tx
            self.rxInc = rx - row[self.IDX_RXTOTAL]
            self.txInc = tx - row[self.IDX_TXTOTAL]

        row = (long(time.time()),
               self.rxInc,
               self.txInc,
               self.rxTotal,
               self.txTotal)

        # save to file
        fd = file(self.usagefile, "a")
        fd.write("%d %d %d %d %d\n" % row)
        fd.close()
        self.data.append(row)

    def getAllData(self):
        """
        Returns a bulk table of all data
        
        Returned as a list of tuples (datesecs, rx, tx)
        """
        try:
            fd = file(self.usagefile)
            all = fd.readlines()
            fd.close()
            self.data = []
            for line in all:
                fields = self.reWhite.split(line.strip())
                row = [long(field) for field in fields]
                self.data.append(row)
        except:
            print "Creating new usage data file"
            fd = file(self.usagefile, "w")
            fd.close()
            self.data = []

    def getClosestToSecs(self, numsecs):
        """
        Returns the index in the database table whose date is closest to numsecs

        Arguments:
        - rows (returned by getAllData)
        - numsecs (the desired date)
        """
        minrow = 0
        maxrow = len(self.data) - 1

        while minrow <= maxrow:
            #trace()
            guess = (minrow + maxrow) / 2
            #print "min=%d guess=%d max=%d" % (minrow, guess, maxrow)
            guesstime = self.data[guess][self.IDX_TIME]
            #print "guesstime=%d, wanted=%d" % (guesstime, numsecs)
            if minrow == maxrow - 1:
                if abs(self.data[minrow][self.IDX_TIME] - guesstime) \
                       < abs(self.data[minrow][self.IDX_TIME] - guesstime):
                    return minrow
                else:
                    return maxrow
            if guesstime < numsecs:
                # too early
                minrow = guess
            elif guesstime > numsecs:
                # too late
                maxrow = guess
            else:
                return guess
        return guess

    def getUsageForSecsRange(self, fromDate, toDate=None):
        """
        Hits the database and returns the usage between fromdate and todate
        
        fromdate and todate are in unix-format (seconds since epoch)

        Returns:
        tuple - rx, tx
        """
        #print "getUsageForSecsRange: calculating usage between %d and %d" % (fromDate, toDate)
        if toDate == None:
            toDate = long(time.time())
        fromIdx = self.getClosestToSecs(fromDate)
        toIdx = self.getClosestToSecs(toDate)
        #print "fromIdx=%d, toIdx=%d" % (fromIdx, toIdx)
        i = fromIdx
        rxTotal = txTotal = 0
        while i < toIdx:
            rxTotal += self.data[i][self.IDX_RX]
            txTotal += self.data[i][self.IDX_TX]
            i += 1
        return rxTotal, txTotal

    def parseDate(self, date):
        """
        Converts a date string in the form "yyyymmdd" into seconds since epoch
        """
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        secs = long(time.mktime((year, month, day, 0, 0, 0, 0, 0, 0)))
        # print "parseDate: secs=%d" % secs
        return secs

    def getUsageForDateRange(self, fromDate, toDate):
        return self.getUsageForSecsRange(
            self.parseDate(fromDate),
            self.parseDate(toDate))

    def parseDateTime(self, date):
        """
        Converts a date/time string in the form "yyyymmddhhmmss"
        into seconds since epoch
        """
        # print "parseDateTime: parsing %s" % date
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        hour = int(date[8:10])
        minute = int(date[10:12])
        secs = int(date[12:14])
        abssecs = long(time.mktime((year, month, day, hour, minute, secs, 0, 0, 0)))
        # print "abssecs=%d" % abssecs
        return abssecs

    def getUsageForRange(self, fromTime, toTime):
        return self.getUsageForSecsRange(
            self.parseDateTime(fromTime),
            self.parseDateTime(toTime))
        
    def numSecs(self, year, month, day, hour=0, min=0, sec=0):
        return time.mktime(year, month, day, hour, min, sec, 0, 0, 0)

    def reportUsageThisMonth(self, billingDay=None, quota=None):
        if len(self.data) == 0:
            return

        if billingDay == None:
            billingDay = myBillingDay
        if quota == None:
            quota = myMonthlyQuota
        now = time.localtime()
        nowSecs = time.time()
        billingDaySecs = (now[0], now[1], billingDay, now[3], now[4], now[5], now[6], now[7], now[8])

        fromYear = toYear = now[0]
        fromMonth = toMonth = now[1]

        if nowSecs > billingDaySecs:
            toMonth += 1
            if toMonth > 12:
                toMonth = 1
                toYear += 1
        else:
            fromMonth =- 1
            if fromMonth <= 0:
                fromMonth = 12
                fromYear -= 1
        fromSecs = time.mktime((fromYear, fromMonth, billingDay, 0, 0, 0, 0, 0, 0))
        toSecs = time.mktime((toYear, toMonth, billingDay, 0, 0, 0, 0, 0, 0))

        rx, tx = self.getUsageForSecsRange(fromSecs, toSecs)
        total = float(rx + tx)
        remaining = float(quota) - total

        propleft = remaining/float(quota)
        #print "propleft = %f" % propleft
        if propleft < 0.04:
            exclamation = "SHIT!!!!! "
        if propleft < 0.1:
            exclamation = "YIKES!! "
        elif propleft < 0.25:
            exclamation = "WARNING: "
        elif propleft < 0.4:
            exclamation = "Take care: "
        else:
            exclamation = ""

        toAddr = username + "@localhost"
        fromAddr = "netusage daemon <netusage@localhost>"
        if total > quota:
            subj = "EMERGENCY - YOU'VE MAXED OUT YOUR TRAFFIC!!!!"
        else:
            subj = "%s%.2f MB left in your monthly quota" % (
                exclamation, (float(quota) - float(total))/1048576.0)
        body = ("Downstream: %.2f MB\n"
               +"Upstream: %.2f\n"
               +"Total: %.2f MB\n"
               +"Quota: %.2f MB\n"
               +"Remaining %.2f MB") % (
            float(rx)/1048576.0,
            float(tx)/1048576.0,
            float(total)/1048576.0,
            float(quota)/1048576.0,
            (float(quota)-float(total))/1048576.0)
        cmd = "To: %s\nFrom: %s\nSender: %s\nSubject: %s\n\n%s\n" % (
            toAddr, fromAddr, fromAddr, subj, body)
        #print cmd
        fdOut, fdIn = popen2.popen2(sendmail)
        fdIn.write(cmd)
        fdIn.close()

def main():
    usageObj = netUsage()
    usageObj.logUsageNow()
    usageObj.reportUsageThisMonth()

if __name__ == '__main__':
    main()

