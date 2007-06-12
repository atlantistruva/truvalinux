#!/usr/bin/env python
# -*- coding: UTF8 -*-
# Based on:
# Main menu program for installing/upgrading Nonux on harddisk 
# Author: Marcel J. Zwiebel <http://www.nnlinux.com>
# Adapted to SLAMPP by Kemas Antonius <http://slampp.abangadek.com/>
# Düzenleyenler : Onur ÖZDEMİR - Atlantis
#                 Daron DEDEOĞLU - T-ReX
#                 http://www.truvalinux.org.tr 

import os
import gtk
import time
import sys
import getopt
import shutil


g_exedir = '/truva_installer'
g_mntdir = '/truva_installer/mount'
g_bootfilesdir = '/truva_installer/bootfiles'
g_installdev = ''
g_gui = 0
g_writelilo = False
g_installok = False
g_bootdisk = ''


def runbg( program, *args ):
	return os.spawnvp( os.P_WAIT, program, (program,) + args )

def write_status( statmsg ):
	global g_exedir
	global g_gui

	if ( g_gui == 1 ):
		statfile = g_exedir
		statfile += '/stat'
		os.system( 'echo "%(statmsg)s" > %(statfile)s' % vars() )
	else:
		print( statmsg )	

def execute_install( installpart ):
	global g_mntdir 
	global g_gui
	global g_bootfilesdir
	global g_installdev
	global g_writelilo
	global g_installok
	global g_bootdisk

	mntdir = g_mntdir
	bootfilesdir = g_bootfilesdir
 	_partname = {}
	_osname = {}
	osidx = 0
	space_error = False
	wincounter = 1
	winname = ''
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
			
	write_status('\nLütfen bekleyin.\n\nDiskiniz analiz ediliyor...')

	partition = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext | cut -d ' ' -f1")
	#print partition
	filesystem = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext")
	#print filesystem

	partname = partition.readline()
	osname = filesystem.readline()


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

#		if ( parttype == '82' ):
#			print "Takas alanı bulundu : %s" %partname[:8]
#			takas_alan = partname[:9]
		
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
                    
		if ( partname != installpart): 
			if ( is_win_part == True ):
				_partname[osidx] = partname
				_osname[osidx]= osname
				osidx = osidx + 1

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
		write_status('\nKritik bir hata oluştu.\nKurulum iptal edildi !')
		return
	else:	
		oscmd = ( 'mkdir %s/boot' % mntdir )
		os.system( oscmd )
				
		for device in ["/dev/hdd", "/dev/hdc", "/dev/hdb", "/dev/hda"]:
			cd_mount = 'mount -o ro -t iso9660 %s /var/log/mount' %device
			status = os.system( cd_mount )
			print "\nStatus : %s" %status
			if status == 0:										
				print "Kurulum cd\'si %s sürücüsünde bulundu..." %device
				dev_cd = device
				break
			else:
				print "\nKurulum cd\'si %s sürücüsünde bulunamadı..." %device
				continue
		try:
			if ( g_gui == 1 ):
				write_status('\nKurulum işlemi devam ediyor.\n\nPaketler kurulmaya başlanıyor...') 
			else:
				print( 'Paketler kurulmaya başlanıyor...' )	

			for dizin in ["a","ap","d","gnome","kde","kdei","l","n","t","tcl","x","xap"]:
				target_dir = "/var/log/mount/truva/" + dizin
				paket_listesi = os.listdir( target_dir )
#				print paket_listesi
				for package in paket_listesi:
#					print package
					if ( g_gui == 1 ):
						write_status('\nKurulum işlemi devam ediyor.\n\nKurulan paket : %s' %package)  
					else:
						print( 'Kurulan paket : %s' %package) 	
	
					oscmd = ('installpkg -root %s %s/%s' %(mntdir,target_dir,package))
#					print oscmd
					os.system( oscmd )
		
		except:
			print " bir hata oluştu..."
				
		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nKonfigürasyon ayarlaniyor...') 
		else:
			print( 'Konfigürasyon ayarlaniyor...' )	

		try:
			o_file = open( ('%s/etc/fstab' % mntdir ), 'w' )
		except:
			mntcmd = ( 'umount %s' % installpart )
			os.system( mntcmd )
			write_status('\n\nKritik bir hata oluştu.\nKurulum iptal edildi !')
			return

		o_file.write( '%s \t		/ \t		ext3 \t		defaults \t\t		1 \t	1\n' % installpart )
