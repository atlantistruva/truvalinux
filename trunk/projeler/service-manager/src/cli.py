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

import sys
import service

def help():
	print "Kullanım: service [servisadı] (start, stop, on, off)"

try: sys.argv[1]
except: help(); sys.exit()

command = sys.argv[1]

if command  == "--help" or command == "-h":
	help()
	sys.exit()

try:
	name = sys.argv[1]
	command = sys.argv[2]

	if command == "start":
		service.start(name)
	elif command == "stop":
		service.stop(name)
	elif command == "on":
		service.on(name)
	elif command == "off":
		service.off(name)
	else:
		print "Hatalı kullanım!"
		help()
except:
	print "Hatalı kullanım!"
	help()