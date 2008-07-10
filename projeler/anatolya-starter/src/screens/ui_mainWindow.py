# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/mainWindow.ui'
#
# Created: Thu Jul 10 11:50:15 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_StarterWindow(object):
    def setupUi(self, StarterWindow):
        StarterWindow.setObjectName("StarterWindow")
        StarterWindow.setEnabled(True)
        StarterWindow.resize(524,463)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(StarterWindow.sizePolicy().hasHeightForWidth())
        StarterWindow.setSizePolicy(sizePolicy)
        StarterWindow.setMinimumSize(QtCore.QSize(524,463))
        StarterWindow.setMaximumSize(QtCore.QSize(524,463))
        StarterWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        StarterWindow.setStyleSheet("QMainWindow {background-image: url(:/beyimage/beyimage.png);}")
        self.centralwidget = QtGui.QWidget(StarterWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,442))
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtGui.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(170,70,301,211))
        self.logoLabel.setPixmap(QtGui.QPixmap(":/truvalogo/truva-logo.png"))
        self.logoLabel.setObjectName("logoLabel")
        self.welcomeLabel = QtGui.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(140,290,361,111))
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/exit-button/application-exit.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-next/go-next.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-previous/go-previous.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setObjectName("backButton")
        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")
        StarterWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(StarterWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,442,524,21))
        self.statusbar.setObjectName("statusbar")
        StarterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StarterWindow)
        QtCore.QMetaObject.connectSlotsByName(StarterWindow)

    def retranslateUi(self, StarterWindow):
        StarterWindow.setWindowTitle(QtGui.QApplication.translate("StarterWindow", "Anatolya Başlangıç", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeLabel.setText(QtGui.QApplication.translate("StarterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Truvaya Hoş Geldiniz!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kurulumu tamamlayarak Truva Linux\'u bilgisayarınıza kurdunuz.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Şimdi \"Anatolya Başlangıç\" ile küçük ama,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gerekli ayarları yapabilirsiniz.</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Truva kullandığınız için teşekkürler.</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">İyi Eğlenceler!</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\">Truva Ekibi</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("StarterWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("StarterWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("StarterWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("StarterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Başlangıç</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fare ayarları</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panel ayarları</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arkaplan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ağ ayarları</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Son</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
