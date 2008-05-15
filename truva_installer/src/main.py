# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Prş Mar 27 12:48:22 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.2
#
# WARNING! All changes made in this file will be lost!


import os
import sys
from qt import *
from const import *


class Form1(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        image_dir = pixmap_dir + "anatolia-kur.png"
	self.image0 = QPixmap(image_dir)

        if not name:
            self.setName("Form1")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.frame4 = QFrame(self.centralWidget(),"frame4")
        self.frame4.setGeometry(QRect(80,20,430,320))
        self.frame4.setFrameShape(QFrame.StyledPanel)
        self.frame4.setFrameShadow(QFrame.Raised)

        self.pixmapLabel1 = QLabel(self.frame4,"pixmapLabel1")
        self.pixmapLabel1.setGeometry(QRect(10,10,410,300))
        self.pixmapLabel1.setPixmap(self.image0)
        self.pixmapLabel1.setScaledContents(1)
        self.pixmapLabel1.setAlignment(QLabel.AlignCenter)

        self.textLabel1 = QLabel(self.centralWidget(),"textLabel1")
        self.textLabel1.setGeometry(QRect(80,350,431,21))
        self.textLabel1.setAlignment(QLabel.AlignCenter)
	
	self.pushButton2 = QPushButton(self.centralWidget(),"pushButton2")
        self.pushButton2.setGeometry(QRect(460,430,110,24))

        self.pushButton3 = QPushButton(self.centralWidget(),"pushButton3")
        self.pushButton3.setGeometry(QRect(30,430,110,24))


        self.languageChange()

	self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton2,SIGNAL("clicked()"),self.pushButton2_clicked)
        self.connect(self.pushButton3,SIGNAL("clicked()"),self.pushButton3_clicked)


    def languageChange(self):
        self.setCaption(self.__tr("Anatolya Kurulum Sistemi"))
        self.pushButton2.setText(self.__tr("Devam Et"))
        self.pushButton3.setText(self.__trUtf8("\x59\x61\x72\x64\xc4\xb1\x6d"))
        self.textLabel1.setText(self.__trUtf8("\x54\x72\x75\x76\x61\x20\x4c\x69\x6e\x75\x78\x20\x41\x6e\x61\x74\x6f\x6c\x79\x61\x20\x4b\x75\x72\x75\x6c\x75\x6d\x20\x53\x69\x73\x74\x65\x6d\x69\x27\x6e\x65\x20\x68\x6f\xc5\x9f\x67\x65\x6c\x64\x69\x6e\x69\x7a\x2e\x2e\x2e"))


    def pushButton2_clicked(self):
	self.hide()	
	cmd = "python " + install_dir + "disk_sec.py"
        os.system(cmd)


    def pushButton3_clicked(self):
        print "Form1.pushButton3_clicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("Form1",s,c,QApplication.UnicodeUTF8)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = Form1()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()


