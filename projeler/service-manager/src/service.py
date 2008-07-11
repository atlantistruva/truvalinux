# -*- coding: utf-8 -*-
#
# Copyright (C) 2008, Truva Linux
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import sys

servicesPath = "/etc/rc.d/"

def isRun(name):
	result = os.popen("ps -e|grep -c %s" % name).read().replace("\n", "")

	if result != '0':
		return True
	else:
		return False

def listServices():
	return os.listdir(servicesPath)

def start(name):
	os.system("sh %src.%s start" % (servicesPath, name))

def stop(name):
	os.system("sh %src.%s stop" % (servicesPath, name))

def on(name):
	os.chmod("%src.%s" % (servicesPath, name), 0777)

def off(name):
	os.chmod("%src.%s" % (servicesPath, name), 777)