#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : Onur Yerlikaya <onur.yerlikaya@linux.org.tr>

# this file is under construction
# file status = alpha!
import sys,os,re

args   = sys.argv
if len(args) < 3:
    print """
        Usage
            service [ServiceName] {start|stop|status}
    """
    sys.exit()

servdir= '/etc/init.d/'
explst = ['start','stop','status']
service= {'name':args[1],'cmd':args[2]}
if service['cmd'] not in explst:
    print "Command not found"
    sys.exit()

def status(sname):
    sres = os.popen('ps -e|grep -c '+sname+'$').readline()
    return sres.replace("\n","")

def run(sname,scmd):
    if os.path.exists(servdir+sname):
        os.system(servdir+sname+' '+scmd)
    else:
        print "Service Not found!"


stat = status(service['name'])

if service['cmd'] == "start":
    if stat == "0":
        run(service['name'],service['cmd'])
    else:
        print "Service already running"
elif service['cmd'] == "stop":
    if stat == "1":
        run(service['name'],service['cmd'])
    else:
        print "Service already not working"
elif service['cmd'] == "status":
    if stat == "0":
        print "Service not running"
    else:
        print "Service running"
