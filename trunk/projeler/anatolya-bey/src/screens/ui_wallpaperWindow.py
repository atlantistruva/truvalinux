# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/wallpaperWindow.ui'
#
# Created: Sat Jul 12 20:29:53 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WallpaperWindow(object):
    def setupUi(self, WallpaperWindow):
        WallpaperWindow.setObjectName("WallpaperWindow")
        WallpaperWindow.resize(524,444)
        WallpaperWindow.setMinimumSize(QtCore.QSize(524,444))
        WallpaperWindow.setMaximumSize(QtCore.QSize(524,444))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        WallpaperWindow.setWindowIcon(icon)
        WallpaperWindow.setStyleSheet("QMainWindow {background-image: url(:/beyimage/beyimage.png);}")
        self.centralwidget = QtGui.QWidget(WallpaperWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,444))
        self.centralwidget.setObjectName("centralwidget")
        self.WallpapersGroup = QtGui.QGroupBox(self.centralwidget)
        self.WallpapersGroup.setGeometry(QtCore.QRect(150,70,151,211))
        self.WallpapersGroup.setObjectName("WallpapersGroup")
        self.listWallpapers = QtGui.QListWidget(self.WallpapersGroup)
        self.listWallpapers.setGeometry(QtCore.QRect(10,20,131,181))
        self.listWallpapers.setObjectName("listWallpapers")
        self.showPictureGroup = QtGui.QGroupBox(self.centralwidget)
        self.showPictureGroup.setGeometry(QtCore.QRect(310,70,181,161))
        self.showPictureGroup.setObjectName("showPictureGroup")
        self.pictureLabel = QtGui.QLabel(self.showPictureGroup)
        self.pictureLabel.setGeometry(QtCore.QRect(10,20,161,131))
        self.pictureLabel.setObjectName("pictureLabel")
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
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/exit-button/application-exit.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon)
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140,300,301,61))
        self.label.setObjectName("label")
        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")
        self.isReplace = QtGui.QRadioButton(self.centralwidget)
        self.isReplace.setGeometry(QtCore.QRect(140,370,151,22))
        self.isReplace.setObjectName("isReplace")
        WallpaperWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WallpaperWindow)
        QtCore.QMetaObject.connectSlotsByName(WallpaperWindow)

    def retranslateUi(self, WallpaperWindow):
        WallpaperWindow.setWindowTitle(QtGui.QApplication.translate("WallpaperWindow", "Masaüstü Arkaplanı - Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        self.WallpapersGroup.setTitle(QtGui.QApplication.translate("WallpaperWindow", "Arkaplanlar", None, QtGui.QApplication.UnicodeUTF8))
        self.showPictureGroup.setTitle(QtGui.QApplication.translate("WallpaperWindow", "Önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("WallpaperWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WallpaperWindow", "Masaüstü arkaplanınızı seçin.\n"
"Bilgi: Çok renkli arkaplanlar \n"
"gözünüzü yorabileceği için \n"
"siyah tonlarına yakın\n"
"arkaplanlar seçmenizi öneririz.", None, QtGui.QApplication.UnicodeUTF8))
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
        self.isReplace.setText(QtGui.QApplication.translate("WallpaperWindow", "Arkaplanı değiştirme", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
