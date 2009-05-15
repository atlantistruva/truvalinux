# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/mouseWindow.ui'
#
# Created: Fri Sep 26 20:15:44 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MouseWindow(object):
    def setupUi(self, MouseWindow):
        MouseWindow.setObjectName("MouseWindow")
        MouseWindow.resize(QtCore.QSize(QtCore.QRect(0,0,524,444).size()).expandedTo(MouseWindow.minimumSizeHint()))
        MouseWindow.setMinimumSize(QtCore.QSize(524,444))
        MouseWindow.setMaximumSize(QtCore.QSize(524,444))
        MouseWindow.setWindowIcon(QtGui.QIcon(":/icon/icon.png"))

        self.centralwidget = QtGui.QWidget(MouseWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170,80,301,211))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10,20,131,151))
        self.label_2.setPixmap(QtGui.QPixmap(":/mouse-left/mouse-left.png"))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(160,20,131,151))
        self.label_3.setPixmap(QtGui.QPixmap(":/mouse-right/mouse-right.png"))
        self.label_3.setObjectName("label_3")

        self.leftMouseSelection = QtGui.QRadioButton(self.groupBox)
        self.leftMouseSelection.setGeometry(QtCore.QRect(40,180,92,22))
        self.leftMouseSelection.setObjectName("leftMouseSelection")

        self.rightMouseSelection = QtGui.QRadioButton(self.groupBox)
        self.rightMouseSelection.setGeometry(QtCore.QRect(190,180,92,22))
        self.rightMouseSelection.setChecked(True)
        self.rightMouseSelection.setObjectName("rightMouseSelection")

        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(True)
        self.backButton.setGeometry(QtCore.QRect(240,410,75,26))
        self.backButton.setIcon(QtGui.QIcon(":/go-previous/go-previous.png"))
        self.backButton.setObjectName("backButton")

        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(430,410,75,26))
        self.cancelButton.setIcon(QtGui.QIcon(":/exit-button/application-exit.png"))
        self.cancelButton.setObjectName("cancelButton")

        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        self.nextButton.setIcon(QtGui.QIcon(":/go-next/go-next.png"))
        self.nextButton.setObjectName("nextButton")

        self.clickSelectionGroup = QtGui.QGroupBox(self.centralwidget)
        self.clickSelectionGroup.setGeometry(QtCore.QRect(170,300,301,101))
        self.clickSelectionGroup.setFlat(True)
        self.clickSelectionGroup.setObjectName("clickSelectionGroup")

        self.singleClickSelection = QtGui.QRadioButton(self.clickSelectionGroup)
        self.singleClickSelection.setGeometry(QtCore.QRect(50,61,92,31))
        self.singleClickSelection.setObjectName("singleClickSelection")

        self.doubleClickSelection = QtGui.QRadioButton(self.clickSelectionGroup)
        self.doubleClickSelection.setGeometry(QtCore.QRect(50,20,92,31))
        self.doubleClickSelection.setChecked(True)
        self.doubleClickSelection.setObjectName("doubleClickSelection")

        self.basementsLabel = QtGui.QLabel(self.centralwidget)
        self.basementsLabel.setGeometry(QtCore.QRect(50,110,81,121))
        self.basementsLabel.setObjectName("basementsLabel")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0,290,161,151))
        self.label.setPixmap(QtGui.QPixmap(":/icon/penguen.png"))
        self.label.setObjectName("label")

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30,250,131,61))
        self.label_4.setObjectName("label_4")
        MouseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MouseWindow)
        QtCore.QMetaObject.connectSlotsByName(MouseWindow)

    def retranslateUi(self, MouseWindow):
        MouseWindow.setWindowTitle(QtGui.QApplication.translate("MouseWindow", "Fare Ayarları - Anatolya Bey", None, QtGui.QApplication.UnicodeUTF8))
        MouseWindow.setStyleSheet(QtGui.QApplication.translate("MouseWindow", "QMainWindow {background-image: url(:/beyimage/beyimage.png);}", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MouseWindow", "Fare seçenekleri", None, QtGui.QApplication.UnicodeUTF8))
        self.leftMouseSelection.setText(QtGui.QApplication.translate("MouseWindow", "Sol el", None, QtGui.QApplication.UnicodeUTF8))
        self.rightMouseSelection.setText(QtGui.QApplication.translate("MouseWindow", "Sağ el", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MouseWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("MouseWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MouseWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.clickSelectionGroup.setTitle(QtGui.QApplication.translate("MouseWindow", "Tıklama seçenkleri", None, QtGui.QApplication.UnicodeUTF8))
        self.singleClickSelection.setText(QtGui.QApplication.translate("MouseWindow", "Tek tıklama", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleClickSelection.setText(QtGui.QApplication.translate("MouseWindow", "Çift tıklama", None, QtGui.QApplication.UnicodeUTF8))
        self.basementsLabel.setText(QtGui.QApplication.translate("MouseWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Başlangıç</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Fare ayarları</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Panel ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arkaplan</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ağ ayarları</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Son</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MouseWindow", "Fare ayarlarınızı\n"
        "yapabilirsiniz :)", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
