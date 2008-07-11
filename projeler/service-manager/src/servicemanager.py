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
# add module path...
sys.path.append("screens/")

from PyQt4 import QtGui, QtCore
from ui_mainWindow import Ui_MainWindow

import service

if os.getuid() != 0:
	print "Servis yöneticisi root olarak çalıştırılmalıdır!"
	sys.exit()

class mainWindow(Ui_MainWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		# Slots/signals.. connections...
		self.connect(self.actionExit, QtCore.SIGNAL("triggered(bool)"), app.exit)
		self.connect(self.actionAbout, QtCore.SIGNAL("triggered(bool)"), self.about)

		self.connect(self.startButton, QtCore.SIGNAL("clicked(bool)"), self.startService)
		self.connect(self.stopButton, QtCore.SIGNAL("clicked(bool)"), self.stopService)
		self.connect(self.onButton, QtCore.SIGNAL("clicked(bool)"), self.onService)
		self.connect(self.offButton, QtCore.SIGNAL("clicked(bool)"), self.offService)

		# set position...
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
        	self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

		self.writeList()

	def writeList(self):
		self.listServices.clear()
		for i in service.listServices():
			if i[0:3] == "rc.":
				serviceName = i[3:]
				if service.isRun(serviceName):
					runResult = u"Çalışıyor"
				else:
					runResult = u"Çalışmıyor"

				file = QtCore.QFileInfo(service.servicesPath + i)
				if file.isExecutable():
					fileResult = u"Evet"
				else:
					fileResult = u"Hayır"

				serviceList = QtCore.QStringList()
				serviceList.append(serviceName)
				serviceList.append(runResult)
				serviceList.append(fileResult)
		
				treeItem = QtGui.QTreeWidgetItem(serviceList)
				self.listServices.addTopLevelItem(treeItem)

	def startService(self):
		name = str(self.listServices.selectedItems()[0].text(0))
		service.start(name)
		self.writeList()

	def stopService(self):
		name = str(self.listServices.selectedItems()[0].text(0))
		service.stop(name)
		self.writeList()

	def onService(self):
		name = str(self.listServices.selectedItems()[0].text(0))
		service.on(name)
		self.writeList()

	def offService(self):
		name = str(self.listServices.selectedItems()[0].text(0))
		service.off(name)
		self.writeList()

	def about(self):
		print "..."
		QtGui.QMessageBox.about(self, u"Servis Yöneticisi Hakkında", u"Truva Servis Yöneticisi\nCopyright (C) 2008, Truva Linux")

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()