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
import re
import sys
# add module path...
sys.path.append("ui")

from ui_mainWindow import Ui_MainWindow

from PyQt4 import QtCore, QtGui

if os.getuid() != 0:
	print "Grub yöneticisi root olarak çalıştırılmalıdır!"
	sys.exit()

class mainWindow(Ui_MainWindow, QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		# set position...
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
        	self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

		# slots/singals connections...
		QtCore.QObject.connect(self.addButton, QtCore.SIGNAL("clicked(bool)"), self.newEntry)
		QtCore.QObject.connect(self.listEntrys, QtCore.SIGNAL("itemSelectionChanged()"), self.linesWrite)
		QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL("clicked(bool)"), self.deleteEntry)
		QtCore.QObject.connect(self.upButton, QtCore.SIGNAL("clicked(bool)"), self.upEntry)
		QtCore.QObject.connect(self.downButton, QtCore.SIGNAL("clicked(bool)"), self.downEntry)
		QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL("clicked(bool)"), self.clearLines)
		QtCore.QObject.connect(self.kernelOpenButton, QtCore.SIGNAL("clicked(bool)"), self.kernelOpen)

		QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered(bool)"), app.exit)
		QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL("triggered(bool)"), self.about)

		self.grubPath = "/boot/grub/menu.lst"

		# add entrys to listEntrys..
		self.writeList()

	def writeList(self):
		self.listEntrys.clear()

		self.grubConf = open(self.grubPath).read()
		self.titles = re.compile("title.*\n.*\n.*\n.*").findall(self.grubConf)

		for i in self.titles:
			title = re.compile("title.*\t\t(.*)").findall(i)[0]
			root = re.compile("root.*\t\t(.*)").findall(i)[0]
			kernel = re.compile("kernel.*\t\t(.*) root").findall(i)[0]
			mountpoint = re.compile("kernel.*\t\t.*root=(.*) ro").findall(i)[0]

			grubList = QtCore.QStringList()
			grubList.append(title)
			grubList.append(root)
			grubList.append(kernel)
			grubList.append(mountpoint)

			treeItem = QtGui.QTreeWidgetItem(grubList)
			self.listEntrys.addTopLevelItem(treeItem)

	def newEntry(self):
		# prepare new entry codes...
		global entryText_, entryText
		entryText_ = "title\t\t%s\nroot\t\t%s\nkernel\t\t%s root=%s ro\nsavedefault\nboot"
		entryText = entryText_ % (self.nameLine.text(), self.discLine.text(), self.kernelLine.text(), self.mountLine.text())

		try:
			title = str(self.listEntrys.selectedItems()[0].text(0))
			selectIf = True
		except:
			selectIf = False
		# control input entry name and selected entry name
		if selectIf:
			grubFile = open(self.grubPath).read()
			writeGrubFile = open(self.grubPath, "w")

			if self.nameLine.text() == title:
				findTitle = re.compile("title.*%s\n.*\n.*\n.*\n.*" % title).findall(grubFile)[0]
	
				writeGrubFile.write(grubFile.replace(findTitle, entryText))
	
				writeGrubFile.close()
			else:
				writeGrubFile.write(grubFile + "\n" + entryText)
				writeGrubFile.close()
		# if not select anything...
		else:
			# control given title in grubFile
			grubFile = open(self.grubPath).read()
			if "title\t\t%s\n" % str(self.nameLine.text()) not in grubFile:
				writeGrubFile = open(self.grubPath, "w")
				writeGrubFile.write(grubFile + "\n" + entryText)
				writeGrubFile.close()

		self.writeList()
		self.clearLines()

	def linesWrite(self):
		try:
			title = str(self.listEntrys.selectedItems()[0].text(0))
			root = str(self.listEntrys.selectedItems()[0].text(1))
			kernel = str(self.listEntrys.selectedItems()[0].text(2))
			mountpoint = str(self.listEntrys.selectedItems()[0].text(3))

			# write to lines...
			self.nameLine.setText(title)
			self.discLine.setText(root)
			self.kernelLine.setText(kernel)
			self.mountLine.setText(mountpoint)
		except:
			pass

	def deleteEntry(self):
		title = str(self.listEntrys.selectedItems()[0].text(0))
		grubFile = open(self.grubPath).read()
		findTitle = re.compile("title.*%s\n.*\n.*\n.*\n.*" % title).findall(grubFile)[0]

		writeGrubFile = open(self.grubPath, "w")
		writeGrubFile.write(grubFile.replace(findTitle, ""))
		writeGrubFile.close()

		self.writeList()
		self.clearLines()

	def upEntry(self):
		title = str(self.listEntrys.selectedItems()[0].text(0))
		title = title.replace("(", "\(").replace(")", "\)")
		grubFile = open(self.grubPath).read()
		findTitle = re.compile("title.*%s\n.*\n.*\n.*\n.*" % title).findall(grubFile)[0]
		doubleTitle = re.compile("title.*\n.*\n.*\n.*\n.*\n*?" + findTitle.replace("(", "\(").replace(")", "\)")).findall(grubFile)[0]

		willEditTitle_up = re.compile("title.*\n.*\n.*\n.*\n.*").findall(doubleTitle)[0]
		grubFile = grubFile.replace(willEditTitle_up, "willdown").replace(findTitle, "willup")

		grubFile = grubFile.replace("willdown", findTitle).replace("willup", willEditTitle_up)

		writeGrubFile = open(self.grubPath, "w")
		writeGrubFile.write(grubFile)
		writeGrubFile.close()

		self.writeList()

	def downEntry(self):
		title = str(self.listEntrys.selectedItems()[0].text(0))
		title = title.replace("(", "\(").replace(")", "\)")
		grubFile = open(self.grubPath).read()
		findTitle = re.compile("title.*%s\n.*\n.*\n.*\n.*" % title).findall(grubFile)[0]
		print findTitle
		doubleTitle = re.compile(findTitle.replace("(", "\(").replace(")", "\)") + "\n*?title.*\n.*\n.*\n.*\n.*").findall(grubFile)[0]

		willEditTitle_down = re.compile("title.*\n.*\n.*\n.*\n.*").findall(doubleTitle)[1]
		grubFile = grubFile.replace(willEditTitle_down, "willup").replace(findTitle, "willdown")

		grubFile = grubFile.replace("willup", findTitle).replace("willdown", willEditTitle_down)
		writeGrubFile = open(self.grubPath, "w")
		writeGrubFile.write(grubFile)
		writeGrubFile.close()

		self.writeList()

	def clearLines(self):
		self.nameLine.clear()
		self.discLine.clear()
		self.kernelLine.clear()
		self.mountLine.clear()

	def kernelOpen(self):
		kernelFile = QtGui.QFileDialog.getOpenFileName(self, u"Kernel dosyasını seçin..", "/boot/", ("Dosyalar (*)"))
		self.kernelLine.setText(str(kernelFile))

	def about(self):
		QtGui.QMessageBox.about(self, u"Grub Yöneticisi Hakkında", u"Truva Grub Yöneticisi\nCopyright (C) 2008, Truva Linux")

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()