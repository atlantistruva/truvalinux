# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi grafik kullanıcı arabirimi
# Author: Oğuzhan Eroğlu (oguzhan@oguzhaneroglu.com)

from PyQt4 import QtCore, QtGui
from ui_servisy import Ui_ServisYoneticisi

class mainWindow(QtGui.QMainWindow, Ui_ServisYoneticisi):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()