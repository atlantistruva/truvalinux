# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/mainWindow.ui'
#
# Created: Mon Aug 11 03:32:41 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(410, 450, 75, 27))
        self.nextButton.setObjectName("nextButton")
        self.descLabel = QtGui.QLabel(self.centralwidget)
        self.descLabel.setGeometry(QtCore.QRect(30, 40, 331, 311))
        self.descLabel.setObjectName("descLabel")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "Anatolya Kurulum Aracı", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("mainWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.descLabel.setText(QtGui.QApplication.translate("mainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

