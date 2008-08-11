# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rohanrhu/python/truva/anatolya-installer/screens/ui/discWindow.ui'
#
# Created: Mon Aug 11 03:26:11 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_discWindow(object):
    def setupUi(self, discWindow):
        discWindow.setObjectName("discWindow")
        discWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(discWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.discGroup = QtGui.QGroupBox(self.centralwidget)
        self.discGroup.setGeometry(QtCore.QRect(40, 80, 421, 261))
        self.discGroup.setObjectName("discGroup")
        self.discBox = QtGui.QComboBox(self.discGroup)
        self.discBox.setGeometry(QtCore.QRect(90, 120, 241, 22))
        self.discBox.setObjectName("discBox")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(400, 440, 75, 27))
        self.nextButton.setObjectName("nextButton")
        discWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(discWindow)
        self.statusbar.setObjectName("statusbar")
        discWindow.setStatusBar(self.statusbar)

        self.retranslateUi(discWindow)
        QtCore.QMetaObject.connectSlotsByName(discWindow)

    def retranslateUi(self, discWindow):
        discWindow.setWindowTitle(QtGui.QApplication.translate("discWindow", "Disk Seçimi - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.discGroup.setTitle(QtGui.QApplication.translate("discWindow", "Bölümler", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("discWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))

