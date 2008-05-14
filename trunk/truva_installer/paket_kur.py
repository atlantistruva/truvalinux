# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paket_kur.ui'
#
# Created: Prş Mar 27 12:48:56 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.2
#
# WARNING! All changes made in this file will be lost!


import os
import sys
import shutil
from qt import *

mntdir = '/truva_installer/mount'

class Form3(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap("/media/hda6/Depolar/truva-svn/truva_installer/pixmaps/anatolia-kur.png")

        if not name:
            self.setName("Form3")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.pixmapLabel3 = QLabel(self.centralWidget(),"pixmapLabel3")
        self.pixmapLabel3.setGeometry(QRect(100,19,401,281))
        self.pixmapLabel3.setPixmap(self.image0)
        self.pixmapLabel3.setScaledContents(1)

        self.textLabel1 = QLabel(self.centralWidget(),"textLabel1")
        self.textLabel1.setGeometry(QRect(30,320,110,20))

        self.textLabel2 = QLabel(self.centralWidget(),"textLabel2")
        self.textLabel2.setGeometry(QRect(160,320,100,20))
	
        self.textLabel3 = QLabel(self.centralWidget(),"textLabel3")
        self.textLabel3.setGeometry(QRect(30,349,110,20))
	
	self.textLabel4 = QLabel(self.centralWidget(),"textLabel4")
        self.textLabel4.setGeometry(QRect(160,350,360,20))

        self.pushButton7 = QPushButton(self.centralWidget(),"pushButton7")
        self.pushButton7.setGeometry(QRect(460,420,110,24))

        self.pushButton8 = QPushButton(self.centralWidget(),"pushButton8")
        self.pushButton8.setGeometry(QRect(30,420,110,24))

        self.progressBar2 = QProgressBar(self.centralWidget(),"progressBar2")
        self.progressBar2.setGeometry(QRect(32,379,540,23))



        self.languageChange()

        self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

	self.paket_kur()
	

    def paket_kur(self):
	kur = open( '/media/hda6/Depolar/truva-svn/truva_installer/files/kurulum_diski.txt' , 'r' )
	kurulum_diski = kur.readline()
	 
	if os.path.isfile("/media/hda6/Depolar/truva-svn/truva_installer/files/diskler.txt"):
		os.remove("/media/hda6/Depolar/truva-svn/truva_installer/files/diskler.txt")
		disk_liste = "fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext > /media/hda6/Depolar/truva-svn/truva_installer/files/diskler.txt"
		os.system(disk_liste)
	else:
		disk_liste = "fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext > /media/hda6/Depolar/truva-svn/truva_installer/files/diskler.txt"
		os.system(disk_liste)
	
	# diskler okunuyor
        disk_oku = open("/media/hda6/Depolar/truva-svn/truva_installer/files/diskler.txt",'r')
	
	# fstab dosyasi eklemek uzere aciliyor
	if os.path.isfile("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab"):
		os.remove("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab")
		fstab = open("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab","a")
	else:
		fstab = open("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab","a")
	
	dizinler = []
	
	EOF = False
	while not EOF:

		line = disk_oku.readline()
		disk_name = line[0:9]
		disk_mount = "/media/" + disk_name[5:9]
		disk_format = line[52:54]
		
		if disk_format == '82' and disk_name <> kurulum_diski:
			fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,"swap","swap","defaults","0","0"))
		elif disk_format == '83' and disk_name <> kurulum_diski:
			fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"ext3", "defaults,noatime","1","1"))
			dizinler.append(disk_mount)
		elif disk_format == '83' and kurulum_diski == disk_name:
			fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,"/","ext3", "defaults,noatime", "1","1"))
		elif (disk_format == '86') or (disk_format == '87'):
			fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"ntfs", "defaults,noatime", "0","0"))
			dizinler.append(disk_mount)
		elif (disk_format == ' b') or (disk_format == ' c') or (disk_format == ' e'):
			fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"vfat", "defaults,noatime", "0","0"))
			dizinler.append(disk_mount)
		else: break

	# cd/dvd aygitlari ekleniyor.
	fstab = open("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab","a")
			
        blocks = os.listdir("/sys/block")
        for block in blocks:
        	if block[:2] == "hd" or block[:2] == "sd":
			medya_oku = os.popen( 'cat /sys/block/%s/device/media' % block )
			medya = medya_oku.readline()
			medya_type = medya[0:5]
			#print medya_type
			medya_disk = "/dev/" + block
			medya_mount = "/mnt/" + block
			
			if medya_type == 'cdrom':
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n'%(medya_disk,medya_mount,"iso9660","noauto,user,ro","0","0"))
				dizinler.append(medya_mount)
			elif medya_type == 'dvd': 
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (medya_disk,medya_mount,"udf", "noauto,user,ro", "0","0"))
				dizinler.append(medya_mount)
			
	#Standart fstab ogeleri ekleniyor
	fstab.write( '%-22s %-13s %-9s %-19s %-3s %s\n' %("devpts","/dev/pts","devpts","gid=5,mode=620","0","0"))
	fstab.write( '%-22s %-13s %-9s %-19s %-3s %s\n' %("proc","/proc","proc","nosuid,noexec","0","0") )
	fstab.write( '%-22s %-13s %-9s %-19s %-3s %s\n' %("/dev/tmpfs","/dev/shm","tmpfs","size=10%,mode=0777","0","0"))
	fstab.write( '%-22s %-13s %-9s %-19s %-3s %s\n' %("/dev/fd0","/mnt/floppy","auto","noauto,owner","0","0"))
	
	fstab.write("\n")
	fstab.close()
	# fstab olusturma tamamlandi.
	
	print dizinler
	
	root_mount = 'mount %s %s' %(kurulum_diski,mntdir)
	
	osres = os.system( root_mount )
	if osres != 0:
		print "hata var"
		#write_status('\nKritik bir hata olu�tu.\nKurulum iptal edildi !')
		return
	else:	
		oscmd = ( 'mkdir %s/boot' % mntdir )
		os.system( oscmd )
				
		for device in ["/dev/hda","/dev/hdb","/dev/hdc","/dev/hdd","/dev/hde","/dev/hdf","/dev/hdg","/dev/hdh","/dev/sr0","/dev/sr1","/dev/sr2", "/dev/sr3","/dev/pcd0","/dev/pcd1","/dev/pcd2","/dev/pcd3","/dev/aztcd","/dev/cdu535","/dev/gscd","/dev/sonycd", "/dev/optcd","/dev/sjcd","/dev/mcdx0","/dev/mcdx1","/dev/sbpcd","/dev/cm205cd","/dev/cm206cd","/dev/mcd"]:
		#,"/dev/sda1","/dev/sda2","/dev/sdb1","/dev/sdb2"]:
			
			cd_mount = 'mount -o ro -t iso9660 %s /var/log/mount' %device
			status = os.system( cd_mount )
			
			print "\nStatus : %s" %status
			
			if status == 0:
				print "Kurulum cd\'si %s cd/dvd sürücüsünde bulundu...\n\n" %device
				dev_cd = device
				break
			else:
				print "\nKurulum cd\'si %s cd/dvd sürücüsünde bulunamadı...\n\n" %device
				continue
		try:
			#if ( g_gui == 1 ):
			#	print "hata var"
				#write_status('\nKurulum i�lemi devam ediyor.\n\nPaketler kurulmaya ba�lan�yor...') 
			#else:
			#	print( 'Paketler kurulmaya ba�lan�yor...' )	

			#os.system('rm -rf *')
			for dizin in ["a","ap","d","kde","kdei","l","n","t","tcl","x","xap","xorg-app","xorg-data","xorg-font","xorg-input","xorg-lib","xorg-proto","xorg-util","xorg-video"]:
				target_dir = "/var/log/mount/Paketler/" + dizin
				
				if os.path.isdir(target_dir):
					paket_listesi = os.listdir( target_dir )
					for package in paket_listesi:
						#if ( g_gui == 1 ):
						#	write_status('\nKurulum i�lemi devam ediyor.\nKurulan Kategori : %s\nKurulan paket : %s' %(dizin,package))  
						#else:
						#	print( 'Kurulan paket : %s' %package) 	
						
						print('Kurulan paket : %s' %package)
						 	
						oscmd = ('installpkg -root %s %s/%s' %(mntdir,target_dir,package))
						os.system( oscmd )
				else:
					print('%s kategorisi bulunamadı...') %dizin		
		except:
			print " Bir hata oluştu..."


		for disk_dizin in dizinler:
			if not os.path.isdir('/media/hda6/Depolar/truva-svn/truva_installer/mount/' + disk_dizin):
		                result = os.makedirs("%s/%s" %(mntdir,disk_dizin))
                		if result != None:
                    			print "%s dizini oluşturulamadı..." %disk_dizin
                    			return 0
				
		self.textLabel1.setText('<font color="#FF6D19">Font ayarları yapılıyor...</font>')
		
		#if ( g_gui == 1 ):
		#	write_status('\nKurulum süreci devam ediyor.\n\nFont ayarları yapılıyor...') 
		#else:
		#	print( 'Font ayarları yapılıyor...' )

		#print self.__trUtf8('Font ayarları yapılıyor...')

		##Kurulum sonrasi ayarlari yapiliyor
		for fontdir in ["100dpi", "75dpi", "Type1", "cyrillic"]: 		
			setup_0 = ('chroot %s /usr/bin/mkfontscale /usr/share/fonts/%s' %(mntdir,fontdir))
			setup_1 = ('chroot %s /usr/bin/mkfontdir /usr/share/fonts/%s' %(mntdir,fontdir))
			os.system(setup_0)
			os.system(setup_1)
			
		setup_2 = ('chroot %s /usr/bin/mkfontscale /usr/share/fonts/misc' %mntdir) 
		os.system (setup_2)
		
		setup_3 = ('chroot %s /usr/bin/mkfontdir -e /usr/share/fonts/encodings -e /usr/share/fonts/encodings/large /usr/share/fonts/misc' %mntdir)
		os.system(setup_3)
		
		setup_4 = ('chroot %s /sbin/ldconfig' %mntdir)
		os.system(setup_4)
		
		setup_5 = ('chroot %s /usr/X11R6/bin/fc-cache -f' %mntdir)
		os.system(setup_5)
		
		
		self.textLabel1.setText('<font color="#FF6D19">Açılış servisleri ayarlanıyor...</font>')
		
		#if ( g_gui == 1 ):
		#	write_status('\nKurulum süreci devam ediyor.\n\nAçılış servisleri ayarlanıyor...') 
		#else:
		#	print( 'Açılış servisleri ayarlanıyor...' )
		
		print('Açılış servisleri ayarlanıyor...')
		
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/rc.keymap","%s/etc/rc.d/rc.keymap" %mntdir)
			
		setup_6 = ('chmod 755 %s/etc/rc.d/rc.keymap' %mntdir)
		os.system(setup_6)
		
		setup_7 = ('chmod 755 %s/etc/rc.d/rc.font' %mntdir)
		os.system(setup_7)
		
		#setup_8 = ('chmod 755 %s/etc/rc.d/rc.postinstall' %mntdir)
		#os.system(setup_8)
		
		setup_9 = ('chmod 755 %s/etc/rc.d/rc.messagebus' %mntdir)
		os.system(setup_9)
		
		setup_10 = ('chmod 755 %s/etc/rc.d/rc.hald' %mntdir)
		os.system(setup_10)
		
		#os.system('chroot %s userdel -r root' %mntdir) 
		#setup_11 = ('chroot %s useradd root -m -G audio,video,cdrom,plugdev' %mntdir)
		#os.system(setup_11)
		
		#if ( g_gui == 1 ):
		#	write_status('\nKurulum süreci devam ediyor.\n\nAçılış servisleri ayarlanıyor...') 
		#else:
		#	print( 'Yapılandırma dosyaları kopyalanıyor...' )
		
		
		self.textLabel1.setText('<font color="#FF6D19">Yapılandırma dosyaları kopyalanıyor...</font>')
		
		print('Yapılandırma dosyaları kopyalanıyor...')
		
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/group","%s/etc/group" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/fstab","%s/etc/fstab" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/xorg.conf","%s/etc/X11/xorg.conf" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/rc.font","%s/etc/rc.d/rc.font" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/lang.sh","%s/etc/profile.d/lang.sh" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/lang.csh","%s/etc/profile.d/lang.csh" %mntdir)
		shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/hardwareclock","%s/etc/hardwareclock" %mntdir)
			
		
		reply = QMessageBox.question(self, "Açılış yöneticisi kurulsun mu?", "Kurma", QMessageBox.Yes|QMessageBox.No|
                QMessageBox.Cancel)
		if reply == QMessageBox.Cancel:
    			return False
		elif reply == QMessageBox.Yes:
