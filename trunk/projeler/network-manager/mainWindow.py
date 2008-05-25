# -*- coding: utf-8 -*-
# Truva Linux network manager application
# Coded by rohanrhu

from PyQt4 import QtCore, QtGui
from ui_mainWindow import Ui_NetworkManager
from ui_newConnect import Ui_newDialogWindow
import network
import pywlan

class newConnectDialog(QtGui.QDialog, Ui_newDialogWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		for net in pywlan.listInterfaces():
			self.nifaceList.addItem(str(net))

class mainWindow(QtGui.QMainWindow, Ui_NetworkManager):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		QtCore.QObject.connect(self.newButton, QtCore.SIGNAL("clicked(bool)"), self.newConnect)
		QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL("clicked(bool)"), self.deneme)

		self.allifaces = network.Networking_Info().listIfaces()

		# List interfaces in listNetworks
		self.refresh()

	def refresh(self):
		self.listNetworks.setRowCount(len(self.allifaces))
		a = 0
		for i in self.allifaces.keys():
			headerItem = QtGui.QTableWidgetItem()
			headerItem.setText(i)
			self.listNetworks.setVerticalHeaderItem(a, headerItem)

			# Bağlantı bilgileri yazdırılıyor...
			b = 0
			for it in self.allifaces[i]:
				item = QtGui.QTableWidgetItem()
				item.setText(self.allifaces[i][b])
				self.listNetworks.setItem(a, b ,item)
				b += 1

			a += 1

	def deneme(self):
		print "..."

	def newConnect(self):
		self.newConnectWindow = newConnectDialog()
		self.newConnectWindow.show()

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()