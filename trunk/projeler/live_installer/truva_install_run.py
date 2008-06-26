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

g_exedir = '/hd_install'
g_mntdir = '/hd_install/mount'
g_bootfilesdir = '/hd_install/bootfiles'
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
			print( 'Disk bölümü %s bilinmiyor ya da kabul edilmedi.\nKurulum durduruldu!\n' % installpart )
			return
		ask = ''
		while ( (ask != 'e') & (ask != 'h') ):
			ask = raw_input( 'Truva Çalışan CD %s bölümüne kurulacak\nDiskteki tüm bilgiler silinecek!\nDevam etmek istiyor musunuz(e/h)? ' % installpart)		
			if ( ask == 'h' ):
				return
			
	write_status('\nLütfen bekleyin.\n\nDisk bölümleriniz inceleniyor...')

	partition = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext | cut -d ' ' -f1")
	filesystem = os.popen("fdisk -l | grep /dev/ | grep -iv Disk | grep -iv Swap | grep -iv Ext")

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
		
		if ( g_gui == 0 ):
			if ( partname == installpart ):
				sizecmd = ( 'df %s | grep /dev/ | cut -c21-30' % partname )
				psize = os.popen( sizecmd )
				partsize = psize.readline()
				partsize = partsize.strip()
				if ( partsize == '' ):
					partsize = int(0)
				if ( int(partsize) < 2000000 ):
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
			print( '\nDisk bölümü %s yeterli alana sahip değil.\nMinimum 2 Gb olmalıdır\n Kurulum durduruldu!\n' % installpart )
			return

	g_installdev = installpart

#	write_status('\nYönetici şifresiChanging password for admin...\n\n')
#	msgtext  = "It is strongly advisable to change password for admin\n"
#	msgtext += "right after installation has taken place.\n"
		
#	if ( g_gui == 1 ):
#		os.spawnl( os.P_WAIT, '/hd_install/changerootpw.py' )
#		os.spawnlp( os.P_WAIT, 'userpasswd' )
#	else:
#		print( msgtext )	
#		os.system( 'passwd' )

	write_status('\nKurulum süreci devam ediyor.\n\nDisk bölümü %s formatlanıyor...' % installpart )
 
	mntcmd = ( 'umount %s' % installpart )
	os.system( mntcmd )
	time.sleep(3)

	#oscmd = ( 'mke2fs -b 4096 -j -L TRUVA -q %s' % installpart )
	#osres = os.system( oscmd )
	#if osres != 0:
	#	write_status('\nFormatlama esnasında kritik\n bir hata oluştu.\nKurulum durduruldu.\n')
	#	return
					
	mntcmd = 'mount %(installpart)s %(mntdir)s' % vars()
	osres = os.system( mntcmd )
	if osres != 0:
		write_status('\nDiski bağlama esnasında kritik\n bir hata oluştu\nKurulum durduruldu.\n')
		return
	else:	
		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nTakas alanı oluşturuluyor...') 
		else:
			print( 'Takas alanı oluşturuluyor...' )	
		oscmd = ( 'dd if=/dev/zero of=%s/swapfile bs=1024 count=10240' % mntdir )
		os.system( oscmd )
				
		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nTakas alanı aktive ediliyor...') 
		else:
			print( 'Takas alanı aktive ediliyor...' )	
		oscmd = ( 'mkswap %s/swapfile' % mntdir )
		os.system( oscmd )
		oscmd = ( 'swapon %s/swapfile' % mntdir )
		os.system( oscmd )
				
		oscmd = ( 'mkdir %s/{boot,tmp,proc,sys,mnt}' % mntdir )
		os.system( oscmd )
				
		msgbase = ('\nKurulum süreci devam ediyor.\n\nDosyalar kopyalanıyor...')
		msgbaseshort = ( 'Dosyalar kopyalanıyor...' )
				
		msgtext = msgbase
		msgtext += ' /boot ...'
		msgtextshort = msgbaseshort
		msgtextshort += ' /boot...'
		if ( g_gui == 1 ):
			write_status( msgtext ) 
		else:
			write_status( msgtextshort ) 
		oscmd = ( 'cp --preserve=all %(bootfilesdir)s/{splash.bmp,System.map,vmlinuz} %(mntdir)s/boot' % vars() )
		os.system( oscmd )

		for cpdir in ( 'bin', 'dev', 'etc', 'home', 'lib', 'opt', 'root', 'sbin', 'usr', 'var'):
			msgtext = msgbase
			msgtext += ' /'
			msgtext += cpdir
			msgtext += ' ...'
			msgtextshort = msgbaseshort
			msgtextshort += ' /'
			msgtextshort += cpdir
			msgtextshort += "..."
			if ( g_gui == 1 ):
				write_status( msgtext )
			else:	 
				write_status( msgtextshort )
			oscmd = ( 'cp --preserve=all -R /%(cpdir)s %(mntdir)s/' % vars() )
			os.system( oscmd )

		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nKonfigürasyon ayarlanıyor...') 
		else:
			print( 'Konfigürasyon ayalanıyor...' )	

		try:
			o_file = open( ('%s/etc/fstab' % mntdir ), 'w' )
		except:
			mntcmd = ( 'umount %s' % installpart )
			os.system( mntcmd )
			write_status('\nBağlama tablosu oluşturulurken\n kritik bir hata oluştu\n Kurulum durduruldu!')
			return
