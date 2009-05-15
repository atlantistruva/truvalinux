# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_networkmanager.ui'
#
# Created: Sun Jun  8 00:29:03 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NetworkManager(object):
    def setupUi(self, NetworkManager):
        NetworkManager.setObjectName("NetworkManager")
        NetworkManager.resize(QtCore.QSize(QtCore.QRect(0,0,553,329).size()).expandedTo(NetworkManager.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(NetworkManager)
        self.centralwidget.setGeometry(QtCore.QRect(0,30,553,276))
        self.centralwidget.setObjectName("centralwidget")

        self.listNetworks = QtGui.QTableWidget(self.centralwidget)
        self.listNetworks.setGeometry(QtCore.QRect(10,30,431,231))
        self.listNetworks.setObjectName("listNetworks")

        self.connectButton = QtGui.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(450,30,91,28))
        self.connectButton.setObjectName("connectButton")

        self.disconnectButton = QtGui.QPushButton(self.centralwidget)
        self.disconnectButton.setGeometry(QtCore.QRect(450,70,91,28))
        self.disconnectButton.setObjectName("disconnectButton")

        self.newButton = QtGui.QPushButton(self.centralwidget)
        self.newButton.setGeometry(QtCore.QRect(450,160,91,28))
        self.newButton.setObjectName("newButton")

        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450,140,91,20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.statusButton = QtGui.QPushButton(self.centralwidget)
        self.statusButton.setGeometry(QtCore.QRect(450,110,91,28))
        self.statusButton.setObjectName("statusButton")

        self.reconfigButton = QtGui.QPushButton(self.centralwidget)
        self.reconfigButton.setGeometry(QtCore.QRect(450,200,91,28))
        self.reconfigButton.setObjectName("reconfigButton")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10,10,101,18))
        self.label.setObjectName("label")
        NetworkManager.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(NetworkManager)
        self.menubar.setGeometry(QtCore.QRect(0,0,553,30))
        self.menubar.setObjectName("menubar")

        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")

        self.menuSe_enekler = QtGui.QMenu(self.menubar)
        self.menuSe_enekler.setObjectName("menuSe_enekler")

        self.menu_k = QtGui.QMenu(self.menubar)
        self.menu_k.setObjectName("menu_k")
        NetworkManager.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(NetworkManager)
        self.statusbar.setGeometry(QtCore.QRect(0,306,553,23))
        self.statusbar.setObjectName("statusbar")
        NetworkManager.setStatusBar(self.statusbar)

        self.actionA_Y_neticisi_Hakk_nda = QtGui.QAction(NetworkManager)
        self.actionA_Y_neticisi_Hakk_nda.setObjectName("actionA_Y_neticisi_Hakk_nda")

        self.actionQT_Hakk_nda = QtGui.QAction(NetworkManager)
        self.actionQT_Hakk_nda.setObjectName("actionQT_Hakk_nda")

        self.actionYap_land_r = QtGui.QAction(NetworkManager)
        self.actionYap_land_r.setObjectName("actionYap_land_r")

        self.action_k = QtGui.QAction(NetworkManager)
        self.action_k.setObjectName("action_k")
        self.menuDosya.addAction(self.actionYap_land_r)
        self.menuDosya.addAction(self.action_k)
        self.menu_k.addAction(self.actionA_Y_neticisi_Hakk_nda)
        self.menu_k.addAction(self.actionQT_Hakk_nda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuSe_enekler.menuAction())
        self.menubar.addAction(self.menu_k.menuAction())

        self.retranslateUi(NetworkManager)
        QtCore.QMetaObject.connectSlotsByName(NetworkManager)

    def retranslateUi(self, NetworkManager):
        NetworkManager.setWindowTitle(QtGui.QApplication.translate("NetworkManager", "Ağ Yöneticisi", None, QtGui.QApplication.UnicodeUTF8))
        self.listNetworks.clear()
        self.listNetworks.setColumnCount(3)
        self.listNetworks.setRowCount(0)

        headerItem = QtGui.QTableWidgetItem()
        headerItem.setText(QtGui.QApplication.translate("NetworkManager", "Arayüz", None, QtGui.QApplication.UnicodeUTF8))
        self.listNetworks.setHorizontalHeaderItem(0,headerItem)

        headerItem1 = QtGui.QTableWidgetItem()
        headerItem1.setText(QtGui.QApplication.translate("NetworkManager", "Bağlantı Türü", None, QtGui.QApplication.UnicodeUTF8))
        self.listNetworks.setHorizontalHeaderItem(1,headerItem1)

        headerItem2 = QtGui.QTableWidgetItem()
        headerItem2.setText(QtGui.QApplication.translate("NetworkManager", "Durumu", None, QtGui.QApplication.UnicodeUTF8))
        self.listNetworks.setHorizontalHeaderItem(2,headerItem2)
        self.connectButton.setText(QtGui.QApplication.translate("NetworkManager", "Bağlan", None, QtGui.QApplication.UnicodeUTF8))
        self.disconnectButton.setText(QtGui.QApplication.translate("NetworkManager", "Kes", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("NetworkManager", "Yeni Bağlantı", None, QtGui.QApplication.UnicodeUTF8))
        self.statusButton.setText(QtGui.QApplication.translate("NetworkManager", "Durum", None, QtGui.QApplication.UnicodeUTF8))
        self.reconfigButton.setText(QtGui.QApplication.translate("NetworkManager", "Düzenle", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkManager", "Tüm bağlantılar:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDosya.setTitle(QtGui.QApplication.translate("NetworkManager", "Dosya", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSe_enekler.setTitle(QtGui.QApplication.translate("NetworkManager", "Seçenekler", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_k.setTitle(QtGui.QApplication.translate("NetworkManager", "Yardım", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_Y_neticisi_Hakk_nda.setText(QtGui.QApplication.translate("NetworkManager", "Ağ Yöneticisi Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQT_Hakk_nda.setText(QtGui.QApplication.translate("NetworkManager", "QT Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.actionYap_land_r.setText(QtGui.QApplication.translate("NetworkManager", "Yapılandır", None, QtGui.QApplication.UnicodeUTF8))
        self.action_k.setText(QtGui.QApplication.translate("NetworkManager", "Çık", None, QtGui.QApplication.UnicodeUTF8))

