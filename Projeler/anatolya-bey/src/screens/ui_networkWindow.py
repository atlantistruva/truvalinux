# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/networkWindow.ui'
#
# Created: Fri Sep 26 20:05:18 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NetworkWindow(object):
    def setupUi(self, NetworkWindow):
        NetworkWindow.setObjectName("NetworkWindow")
        NetworkWindow.resize(QtCore.QSize(QtCore.QRect(0,0,524,444).size()).expandedTo(NetworkWindow.minimumSizeHint()))
        NetworkWindow.setMinimumSize(QtCore.QSize(524,444))
        NetworkWindow.setMaximumSize(QtCore.QSize(524,444))
        NetworkWindow.setWindowIcon(QtGui.QIcon(":/icon/icon.png"))

        self.centralwidget = QtGui.QWidget(NetworkWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        self.backButton.setIcon(QtGui.QIcon(":/go-previous/go-previous.png"))
        self.backButton.setObjectName("backButton")

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        self.nextButton.setIcon(QtGui.QIcon(":/go-next/go-next.png"))
        self.nextButton.setObjectName("nextButton")

        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        self.cancelButton.setIcon(QtGui.QIcon(":/exit-button/application-exit.png"))
        self.cancelButton.setObjectName("cancelButton")

        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240,190,181,171))
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/penguen.png"))
        self.label_2.setObjectName("label_2")

        self.openNetworkButton = QtGui.QPushButton(self.centralwidget)
        self.openNetworkButton.setGeometry(QtCore.QRect(190,140,81,28))
        self.openNetworkButton.setObjectName("openNetworkButton")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280,140,181,31))
        self.label.setObjectName("label")
        NetworkWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NetworkWindow)
        QtCore.QMetaObject.connectSlotsByName(NetworkWindow)

    def retranslateUi(self, NetworkWindow):
        NetworkWindow.setWindowTitle(QtGui.QApplication.translate("NetworkWindow", "Ağ Ayarları - Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        NetworkWindow.setStyleSheet(QtGui.QApplication.translate("NetworkWindow", "QMainWindow {background-image: url(:/beyimage/beyimage.png);}", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("NetworkWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("NetworkWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("NetworkWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("NetworkWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Başlangıç</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fare ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panel ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arkaplan</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ağ ayarları</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Son</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.openNetworkButton.setText(QtGui.QApplication.translate("NetworkWindow", "Ağ Yöneticisi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkWindow", "Ağ yöneticisini başlatabilirsiniz.", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
