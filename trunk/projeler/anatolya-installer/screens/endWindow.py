# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rohanrhu/python/truva/anatolya-installer/screens/ui/endWindow.ui'
#
# Created: Mon Aug 11 03:26:11 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_endWindow(object):
    def setupUi(self, endWindow):
        endWindow.setObjectName("endWindow")
        endWindow.resize(516, 511)
        self.centralwidget = QtGui.QWidget(endWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(420, 460, 75, 27))
        self.nextButton.setObjectName("nextButton")
        endWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(endWindow)
        self.statusbar.setObjectName("statusbar")
        endWindow.setStatusBar(self.statusbar)

        self.retranslateUi(endWindow)
        QtCore.QMetaObject.connectSlotsByName(endWindow)

    def retranslateUi(self, endWindow):
        endWindow.setWindowTitle(QtGui.QApplication.translate("endWindow", "Son - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("endWindow", "Bitir", None, QtGui.QApplication.UnicodeUTF8))

