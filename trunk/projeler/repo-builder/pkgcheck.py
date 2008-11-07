#!/usr/bin/env python
PROGRAM = 'pkgcheck'
VERSION = '0.02'
# Purpose : check a Slackware package for correct structure
# License : GNU General Public License (http://www.gnu.org/copyleft/gpl.html))
#           Copyright (C) 2005 Patrick Useldinger, http://www.homepages.lu/pu/

import getopt, os, subprocess, sys, tarfile, warnings

LVL_NONE,LVL_INFO,LVL_WARN,LVL_ERR,LVL_KO=0,1,2,3,4
LVL_LIB=('','info','Warning','ERROR','*KO*')
OBJTYPE={'f':'file','d':'directory','s':'symlink','h':'hardlink','v':'device','?':'unknown object'}
ANYEXEC=tarfile.TUEXEC|tarfile.TGEXEC|tarfile.TOEXEC

warnings.filterwarnings(action='ignore',message='tempnam is a potential security risk to your program')
TMPFILE=os.tempnam(None,'%i-'%os.getpid())

class Messages(object):
    def __init__(self,minlevel):
        self.maxSeverity=LVL_NONE
        self.minlevel=minlevel
        self.filenames=[]
    def add(self,filename,severity,message):
        if severity >= self.minlevel:
            if filename not in self.filenames:
                self.filenames.append(filename)
                print filename
            print '  %-7s: %s' % (LVL_LIB[severity],message)
            if severity>self.maxSeverity:
                self.maxSeverity=severity


