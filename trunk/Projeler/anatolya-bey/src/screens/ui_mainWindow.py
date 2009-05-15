# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/mainWindow.ui'
#
# Created: Fri Sep 26 02:25:45 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_StarterWindow(object):
    def setupUi(self, StarterWindow):
        StarterWindow.setObjectName("StarterWindow")
        StarterWindow.setEnabled(True)
        StarterWindow.resize(QtCore.QSize(QtCore.QRect(0,0,524,444).size()).expandedTo(StarterWindow.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(StarterWindow.sizePolicy().hasHeightForWidth())
        StarterWindow.setSizePolicy(sizePolicy)
        StarterWindow.setMinimumSize(QtCore.QSize(524,444))
        StarterWindow.setMaximumSize(QtCore.QSize(524,444))
        StarterWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        StarterWindow.setWindowIcon(QtGui.QIcon(":/icon/icon.png"))

        self.centralwidget = QtGui.QWidget(StarterWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.logoLabel = QtGui.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(170,70,321,211))
        self.logoLabel.setPixmap(QtGui.QPixmap(":/truvalogo/truva-logo.png"))
        self.logoLabel.setObjectName("logoLabel")

        self.welcomeLabel = QtGui.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(180,260,291,131))
        self.welcomeLabel.setObjectName("welcomeLabel")

        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        self.cancelButton.setIcon(QtGui.QIcon(":/exit-button/application-exit.png"))
        self.cancelButton.setObjectName("cancelButton")

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        self.nextButton.setIcon(QtGui.QIcon(":/go-next/go-next.png"))
        self.nextButton.setObjectName("nextButton")

        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        self.backButton.setIcon(QtGui.QIcon(":/go-previous/go-previous.png"))
        self.backButton.setObjectName("backButton")

        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")
        StarterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StarterWindow)
        QtCore.QMetaObject.connectSlotsByName(StarterWindow)

    def retranslateUi(self, StarterWindow):
        StarterWindow.setWindowTitle(QtGui.QApplication.translate("StarterWindow", "Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        StarterWindow.setStyleSheet(QtGui.QApplication.translate("StarterWindow", "QMainWindow {background-image: url(:/beyimage/beyimage.png);}", None, QtGui.QApplication.UnicodeUTF8))
        self.welcomeLabel.setText(QtGui.QApplication.translate("StarterWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Truvaya Hoş Geldiniz</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Anatolya Bey size kurulum sonrası küçük ama gerekli</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ayarları yapmanızda yardımcı olacaktır.</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">İyi eğlenceler...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
