# -*- coding: utf-8 -*-
# Authors: Oğuzhan Eroğlu <oguzhan@oguzhaneroglu.com>
 # Copyright (C) Truva Developers
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.

from PyQt4 import QtCore, QtGui
from ui_mainWindow import Ui_NetworkManager
from ui_wlanInfo import Ui_wirelessWindow
from ui_getPasswd import Ui_passwdWindow
import network
import pywlan
import thread

class getPasswordWindow(QtGui.QDialog, Ui_passwdWindow):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)

class wlanInfoWindow(QtGui.QDialog, Ui_wirelessWindow):
	def __init__(self, iface):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.iface = iface

		# Signal / Slots
		QtCore.QObject.connect(self.listWireless, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.refresh_bar)
		QtCore.QObject.connect(self.scanWirelessButton, QtCore.SIGNAL("clicked(bool)"), self.refreshwlan)
		QtCore.QObject.connect(self.connectWirelessButton, QtCore.SIGNAL("clicked(bool)"), self.connectWireless)

		self.wireless = pywlan.Wireless(self.iface)

		# Show wlans in listWireless and write connected network
		try:
			thread.start_new(self.refreshwlan, ())
			self.refreshConnectedWlan()
		except:
			pass

	def refreshwlan(self):
		self.statusLabel.setText(u"Ağlar taranıyor...")
		scanresult = self.wireless.scanning()
		self.listWireless.setRowCount(len(scanresult))
		a = 0
		for i in scanresult:
			HeaderItem = QtGui.QTableWidgetItem()
			HeaderItem.setText(str(a + 1))
			self.listWireless.setVerticalHeaderItem(a, HeaderItem)

			# Wlan infos write to listWireless
			self.wireless_info = pywlan.wlanInfo(self.iface, i)
			b = 0
			for it in [self.wireless_info.getEssid(), self.isCrypted(self.iface, i), self.wireless_info.getQuality()]:
				item = QtGui.QTableWidgetItem()
				item.setText(str(it))
				self.listWireless.setItem(a, b, item)
				b += 1
			a += 1
		if a == scanresult.__len__():
			self.statusLabel.setText(u"Tarama tamamlandı.")

	def refreshConnectedWlan(self):
		self.networkIfaceLabel.setText(self.iface)
		self.connectedNetLabel.setText(pywlan.getConnected(self.iface))
		self.bssidLabel.setText(pywlan.wlanInfo(self.iface, pywlan.getConnected(self.iface)).getBssid())
		self.isCryptLabel.setText(self.isCrypted(self.iface, pywlan.getConnected(self.iface)))
		self.qualityLabel.setText(pywlan.wlanInfo(self.iface, pywlan.getConnected(self.iface)).getQuality())

	def refresh_bar(self):
		self.qualityBar.setValue(int(pywlan.wlanInfo(self.iface, str(self.listWireless.selectedItems()[0].text())).getQuality()))

	def isCrypted(self, iface, wlan):
		if pywlan.wlanInfo(iface, wlan).isEncryption():
			return "Evet"
		else:
			return "Hayır"

			a += 1

	def connectWireless(self):
		self.selecteditem = str(self.listWireless.selectedItems()[0].text())
		if pywlan.wlanInfo(self.iface, self.selecteditem).isEncryption():
			a = getPasswordWindow()
			a.show()

class mainWindow(QtGui.QMainWindow, Ui_NetworkManager):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		QtCore.QObject.connect(self.statusButton, QtCore.SIGNAL("clicked(bool)"), self.showInfo)

		self.allifaces = network.Networking_Info().listIfaces()

		# List interfaces in listNetworks
		self.refresh()

	def refresh(self):
		self.listNetworks.setRowCount(len(self.allifaces))
		a = 0
		for i in self.allifaces.keys():
			headerItem = QtGui.QTableWidgetItem()
			headerItem.setText(str(a + 1))
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
		try:
			self.selecteditem = str(self.listNetworks.selectedItems()[0].text())
			self.wlanInfoWindow = wlanInfoWindow(self.selecteditem)
			self.wlanInfoWindow.show()
		except(IndexError):
			QtGui.QMessageBox.critical(self, u"Hata!", u"Lütfen bir bağlantı arayüzü seçin.")

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()