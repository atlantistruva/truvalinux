# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/partedWindow.ui'
#
# Created: Thu Aug 14 18:31:59 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_partedWindow(object):
    def setupUi(self, partedWindow):
        partedWindow.setObjectName("partedWindow")
        partedWindow.resize(661, 586)
        partedWindow.setStyleSheet("""#partedWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(partedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 591, 121))
        self.label.setObjectName("label")
        self.gpartedButton = QtGui.QPushButton(self.groupBox)
        self.gpartedButton.setGeometry(QtCore.QRect(20, 190, 311, 27))
        self.gpartedButton.setObjectName("gpartedButton")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        partedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(partedWindow)
        QtCore.QMetaObject.connectSlotsByName(partedWindow)

    def retranslateUi(self, partedWindow):
        partedWindow.setWindowTitle(QtGui.QApplication.translate("partedWindow", "Disk Bölümleme - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("partedWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00aaff;\">Kurulum yapabilmeniz için Truva'ya yer ayırmanız gerekmektedir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\">Gparted ile diskinizi bölümlendirebilirsiniz.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.gpartedButton.setText(QtGui.QApplication.translate("partedWindow", "Gparted\'i Aç", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("partedWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("partedWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
