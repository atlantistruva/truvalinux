#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os,re

# service [ServiceName] [Command]

params = sys.argv
servdir= '/etc/init.d'
explst = ['start','stop']
service= {'name':params[1],'cmd':params[2]}

if service['cmd'] not in explst:
    print "Command not found"
    sys.exit()

def status(sname):
    sres = os.popen('ps -e|grep -c '+sname+'$').readline()
    return sres.replace("\n","")

def run(sname,scmd):
    os.system("/etc/init.d/"+sname+' '+scmd)

stat = status(service['name'])
if stat == "0":
    print "Service not running"
    run(service['name'],service['cmd'])
else:
    print "Service running"
