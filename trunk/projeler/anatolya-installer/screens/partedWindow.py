# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rohanrhu/python/truva/anatolya-installer/screens/ui/partedWindow.ui'
#
# Created: Mon Aug 11 03:26:12 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_partedWindow(object):
    def setupUi(self, partedWindow):
        partedWindow.setObjectName("partedWindow")
        partedWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(partedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(420, 450, 75, 27))
        self.nextButton.setObjectName("nextButton")
        self.descLabel = QtGui.QLabel(self.centralwidget)
        self.descLabel.setGeometry(QtCore.QRect(30, 70, 391, 301))
        self.descLabel.setObjectName("descLabel")
        partedWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(partedWindow)
        self.statusbar.setObjectName("statusbar")
        partedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(partedWindow)
        QtCore.QMetaObject.connectSlotsByName(partedWindow)

    def retranslateUi(self, partedWindow):
        partedWindow.setWindowTitle(QtGui.QApplication.translate("partedWindow", "Disk Bölümleme - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("partedWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.descLabel.setText(QtGui.QApplication.translate("partedWindow", "parted ...", None, QtGui.QApplication.UnicodeUTF8))

