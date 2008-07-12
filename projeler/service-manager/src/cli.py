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
import os

if os.getuid() != 0:
	print "Servis yöneticisi root olarak çalıştırılmalıdır!"
	sys.exit()

def help():
	print "Kullanım: service [servisadı] (start, stop, on, off)"
	print "Kullanım: service (--list, -l) (--help, -h)"

if len(sys.argv) < 2:
	help()
	sys.exit()

command = sys.argv[1]

if command  == "--help" or command == "-h":
	help()
	sys.exit()

if command == "--list" or command == "-l":
	services = service.listServices()

	print "|        Servis        |        Durum        |"
	for i in services:
		name = i[3:]
		if service.isRun(name):
			result = "Çalışıyor"
		else:
			result = "Çalışmıyor"

		print " " + name + " " * (24 - len(name)) + result

	sys.exit()

if len(sys.argv) == 3:
	name = sys.argv[1]
	command = sys.argv[2]

	if command == "start":
		service.start(name)
	elif command == "stop":
		service.stop(name)
	elif command == "on":
		service.on(name)
		print "'%s' servisi açılışta başlatılacak." % name
	elif command == "off":
		service.off(name)
		print "'%s' servisi açılışta başlatımlayacak." % name
	else:
		print "Hatalı kullanım!"
		help()
else:
	print "Hatalı kullanım!"
	help()