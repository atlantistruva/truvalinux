# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/endWindow.ui'
#
# Created: Fri Aug 15 16:06:50 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_endWindow(object):
    def setupUi(self, endWindow):
        endWindow.setObjectName("endWindow")
        endWindow.resize(661, 586)
        endWindow.setStyleSheet("""#endWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(endWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 561, 301))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/dialog-ok-apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        endWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(endWindow)
        QtCore.QMetaObject.connectSlotsByName(endWindow)

    def retranslateUi(self, endWindow):
        endWindow.setWindowTitle(QtGui.QApplication.translate("endWindow", "Son - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("endWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#00aaff;\">Tebrikler! Truva GNU/Linux\'unuzu kurdunuz.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\">\'Bitir\' düğmesi ile sistemi yeniden başlatabilirsiniz.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\">Truva açıltıktan sonra oluşturduğunuz kullanıcı adınızla giriş yapabilir daha</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\">sonra Anatolya Bey ile gerekli ayarlar yapıp Truva</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#00aaff;\">kullanmaya başlayabilirsiniz.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("endWindow", "Bitir", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("endWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
