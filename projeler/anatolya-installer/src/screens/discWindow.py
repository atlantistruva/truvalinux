# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/discWindow.ui'
#
# Created: Wed Aug 13 07:14:35 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_discWindow(object):
    def setupUi(self, discWindow):
        discWindow.setObjectName("discWindow")
        discWindow.resize(661, 686)
        discWindow.setStyleSheet("""#discWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(discWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.discGroup = QtGui.QGroupBox(self.centralwidget)
        self.discGroup.setFlat(True)
        self.discGroup.setObjectName("discGroup")
        self.label = QtGui.QLabel(self.discGroup)
        self.label.setGeometry(QtCore.QRect(0, 10, 431, 91))
        self.label.setObjectName("label")
        self.groupBox = QtGui.QGroupBox(self.discGroup)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 471, 191))
        self.groupBox.setObjectName("groupBox")
        self.discsList = QtGui.QComboBox(self.groupBox)
        self.discsList.setGeometry(QtCore.QRect(110, 80, 241, 22))
        self.discsList.setObjectName("discsList")
        self.gridLayout.addWidget(self.discGroup, 1, 0, 1, 3)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        discWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(discWindow)
        QtCore.QMetaObject.connectSlotsByName(discWindow)

    def retranslateUi(self, discWindow):
        discWindow.setWindowTitle(QtGui.QApplication.translate("discWindow", "Disk Seçimi - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("discWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("discWindow", "Diskinizi bölümlediyseniz, Truva\'yı kuracağınız disk bölümünü seçiniz.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("discWindow", "Bölümler", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("discWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
