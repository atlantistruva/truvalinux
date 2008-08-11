# -*- coding: utf-8 -*-
#
# Copyright (C) 2008, Truva Linux
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import sys
# add module paths..
sys.path.append("screens/")

import os

# import screens..
from mainWindow import Ui_mainWindow
from partedWindow import Ui_partedWindow
from discWindow import Ui_discWindow
from installWindow import Ui_installWindow
from userWindow import Ui_userWindow
from grubWindow import Ui_grubWindow
from endWindow import Ui_endWindow

import anatolyaglobals as glbs

from PyQt4 import QtCore, QtGui

import time
import gobject
import array
import shutil
import getopt

g_exedir = '/truva_installer'
g_mntdir = '/truva_installer/mount'
g_bootfilesdir = '/truva_installer/bootfiles'
g_installdev = ''
g_gui = 0
g_writelilo = False
g_installok = False
g_bootdisk = ''

vmlinuz = "vmlinuz-2.6.24.3"
initrd = "initrd.bs"

grub_betik ="""\
grub --device-map=/boot/grub/device.map --batch <<EOF
root %(root_dev)s
setup --stage2=/boot/grub/stage2 (hd0)
quit
EOF

"""

class mainWindow(QtGui.QMainWindow, Ui_mainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 0
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class partedWindow(QtGui.QMainWindow, Ui_partedWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 1
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class discWindow(QtGui.QMainWindow, Ui_discWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 2
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class installWindow(QtGui.QMainWindow, Ui_installWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 3
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

		# os.system("sudo python install_run.py -g --device=/dev/sda2")
		self.main()

	def runbg(self, program, *args ):
		return os.spawnvp( os.P_WAIT, program, (program,) + args )
	
	def write_status(self, statmsg ):
		global g_exedir
		global g_gui
	
		if ( g_gui == 1 ):
			statfile = g_exedir
			statfile += '/stat'
			os.system( 'echo "%(statmsg)s" > %(statfile)s' % vars() )
		else:
			print( statmsg )	
	
	def execute_install(self, installpart ):
		global g_mntdir 
		global g_gui
		global g_bootfilesdir
		global g_installdev
		global g_writelilo
		global g_installok
		global g_bootdisk
	
		mntdir = g_mntdir
		bootfilesdir = g_bootfilesdir
		_osname = {}
		space_error = False
		bootsafemode = False
		bootdisk = ''
	
		if ( g_gui == 0 ):	
			pcheck = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext | grep %s" % installpart )
			pvalid = pcheck.readline()
			pvalid = pvalid.strip()
			if ( pvalid == '' ):
				print( 'Disk bölümü %s bilinmiyor veya kabul edilmedi.\nKurulum durduruldu !\n' % installpart )
				return
			ask = ''
			while ( (ask != 'e') & (ask != 'h') ):
				ask = raw_input( 'Truva Linux %s bölümüne kuruluyor.\nBölüm üzerindeki tüm veriler silinecek!\nEmin misiniz? (e/h)? ' % installpart)		
				if ( ask == 'h' ):
					return
				
		self.write_status('\nLütfen bekleyin.\n\nDiskiniz analiz ediliyor...')
	
		partition = os.popen("sudo fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext | cut -d ' ' -f1")
		filesystem = os.popen("sudo fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext")
		
		partname = partition.readline()
		osname = filesystem.readline()
		
		if os.path.isfile("/truva_installer/file/diskler.txt"):
			os.remove("/truva_installer/file/diskler.txt")
			disk_liste = "sudo fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext > /truva_installer/files/diskler.txt"
			os.system(disk_liste)
		else:
			disk_liste = "sudo fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext > /truva_installer/files/diskler.txt"
			os.system(disk_liste)
		
		# diskler okunuyor
		disk_oku = open("/truva_installer/files/diskler.txt",'r')
		
		# fstab dosyasi eklemek uzere aciliyor
		if os.path.isfile("/truva_installer/files/fstab"):
			os.remove("/truva_installer/files/fstab")
			fstab = open("/truva_installer/files/fstab","a")
		else:
			fstab = open("/truva_installer/files/fstab","a")
		
		dizinler = []
		
		EOF = False
		while not EOF:
	
			line = disk_oku.readline()
			disk_name = line[0:9]
			disk_mount = "/media/" + disk_name[5:9]
			disk_format = line[52:54]
			
			if disk_format == '82' and disk_name <> installpart:
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,"swap","swap","defaults","0","0"))
			elif disk_format == '83' and disk_name <> installpart:
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"ext3", "defaults,noatime","1","1"))
				dizinler.append(disk_mount)
			elif disk_format == '83' and installpart == disk_name:
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,"/","ext3", "defaults,noatime", "1","1"))
			elif (disk_format == '86') or (disk_format == '87'):
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"ntfs", "defaults,noatime", "0","0"))
				dizinler.append(disk_mount)
			elif (disk_format == ' b') or (disk_format == ' c') or (disk_format == ' e'):
				fstab.write('%-22s %-13s %-9s %-19s %-3s %s\n' % (disk_name,disk_mount,"vfat", "defaults,noatime", "0","0"))
				dizinler.append(disk_mount)
			else: break
	
		# cd/dvd aygitlari ekleniyor.
		#fstab = open("/truva_installer/files/fstab","a")
				
		blocks = os.listdir("/sys/block")
		for block in blocks:
			if block[:2] == "hd":
			#if block[:2] == "hd" or block[:2] == "sd":			
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
		
		print "Disk dizinleri : %s" %dizinler
		
		while partname:
			partname = partname.strip()
			mntcmd = 'mount %(partname)s %(mntdir)s' % vars()
			os.system( mntcmd )
			osname = osname.strip()
	
			if osname[13] == '*':
				bootdisk = partname[:8]
	
			# check for Windows primary partitions
			is_win_part = False
			parttype = osname[52:54]
			parttype = parttype.strip()
			# windows partition types (no hidden ones)
			if ( parttype == '6' or parttype == '7' or parttype == 'b' or parttype == 'c' or parttype == 'e' ):
				is_win_part = True
				# check if primary partition 
				primaries = os.popen( 'parted %s print | grep prima' % partname[:8] )		
				primname = primaries.readline()
				primname = primname.strip()
				if ( primname != '' ):
					is_win_part = False
					while primname:
						ppnr = primname[:2]
						if ( ppnr.strip() == partname[8] ):
							is_win_part = True
						primname = primaries.readline()
	
			osname = osname[-(len(osname)-56): ]
			if ( is_win_part == True ):
				osname += " (Windows)"
	
			if ( g_gui == 0 ):
				if ( partname == installpart ):
					sizecmd = ( 'df %s | grep /dev/ | cut -c21-30' % partname )
					psize = os.popen( sizecmd )
					partsize = psize.readline()
					partsize = partsize.strip()
					if ( partsize == '' ):
						partsize = int(0)
					if ( int(partsize) < 3000000 ):
						space_error = True
			
			time.sleep(3)
			mntcmd = ( 'umount %s' % partname )
			os.system( mntcmd )
			time.sleep(2)
	
			partname = partition.readline()
			osname = filesystem.readline()
	
		if ( g_gui == 0 ):
			if ( space_error == True ):
				print( '\n%s disk bölümü kurulum için yeterli alana sahip değil.\nKurulum iptal ediliyor\n' % installpart )
				return
	
		g_installdev = installpart
	
		mntcmd = ( 'umount %s' % installpart )
		os.system( mntcmd )
		time.sleep(3)
	
		mntcmd = 'mount %(installpart)s %(mntdir)s' % vars()
		osres = os.system( mntcmd )
		if osres != 0:
			self.self.write_status('\nKritik bir hata oluştu.\nKurulum iptal edildi !')
			return
		else:	
			oscmd = ( 'mkdir %s/boot' % mntdir )
			os.system( oscmd )
					
			for device in ["/dev/hda","/dev/hdb","/dev/hdc","/dev/hdd","/dev/hde","/dev/hdf","/dev/hdg","/dev/hdh","/dev/sr0","/dev/sr1","/dev/sr2", "/dev/sr3","/dev/pcd0","/dev/pcd1","/dev/pcd2","/dev/pcd3","/dev/aztcd","/dev/cdu535","/dev/gscd","/dev/sonycd", "/dev/optcd","/dev/sjcd","/dev/mcdx0","/dev/mcdx1","/dev/sbpcd","/dev/cm205cd","/dev/cm206cd","/dev/mcd"]:
				
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
				if ( g_gui == 1 ):
					self.write_status('\nKurulum işlemi devam ediyor.\n\nPaketler kurulmaya başlanıyor...') 
				else:
					print( 'Paketler kurulmaya başlanıyor...' )	
	
				#os.system('rm -rf *')
				for dizin in os.listdir("/home/rohanrhu/truva/paketler/"):
					target_dir = "/home/rohanrhu/truva/paketler/" + dizin
					
					if os.path.isdir(target_dir):
						paket_listesi = os.listdir( target_dir )
						for package in paket_listesi:
							if ( g_gui == 1 ):
								self.write_status('\nKurulum işlemi devam ediyor.\nKurulan Kategori : %s\nKurulan paket : %s' %(dizin,package))  
							else:
								print( 'Kurulan paket : %s' %package) 	
		
							oscmd = ('installpkg -root %s %s/%s' %(mntdir,target_dir,package))
							os.system( oscmd )
					else:
						print "dizin: %s" % target_dir
						print('%s kategorisi bulunamadi...') %dizin		
			except:
				print " Bir hata oluştu..."
							
			if ( g_gui == 1 ):
				self.write_status('\nKurulum süreci devam ediyor.\n\nKonfigürasyon ayarlaniyor...') 
			else:
				print( 'Konfigürasyon ayarlaniyor...' )
	
			for disk_dizin in dizinler:
				if not os.path.isdir('/truva_installer/mount/' + disk_dizin):
					result = os.makedirs("%s/%s" %(mntdir,disk_dizin))
					if result != None:
						print "%s dizini oluşturulamadı..." %disk_dizin
						return 0
					
			if ( g_gui == 1 ):
				self.write_status('\nKurulum süreci devam ediyor.\n\nFont ayarları yapılıyor...') 
			else:
				print( 'Font ayarları yapılıyor...' )
			
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
			
			if ( g_gui == 1 ):
				self.write_status('\nKurulum süreci devam ediyor.\n\nAçılış servisleri ayarlanıyor...') 
			else:
				print( 'Açılış servisleri ayarlanıyor...' )
			
			shutil.copyfile("/truva_installer/files/rc.keymap","%s/etc/rc.d/rc.keymap" %mntdir)
				
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
			
			if ( g_gui == 1 ):
				self.write_status('\nKurulum süreci devam ediyor.\n\nAçılış servisleri ayarlanıyor...') 
			else:
				print( 'Yapılandırma dosyaları kopyalanıyor...' )
			
			shutil.copyfile("/truva_installer/files/group","%s/etc/group" %mntdir)
			shutil.copyfile("/truva_installer/files/fstab","%s/etc/fstab" %mntdir)
			shutil.copyfile("/truva_installer/files/rc.font","%s/etc/rc.d/rc.font" %mntdir)		
			shutil.copyfile("/truva_installer/files/xorg.conf","%s/etc/X11/xorg.conf" %mntdir)
			shutil.copyfile("/truva_installer/files/lang.sh","%s/etc/profile.d/lang.sh" %mntdir)
			shutil.copyfile("/truva_installer/files/lang.csh","%s/etc/profile.d/lang.csh" %mntdir)
			shutil.copyfile("/truva_installer/files/hardwareclock","%s/etc/hardwareclock" %mntdir)
			
			
			msgtext  = '\nAçılış yöneticisini kurmak istiyor musunuz?'
			
			msgdialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, msgtext )
			response = msgdialog.run()
			msgdialog.destroy()
			
			
			if response == gtk.RESPONSE_YES:		
				if ( g_gui == 1 ):
					self.write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi ayarlanıyor...') 
				else:
					print( 'Açılış yöneticisi ayarlanıyor...' )
					
				part_root = installpart[5:9]
				print "part root : %s" %part_root
				
				dev = ord(part_root[2:3])-97
				part_root1 = int(part_root[3:4])-1
				root_dev = "(hd%d,%d)" % (dev , part_root1)
				print "kurulum diskinin hd karsiligi : (hd%d,%d)" % (dev , part_root1)
				
				
				grub_hazirla = grub_betik % {"root_dev": root_dev}
				
				if os.path.isfile("%s/sbin/grub_kur.sh"  %mntdir):
					os.remove("%s/sbin/grub_kur.sh"  %mntdir)
					grub_yaz = open("%s/sbin/grub_kur.sh"  %mntdir,"w")
					grub_yaz.write ( grub_hazirla )
					grub_yaz.close()
				else:
					grub_yaz = open("%s/sbin/grub_kur.sh"  %mntdir,"w")
					grub_yaz.write ( grub_hazirla )
					grub_yaz.close()
				
				os.system("cp -dpR %s/lib/grub/i386-pc/* %s/boot/grub/" %(mntdir,mntdir))
				#shutil.copytree("%s/lib/grub/i386-pc/*" %mntdir, "%s/boot/grub/" %mntdir)
				
				setup_13 = ('chmod 755 %s/sbin/grub_kur.sh' %mntdir)
				os.system ( setup_13 )
				
				setup_14 = ('chroot %s /sbin/grub_kur.sh' %mntdir)
				os.system ( setup_14 )
				
		
				if os.path.isfile("%s/boot/grub/menu.lst" %mntdir):
					os.remove("%s/boot/grub/menu.lst" %mntdir)
					menu_lst = open("%s/boot/grub/menu.lst" %mntdir,"a")
				else:
					menu_lst = open("%s/boot/grub/menu.lst" %mntdir,"a")				
				
				menu_lst.write("default		0 \n")
				menu_lst.write("timeout		5 \n")
				menu_lst.write("splashimage=%s/boot/grub/splash.xpm.gz \n\n" %root_dev)
	
				fcmdline=open("/proc/cmdline","r")
				params=fcmdline.read().split()
				fcmdline.close()
				for param in params:
					if param.startswith("vga=") or param.startswith("video="):
						print param
	
		
				menu_lst.write("title  Truva Linux\n")
				menu_lst.write("root   " + root_dev + "\n")
				menu_lst.write("kernel /boot/" + vmlinuz + " root=" + installpart + " ro quiet " + param + "\n")
				menu_lst.write("initrd /boot/" + initrd + "\n\n")
				
				#elif (disk_format_2 == '86') or (disk_format == '87') or (disk_format == ' b') or (disk_format == ' c') or (disk_format == ' e'):
				menu_lst.write("# title  Windows\n")
				menu_lst.write("# root   hd(0,0)\n")
				menu_lst.write("# makeactive \n")
				menu_lst.write("# chainloader +1 \n")
				
				menu_lst.close()
				
				#shutil.copyfile("/truva_installer/files/menu.lst","%s/boot/grub/menu.lst" %mntdir)
				
			else:
				if ( g_gui == 1 ):
					self.write_status('\nAçılış yöneticisi ayarlanmadı...') 
				else:
					print( 'Açılış yöneticisi ayarlanmadı...' )
						
			time.sleep(1)				
			os.system( 'sync' )
			time.sleep(2)
			
			g_installok = True
			
			if ( g_gui == 1 ):
				self.write_status('\nCd çıkartılıyor...') 
			else:
				print( 'Cd çıkartılıyor...' )
			
			os.system("umount %s" %device)
			os.system("/usr/bin/eject %s" %device)
	
	def main(self):
		global g_gui
		global g_exedir
		global g_installdev
		global g_writelilo
		global g_installok
		global g_mntdir
		global g_bootdisk
		exedir = g_exedir
		mntdir = g_mntdir
		
		partname = ''
	
		"""try:
			opts, args = getopt.getopt( sys.argv[1:], "g", ["device="]) 
		except getopt.GetoptError:
			print( '\nGeçersiz parametre(ler):\n--device, Örnek: --device=/dev/hda1\n -g grafiksel çıktı için.\n' ) 
			sys.exit(2)"""
		opts = [('-g', ''), ('--device', '/dev/sda2')]
		args = []
	
		pid = os.getpid()
		oscmd = ( 'echo "%(pid)s" > %(exedir)s/pid' % vars() ) 
		os.system( oscmd )
	
		for o, a in opts:
			if o == '-g':
				g_gui = 1
			if o == '--device':
				partname = a	
				
		if ( partname == '' ):		
			print( '\nParameter "--device" is needed.\nFor example: --device=/dev/hda1\n' ) 
			sys.exit(2)
		
		self.write_status('\n\nLütfen bekleyiniz...\n')
	
		time.sleep(4)
		self.execute_install( partname )
		
		mntcmd = ( 'umount %s' % g_installdev )
		os.system( mntcmd )
	
		oscmd = ( 'echo "0" > %s/pid' % exedir ) 
		os.system( oscmd )
	
		if ( g_installok == True ):
			time.sleep(1)
			self.write_status('\nKurulum tamamlandı!\n\nSistem yeniden başlatıldıktan sonra yönetici şifrenizi\ndeğiştirmeyi unutmayınız...\n\nSistem şimdi yeniden başlatılıyor...')
			#os.system("/sbin/reboot")

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class userWindow(QtGui.QMainWindow, Ui_userWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 4
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class grubWindow(QtGui.QMainWindow, Ui_grubWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 5
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

class endWindow(QtGui.QMainWindow, Ui_endWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setupUi(self)

		self.windowNo = 6
		exec(glbs.defaultPosition)

		exec(glbs.defaultSignals)

	def nextWindow(self):
		windowname = glbs.allWindows[self.windowNo + 1]
		exec("self.%s = %s()" % (windowname, windowname))
		exec("self.%s.show()" % windowname)
		self.close()

app = QtGui.QApplication([])
mw = mainWindow()
mw.show()
app.exec_()