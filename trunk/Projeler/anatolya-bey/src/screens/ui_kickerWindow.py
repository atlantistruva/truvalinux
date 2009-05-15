# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/kickerWindow.ui'
#
# Created: Fri Sep 26 20:00:35 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_KickerWindow(object):
    def setupUi(self, KickerWindow):
        KickerWindow.setObjectName("KickerWindow")
        KickerWindow.resize(QtCore.QSize(QtCore.QRect(0,0,524,444).size()).expandedTo(KickerWindow.minimumSizeHint()))
        KickerWindow.setMinimumSize(QtCore.QSize(524,444))
        KickerWindow.setMaximumSize(QtCore.QSize(524,444))
        KickerWindow.setWindowIcon(QtGui.QIcon(":/icon/icon.png"))

        self.centralwidget = QtGui.QWidget(KickerWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.kickersGroup = QtGui.QGroupBox(self.centralwidget)
        self.kickersGroup.setGeometry(QtCore.QRect(160,70,321,81))
        self.kickersGroup.setObjectName("kickersGroup")

        self.listKickers = QtGui.QComboBox(self.kickersGroup)
        self.listKickers.setGeometry(QtCore.QRect(50,30,251,22))
        self.listKickers.setObjectName("listKickers")

        self.viewGroup = QtGui.QGroupBox(self.centralwidget)
        self.viewGroup.setGeometry(QtCore.QRect(160,160,321,171))
        self.viewGroup.setObjectName("viewGroup")

        self.viewPicture = QtGui.QLabel(self.viewGroup)
        self.viewPicture.setGeometry(QtCore.QRect(50,40,241,91))
        self.viewPicture.setObjectName("viewPicture")

        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        self.cancelButton.setIcon(QtGui.QIcon(":/exit-button/application-exit.png"))
        self.cancelButton.setObjectName("cancelButton")

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        self.nextButton.setIcon(QtGui.QIcon(":/go-next/go-next.png"))
        self.nextButton.setObjectName("nextButton")

        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        self.backButton.setIcon(QtGui.QIcon(":/go-previous/go-previous.png"))
        self.backButton.setObjectName("backButton")

        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")

        self.isConfig = QtGui.QCheckBox(self.centralwidget)
        self.isConfig.setGeometry(QtCore.QRect(160,360,151,23))
        self.isConfig.setObjectName("isConfig")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0,290,161,161))
        self.label.setPixmap(QtGui.QPixmap(":/icon/penguen.png"))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40,270,111,36))
        self.label_2.setObjectName("label_2")
        KickerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KickerWindow)
        QtCore.QMetaObject.connectSlotsByName(KickerWindow)

    def retranslateUi(self, KickerWindow):
        KickerWindow.setWindowTitle(QtGui.QApplication.translate("KickerWindow", "Panel Seçenekleri - Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        KickerWindow.setStyleSheet(QtGui.QApplication.translate("KickerWindow", "QMainWindow {background-image: url(:/beyimage/beyimage.png);}", None, QtGui.QApplication.UnicodeUTF8))
        self.kickersGroup.setTitle(QtGui.QApplication.translate("KickerWindow", "Paneller", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Transparan", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "ModernTransparan", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Klasik", None, QtGui.QApplication.UnicodeUTF8))
        self.listKickers.addItem(QtGui.QApplication.translate("KickerWindow", "Modern", None, QtGui.QApplication.UnicodeUTF8))
        self.viewGroup.setTitle(QtGui.QApplication.translate("KickerWindow", "Önizleme", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("KickerWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("KickerWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("KickerWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("KickerWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Başlangıç</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fare ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Panel Ayarları</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arkaplan</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ağ ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><span style=\" font-weight:400;\">Son</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.isConfig.setText(QtGui.QApplication.translate("KickerWindow", "Paneli değiştirme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("KickerWindow", "KDE panelinizin\n"
        "şeklini seçin :)", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
