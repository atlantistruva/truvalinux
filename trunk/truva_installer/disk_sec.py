# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disk_sec.ui'
#
# Created: PrÅŸ Mar 27 12:48:39 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.2
#
# WARNING! All changes made in this file will be lost!


import os
import sys
from qt import *

class Form2(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap("/media/hda6/Depolar/truva-svn/truva_installer/pixmaps/hdd.jpg")

        if not name:
            self.setName("Form2")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.pixmapLabel2 = QLabel(self.centralWidget(),"pixmapLabel2")
        self.pixmapLabel2.setGeometry(QRect(120,39,381,281))
        self.pixmapLabel2.setPixmap(self.image0)
        self.pixmapLabel2.setScaledContents(1)
	
        self.textLabel1 = QLabel(self.centralWidget(),"textLabel1")
        self.textLabel1.setGeometry(QRect(200,340,80,20))
        self.textLabel1.setPaletteForegroundColor(QColor(255,0,0))
        textLabel1_font = QFont(self.textLabel1.font())
        textLabel1_font.setBold(1)
        self.textLabel1.setFont(textLabel1_font)

        self.comboBox2 = QComboBox(0,self.centralWidget(),"comboBox2")
        self.comboBox2.setGeometry(QRect(200,370,230,22))

        self.pushButton5 = QPushButton(self.centralWidget(),"pushButton5")
        self.pushButton5.setGeometry(QRect(460,420,110,24))

        self.pushButton6 = QPushButton(self.centralWidget(),"pushButton6")
        self.pushButton6.setGeometry(QRect(30,420,110,24))


        self.languageChange()

        self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton5,SIGNAL("clicked()"),self.pushButton5_clicked)
        self.connect(self.pushButton6,SIGNAL("clicked()"),self.pushButton6_clicked)
#        self.connect(self.comboBox2,SIGNAL("textChanged(const QString&)"),self.comboBox2_textChanged)
        self.connect(self.comboBox2,SIGNAL("activated(const QString&)"),self.comboBox2_activated)
	
	self.disk_bul()
    
    def disk_bul(self):
	partition = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext | cut -d ' ' -f1")
	filesystem = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext")

	partname = partition.readlines()
	#print partname
	osname = filesystem.readline()
	
	for i in partname :
		ekle_i = i[0:9].strip()
		self.comboBox2.insertItem(ekle_i)
	


    def languageChange(self):
        self.setCaption(self.__tr("Anatolya Kurulum Sistemi- Disk Seçimi"))
        self.pushButton5.setText(self.__trUtf8("\xc4\xb0\x6c\x65\x72\x69"))
        self.pushButton6.setText(self.__trUtf8("\x59\x61\x72\x64\xc4\xb1\x6d"))
        self.textLabel1.setText(self.__trUtf8("\x44\x69\x73\x6b\x20\x53\x65\xc3\xa7\x69\x6d\x69"))


    def pushButton5_clicked(self):
        os.system("python /media/hda6/Depolar/truva-svn/truva_installer/paket_kur.py")
	self.hide()

    def pushButton6_clicked(self):
        print "Form2.pushButton6_clicked(): Not implemented yet"

    def comboBox2_textChanged(self,a0):
        print "Form2.comboBox2_textChanged(const QString&): Not implemented yet"

    def comboBox2_activated(self,a0):
	if os.path.isfile("/media/hda6/Depolar/truva-svn/truva_installer/files/kurulum_diski.txt"):
		os.remove("/media/hda6/Depolar/truva-svn/truva_installer/files/kurulum_diski.txt")
		disk_kur = open("/media/hda6/Depolar/truva-svn/truva_installer/files/kurulum_diski.txt","a")
	else:
		disk_kur = open("/media/hda6/Depolar/truva-svn/truva_installer/files/kurulum_diski.txt","a")
	
	kur = self.comboBox2.currentText()
	print "Kurulum diski : %s" %kur
	
	disk_kur.write('%s' %kur)
	disk_kur.close()


    def __tr(self,s,c = None):
        return qApp.translate("Form2",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("Form2",s,c,QApplication.UnicodeUTF8)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = Form2()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()


