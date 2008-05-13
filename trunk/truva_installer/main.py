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

class Form1(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

#        self.image0 = QPixmap(image0_data)
	self.image0 = QPixmap("/truva_installer/pixmaps/anatolia-kur.png")

        if not name:
            self.setName("Form1")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.pixmapLabel1 = QLabel(self.centralWidget(),"pixmapLabel1")
        self.pixmapLabel1.setGeometry(QRect(80,10,430,320))
        self.pixmapLabel1.setPixmap(self.image0)
        self.pixmapLabel1.setScaledContents(1)
	
        self.pushButton2 = QPushButton(self.centralWidget(),"pushButton2")
        self.pushButton2.setGeometry(QRect(460,430,110,24))

        self.pushButton3 = QPushButton(self.centralWidget(),"pushButton3")
        self.pushButton3.setGeometry(QRect(30,430,110,24))



        self.languageChange()

	#self.resize(QtCore.QSize(QtCore.QRect(0,0,x,y).size()).expandedTo(Form.minimumSizeHint()))
	self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton2,SIGNAL("clicked()"),self.pushButton2_clicked)
        self.connect(self.pushButton3,SIGNAL("clicked()"),self.pushButton3_clicked)


    def languageChange(self):
        self.setCaption(self.__tr("Anatolya Kurulum Sistemi"))
        self.pushButton2.setText(self.__tr("Devam Et"))
        self.pushButton3.setText(self.__trUtf8("\x59\x61\x72\x64\xc4\xb1\x6d"))


    def pushButton2_clicked(self):
        os.system("python /truva_installer/disk_sec.py")

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


