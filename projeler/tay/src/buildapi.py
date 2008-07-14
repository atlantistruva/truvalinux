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
import urlgrabber
import urlgrabber.progress
import tarfile
import shutil
from glob import glob
from distutils import dir_util

import tayfile
import package

def setNames(packageName_, packageDesc_, packageAdress_):
	global packageName
	global packageDesc
	global packageAdress
	global tmp

	packageName = packageName_
	packageDesc = packageDesc_
	packageAdress = packageAdress_

	tmp = "/tmp/package-%s" % packageName

def setPackage():
	print "Dizinler yaratılıyor..."
	os.mkdir("/tmp/package-%s" % packageName)
	os.mkdir("/tmp/package-%s/install-tay" % packageName)
	descFile = open("/tmp/package-%s/install-tay/tay-desc" % packageName, "w")
	descFile.write(packageDesc)
	descFile.close()

def download():
	print "Arşiv indiriliyor..."
	prgs = urlgrabber.progress.text_progress_meter()
	cwd = os.getcwd()
	os.chdir("/tmp/package-%s" % packageName)
	urlgrabber.urlgrab(packageAdress, "packagearchive", progress_obj=prgs)
	os.chdir(cwd)

def extract():
	global file
	global dirFile
	
	tar = tarfile.open("%s/packagearchive" % tmp, "r")
	tar.extractall(tmp + "/archive")
	os.remove("%s/packagearchive" % tmp)

	dirFile = tmp + "/" + "archive"
	dirFile = glob("%s/*" % dirFile)[0]

def compileInst():
	print "Compiling package..."
	
	cwd = os.getcwd()
	os.chdir(dirFile)
	os.system("./configure")
	os.system("make")
	os.system("make install DESTDIR=%s" % tmp)
	os.chdir(cwd)
	dir_util.remove_tree(dirFile)

def shell(command):
	cwd = os.getcwd()
	os.chdir(dirFile)
	os.system(command)
	os.chdir(cwd)

def copy(file, path):
	# control path "/"
	if path[-1] == "/":
		path = path[0:-1]

	cwd = os.getcwd()
	
	os.chdir(dirFile)
	if os.path.isfile(file):
		try: os.mkdir("%s/%s" % (tmp, path))
		except: pass
		shutil.copy(dirFile + "/" + file, tmp + "/" + path)
		dir_util.remove_tree(tmp + "/" + "archive")
	else:
		try: os.mkdir("%s%s" % (tmp, path))
		except: pass
		dir_util.copy_tree(dirFile + "/" + file, tmp + "/" + path)
		dir_util.remove_tree(tmp + "/" + "archive")
	os.chdir(cwd)

def build():
	print "%s.tay paketi oluşturuluyor.." % packageName
	tay = tayfile.build(packageName)
	tay.buildPackage()
	dir_util.remove_tree(tmp)

# build example...
"""
desc = "python internet modülü\nurlgrabber ile dosya indirebilir ve daha pekçok şeyi yapabilirsiniz"
setNames("urlgrabber2", desc, "http://linux.duke.edu/projects/urlgrabber/download/urlgrabber-3.1.0.tar.gz")
setPackage()
download()
extract()
copy("urlgrabber", "/usr/lib/python2.5/site-packages")
build()"""