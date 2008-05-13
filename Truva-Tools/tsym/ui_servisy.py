# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_servisy.ui'
#
# Created: Tue May 13 17:36:30 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ServisYoneticisi(object):
    def setupUi(self, ServisYoneticisi):
        ServisYoneticisi.setObjectName("ServisYoneticisi")
        ServisYoneticisi.resize(QtCore.QSize(QtCore.QRect(0,0,497,332).size()).expandedTo(ServisYoneticisi.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(ServisYoneticisi)
        self.centralwidget.setGeometry(QtCore.QRect(0,30,497,279))
        self.centralwidget.setObjectName("centralwidget")

        self.servisBox = QtGui.QGroupBox(self.centralwidget)
        self.servisBox.setGeometry(QtCore.QRect(0,0,221,241))
        self.servisBox.setObjectName("servisBox")

        self.servisList = QtGui.QListWidget(self.servisBox)
        self.servisList.setGeometry(QtCore.QRect(10,20,201,211))
        self.servisList.setObjectName("servisList")

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20,250,75,28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120,250,75,28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.durumBox = QtGui.QGroupBox(self.centralwidget)
        self.durumBox.setGeometry(QtCore.QRect(230,0,261,241))
        self.durumBox.setObjectName("durumBox")

        self.label = QtGui.QLabel(self.durumBox)
        self.label.setGeometry(QtCore.QRect(10,70,54,18))
        self.label.setObjectName("label")

        self.durumLabel = QtGui.QLabel(self.durumBox)
        self.durumLabel.setGeometry(QtCore.QRect(70,70,54,18))
        self.durumLabel.setObjectName("durumLabel")

        self.label_2 = QtGui.QLabel(self.durumBox)
        self.label_2.setGeometry(QtCore.QRect(10,90,101,18))
        self.label_2.setObjectName("label_2")

        self.acilis_cLabel = QtGui.QLabel(self.durumBox)
        self.acilis_cLabel.setGeometry(QtCore.QRect(110,90,54,18))
        self.acilis_cLabel.setObjectName("acilis_cLabel")

        self.label_3 = QtGui.QLabel(self.durumBox)
        self.label_3.setGeometry(QtCore.QRect(10,30,61,18))
        self.label_3.setObjectName("label_3")

        self.sad_Label = QtGui.QLabel(self.durumBox)
        self.sad_Label.setGeometry(QtCore.QRect(80,30,54,18))
        self.sad_Label.setObjectName("sad_Label")

        self.line = QtGui.QFrame(self.durumBox)
        self.line.setGeometry(QtCore.QRect(10,200,241,16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.checkBox = QtGui.QCheckBox(self.durumBox)
        self.checkBox.setGeometry(QtCore.QRect(139,210,101,23))
        self.checkBox.setObjectName("checkBox")
        ServisYoneticisi.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(ServisYoneticisi)
        self.menubar.setGeometry(QtCore.QRect(0,0,497,30))
        self.menubar.setObjectName("menubar")

        self.menuDosya = QtGui.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")

        self.menuYard_m = QtGui.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        ServisYoneticisi.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(ServisYoneticisi)
        self.statusbar.setGeometry(QtCore.QRect(0,309,497,23))
        self.statusbar.setObjectName("statusbar")
        ServisYoneticisi.setStatusBar(self.statusbar)

        self.actionYap_land_r = QtGui.QAction(ServisYoneticisi)
        self.actionYap_land_r.setObjectName("actionYap_land_r")

        self.action_k = QtGui.QAction(ServisYoneticisi)
        self.action_k.setObjectName("action_k")

        self.actionServis_Y_neticisi_Hakk_nda = QtGui.QAction(ServisYoneticisi)
        self.actionServis_Y_neticisi_Hakk_nda.setObjectName("actionServis_Y_neticisi_Hakk_nda")

        self.actionQT_Hakk_nda = QtGui.QAction(ServisYoneticisi)
        self.actionQT_Hakk_nda.setObjectName("actionQT_Hakk_nda")
        self.menuDosya.addAction(self.actionYap_land_r)
        self.menuDosya.addAction(self.action_k)
        self.menuYard_m.addAction(self.actionServis_Y_neticisi_Hakk_nda)
        self.menuYard_m.addAction(self.actionQT_Hakk_nda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(ServisYoneticisi)
        QtCore.QMetaObject.connectSlotsByName(ServisYoneticisi)

    def retranslateUi(self, ServisYoneticisi):
        ServisYoneticisi.setWindowTitle(QtGui.QApplication.translate("ServisYoneticisi", "Servis Yöneticisi", None, QtGui.QApplication.UnicodeUTF8))
        self.servisBox.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Sistem servisleri:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ServisYoneticisi", "Başlat", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("ServisYoneticisi", "Durdur", None, QtGui.QApplication.UnicodeUTF8))
        self.durumBox.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Servis durumu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ServisYoneticisi", "Durum:", None, QtGui.QApplication.UnicodeUTF8))
        self.durumLabel.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ServisYoneticisi", "Açılışta çalıştır ?:", None, QtGui.QApplication.UnicodeUTF8))
        self.acilis_cLabel.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ServisYoneticisi", "Servis adı:", None, QtGui.QApplication.UnicodeUTF8))
        self.sad_Label.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("ServisYoneticisi", "Açılışta çalıştır", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDosya.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Dosya", None, QtGui.QApplication.UnicodeUTF8))
        self.menuYard_m.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Yardım", None, QtGui.QApplication.UnicodeUTF8))
        self.actionYap_land_r.setText(QtGui.QApplication.translate("ServisYoneticisi", "Yapılandır", None, QtGui.QApplication.UnicodeUTF8))
        self.action_k.setText(QtGui.QApplication.translate("ServisYoneticisi", "Çık", None, QtGui.QApplication.UnicodeUTF8))
        self.actionServis_Y_neticisi_Hakk_nda.setText(QtGui.QApplication.translate("ServisYoneticisi", "Servis Yöneticisi Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQT_Hakk_nda.setText(QtGui.QApplication.translate("ServisYoneticisi", "QT Hakkında", None, QtGui.QApplication.UnicodeUTF8))

