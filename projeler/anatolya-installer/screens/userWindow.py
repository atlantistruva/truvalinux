# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rohanrhu/python/truva/anatolya-installer/screens/ui/userWindow.ui'
#
# Created: Mon Aug 11 03:26:12 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName("userWindow")
        userWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(userWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(410, 440, 75, 27))
        self.nextButton.setObjectName("nextButton")
        userWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(userWindow)
        self.statusbar.setObjectName("statusbar")
        userWindow.setStatusBar(self.statusbar)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(QtGui.QApplication.translate("userWindow", "Kullanıcı Ayarları - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("userWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))

