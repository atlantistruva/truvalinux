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

class tayFile:
	def __init__(self, tmpname):
		self.tmpPath = "/tmp/package-" + tmpname

	def deCompressPackage(self, file, path):
		""" decompress tay package. """
		try:
			tar = tarfile.open(file, "r")
		except:
			print "Dosya (%s) bulunamadı." % file
			sys.exit()
		tar.extractall(path)
		tar.close()
	
	def compressPackage(self, fileName, files, path):
		""" compress tay package. """
		tar = tarfile.open(path + fileName + ".tay", "w")
		for file in files:
			tar.add(file)
		tar.close()

class build(tayFile):
	def __init__(self, package):
		self.package = package
		tayFile.__init__(self, self.package)

	def buildPackage(self):
		files = []
		cwd = os.getcwd()
		os.chdir(self.tmpPath)
		for file in os.listdir(self.tmpPath):
			files.append("%s" % file)

		self.compressPackage(self.package, files, cwd + "/")
		print "Paket oluşturuldu!"
		os.chdir(cwd)