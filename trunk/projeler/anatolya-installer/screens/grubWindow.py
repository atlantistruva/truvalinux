# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/grubWindow.ui'
#
# Created: Mon Aug 11 03:34:45 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_grubWindow(object):
    def setupUi(self, grubWindow):
        grubWindow.setObjectName("grubWindow")
        grubWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(grubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(420, 450, 75, 27))
        self.nextButton.setObjectName("nextButton")
        grubWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(grubWindow)
        self.statusbar.setObjectName("statusbar")
        grubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(grubWindow)
        QtCore.QMetaObject.connectSlotsByName(grubWindow)

    def retranslateUi(self, grubWindow):
        grubWindow.setWindowTitle(QtGui.QApplication.translate("grubWindow", "Grub Kurulumu - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("grubWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))

