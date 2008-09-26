# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/wallpaperWindow.ui'
#
# Created: Fri Sep 26 19:49:36 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WallpaperWindow(object):
    def setupUi(self, WallpaperWindow):
        WallpaperWindow.setObjectName("WallpaperWindow")
        WallpaperWindow.resize(QtCore.QSize(QtCore.QRect(0,0,524,444).size()).expandedTo(WallpaperWindow.minimumSizeHint()))
        WallpaperWindow.setMinimumSize(QtCore.QSize(524,444))
        WallpaperWindow.setMaximumSize(QtCore.QSize(524,444))
        WallpaperWindow.setWindowIcon(QtGui.QIcon(":/icon/icon.png"))

        self.centralwidget = QtGui.QWidget(WallpaperWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.showPictureGroup = QtGui.QGroupBox(self.centralwidget)
        self.showPictureGroup.setGeometry(QtCore.QRect(310,260,151,131))
        self.showPictureGroup.setObjectName("showPictureGroup")

        self.pictureLabel = QtGui.QLabel(self.showPictureGroup)
        self.pictureLabel.setGeometry(QtCore.QRect(10,20,131,101))
        self.pictureLabel.setObjectName("pictureLabel")

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        self.nextButton.setIcon(QtGui.QIcon(":/go-next/go-next.png"))
        self.nextButton.setObjectName("nextButton")

        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        self.backButton.setIcon(QtGui.QIcon(":/go-previous/go-previous.png"))
        self.backButton.setObjectName("backButton")

        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        self.cancelButton.setIcon(QtGui.QIcon(":/exit-button/application-exit.png"))
        self.cancelButton.setObjectName("cancelButton")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10,250,161,161))
        self.label.setPixmap(QtGui.QPixmap(":/icon/penguen.png"))
        self.label.setObjectName("label")

        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")

        self.isConfig = QtGui.QCheckBox(self.centralwidget)
        self.isConfig.setGeometry(QtCore.QRect(140,370,181,23))
        self.isConfig.setObjectName("isConfig")

        self.listWallpapers = QtGui.QListWidget(self.centralwidget)
        self.listWallpapers.setGeometry(QtCore.QRect(180,80,281,171))
        self.listWallpapers.setObjectName("listWallpapers")

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150,270,111,41))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        WallpaperWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WallpaperWindow)
        QtCore.QMetaObject.connectSlotsByName(WallpaperWindow)

    def retranslateUi(self, WallpaperWindow):
        WallpaperWindow.setWindowTitle(QtGui.QApplication.translate("WallpaperWindow", "Masaüstü Arkaplanı - Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        WallpaperWindow.setStyleSheet(QtGui.QApplication.translate("WallpaperWindow", "QMainWindow {background-image: url(:/beyimage/beyimage.png);}", None, QtGui.QApplication.UnicodeUTF8))
        self.showPictureGroup.setTitle(QtGui.QApplication.translate("WallpaperWindow", "Önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("WallpaperWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("WallpaperWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Başlangıç</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fare ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panel ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Arkaplan</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ağ ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Son</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.isConfig.setText(QtGui.QApplication.translate("WallpaperWindow", "Arkaplanı değiştirme", None, QtGui.QApplication.UnicodeUTF8))
        self.listWallpapers.setWhatsThis(QtGui.QApplication.translate("WallpaperWindow", "Buradan arkaplanınızı seçebilirsiniz...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("WallpaperWindow", "Arkaplanınızı \n"
        "değiştirebilirsiniz :)", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
