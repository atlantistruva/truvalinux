# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/kickerWindow.ui'
#
# Created: Thu Jul 10 13:18:33 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_KickerWindow(object):
    def setupUi(self, KickerWindow):
        KickerWindow.setObjectName("KickerWindow")
        KickerWindow.resize(524,463)
        KickerWindow.setMaximumSize(QtCore.QSize(524,463))
        KickerWindow.setStyleSheet("QMainWindow {background-image: url(:/beyimage/beyimage.png);}")
        self.centralwidget = QtGui.QWidget(KickerWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,442))
        self.centralwidget.setObjectName("centralwidget")
        self.kickersGroup = QtGui.QGroupBox(self.centralwidget)
        self.kickersGroup.setGeometry(QtCore.QRect(150,70,341,81))
        self.kickersGroup.setObjectName("kickersGroup")
        self.listKickers = QtGui.QComboBox(self.kickersGroup)
        self.listKickers.setGeometry(QtCore.QRect(50,30,251,22))
        self.listKickers.setObjectName("listKickers")
        self.viewGroup = QtGui.QGroupBox(self.centralwidget)
        self.viewGroup.setGeometry(QtCore.QRect(150,160,341,171))
        self.viewGroup.setObjectName("viewGroup")
        self.viewPicture = QtGui.QLabel(self.viewGroup)
        self.viewPicture.setGeometry(QtCore.QRect(10,20,321,131))
        self.viewPicture.setObjectName("viewPicture")
        self.isConfig = QtGui.QRadioButton(self.centralwidget)
        self.isConfig.setGeometry(QtCore.QRect(150,370,181,22))
        self.isConfig.setObjectName("isConfig")
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
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-previous/go-previous.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setObjectName("backButton")
        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")
        KickerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(KickerWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,442,524,21))
        self.statusbar.setObjectName("statusbar")
        KickerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(KickerWindow)
        QtCore.QMetaObject.connectSlotsByName(KickerWindow)

    def retranslateUi(self, KickerWindow):
        KickerWindow.setWindowTitle(QtGui.QApplication.translate("KickerWindow", "Panel Seçenekleri - Anatolya Starter", None, QtGui.QApplication.UnicodeUTF8))
        self.kickersGroup.setTitle(QtGui.QApplication.translate("KickerWindow", "Paneller", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Transparan", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "ModernTransparan", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Klasik", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Modern", None, QtGui.QApplication.UnicodeUTF8))
        self.viewGroup.setTitle(QtGui.QApplication.translate("KickerWindow", "Önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.viewPicture.setText(QtGui.QApplication.translate("KickerWindow", "önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.isConfig.setText(QtGui.QApplication.translate("KickerWindow", "Paneli değiştirme", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("KickerWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("KickerWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("KickerWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("KickerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Başlangıç</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fare ayarları</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Panel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arkaplan</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ağ ayarları</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Son</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
