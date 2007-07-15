#!/usr/bin/python

import sys,os

commands    	= ['start','stop']
args            = sys.argv
tmp_file        = 'tmp.sm'
service_dir	= "/etc/init.d/"

if len(args) < 3:
    print """
    Usage : 
        service {service_name} {start|stop}
    """
    sys.exit()
    
if args[2] not in commands:
    print " Command not found.."
    sys.exit()   
service = {'name':args[1],'param':args[2]}

if service['param'] == 'start':
    os.system('ps -e |grep '+service['name']+' > '+tmp_file)
    f = open(tmp_file)
    alldata = f.readlines()
    if len(alldata) == 0:
        os.system(service_dir+service['name']+' start')
        print service['name']+" is started"
    else:
        print  service['name'] +" is running"
    f.close()
elif service['param'] == 'stop':
    os.system('ps -e |grep '+service['name']+' > '+tmp_file)
    f = open(tmp_file)
    alldata = f.readlines()
    if len(alldata) == 0:
        print service['name']+" is already stopped."
    else:
         os.system(service_dir+service['name']+' stop')
         print service['name'] +" is stopped"
    f.close()
