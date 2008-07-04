# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/mouseWindow.ui'
#
# Created: Fri Jul  4 20:54:24 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MouseWindow(object):
    def setupUi(self, MouseWindow):
        MouseWindow.setObjectName("MouseWindow")
        MouseWindow.resize(524,463)
        MouseWindow.setMinimumSize(QtCore.QSize(524,463))
        MouseWindow.setMaximumSize(QtCore.QSize(524,463))
        self.centralwidget = QtGui.QWidget(MouseWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,0,524,442))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10,20,231,16))
        self.label.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10,40,501,231))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50,30,131,151))
        self.label_2.setPixmap(QtGui.QPixmap(":/mouse-left/mouse-left.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(310,30,131,151))
        self.label_3.setPixmap(QtGui.QPixmap(":/mouse-right/mouse-right.png"))
        self.label_3.setObjectName("label_3")
        self.leftMouseSelection = QtGui.QRadioButton(self.groupBox)
        self.leftMouseSelection.setGeometry(QtCore.QRect(70,190,92,22))
        self.leftMouseSelection.setObjectName("leftMouseSelection")
        self.rightMouseSelection = QtGui.QRadioButton(self.groupBox)
        self.rightMouseSelection.setGeometry(QtCore.QRect(340,190,92,22))
        self.rightMouseSelection.setChecked(True)
        self.rightMouseSelection.setObjectName("rightMouseSelection")
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
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(320,410,75,26))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/go-next/go-next.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.clickSelectionGroup = QtGui.QGroupBox(self.centralwidget)
        self.clickSelectionGroup.setGeometry(QtCore.QRect(10,280,311,111))
        self.clickSelectionGroup.setObjectName("clickSelectionGroup")
        self.singleClickSelection = QtGui.QRadioButton(self.clickSelectionGroup)
        self.singleClickSelection.setGeometry(QtCore.QRect(20,20,92,22))
        self.singleClickSelection.setObjectName("singleClickSelection")
        self.doubleClickSelection = QtGui.QRadioButton(self.clickSelectionGroup)
        self.doubleClickSelection.setGeometry(QtCore.QRect(20,60,92,22))
        self.doubleClickSelection.setChecked(True)
        self.doubleClickSelection.setObjectName("doubleClickSelection")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330,270,161,111))
        self.label_4.setObjectName("label_4")
        MouseWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MouseWindow)
        self.statusBar.setGeometry(QtCore.QRect(0,442,524,21))
        self.statusBar.setObjectName("statusBar")
        MouseWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MouseWindow)
        QtCore.QMetaObject.connectSlotsByName(MouseWindow)

    def retranslateUi(self, MouseWindow):
        MouseWindow.setWindowTitle(QtGui.QApplication.translate("MouseWindow", "Fare Ayarları - Anatolya Başlangıç", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MouseWindow", "Farenizi hangi el ile kullanacağınızı seçin:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MouseWindow", "Fare seçenekleri", None, QtGui.QApplication.UnicodeUTF8))
        self.leftMouseSelection.setText(QtGui.QApplication.translate("MouseWindow", "Sol el", None, QtGui.QApplication.UnicodeUTF8))
        self.rightMouseSelection.setText(QtGui.QApplication.translate("MouseWindow", "Sağ el", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MouseWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("MouseWindow", "İptal", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MouseWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.clickSelectionGroup.setTitle(QtGui.QApplication.translate("MouseWindow", "Tıklama seçenkleri", None, QtGui.QApplication.UnicodeUTF8))
        self.singleClickSelection.setText(QtGui.QApplication.translate("MouseWindow", "Tek tıklama", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleClickSelection.setText(QtGui.QApplication.translate("MouseWindow", "Çift tıklama", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MouseWindow", "Dosyaları çift tıklama (ilk tıklamada\n"
"dosyalar seçilir)\n"
"ilemi yoksa tek tıklama\n"
"ile mi açmak istiyorsunuz ?\n"
"-çift tıklama önerilir-", None, QtGui.QApplication.UnicodeUTF8))

import startericons_rc
