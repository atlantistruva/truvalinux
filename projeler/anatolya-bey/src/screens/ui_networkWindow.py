# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/networkWindow.ui'
#
# Created: Thu Jul 10 11:57:42 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NetworkWindow(object):
    def setupUi(self, NetworkWindow):
        NetworkWindow.setObjectName("NetworkWindow")
        NetworkWindow.resize(524,463)
        NetworkWindow.setMaximumSize(QtCore.QSize(524,463))
        NetworkWindow.setStyleSheet("QMainWindow {background-image: url(:/beyimage/beyimage.png);}")
        self.centralwidget = QtGui.QWidget(NetworkWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,442))
        self.centralwidget.setObjectName("centralwidget")
        self.networkGroup = QtGui.QGroupBox(self.centralwidget)
        self.networkGroup.setGeometry(QtCore.QRect(150,60,341,181))
        self.networkGroup.setObjectName("networkGroup")
        self.listIfaces = QtGui.QListWidget(self.networkGroup)
        self.listIfaces.setGeometry(QtCore.QRect(10,20,321,151))
        self.listIfaces.setObjectName("listIfaces")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140,250,361,151))
        self.label.setObjectName("label")
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-previous/go-previous.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setObjectName("backButton")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-next/go-next.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/exit-button/application-exit.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")
        NetworkWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(NetworkWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,442,524,21))
        self.statusbar.setObjectName("statusbar")
        NetworkWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NetworkWindow)
        QtCore.QMetaObject.connectSlotsByName(NetworkWindow)

    def retranslateUi(self, NetworkWindow):
        NetworkWindow.setWindowTitle(QtGui.QApplication.translate("NetworkWindow", "Ağ Ayarları - Anatolya Başlangıç", None, QtGui.QApplication.UnicodeUTF8))
        self.networkGroup.setTitle(QtGui.QApplication.translate("NetworkWindow", "Ağ arayüzleri", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NetworkWindow", "Bu adımda internete bağlanabilmek\n"
"için ağ ayarlarını yapabilirsiniz.\n"
"Bağlantı sağlamak istediğiniz arayüzü\n"
"seçin ve \"İleri\" ye tıklayın.\n"
"\n"
"bu ayar arayüzü sadece yüzeyseldir\n"
"ve ethernet ağları içindir...\n"
"Daha fazla ayrıntı için \n"
"\"Ağ Yöneticisi\" ne bakabilirsiniz.\n"
"Herhangibir sorun çıkarsa bunu lütfen bildirin.", None, QtGui.QApplication.UnicodeUTF8))
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

import startericons_rc
