# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/mainWindow.ui'
#
# Created: Sat Jul 12 16:34:04 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470,317)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/serviceicon.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,28,470,289))
        self.centralwidget.setObjectName("centralwidget")
        self.listServices = QtGui.QTreeWidget(self.centralwidget)
        self.listServices.setGeometry(QtCore.QRect(10,10,421,271))
        self.listServices.setObjectName("listServices")
        self.startButton = QtGui.QToolButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(440,10,25,25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/apply/apply.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setObjectName("startButton")
        self.stopButton = QtGui.QToolButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(440,50,25,25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/shutdown/shutdown.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.stopButton.setIcon(icon)
        self.stopButton.setObjectName("stopButton")
        self.onButton = QtGui.QToolButton(self.centralwidget)
        self.onButton.setGeometry(QtCore.QRect(440,90,25,25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/on/serviceon.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.onButton.setIcon(icon)
        self.onButton.setObjectName("onButton")
        self.offButton = QtGui.QToolButton(self.centralwidget)
        self.offButton.setGeometry(QtCore.QRect(440,130,25,25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/off/serviceoff.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.offButton.setIcon(icon)
        self.offButton.setObjectName("offButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,470,28))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuYard_m = QtGui.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.actionConfig = QtGui.QAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/shutdown/shutdown.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/serviceicon.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuDosya.addAction(self.actionConfig)
        self.menuDosya.addAction(self.actionExit)
        self.menuYard_m.addAction(self.actionHelp)
        self.menuYard_m.addAction(self.actionAbout)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Servis Yöneticisi", None, QtGui.QApplication.UnicodeUTF8))
        self.listServices.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Burada sistem servisleri listelenir.", None, QtGui.QApplication.UnicodeUTF8))
        self.listServices.headerItem().setText(0,QtGui.QApplication.translate("MainWindow", "Servis adı", None, QtGui.QApplication.UnicodeUTF8))
        self.listServices.headerItem().setText(1,QtGui.QApplication.translate("MainWindow", "Durumu", None, QtGui.QApplication.UnicodeUTF8))
        self.listServices.headerItem().setText(2,QtGui.QApplication.translate("MainWindow", "Açılışta başlat ?", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Servisi başlat.", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Servisi durdur.", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.onButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Servisi açılışta başlat.", None, QtGui.QApplication.UnicodeUTF8))
        self.onButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.offButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Servisi açılışta başlatma.", None, QtGui.QApplication.UnicodeUTF8))
        self.offButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDosya.setTitle(QtGui.QApplication.translate("MainWindow", "Dosya", None, QtGui.QApplication.UnicodeUTF8))
        self.menuYard_m.setTitle(QtGui.QApplication.translate("MainWindow", "Yardım", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig.setText(QtGui.QApplication.translate("MainWindow", "Yapılandır", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Çık", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "Servis Yöneticisi Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "El kitabı", None, QtGui.QApplication.UnicodeUTF8))

import serviceicons_rc
