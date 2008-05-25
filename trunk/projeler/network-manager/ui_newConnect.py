# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_newconnect.ui'
#
# Created: Thu May 22 17:44:50 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_newDialogWindow(object):
    def setupUi(self, newDialogWindow):
        newDialogWindow.setObjectName("newDialogWindow")
        newDialogWindow.resize(QtCore.QSize(QtCore.QRect(0,0,400,284).size()).expandedTo(newDialogWindow.minimumSizeHint()))

        self.nifaceList = QtGui.QListWidget(newDialogWindow)
        self.nifaceList.setGeometry(QtCore.QRect(10,30,121,241))
        self.nifaceList.setObjectName("nifaceList")

        self.label = QtGui.QLabel(newDialogWindow)
        self.label.setGeometry(QtCore.QRect(10,10,121,18))
        self.label.setObjectName("label")

        self.nameLine = QtGui.QLineEdit(newDialogWindow)
        self.nameLine.setGeometry(QtCore.QRect(150,50,221,24))
        self.nameLine.setObjectName("nameLine")

        self.label_2 = QtGui.QLabel(newDialogWindow)
        self.label_2.setGeometry(QtCore.QRect(150,30,91,18))
        self.label_2.setObjectName("label_2")

        self.okButton = QtGui.QPushButton(newDialogWindow)
        self.okButton.setGeometry(QtCore.QRect(210,240,75,28))
        self.okButton.setObjectName("okButton")

        self.cancelbutton = QtGui.QPushButton(newDialogWindow)
        self.cancelbutton.setGeometry(QtCore.QRect(310,240,75,28))
        self.cancelbutton.setObjectName("cancelbutton")

        self.line = QtGui.QFrame(newDialogWindow)
        self.line.setGeometry(QtCore.QRect(140,220,251,16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(newDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(newDialogWindow)

    def retranslateUi(self, newDialogWindow):
        newDialogWindow.setWindowTitle(QtGui.QApplication.translate("newDialogWindow", "Yeni Bağlantı Ekle", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("newDialogWindow", "Bağlantı arayüzleri:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("newDialogWindow", "Bağlantı adı:", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("newDialogWindow", "Tamam", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelbutton.setText(QtGui.QApplication.translate("newDialogWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))

