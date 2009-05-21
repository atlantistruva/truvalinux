#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

TRUVAPACKAGE="/media/sda1/Truva/Release/Gelistirilen/truva/Paketler/"
TRUVADEPO="/media/sda1/Truva/Release/Gelistirilen/kaynak/"
SLACKDEPO="/media/sda1/Software/Rsync/Slackware/slackware-current/source/"

#-------TANIMLAMALAR-------------
AUTHOR = "Onur ÖZDEMİR <atlantis@truvalinux.org.tr>"
FILE = "Package Source Manager"
VERSION = ['0','0','2']
DESC = "Kaynak kod paketi senkron aracı"
CHANGELOG = "* Kde ve X klasörlerini komple eşleme eklendi. \
             * Uyarı mesajları eklendi. \
	     * kernel kaynak kod paketini komple eşleme eklendi. \
	     * Slackware deposunda olup Truva\'da olmayan klasörler için dizin eşleşme sistemi tasarlandı"

#------AYARLAMALAR---------------
paket_adi=[]
rsync_cmd = "rsync -rulzv "


def paketleri_oku():
	
	dizin_esleme = {'a':'a',
			'ap':'ap',
			'd':'d',
			'k':'kernel',
			'kde':'kde',
			'l':'l',
			'n':'n',
			't':'t',
			'tcl':'tcl',
			'x':'x',
			'xap':'xap'}
	
	paket_esleme = ['kernel-source']
	
	komple_kaynak = ["kde","x"]

	#for dizin in ["kde","x"]:
	for dizin in ["a","ap","d","k","kde","l","n","t","tcl","x","xap"]: 
		
		dizin_ata = dizin_esleme[dizin]
		target_dir = TRUVAPACKAGE + dizin_ata
		print " Hedef Truva paketleri dizini : %s \n" %target_dir
		
		#Kategorileri gosterir
		paket_listesi = os.listdir(target_dir)
		#print paket_listesi
		
		other_depo = []
		if len(paket_listesi) > 0:
				package=paket_listesi
				for x in range(len(package)):
					parts = package[x].split("-")
					# paketi adina gore paket adi, versiyonu, mimarisi ve revizyonu ayriliyor
					if len(parts) > 3:
						revision = parts.pop()
						arch = parts.pop()
						version = parts.pop()
						pkgname = '-'.join(parts)
						this_package = {}
						this_package['package'] = package
						this_package['name'] = pkgname
						this_package['version'] = version
						this_package['arch'] = arch
						this_package['revision'] = revision
						paket=pkgname+"\n"
						paket_adi.append((dizin,paket))
					
					
					print "----------------------------------\n"
					
					truva_path = TRUVADEPO + dizin_ata + "/"
					print "Truva dizin yolu : %s \n" %truva_path
					
					#if dizin in dizin_esleme:
					#	if pkgname in paket_esleme:
					#		slack_path =  SLACKDEPO + dizin + "/"
					#		print "Slackware kısa dizin yolu : %s" %slack_path
					#else:	
					#	slack_path =  SLACKDEPO + dizin + "/" + pkgname
					#	print "Slackware uzun dizin yolu : %s" %slack_path
	
						
						#slack_path =  SLACKDEPO + dizin + "/"
						#print "Slackware kısa dizin yolu : %s" %slack_path
						
					if dizin in komple_kaynak:
						print "Slackware dizini : %s \n" %dizin
						print "Truva dizini : %s \n" %dizin_ata
						
						slack_path =  SLACKDEPO + dizin + "/"
						print "Slackware kısa dizin yolu : %s \n" %slack_path
					
					else:
						print "Eşlenen paket : %s \n" %package[x]
						print "Aktif dizin : %s \n" %dizin
								
						if pkgname in paket_esleme:
							slack_path =  SLACKDEPO + dizin + "/"
							print "Slackware kısa dizin yolu : %s \n" %slack_path
						else:	
							slack_path =  SLACKDEPO + dizin + "/" + pkgname
							print "Slackware uzun dizin yolu : %s \n" %slack_path
					
					if not os.path.exists(slack_path):
						print "Paket/Yol, Slackware deposunda bulunamadı. Lütfen diğer depolardan kontrol ediniz..."
						other_depo.append(pkgname)
					else:
						kaynak_cek = rsync_cmd + slack_path + " " + truva_path + " >> /tmp/source_rsync.log"
						print "Verilen komut : %s \n" %kaynak_cek
						print "----------------------------------\n"
						os.system(kaynak_cek)
					
	print "Kaynak kod aktarma işlemi tamamlandı...\n"
	print "Slackware deposunda olmayan paketleri listesi : %s \n" %other_depo

# Paketlerin okunmasi ve Ana pencerenin calistirilmasi
if __name__ == '__main__':
    oku = paketleri_oku()
