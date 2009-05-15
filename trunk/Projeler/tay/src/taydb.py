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

import shelve

def opendb():
	global db
	db = shelve.open("/home/rohanrhu/python/truva/tay/tay.db")

opendb()

def addPackage(packageName, dirs):
	opendb()
	db[packageName] = dirs
	db.close()

def removePackage(packageName):
	opendb()
	del db[packageName]
	db.close()