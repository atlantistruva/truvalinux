#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

TRUVAPACKAGE="/media/sda1/Truva/Release/Gelistirilen/truva/Paketler/"
TRUVADEPO="/media/sda1/Truva/Release/Gelistirilen/kaynak/"
SLACKDEPO="/media/sda1/Software/Rsync/Slackware/slackware-current/source/"

#-------TANIMLAMALAR-------------
AUTHOR="Onur ÖZDEMİR <atlantis@truvalinux.org.tr>"
FILE="Package Source Manager"
VERSION = ['0','0','1']
DESC="Kaynak kod paketi senkron aracı"


#------AYARLAMALAR---------------
paket_adi=[]

def paketleri_oku():
	
	for dizin in ["a","ap","araclar","cokluortam","d","dokuman","egitim","gelistirme","gnome","grafik","guvenlik","internet","kde","kernel","konsol","kutuphane","l","lang","masaustu","n","ofis","oyunlar","sistem","sunucu","suruculer","t","tcl","temalar","uygulama","veritabani","x","xap","xorg-extra"]:
		
		target_dir = TRUVAPACKAGE + dizin
		
		#Kategorileri gosterir
		paket_listesi = os.listdir(target_dir)
		print paket_listesi
		
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
					
					print "Eşlenen paket : %s" %package[x]
					rsync_cmd = "rsync -rulzv "
					truva_path = TRUVADEPO + dizin + "/"					
					slack_path =  SLACKDEPO + dizin + "/" + pkgname
					
					if not os.path.exists(slack_path): 
						other_depo.append(pkgname)
					
					kaynak_cek = rsync_cmd + slack_path + " " + truva_path + " >> /tmp/source_rsync.log"
					print "Verilen komut : %s" %kaynak_cek
					os.system(kaynak_cek)
					
	print "Kaynak kod aktarma işlemi tamamlandı...\n"
	print "Slackware deposunda olmayan paketleri listesi : %s \n" %other_depo

# Paketlerin okunmasi ve Ana pencerenin calistirilmasi
if __name__ == '__main__':
    oku=paketleri_oku()