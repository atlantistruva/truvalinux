# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/wallpaperWindow.ui'
#
# Created: Fri Jul  4 22:56:47 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WallpaperWindow(object):
    def setupUi(self, WallpaperWindow):
        WallpaperWindow.setObjectName("WallpaperWindow")
        WallpaperWindow.resize(524,463)
        WallpaperWindow.setMaximumSize(QtCore.QSize(524,463))
        self.centralwidget = QtGui.QWidget(WallpaperWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,442))
        self.centralwidget.setObjectName("centralwidget")
        self.WallpapersGroup = QtGui.QGroupBox(self.centralwidget)
        self.WallpapersGroup.setGeometry(QtCore.QRect(10,10,221,291))
        self.WallpapersGroup.setObjectName("WallpapersGroup")
        self.listWallpapers = QtGui.QListWidget(self.WallpapersGroup)
        self.listWallpapers.setGeometry(QtCore.QRect(10,20,201,261))
        self.listWallpapers.setObjectName("listWallpapers")
        self.showPictureGroup = QtGui.QGroupBox(self.centralwidget)
        self.showPictureGroup.setGeometry(QtCore.QRect(240,10,271,291))
        self.showPictureGroup.setObjectName("showPictureGroup")
        self.pictureLabel = QtGui.QLabel(self.showPictureGroup)
        self.pictureLabel.setGeometry(QtCore.QRect(20,40,231,221))
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
        self.label.setGeometry(QtCore.QRect(20,310,491,61))
        self.label.setObjectName("label")
        WallpaperWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(WallpaperWindow)
        self.statusbar.setGeometry(QtCore.QRect(0,442,524,21))
        self.statusbar.setObjectName("statusbar")
        WallpaperWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WallpaperWindow)
        QtCore.QMetaObject.connectSlotsByName(WallpaperWindow)

    def retranslateUi(self, WallpaperWindow):
        WallpaperWindow.setWindowTitle(QtGui.QApplication.translate("WallpaperWindow", "Masaüstü Arkaplanı - Anatolya Başlangıç", None, QtGui.QApplication.UnicodeUTF8))
        self.WallpapersGroup.setTitle(QtGui.QApplication.translate("WallpaperWindow", "Arkaplanlar", None, QtGui.QApplication.UnicodeUTF8))
        self.showPictureGroup.setTitle(QtGui.QApplication.translate("WallpaperWindow", "Önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("WallpaperWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("WallpaperWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WallpaperWindow", "Masaüstü arkaplanınızı seçin.\n"
"Bilgi: Çok renkli arkaplanlar gözünüzü yorabileceği için siyah tonlarına yakın\n"
"arkaplanlar seçmenizi öneririz.", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
