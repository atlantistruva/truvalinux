# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getPasswd.ui'
#
# Created: Sun Jun  8 00:29:15 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_passwdWindow(object):
    def setupUi(self, passwdWindow):
        passwdWindow.setObjectName("passwdWindow")
        passwdWindow.resize(QtCore.QSize(QtCore.QRect(0,0,374,101).size()).expandedTo(passwdWindow.minimumSizeHint()))

        self.label = QtGui.QLabel(passwdWindow)
        self.label.setGeometry(QtCore.QRect(10,10,161,18))
        self.label.setObjectName("label")

        self.passwdLine = QtGui.QLineEdit(passwdWindow)
        self.passwdLine.setGeometry(QtCore.QRect(10,30,351,24))
        self.passwdLine.setObjectName("passwdLine")

        self.submitButton = QtGui.QPushButton(passwdWindow)
        self.submitButton.setGeometry(QtCore.QRect(290,60,71,28))
        self.submitButton.setObjectName("submitButton")

        self.retranslateUi(passwdWindow)
        QtCore.QMetaObject.connectSlotsByName(passwdWindow)

    def retranslateUi(self, passwdWindow):
        passwdWindow.setWindowTitle(QtGui.QApplication.translate("passwdWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("passwdWindow", "Ağ parolasını girin:", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("passwdWindow", "Tamam", None, QtGui.QApplication.UnicodeUTF8))