def check(filename,msg,listOnly):
    mustHave = { './'                      : ['d',LVL_ERR,0],
                 'install/doinst.sh'       : ['f',LVL_INFO,0],
                 'install/slack-desc'      : ['f',LVL_ERR,0],
                 'install/slack-required'  : ['f',LVL_INFO,0],
                 'install/slack-conflicts' : ['f',LVL_INFO,0],
                 'install/slack-suggests'  : ['f',LVL_INFO,0]}
    directories = {}
    basename=os.path.basename(filename)
    nvab,ext=os.path.splitext(basename)
    if ext != '.tgz':
        msg.add(filename,LVL_ERR,'filename does not end in .tgz but in %s'%ext)   
    nvabSplit=nvab.rsplit('-',3)
    if len(nvabSplit) != 4:
        msg.add(filename,LVL_KO,'filename does not respect name-version-arch-build structure')
        return
    name,version,arch,build=nvabSplit
    if arch == 'i386':
        msg.add(filename,LVL_INFO,'obsolete architecture %s'%arch)  
    elif arch not in ('noarch','i486','i586','i686','x86_64','s390'):
        msg.add(filename,LVL_WARN,'unknown architecture %s'%arch)
    size=os.stat(filename).st_size
    if size > 5000000:
        msg.add(filename,LVL_INFO,'file too large to be hosted by linuxpackages.net (%i)'%size)
    mustHave['usr/doc/%s-%s/'%(name,version)]        =['d',LVL_INFO,0]
    mustHave['usr/doc/%s-%s/README'%(name,version)]  =['f',LVL_INFO,0]
    mustHave['usr/doc/%s-%s/COPYING'%(name,version)] =['f',LVL_INFO,0]
    try:
        tf=tarfile.open(filename,'r:gz')
    except:
        msg.add(filename,LVL_KO,'cannot open file')
        return
    try:
        if listOnly:
            tf.list()
            tf.close()
            return
        for ti in tf:
            if ti.isfile():
                objType='f'
            elif ti.isdir():
                objType='d'
            elif ti.issym():
                objType='s'
            elif ti.islnk():
                objType='h'
            elif ti.isdev():
                objType='v'
            else:
                objType='?'
            objDesc=OBJTYPE[objType]
            mode=ti.mode % 010000
            if not(ti.name.startswith('dev/')):
                if mode & tarfile.TSUID == tarfile.TSUID:
                    msg.add(filename,LVL_WARN,'%s "%s" has SUID (%i,%s) bit set'%(objDesc,ti.name,ti.uid,ti.uname))
                if mode & tarfile.TSUID == tarfile.TSGID:
                    msg.add(filename,LVL_WARN,'%s "%s" has SGID (%i,%s) bit set'%(objDesc,ti.name,ti.gid,ti.gname))
                if mode & tarfile.TSUID == tarfile.TSVTX:
                    msg.add(filename,LVL_WARN,'%s "%s" has sticky bit set'%(objDesc,ti.name))
                if mode & tarfile.TGWRITE == tarfile.TGWRITE:
                    msg.add(filename,LVL_WARN,'%s "%s" is writeable by group'%(objDesc,ti.name))
                if mode & tarfile.TOWRITE == tarfile.TOWRITE:
                    msg.add(filename,LVL_WARN,'%s "%s" is writeable by other'%(objDesc,ti.name))
            modestring=tarfile.filemode(mode % 01000)
            permsOK=True
            for i in (1,2,3,4,5,6):
                j=i+3
                if not(modestring[j]=='-' or modestring[i] == modestring[j]):
                    permsOK=False
            if not permsOK:
                msg.add(filename,LVL_WARN,'%s "%s" has illogical mode %s'%(objDesc,ti.name,modestring))
            if (ti.name in mustHave) and (objType in mustHave[ti.name][0]):
                mustHave[ti.name][2]+=1
            if ti.name.startswith('usr/local'):
                msg.add(filename,LVL_WARN,'%s "%s" refers to a "local" directory' %(objDesc,ti.name))
            if (ti.uid,ti.uname)!=(0,'root'):
                msg.add(filename,LVL_WARN,'%s "%s" has user (%i,%s) instead of (0,root)' \
                        %(objDesc,ti.name,ti.uid,ti.uname))
            if ti.name.startswith('bin/') or ti.name.startswith('sbin/') \
               or ti.name.startswith('usr/bin/') or ti.name.startswith('usr/sbin/') \
               or ti.name.startswith('usr/local/bin/') or ti.name.startswith('usr/local/sbin/') \
               or ti.name.startswith('usr/X11R6/bin/'):
                if (ti.gid,ti.gname)!=(1,'bin'):
                    msg.add(filename,LVL_WARN,'%s "%s" has group (%i,%s) instead of (1,bin)' \
                            %(objDesc,ti.name,ti.gid,ti.gname))
            elif ti.name.startswith('dev/'):
                pass
            else:
                if (ti.gid,ti.gname)!=(0,'root'):
                    msg.add(filename,LVL_WARN,'%s "%s" has group (%i,%s) instead of (0,root)' \
                            %(objDesc,ti.name,ti.gid,ti.gname))                
            if objType=='d':
                if ti.name in directories:
                    msg.add(filename,LVL_ERR,'duplicate directory "%s"' %ti.name)
                else:
                    directories[ti.name]=0
                checkParent='%s/'%os.path.dirname(ti.name[:-1])
            else:
                dirname=os.path.dirname(ti.name)
                checkParent='%s/'%dirname
                if ti.issym():
                    msg.add(filename,LVL_INFO,'symlink "%s"' %ti.name)
                if dirname[:-1].endswith('/man/man'):
                    category=dirname[-1]
                    if not(ti.name.endswith('.gz')):
                        msg.add(filename,LVL_INFO,'man file %s is not zipped'%ti.name)
                    else:
                        if not (ti.name[:-3].rsplit('.',1)[-1].startswith(category)):
                            msg.add(filename,LVL_WARN,'wrong man file name %s'%ti.name)                            
                if dirname[:-1].endswith('/info'):
                    category=dirname[-1]
                    if not(ti.name.endswith('.gz')):
                        msg.add(filename,LVL_INFO,'info file %s is not zipped'%ti.name)
                if ti.name=='install/slack-desc':
                    slackdesc=tf.extractfile(ti.name).readlines()
                    lines=0
                    longlines=0
                    maxLen=len(name)+72+1 # 1 for trailing \n
                    for line in slackdesc:
                        if line.startswith('%s:\n'% name):
                            lines+=1                            
                        elif line.startswith('%s: '% name):
                            lines+=1
                            if len(line)>maxLen:
                                longlines+=1
                    if lines!=11:
                        msg.add(filename,LVL_WARN,'%s has %i lines instead of 11'%(ti.name,lines))
                    if longlines>0:
                        msg.add(filename,LVL_WARN,'%s has %i lines that are too long'%(ti.name,longlines))
                if ti.isfile and (ti.mode & ANYEXEC):
                    tf._extract_member(ti,TMPFILE)
                    try:
                        output = subprocess.Popen(['/usr/bin/file', TMPFILE], stdout=subprocess.PIPE).communicate()[0]
                        if ('executable' in output or 'shared object' in output) \
                           and ('ELF' in output) and ('not stripped' in output):
                            msg.add(filename,LVL_INFO,'%s is not stripped'%ti.name)                           
                    finally:
                        os.remove(TMPFILE)
            if checkParent != '/':
                if checkParent not in directories:
                    msg.add(filename,LVL_ERR,'%s "%s" without corresponding parent "%s"' %(objDesc,ti.name,checkParent))
                else:
                    directories[checkParent]+=1
    finally:
        tf.close()
    mhKeys=mustHave.keys()
    mhKeys.sort()
    for key in mhKeys:
        if mustHave[key][2]==0:
            msg.add(filename,mustHave[key][1],'missing %s "%s"'%(OBJTYPE[mustHave[key][0][0]],key))
    dirKeys=directories.keys()
    dirKeys.sort()
    for key in dirKeys:
        if key != './':
            if directories[key]==0:
                msg.add(filename,LVL_INFO,'empty directory "%s"'%key)
       
def usage():
    print >> sys.stderr, '%s version %s' % (PROGRAM,VERSION)
    print >> sys.stderr, 'usage: %s [options] <package1> [<package2> ...]' % os.path.basename(sys.argv[0])
    print >> sys.stderr, '       options:'
    print >> sys.stderr, '                            -e  specify minumum level 1=info, 2=warning'
    print >> sys.stderr, '                    --help, -h  print this'
    print >> sys.stderr, '                            -l  list contents only'
    sys.exit(1)
           
if __name__ == '__main__':
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:],'he:l',['help'])
    except getopt.GetoptError:
        usage()
    if len(args)==0:
        usage()
    minlevel=LVL_NONE
    listOnly=False
    for o,a in opts:
        if o == '-e'               : minlevel=int(a)
        if o in ('-h','--help')    : usage()
        if o == '-l'               : listOnly=True
    msg=Messages(minlevel)
    for package in args:
        check(package,msg,listOnly)
    if msg.maxSeverity != 0:
        print 'rc=%i (%s)' % (msg.maxSeverity,LVL_LIB[msg.maxSeverity])
    sys.exit(msg.maxSeverity)
    