#		o_file.write( '%s		swap		swap		defaults	0	0\n' % takas_alan ) 
		o_file.write( '%s \t	        /mnt/cdrom \t iso9660 \t   	noauto,user,ro \t\t	0 \t	0\n' % dev_cd )
		o_file.write( 'devpts		/dev/pts	devpts		gid=5,mode=620	0 	0\n' )
		o_file.write( 'proc             /proc           proc       	nosuid,noexec   0	0\n' )
		o_file.write( '/dev/tmpfs       /dev/shm        tmpfs	        size=10%,mode=0777 0	   0\n' )
		o_file.close

		#Kurulum sonrasi ayarlari yapiliyor
		setup_1 = ('chroot %s /sbin/ldconfig' %mntdir)
		os.system(setup_1)
		
		setup_2 = ('chroot %s /usr/X11R6/bin/fc-cache -f' %mntdir)
		os.system(setup_2)
		
		shutil.copyfile("/truva_installer/files/rc.keymap","%s/etc/rc.d/rc.keymap" %mntdir)
			
		setup_3 = ('chmod 755 %s/etc/rc.d/rc.keymap' %mntdir)
		os.system(setup_3)
		
		shutil.copyfile("/truva_installer/files/rc.font","%s/etc/rc.d/rc.font" %mntdir)
				
		setup_4 = ('chmod 755 %s/etc/rc.d/rc.font' %mntdir)
		os.system(setup_4)
		
		setup_5 = ('chmod 755 %s/etc/rc.d/rc.postinstall' %mntdir)
		os.system(setup_5)
		
		setup_6 = ('chmod 644 %s/etc/rc.d/rc.yp' %mntdir)
		os.system(setup_6)
		
		setup_7 = ('chmod 644 %s/etc/rc.d/rc.sshd' %mntdir)
		os.system(setup_7)
		
		
		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi ayarlanıyor...') 
		else:
			print( 'Açılış yöneticisi ayarlanıyor...' )	
		try:
			o_file = open( ('%s/etc/lilo.conf' % mntdir ), 'w' )
		except:
			mntcmd = ( 'umount %s' % installpart )
			os.system( mntcmd )
			write_status('\nKritik bir hata oluştu.\nKurulum iptal edildi.')
			return

		if ( bootdisk == '' ):
			bootsector = os.popen('fdisk -l | grep /dev/hda:')
			if bootsector.readline() != '':
				o_file.write( 'boot = /dev/hda\n' )
				bootdisk = '/dev/hda'
			else:
				bootsector = os.popen('fdisk -l | grep /dev/sda:')
				if bootsector.readline() != '':
					o_file.write( 'boot = /dev/sda\n' )
					bootdisk = '/dev/sda'
		else:
			o_file.write( 'boot = %s\n' % bootdisk )
		
		g_bootdisk = bootdisk

		if ( osidx > 0 ):
			o_file.write( 'prompt\n' )				
			o_file.write( 'timeout = 600\n' )
		else:
			o_file.write( 'timeout = 300\n' )
		if ( bootsafemode == False ):	
			o_file.write( 'vga=791\n\n' )
		o_file.write( 'change-rules\n')
		o_file.write( '  reset\n')
		o_file.write( 'bitmap=/boot/splash.bmp\n' )
		o_file.write( 'bmp-table=234p,348p,1,4\n' )		
		o_file.write( 'bmp-colors=220,0,,255,220,\n' )
		o_file.write( 'bmp-timer=539p,396p,220,0,\n\n' )
		o_file.write( 'image = /boot/vmlinuz-2.6.17.11\n' )
		o_file.write( '  root = %s\n' % installpart )
		o_file.write( '  label = Truva\n' )
		o_file.write( '  initrd = /boot/initrd.bs\n')
		o_file.write( '  append=\"splash=verbose\"\n')
		o_file.write( '  read-only\n')
		
		oscounter = osidx
			
		while ( osidx > 0 ):
			osidx = ( osidx - 1 )
			partname = _partname[osidx]
			osname = _osname[osidx]

			if ( wincounter > 1 ):
				winname = ( 'Windows%s' % wincounter )
			else:
				winname = 'Windows'	
			# note: windows only can boot from first disk and (parimary) partionnumbers less than 5 and 
			# partition 4 not a logical disk
			if ( partname.find( bootdisk ) > -1 and len( partname ) == 9 ):
				# fallback check if parted detection didn't work	
				if ( partname[8] == '1' or partname[8] == '2' or partname[8] == '3' or partname[8] == '4' ):							
					wincounter = ( wincounter + 1 )
					o_file.write( '\nother = %s\n' % partname )
					o_file.write( '  label = %s\n' % winname )
					#o_file.write( '  table = %s\n' % bootdisk )
					o_file.write( '  boot-as=0x80\n' )
		o_file.close

		time.sleep(1)				
		os.system( 'sync' )
		time.sleep(2)

		# check MBR for GRUB bootmanager
		if bootdisk != '':
			os.system( 'dd ibs=512 count=1 if=%s of=/tmp/mbr.dump' % bootdisk )
		else:
			bootsector = os.popen('fdisk -l | grep /dev/hda:')
			if bootsector.readline() != '':
				os.system( 'dd ibs=512 count=1 if=/dev/hda of=/tmp/mbr.dump' )
			else:
				bootsector = os.popen('fdisk -l | grep /dev/sda:')
				if bootsector.readline() != '':
					os.system( 'dd ibs=512 count=1 if=/dev/sda of=/tmp/mbr.dump' )
		grub_check = os.popen( 'cat /tmp/mbr.dump | grep -i grub' )
		grub_installed = grub_check.readline()
		grub_installed = grub_installed.strip()

		if ( grub_installed != '' ):
			# GRUB is used as bootmanager, ask if to be replaced by LILO
			if ( g_gui == 1 ):
				msgdialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'GRUB is detected as bootmanager.\nTRUVA uses LILO. You can set GRUB\nor choose automatic installation of LILO\n(only TRUVA and Windows partition)\n\nInstalling LILO in the MBR (y/n)?' )
				response = msgdialog.run()
				msgdialog.destroy()
				if response == gtk.RESPONSE_YES:
					g_writelilo = True
			else:
				ask = ''
				while ( (ask != 'y') & (ask != 'n') ):
					ask = raw_input( 'GRUB is detected as bootmanager.\nTRUVA uses LILO. You can set GRUB\nor choose automatic installation of LILO\n(only TRUVA and Windows partition).\n\nInstalling LILO in the MBR (y/n)? ' )		
					if ( ask == 'y' ):
						g_writelilo = True
		else:
			# GRUB not detected, install LILO
			if ( oscounter > 0 ):
				# Nonux and Windows (multiboot)
				if ( g_gui == 1 ):
					msgdialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Installing bootmanager?\nIf you do not know what it is,\nanswer with 'Yes'." )
					response = msgdialog.run()
					msgdialog.destroy()
					if response == gtk.RESPONSE_YES:
						g_writelilo = True
				else:
					ask = ''
					while ( (ask != 'y') & (ask != 'n') ):
						ask = raw_input( 'Installing bootmanager (y/n)?\nIf you do not know what it is, answer with "y". ' )		
						if ( ask == 'y' ):
							g_writelilo = True
			else:
				# only boot Nonux
				g_writelilo = True		

		g_installok = True
          	

