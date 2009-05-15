# -*- coding: utf-8 -*-
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
import os

import taypackage

def help():
	print "kullanım: tay (komut) [paket]"
	print \
	"""
	Komutlar:
	install (it) <paket> verilen paketi kurar.
	remove (rm) <paket> verilen paketi siler.
	reinstall (re) verilen paketi tekrar kurar.
	"""
	

if len(sys.argv) < 2:
	help()
	sys.exit()

if len(sys.argv) < 3:
	if sys.argv[1] in ("--help", "-h"):
		help()
		sys.exit()

	print "Hatalı kullanım!"
	help()
	sys.exit()

command = sys.argv[1]
package = sys.argv[2]

if command in ("install", "it"):
	package = taypackage.package(package)
	package.installPackage()

if command in ("remove", "rm"):
	package = taypackage.package(package + ".tay")
	package.removePackage()

if command in ("reinstall", "re"):
	package = taypackage.package(package + ".tay")
	package.removePackage()
	package.installPackage()