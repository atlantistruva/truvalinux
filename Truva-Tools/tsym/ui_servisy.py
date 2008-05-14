# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_servisy.ui'
#
# Created: Wed May 14 16:30:23 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ServisYoneticisi(object):
    def setupUi(self, ServisYoneticisi):
        ServisYoneticisi.setObjectName("ServisYoneticisi")
        ServisYoneticisi.setWindowModality(QtCore.Qt.NonModal)
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

        self.calistirButton = QtGui.QPushButton(self.centralwidget)
        self.calistirButton.setGeometry(QtCore.QRect(20,250,75,28))
        self.calistirButton.setObjectName("calistirButton")

        self.durdurButton = QtGui.QPushButton(self.centralwidget)
        self.durdurButton.setGeometry(QtCore.QRect(120,250,75,28))
        self.durdurButton.setObjectName("durdurButton")

        self.durumBox = QtGui.QGroupBox(self.centralwidget)
        self.durumBox.setGeometry(QtCore.QRect(230,0,261,241))
        self.durumBox.setObjectName("durumBox")

        self.label = QtGui.QLabel(self.durumBox)
        self.label.setGeometry(QtCore.QRect(10,70,54,18))
        self.label.setObjectName("label")

        self.durumLabel = QtGui.QLabel(self.durumBox)
        self.durumLabel.setGeometry(QtCore.QRect(70,70,91,18))
        self.durumLabel.setObjectName("durumLabel")

        self.label_2 = QtGui.QLabel(self.durumBox)
        self.label_2.setGeometry(QtCore.QRect(10,90,101,18))
        self.label_2.setObjectName("label_2")

        self.acilis_cLabel = QtGui.QLabel(self.durumBox)
        self.acilis_cLabel.setGeometry(QtCore.QRect(110,90,71,18))
        self.acilis_cLabel.setObjectName("acilis_cLabel")

        self.label_3 = QtGui.QLabel(self.durumBox)
        self.label_3.setGeometry(QtCore.QRect(10,30,61,18))
        self.label_3.setObjectName("label_3")

        self.sad_Label = QtGui.QLabel(self.durumBox)
        self.sad_Label.setGeometry(QtCore.QRect(80,30,171,18))
        self.sad_Label.setObjectName("sad_Label")

        self.line = QtGui.QFrame(self.durumBox)
        self.line.setGeometry(QtCore.QRect(10,200,241,16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")

        self.acalistirButton = QtGui.QCheckBox(self.durumBox)
        self.acalistirButton.setGeometry(QtCore.QRect(139,210,101,23))
        self.acalistirButton.setObjectName("acalistirButton")
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

        self.actionYapilandir = QtGui.QAction(ServisYoneticisi)
        self.actionYapilandir.setObjectName("actionYapilandir")

        self.actionCik = QtGui.QAction(ServisYoneticisi)
        self.actionCik.setObjectName("actionCik")

        self.syHakkinda = QtGui.QAction(ServisYoneticisi)
        self.syHakkinda.setObjectName("syHakkinda")

        self.qtHakkinda = QtGui.QAction(ServisYoneticisi)
        self.qtHakkinda.setObjectName("qtHakkinda")
        self.menuDosya.addAction(self.actionYapilandir)
        self.menuDosya.addAction(self.actionCik)
        self.menuYard_m.addAction(self.syHakkinda)
        self.menuYard_m.addAction(self.qtHakkinda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(ServisYoneticisi)
        QtCore.QMetaObject.connectSlotsByName(ServisYoneticisi)

    def retranslateUi(self, ServisYoneticisi):
        ServisYoneticisi.setWindowTitle(QtGui.QApplication.translate("ServisYoneticisi", "Servis Yöneticisi", None, QtGui.QApplication.UnicodeUTF8))
        self.servisBox.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Sistem servisleri:", None, QtGui.QApplication.UnicodeUTF8))
        self.calistirButton.setText(QtGui.QApplication.translate("ServisYoneticisi", "Başlat", None, QtGui.QApplication.UnicodeUTF8))
        self.durdurButton.setText(QtGui.QApplication.translate("ServisYoneticisi", "Durdur", None, QtGui.QApplication.UnicodeUTF8))
        self.durumBox.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Servis durumu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ServisYoneticisi", "Durum:", None, QtGui.QApplication.UnicodeUTF8))
        self.durumLabel.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ServisYoneticisi", "Açılışta çalıştır ?:", None, QtGui.QApplication.UnicodeUTF8))
        self.acilis_cLabel.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ServisYoneticisi", "Servis adı:", None, QtGui.QApplication.UnicodeUTF8))
        self.sad_Label.setText(QtGui.QApplication.translate("ServisYoneticisi", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.acalistirButton.setText(QtGui.QApplication.translate("ServisYoneticisi", "Açılışta çalıştır", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDosya.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Dosya", None, QtGui.QApplication.UnicodeUTF8))
        self.menuYard_m.setTitle(QtGui.QApplication.translate("ServisYoneticisi", "Yardım", None, QtGui.QApplication.UnicodeUTF8))
        self.actionYapilandir.setText(QtGui.QApplication.translate("ServisYoneticisi", "Yapılandır", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCik.setText(QtGui.QApplication.translate("ServisYoneticisi", "Çık", None, QtGui.QApplication.UnicodeUTF8))
        self.syHakkinda.setText(QtGui.QApplication.translate("ServisYoneticisi", "Servis Yöneticisi Hakkında", None, QtGui.QApplication.UnicodeUTF8))
        self.qtHakkinda.setText(QtGui.QApplication.translate("ServisYoneticisi", "QT Hakkında", None, QtGui.QApplication.UnicodeUTF8))

