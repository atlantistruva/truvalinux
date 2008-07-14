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

import os
import sys
import tarfile
from distutils import dir_util

import tayfile
import taydb

class package:
	def __init__(self, package):
		self.package = package
		self.packageName = package[0:-4]
		self.packageTmp = "/tmp/install-" + self.packageName
		try: os.mkdir(self.packageTmp)
		except: pass

	def installPackage(self):
		print "%s paketi kuruluyor..." % self.packageName
		tayFile = tayfile.tayFile(self.packageName)
	
		tayFile.deCompressPackage(self.package, self.packageTmp)
		print self.installDesc()
		dir_util.remove_tree("%s/install-tay" % self.packageTmp)

		files = dir_util.copy_tree(self.packageTmp, "/")

		# this package add packages db
		taydb.addPackage(self.packageName, files)
		dir_util.remove_tree(self.packageTmp)

		print "Paket kuruldu!"

	def removePackage(self):
		if self.packageName not in taydb.db.keys():
			print "%s paketi zaten kurulu değil!" % self.packageName
			sys.exit()

		memberFiles = taydb.db[self.packageName]

		print "Paket shelveden siliniyor."
		taydb.removePackage(self.packageName)

		# remove package
		for file in memberFiles:
			print "Siliniyor: " + file
			if os.path.isfile(file):
				os.remove(file)
			else:
				dir_util.remove_tree(file)

		print "\n Paket (%s) silindi." % self.packageName

	def installDesc(self):
		desc = open("%s/install-tay/tay-desc" % self.packageTmp).read()
		return "\nPaket açıklaması:\n" + desc