# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/installWindow.ui'
#
# Created: Wed Aug 13 22:15:39 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_installWindow(object):
    def setupUi(self, installWindow):
        installWindow.setObjectName("installWindow")
        installWindow.resize(661, 609)
        installWindow.setStyleSheet("""#installWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(installWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 3)
        self.installInfoGroup = QtGui.QGroupBox(self.centralwidget)
        self.installInfoGroup.setFlat(True)
        self.installInfoGroup.setObjectName("installInfoGroup")
        self.gridLayout_2 = QtGui.QGridLayout(self.installInfoGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtGui.QSpacerItem(20, 250, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.installBar = QtGui.QProgressBar(self.installInfoGroup)
        self.installBar.setProperty("value", QtCore.QVariant(0))
        self.installBar.setObjectName("installBar")
        self.gridLayout_2.addWidget(self.installBar, 9, 0, 1, 2)
        self.label = QtGui.QLabel(self.installInfoGroup)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.installInfoGroup)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)
        self.packageLabel = QtGui.QLabel(self.installInfoGroup)
        self.packageLabel.setObjectName("packageLabel")
        self.gridLayout_2.addWidget(self.packageLabel, 4, 1, 1, 1)
        self.categoryLabel = QtGui.QLabel(self.installInfoGroup)
        self.categoryLabel.setObjectName("categoryLabel")
        self.gridLayout_2.addWidget(self.categoryLabel, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.installInfoGroup)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 2)
        self.line = QtGui.QFrame(self.installInfoGroup)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 7, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.installInfoGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.randomPicture = QtGui.QLabel(self.installInfoGroup)
        self.randomPicture.setPixmap(QtGui.QPixmap(":/betizler/installlogo.png"))
        self.randomPicture.setObjectName("randomPicture")
        self.gridLayout_2.addWidget(self.randomPicture, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 1, 1, 1)
        self.infoLabel = QtGui.QLabel(self.installInfoGroup)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout_2.addWidget(self.infoLabel, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.installInfoGroup)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.installInfoGroup, 1, 0, 1, 3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 3, 1, 1, 1)
        installWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(installWindow)
        QtCore.QMetaObject.connectSlotsByName(installWindow)

    def retranslateUi(self, installWindow):
        installWindow.setWindowTitle(QtGui.QApplication.translate("installWindow", "Paketler Kuruluyor - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("installWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("installWindow", "Kurulan paket\t:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("installWindow", "Kategori\t\t:", None, QtGui.QApplication.UnicodeUTF8))
        self.packageLabel.setText(QtGui.QApplication.translate("installWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.categoryLabel.setText(QtGui.QApplication.translate("installWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("installWindow", "Toplam ilerleme :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("installWindow", "Paketler kuruluyor...\n"
"Bu işlem biraz zaman alabilir.\n"
"Şimdi kendinize bir kahve yapabilir ve Truva\'nızın kurulmasını bekleyebilirsiniz.", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("installWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
