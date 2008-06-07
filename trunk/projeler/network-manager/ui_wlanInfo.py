# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wlanInfo.ui'
#
# Created: Fri Jun  6 16:34:07 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_wirelessWindow(object):
    def setupUi(self, wirelessWindow):
        wirelessWindow.setObjectName("wirelessWindow")
        wirelessWindow.resize(QtCore.QSize(QtCore.QRect(0,0,431,403).size()).expandedTo(wirelessWindow.minimumSizeHint()))

        self.connectInfoBox = QtGui.QGroupBox(wirelessWindow)
        self.connectInfoBox.setGeometry(QtCore.QRect(10,10,401,121))
        self.connectInfoBox.setObjectName("connectInfoBox")

        self.label = QtGui.QLabel(self.connectInfoBox)
        self.label.setGeometry(QtCore.QRect(10,20,101,18))
        self.label.setObjectName("label")

        self.networkIfaceLabel = QtGui.QLabel(self.connectInfoBox)
        self.networkIfaceLabel.setGeometry(QtCore.QRect(120,20,81,18))
        self.networkIfaceLabel.setObjectName("networkIfaceLabel")

        self.label_2 = QtGui.QLabel(self.connectInfoBox)
        self.label_2.setGeometry(QtCore.QRect(10,50,101,18))
        self.label_2.setObjectName("label_2")

        self.connectedNetLabel = QtGui.QLabel(self.connectInfoBox)
        self.connectedNetLabel.setGeometry(QtCore.QRect(120,50,54,18))
        self.connectedNetLabel.setObjectName("connectedNetLabel")

        self.label_3 = QtGui.QLabel(self.connectInfoBox)
        self.label_3.setGeometry(QtCore.QRect(200,20,71,18))
        self.label_3.setObjectName("label_3")

        self.isCryptLabel = QtGui.QLabel(self.connectInfoBox)
        self.isCryptLabel.setGeometry(QtCore.QRect(300,20,54,18))
        self.isCryptLabel.setObjectName("isCryptLabel")

        self.label_4 = QtGui.QLabel(self.connectInfoBox)
        self.label_4.setGeometry(QtCore.QRect(200,50,81,18))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtGui.QLabel(self.connectInfoBox)
        self.label_5.setGeometry(QtCore.QRect(10,80,91,18))
        self.label_5.setObjectName("label_5")

        self.bssidLabel = QtGui.QLabel(self.connectInfoBox)
        self.bssidLabel.setGeometry(QtCore.QRect(120,80,201,18))
        self.bssidLabel.setObjectName("bssidLabel")

        self.qualityLabel = QtGui.QLabel(self.connectInfoBox)
        self.qualityLabel.setGeometry(QtCore.QRect(300,50,54,18))
        self.qualityLabel.setObjectName("qualityLabel")

        self.listWireless = QtGui.QTableWidget(wirelessWindow)
        self.listWireless.setEnabled(True)
        self.listWireless.setGeometry(QtCore.QRect(10,150,401,171))
        self.listWireless.setObjectName("listWireless")

        self.label_6 = QtGui.QLabel(wirelessWindow)
        self.label_6.setGeometry(QtCore.QRect(10,130,101,18))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtGui.QLabel(wirelessWindow)
        self.label_7.setGeometry(QtCore.QRect(10,350,91,18))
        self.label_7.setObjectName("label_7")

        self.qualityBar = QtGui.QProgressBar(wirelessWindow)
        self.qualityBar.setGeometry(QtCore.QRect(10,370,401,23))
        self.qualityBar.setProperty("value",QtCore.QVariant(0))
        self.qualityBar.setObjectName("qualityBar")

        self.scanWirelessButton = QtGui.QPushButton(wirelessWindow)
        self.scanWirelessButton.setGeometry(QtCore.QRect(330,330,75,28))
        self.scanWirelessButton.setObjectName("scanWirelessButton")

        self.line = QtGui.QFrame(wirelessWindow)
        self.line.setGeometry(QtCore.QRect(310,330,20,31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.connectWirelessButton = QtGui.QPushButton(wirelessWindow)
        self.connectWirelessButton.setGeometry(QtCore.QRect(230,330,75,28))
        self.connectWirelessButton.setObjectName("connectWirelessButton")

        self.statusLabel = QtGui.QLabel(wirelessWindow)
        self.statusLabel.setGeometry(QtCore.QRect(10,330,171,18))

        font = QtGui.QFont()
        font.setItalic(True)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(wirelessWindow)
        QtCore.QMetaObject.connectSlotsByName(wirelessWindow)

    def retranslateUi(self, wirelessWindow):
        wirelessWindow.setWindowTitle(QtGui.QApplication.translate("wirelessWindow", "Wireless Ağı", None, QtGui.QApplication.UnicodeUTF8))
        self.connectInfoBox.setTitle(QtGui.QApplication.translate("wirelessWindow", "Bağlantı durumu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wirelessWindow", "Bağlantı arayüzü:", None, QtGui.QApplication.UnicodeUTF8))
        self.networkIfaceLabel.setText(QtGui.QApplication.translate("wirelessWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("wirelessWindow", "Bağlı olunan ağ:", None, QtGui.QApplication.UnicodeUTF8))
        self.connectedNetLabel.setText(QtGui.QApplication.translate("wirelessWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("wirelessWindow", "Şifrelenmiş:", None, QtGui.QApplication.UnicodeUTF8))
        self.isCryptLabel.setText(QtGui.QApplication.translate("wirelessWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("wirelessWindow", "Sinyal kalitesi:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("wirelessWindow", "Makine adresi:", None, QtGui.QApplication.UnicodeUTF8))
        self.bssidLabel.setText(QtGui.QApplication.translate("wirelessWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.qualityLabel.setText(QtGui.QApplication.translate("wirelessWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.listWireless.clear()
        self.listWireless.setColumnCount(3)
        self.listWireless.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("wirelessWindow", "Essid", None, QtGui.QApplication.UnicodeUTF8))
        self.listWireless.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("wirelessWindow", "Şifreli ?", None, QtGui.QApplication.UnicodeUTF8))
        self.listWireless.setHorizontalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("wirelessWindow", "Sİnyal kalitesi", None, QtGui.QApplication.UnicodeUTF8))
        self.listWireless.setHorizontalHeaderItem(2,headerItem2)
        self.label_6.setText(QtGui.QApplication.translate("wirelessWindow", "Tarama sonuçları:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("wirelessWindow", "Sinyal kalitesi:", None, QtGui.QApplication.UnicodeUTF8))
        self.scanWirelessButton.setText(QtGui.QApplication.translate("wirelessWindow", "Tara", None, QtGui.QApplication.UnicodeUTF8))
        self.connectWirelessButton.setText(QtGui.QApplication.translate("wirelessWindow", "Bağlan", None, QtGui.QApplication.UnicodeUTF8))

