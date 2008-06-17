# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi uygulaması
# Grafik arabirimi
#  Copyright (C) 2008  Truva Linux
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore, QtGui
from ui_servisy import Ui_ServisYoneticisi
import sys
import os
import servisy_core

class mainWindow(QtGui.QMainWindow, Ui_ServisYoneticisi, servisy_core.Yonetici):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		servisy_core.Yonetici.__init__(self)
		# Sinyal / Slot bağlantıları
		QtCore.QObject.connect(self.calistirButton, QtCore.SIGNAL("clicked(bool)"), self.calistir_gui)
		QtCore.QObject.connect(self.servisList, QtCore.SIGNAL("itemSelectionChanged()"), self.tazele)
		QtCore.QObject.connect(self.durdurButton, QtCore.SIGNAL("clicked(bool)"), self.durdur_gui)
		QtCore.QObject.connect(self.acalistirButton, QtCore.SIGNAL("clicked(bool)"), self.acalistir_gui)

		QtCore.QObject.connect(self.syHakkinda, QtCore.SIGNAL("triggered(bool)"), self.syHakkinda_gui)
		QtCore.QObject.connect(self.qtHakkinda, QtCore.SIGNAL("triggered(bool)"), self.qtHakkinda_gui)
		QtCore.QObject.connect(self.actionCik, QtCore.SIGNAL("triggered(bool)"), sys.exit)

		for i in os.listdir(self.servis_dizin):
			self.servisList.addItem(str(i))

	def try_servisisim(self, komut):
		exec( \
u"""
try:
	%s
except(IndexError):
	QtGui.QMessageBox.critical(self, u"Hata!", u"Bir servis seçin.")
""" % komut)

	def tazele(self):
		# TODO: Servis durumu gösterilecek.
		self.servisIsim = str(self.servisList.selectedItems()[0].text())
		self.sad_Label.setText(self.servisIsim)
		if self.durum(self.servisIsim[2:]) == "0":
			self.durumLabel.setText(u"Çalışmıyor")
		else:
			self.durumLabel.setText(u"Çalışıyor")

	def calistir_gui(self):
		self.try_servisisim("self.servis_baslat(self.servisIsim)")
		self.tazele()

	def durdur_gui(self):
		self.try_servisisim("self.servis_durdur(self.servisIsim)")
		self.tazele()

	def acalistir_gui(self):
		if self.acalistirButton.isChecked():
			self.try_servisisim("self.servis_aktif(self.servisIsim)")
		else:
			self.try_servisisim("self.servis_deaktif(self.servisIsim)")

	def syHakkinda_gui(self):
		QtGui.QMessageBox.about(self, u"Sistem Yöneticisi Hakkında", u"Truva Servis Yöneticisi\nYazarlar:\nOğuzhan Eroğlu <oguzhan@oguzhaneroglu.com>\nTruva Geliştiricileri")

	def qtHakkinda_gui(self):
		QtGui.QMessageBox.aboutQt(self)

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()