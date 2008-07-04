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

from PyQt4 import QtCore, QtGui
import sys
import os
from glob import glob
import anatolyaglobals as glbs
from Xlib import display

# add module paths
sys.path.append("screens/")

# import screens
from ui_mainWindow import Ui_StarterWindow
from ui_mouseWindow import Ui_MouseWindow
from ui_wallpaperWindow import Ui_WallpaperWindow
from ui_networkWindow import Ui_NetworkWindow
from ui_endWindow import Ui_EndWindow

class mainWindow(Ui_StarterWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowno = 0

		# set screen position
		exec(glbs.defaultposition)

		# Signals / slots connection
		exec(glbs.defaultsignals)

	def nextWindow(self):
		windowname = glbs.allwindows[self.windowno + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def backWindow(self):
		pass

class mouseWindow(Ui_MouseWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowno = 1

		# set screen position
		exec(glbs.defaultposition)

		# Signals / slots connection
		exec(glbs.defaultsignals)

	def setMouse(self):
		if self.leftMouseSelection.isChecked():
			mouseSelect = "left"
		else:
			mouseSelect = "right"

		mouseMap = display.Display().get_pointer_mapping()
		lenButtons = len(mouseMap)

		# set mouse points...
		if lenButtons == 1:
			mouseMap[0] = 1
		elif lenButtons == 2:
			if mouseSelect == "right":
				mouseMap[0] = 1
				mouseMap[0] = 3
			else:
				mouseMap[1] = 3
				mouseMap[1] = 1
		else:
			if mouseSelect == "right":
				mouseMap[0] = 1
				mouseMap[2] = 3
			else:
				mouseMap[0] = 3
				mouseMap[2] = 1
			if lenButtons >= 5:
				pos = 0
				for pos in range(lenButtons):
					if mouseMap[pos] == 4 or mouseMap[pos] == 5:
						break
				if pos < lenButtons - 1:
					mouseMap[pos] = 4
					mouseMap[pos + 1] = 5

		display.Display().set_pointer_mapping(mouseMap)

		if self.singleClickSelection.isChecked():
			clickselection = "SingleClick"
		else:
			clickselection = "DoubleClick"

		# run mouse config...
		if self.rightMouseSelection.isChecked():
			os.system("python kdeconfig_mouse.py RightHanded %s" % clickselection)
		else:
			os.system("python kdeconfig_mouse.py LeftHanded %s" % clickselection)

	def nextWindow(self):
		self.setMouse()
		windowname = glbs.allwindows[self.windowno + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def backWindow(self):
		windowname = glbs.allwindows[self.windowno - 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class wallpaperWindow(Ui_WallpaperWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowno = 2

		# set screen position
		exec(glbs.defaultposition)

		# Signals / slots connection
		exec(glbs.defaultsignals)

		# insert wallpapers to listWallpapers
		for i in os.listdir("/usr/share/wallpapers"):
			self.listWallpapers.addItem(i)

		# slots/singls connections...
		QtCore.QObject.connect(self.listWallpapers, QtCore.SIGNAL("itemSelectionChanged()"), self.showPicture)

	def nextWindow(self):
		self.setWallpaper()
		windowname = glbs.allwindows[self.windowno + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def backWindow(self):
		windowname = glbs.allwindows[self.windowno - 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def showPicture(self):
		# show picture in pictureLabel
		self.selectedPicture = str(self.listWallpapers.selectedItems()[0].text())
		picture_file = QtGui.QPixmap()
		picture_file.load("/usr/share/wallpapers/" + self.selectedPicture)
		self.pictureLabel.setPixmap(picture_file)

	def setWallpaper(self):
		os.system("python kdeconfig_wallpaper.py %s" % "/usr/share/wallpapers/" + self.selectedPicture)

class networkWindow(Ui_NetworkWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowno = 3

		# set screen position
		exec(glbs.defaultposition)

		# Signals / slots connection
		exec(glbs.defaultsignals)

		for iface in os.listdir("/sys/class/net/"):
			self.listIfaces.addItem(str(iface))

	def nextWindow(self):
		self.setNetwork()
		windowname = glbs.allwindows[self.windowno + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def backWindow(self):
		windowname = glbs.allwindows[self.windowno - 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

	def setNetwork(self):
		self.selectedItem = str(self.listIfaces.selectedItems()[0].text())
		os.system("/sbin/ifconfig %s up" % self.selectedItem)
		os.system("sh /etc/rc.d/rc.inet1")

class endWindow(Ui_EndWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowno = 4

		# set screen position
		exec(glbs.defaultposition)

		# Signals / slots connection
		exec(glbs.defaultsignals)

	def nextWindow(self):
		app.exit()

	def backWindow(self):
		windowname = glbs.allwindows[self.windowno - 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

if __name__ == "__main__":
	app = QtGui.QApplication([])
	mw = mainWindow()
	mw.show()
	app.exec_()