#		o_file.write( '/swapfile		swap		swap		defaults	0	0\n' )
		o_file.write( '%s		/		ext3		defaults		1	1\n' % installpart )
		o_file.write( 'devpts		/dev/pts	devpts		auto		0 	0\n' )
		o_file.close
				

		if ( g_gui == 1 ):
			write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi konfigüre ediliyor...') 
		else:
			print( 'Açılış yöneticisi konfigüre ediliyor...' )	
		try:
			o_file = open( ('%s/etc/lilo.conf' % mntdir ), 'w' )
		except:
			mntcmd = ( 'umount %s' % installpart )
			os.system( mntcmd )
			write_status('\nLilo.conf dosyası oluşturulurken\n kritik bir hata oluştu.\n Kurulum durduruldu!')
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
			o_file.write( 'timeout = 300\n' )
		else:
			o_file.write( 'timeout = 100\n' )
		if ( bootsafemode == False ):	
			o_file.write( 'vga=791\n\n' )

		o_file.write( 'bitmap=/boot/splash.bmp\n' )
		o_file.write( 'bmp-colors=220,0,,255,220,\n' )
		o_file.write( 'bmp-table=234p,348p,1,4\n' )
		o_file.write( 'bmp-timer=539p,396p,220,0,\n\n' )
		o_file.write( 'prompt\n\n' )
		o_file.write( 'change-rules\n\n' )
		o_file.write( 'reset\n\n' )
		o_file.write( 'image = /boot/vmlinuz\n' )
		o_file.write( '  root = %s\n' % installpart )
		o_file.write( '  label = Truva\n  read-only\n' )


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
						# msgdialog2 = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Wil u het standaard grafische opstartscherm gebruiken?\n(Antwoord met 'Nee' als u de LiveCD met de optie\n'nonux-safe' heeft moeten opstarten)." )
						# response = msgdialog2.run()
						# msgdialog2.destroy()
						# if response == gtk.RESPONSE_NO:
						#	bootsafemode = True
				else:
					ask = ''
					while ( (ask != 'y') & (ask != 'n') ):
						ask = raw_input( 'Installing bootmanager (y/n)?\nIf you do not know what it is, answer with "y". ' )		
						if ( ask == 'y' ):
							g_writelilo = True
							# ask = ''
							# while ( (ask != 'y') & (ask != 'n') ):
							#	ask = raw_input( '"Wil u het standaard grafische opstartscherm gebruiken?\n(Antwoord met "n" als u de LiveCD met de optie\n"nonux-safe" heeft moeten opstarten). ' )		
							#	if ( ask == 'n' ):
							#		bootsafemode = True
			else:
				# only boot Nonux
				g_writelilo = True		
				# if ( g_gui == 1 ):
				#	msgdialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Wil u het standaard grafische opstartscherm gebruiken?\n(Antwoord met 'Nee' als u de LiveCD met de optie\n'nonux-safe' heeft moeten opstarten)." )
				#	response = msgdialog.run()
				#	msgdialog.destroy()
				#	if response == gtk.RESPONSE_NO:
				#		bootsafemode = True
				#else:
				#	ask = ''
				#	while ( (ask != 'y') & (ask != 'n') ):
				#		ask = raw_input( '"Wil u het standaard grafische opstartscherm gebruiken?\n(Antwoord met "n" als u de LiveCD met de optie\n"nonux-safe" heeft moeten opstarten). ' )		
				#		if ( ask == 'n' ):
				#			bootsafemode = True
						
					

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
		print( '\nWrong parameter(s):\n--device, example: --device=/dev/hda1\n -g for gui output\n' ) 
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
	
	write_status('\n\nLütfen bekleyin...\n')


	time.sleep(4)
	execute_install( partname )

	if ( g_installok == True ):
		if ( g_writelilo == True ):
			if ( g_gui == 1 ):
				write_status('\nKurulum süreci devam ediyor.\n\nAçılış yöneticisi kuruluyor...') 
			else:
				print( 'Açılış yöneticisi kuruluyor...' )	
			oscmd = ( '/sbin/lilo -r %s/ -w' % mntdir )
			os.system( oscmd )

			time.sleep(1)				
			os.system( 'sync' )
			time.sleep(2)
			
			bootdisk = g_bootdisk
			
			# check of lilo was written to MBR
			os.system( 'dd ibs=512 count=1 if=%s of=/tmp/mbr.dump' % bootdisk )
			lilo_check = os.popen( 'cat /tmp/mbr.dump | grep -i lilo' )
			lilo_installed = lilo_check.readline()
			lilo_installed = lilo_installed.strip()

			if ( lilo_installed == '' ):
				msgtext  = "\nKritik bir hata oluştu.\n"
				msgtext += "Truva diske kuruldu fakat açılış\n"
				msgtext += "yöneticisi kurulamadı\n"
				msgtext += ( "disk %s .\n" % bootdisk )
				msgtext += "Truva otomatik olarak başlatılamayacak.\n"
				msgtext += "Açılış yöneticisini ayarlamayı bilmiyorsanız\n"
				msgtext += "lütfen forum sayfalarımızı ziyaret ediniz...\n"
				if ( g_gui == 1 ):
					msgdialog = gtk.MessageDialog( None, gtk.DIALOG_MODAL, gtk.MESSAGE_WARNING, gtk.BUTTONS_OK, msgtext )
					msgdialog.run()
					msgdialog.destroy()
				else:
					print( msgtext )	

		mntcmd = ( 'umount %s' % g_installdev )
		os.system( mntcmd )

	oscmd = ( 'echo "0" > %s/pid' % exedir ) 
	os.system( oscmd )

	if ( g_installok == True ):
		time.sleep(1)
		write_status('\nKurulum tamamlandı!\n\nSistemi yeniden başlatın ve Truva Cd\'sini CD/DVD sürücüsünden çıkarınız...')

	sys.exit(0)

if __name__ == "__main__":
	main()
