# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rohanrhu/python/truva/anatolya-installer/screens/ui/installWindow.ui'
#
# Created: Mon Aug 11 03:26:11 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_installWindow(object):
    def setupUi(self, installWindow):
        installWindow.setObjectName("installWindow")
        installWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(installWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.installInfoGroup = QtGui.QGroupBox(self.centralwidget)
        self.installInfoGroup.setGeometry(QtCore.QRect(30, 50, 441, 291))
        self.installInfoGroup.setObjectName("installInfoGroup")
        self.label = QtGui.QLabel(self.installInfoGroup)
        self.label.setGeometry(QtCore.QRect(30, 80, 91, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.installInfoGroup)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 61, 18))
        self.label_2.setObjectName("label_2")
        self.packageLabel = QtGui.QLabel(self.installInfoGroup)
        self.packageLabel.setGeometry(QtCore.QRect(120, 80, 56, 18))
        self.packageLabel.setObjectName("packageLabel")
        self.categoryLabel = QtGui.QLabel(self.installInfoGroup)
        self.categoryLabel.setGeometry(QtCore.QRect(100, 100, 56, 18))
        self.categoryLabel.setObjectName("categoryLabel")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(420, 450, 75, 27))
        self.nextButton.setObjectName("nextButton")
        installWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(installWindow)
        self.statusbar.setObjectName("statusbar")
        installWindow.setStatusBar(self.statusbar)

        self.retranslateUi(installWindow)
        QtCore.QMetaObject.connectSlotsByName(installWindow)

    def retranslateUi(self, installWindow):
        installWindow.setWindowTitle(QtGui.QApplication.translate("installWindow", "Paketler Kuruluyor - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.installInfoGroup.setTitle(QtGui.QApplication.translate("installWindow", "Kurulan Paketler", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("installWindow", "Kurulan paket:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("installWindow", "Kategori:", None, QtGui.QApplication.UnicodeUTF8))
        self.packageLabel.setText(QtGui.QApplication.translate("installWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.categoryLabel.setText(QtGui.QApplication.translate("installWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("installWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))