#			if ( g_gui == 1 ):
#				write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi ayarlanıyor...') 
#			else:
#				print( 'Açılış yöneticisi ayarlanıyor...' )
				
			if ( bootdisk == '' ):
				bootsector = os.popen('fdisk -l | grep /dev/hda:')
				if bootsector.readline() != '':
					bootdisk = '/dev/hda'
				else:
					bootsector = os.popen('fdisk -l | grep /dev/sda:')
					if bootsector.readline() != '':
						bootdisk = '/dev/sda'
			else:
				return
			
			boot_dizini = ( 'mkdir %s/boot/grub' % mntdir )
			os.system( boot_dizini )
			
			#os.system("mount -t proc proc %s/proc" %mntdir)
			#os.system("mount -o bind /dev/ %s/dev/" %mntdir)
			#os.system("mount -t sysfs sys /mnt/sys" %mntdir)
			os.system("mount --bind /dev/ %s/dev/" %mntdir)
			#setup_12 = ('chroot %s /sbin/grub-install --no-floppy --recheck %s' %(mntdir,bootdisk))
			setup_12 = ('/sbin/grub-install --root-directory=%s --no-floppy --recheck %s' %(mntdir,bootdisk))
			print setup_12
			os.system(setup_12)
			
			shutil.copyfile("/media/hda6/Depolar/truva-svn/truva_installer/files/menu.lst","%s/boot/grub/menu.lst" %mntdir)
			
			setup_13 = ('chmod 755 %s/usr/sbin/update-grub' %mntdir)
			os.system(setup_13)
			
			setup_14 = ('chroot %s /sbin/update-grub' %mntdir)
			#setup_14 = ('/usr/sbin/update-grub')
			os.system(setup_14)
		else:
			#if ( g_gui == 1 ):
			#	write_status('\nAçılış yöneticisi ayarlanmadı...') 
			#else:
				print( 'Açılış yöneticisi ayarlanmadı...' )
		
		
		os.system("umount %s" %device)
		os.system("/usr/bin/eject %s" %device)


    def languageChange(self):
        self.setCaption(self.__tr("Anatolya Kurulum Sistemi - Paket Kurulumu"))
        self.pushButton7.setText(self.__trUtf8("\xc4\xb0\x6c\x65\x72\x69"))
        self.pushButton8.setText(self.__trUtf8("\x59\x61\x72\x64\xc4\xb1\x6d"))
        self.textLabel1.setText(self.__tr("Kurulan Kategori :"))
        self.textLabel2.setText(self.__trUtf8("\x44\x69\x73\x6b\x20\x53\x65\xc3\xa7\x69\x6d\x69"))	
        self.textLabel3.setText(self.__tr("Kurulan Paket     :"))
        self.textLabel4.setText(QString.null)

    def __tr(self,s,c = None):
        return qApp.translate("Form3",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("Form3",s,c,QApplication.UnicodeUTF8)
    

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = Form3()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()