def main():
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

	try:
		opts, args = getopt.getopt( sys.argv[1:], "g", ["device="]) 
	except getopt.GetoptError:
		print( '\nGeçersiz parametre(ler):\n--device, Örnek: --device=/dev/hda1\n -g grafiksel çıktı için.\n' ) 
		sys.exit(2)

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
	
	write_status('\n\nLütfen bekleyiniz...\n')

	time.sleep(4)
	execute_install( partname )
	
	

	if ( g_installok == True ):
		if ( g_writelilo == True ):
			if ( g_gui == 1 ):
				write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi ayarlanıyor...') 
			else:
				print( 'Açılış yöneticisi ayarlanıyor...' )	
			oscmd = ( '/sbin/lilo -r %s/ -w' % mntdir )
			os.system( oscmd )

			time.sleep(1)				
			os.system( 'sync' )
			time.sleep(2)
			
			bootdisk = g_bootdisk
			

		mntcmd = ( 'umount %s' % g_installdev )
		os.system( mntcmd )

	oscmd = ( 'echo "0" > %s/pid' % exedir ) 
	os.system( oscmd )

	if ( g_installok == True ):
		time.sleep(1)
		write_status('\nKurulum tamamlandı!\n\n Sistemi yeniden başlatın ve\n kurulum diskini sürücüden çıkarın...')
				
	sys.exit(0)


if __name__ == "__main__":
	main()
