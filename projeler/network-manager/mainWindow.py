# -*- coding: utf-8 -*-
# Truva Linux network manager application
# Coded by rohanrhu

from PyQt4 import QtCore, QtGui
from ui_mainWindow import Ui_NetworkManager
from ui_wlanInfo import Ui_wirelessWindow
import network
import pywlan

class wlanInfoWindow(QtGui.QDialog, Ui_wirelessWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)

		# Signal / Slots
		QtCore.QObject.connect(self.listWireless, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.refresh_bar)

		# Show wlans in listWireless
		self.wireless = pywlan.Wireless("eth1")
		self.listWireless.setRowCount(len(self.wireless.scanning()))
		a = 0
		for i in self.wireless.scanning():
			HeaderItem = QtGui.QTableWidgetItem()
			HeaderItem.setText(i)
			self.listWireless.setVerticalHeaderItem(a, HeaderItem)

			# Wlan infos write to listWireless
			self.wireless_info = pywlan.wlanInfo("eth1", i)
			b = 0
			for it in [self.wireless_info.getEssid(), self.isCrypted("eth1", i), self.wireless_info.getQuality()]:
				item = QtGui.QTableWidgetItem()
				item.setText(str(it))
				self.listWireless.setItem(a, b, item)
				b += 1
			a += 1

	def refresh_bar(self):
		print "..."
		self.qualityBar.setValue(int(pywlan.wlanInfo("eth1", str(self.listWireless.selectedItems()[0].text())).getQuality()))

	def isCrypted(self, iface, wlan):
		if pywlan.wlanInfo(iface, wlan).isEncryption():
			return "Evet"
		else:
			return "Hayır"

			a += 1

class mainWindow(QtGui.QMainWindow, Ui_NetworkManager):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		QtCore.QObject.connect(self.newButton, QtCore.SIGNAL("clicked(bool)"), self.newConnect)
		QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL("clicked(bool)"), self.showInfo)

		self.wlanInfoWindow = wlanInfoWindow()

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

			# Write connecting info to listNetwroks
			b = 0
			for it in self.allifaces[i]:
				item = QtGui.QTableWidgetItem()
				item.setText(self.allifaces[i][b])
				self.listNetworks.setItem(a, b ,item)
				b += 1

			a += 1

	def showInfo(self):
		self.selecteditem = str(self.listNetworks.selectedItems()[0].text())
		self.wlanInfoWindow.show()

	def newConnect(self):
		self.newConnectWindow = newConnectDialog()
		self.newConnectWindow.show()

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()