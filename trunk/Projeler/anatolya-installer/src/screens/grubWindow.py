# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/grubWindow.ui'
#
# Created: Thu Aug 14 18:26:39 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_grubWindow(object):
    def setupUi(self, grubWindow):
        grubWindow.setObjectName("grubWindow")
        grubWindow.resize(661, 586)
        grubWindow.setStyleSheet("""#grubWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(grubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 451, 41))
        self.label.setObjectName("label")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 160, 431, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.noInstallGrubCheck = QtGui.QRadioButton(self.groupBox_2)
        self.noInstallGrubCheck.setGeometry(QtCore.QRect(20, 100, 95, 23))
        self.noInstallGrubCheck.setObjectName("noInstallGrubCheck")
        self.installGrubCheck = QtGui.QRadioButton(self.groupBox_2)
        self.installGrubCheck.setGeometry(QtCore.QRect(20, 60, 341, 23))
        self.installGrubCheck.setObjectName("installGrubCheck")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        grubWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(grubWindow)
        QtCore.QMetaObject.connectSlotsByName(grubWindow)

    def retranslateUi(self, grubWindow):
        grubWindow.setWindowTitle(QtGui.QApplication.translate("grubWindow", "Grub Kurulumu - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("grubWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00aaff;\">Sistem önyükleyicisini (Grub) kurmak istiyor musunuz ?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.noInstallGrubCheck.setText(QtGui.QApplication.translate("grubWindow", "Hayır", None, QtGui.QApplication.UnicodeUTF8))
        self.installGrubCheck.setText(QtGui.QApplication.translate("grubWindow", "Evet (Önerilen)", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("grubWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("grubWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
