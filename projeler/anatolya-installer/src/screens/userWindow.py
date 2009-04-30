# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screens/ui/userWindow.ui'
#
# Created: Wed Aug 13 21:10:33 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName("userWindow")
        userWindow.resize(661, 586)
        userWindow.setStyleSheet("""#userWindow { 
    background-image: url(:/artalan/artalan.png); }""")
        self.centralwidget = QtGui.QWidget(userWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.userPasswdLine_2 = QtGui.QLineEdit(self.groupBox_2)
        self.userPasswdLine_2.setGeometry(QtCore.QRect(30, 310, 191, 23))
        self.userPasswdLine_2.setEchoMode(QtGui.QLineEdit.Password)
        self.userPasswdLine_2.setObjectName("userPasswdLine_2")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 18))
        self.label.setObjectName("label")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 56, 18))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 131, 18))
        self.label_2.setObjectName("label_2")
        self.rootPasswdLine_1 = QtGui.QLineEdit(self.groupBox_2)
        self.rootPasswdLine_1.setGeometry(QtCore.QRect(30, 50, 191, 23))
        self.rootPasswdLine_1.setEchoMode(QtGui.QLineEdit.Password)
        self.rootPasswdLine_1.setObjectName("rootPasswdLine_1")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 56, 18))
        self.label_4.setObjectName("label_4")
        self.rootPasswdLine_2 = QtGui.QLineEdit(self.groupBox_2)
        self.rootPasswdLine_2.setGeometry(QtCore.QRect(30, 100, 191, 23))
        self.rootPasswdLine_2.setEchoMode(QtGui.QLineEdit.Password)
        self.rootPasswdLine_2.setObjectName("rootPasswdLine_2")
        self.userNameLine = QtGui.QLineEdit(self.groupBox_2)
        self.userNameLine.setGeometry(QtCore.QRect(30, 210, 191, 23))
        self.userNameLine.setEchoMode(QtGui.QLineEdit.Normal)
        self.userNameLine.setObjectName("userNameLine")
        self.userPasswdLine_1 = QtGui.QLineEdit(self.groupBox_2)
        self.userPasswdLine_1.setGeometry(QtCore.QRect(30, 260, 191, 23))
        self.userPasswdLine_1.setEchoMode(QtGui.QLineEdit.Password)
        self.userPasswdLine_1.setObjectName("userPasswdLine_1")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 81, 18))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 56, 18))
        self.label_6.setObjectName("label_6")
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(30, 140, 201, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(230, 40, 271, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(240, 200, 191, 61))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)
        self.nextButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 2, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 2, 1, 1, 1)
        userWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(QtGui.QApplication.translate("userWindow", "Kullanıcı Ayarları - Anatolya Kurulum", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("userWindow", "Kullanıcı Ayarları", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("userWindow", "Yönetici Parolası:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("userWindow", "Tekrar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("userWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kullanıcı Oluştur:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("userWindow", "Şifre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("userWindow", "Kullanıcı adı:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("userWindow", "Tekrar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("userWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aaff;\">* root (sistem yöneticisi) parolası</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aaff;\">sisteminizi koruyabilmeniz için gereklidir.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("userWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aaff;\">* Yeni bir kullanıcı oluşturunuz.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aaff;\">Sisteme root kullanıcısı ile girmeniz kesinlikle</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#00aaff;\">önerilmemektedir.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("userWindow", "İleri", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("userWindow", "Geri", None, QtGui.QApplication.UnicodeUTF8))

import anatolyaimages_rc
