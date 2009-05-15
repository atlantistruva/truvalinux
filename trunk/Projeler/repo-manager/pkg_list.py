#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


#-------TANIMLAMALAR-------------
AUTHOR="Onur ÖZDEMİR <atlantis@truvalinux.org.tr>"
FILE="Package Name List Creator"
VERSION = ['0','0','1']
DESC="Truva Paket İsim Listesi Oluşturma Programı Versiyon %s" %VERSION

#------AYARLAMALAR---------------
paket_adi=[]

def paketleri_oku():
	#global packages,a,ap,d,driver,extra,f,gnome,k,kde,kdei,l,n,t,tcl,x,xap,say
	
	tam_liste = os.getcwd() + "/" + "Paketler"
	if os.path.exists(tam_liste):
		os.remove(tam_liste)
	
	for dizin in ["a","ap","araclar","cokluortam","d","dokuman","egitim","gelistirme","gnome","grafik","guvenlik","internet","kde","kernel","konsol","kutuphane","l","lang","masaustu","n","ofis","oyunlar","sistem","sunucu","suruculer","t","tcl","temalar","uygulama","veritabani","x","xap","xorg-extra"]:
	
		target_dir = os.getcwd() + "/" + dizin
		#Kategorileri gosterir
		paket_listesi = os.listdir(target_dir)
		if "PACKAGES" in paket_listesi:
			paket_listesi.remove("PACKAGES")
			
		print paket_listesi
		
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
					
					#print dizin + "/" + package[x]
					tam_liste = os.getcwd() + "/" + "Paketler"
					tam_liste_ekle=[]
					ekle = package[x] + " \n"
					tam_liste_ekle.append(ekle)
					if not os.path.exists(tam_liste):
						open(tam_liste,"w").writelines(tam_liste_ekle)
						#list.close()
					else: 
						open(tam_liste,"a").writelines(tam_liste_ekle)
						#list.close()
	kategori = paket_adi
	say = 1
	for y in range(len(kategori)):
		#print paket_adi[y][0]
		#print "------------"
		dosya = os.getcwd() + "/" + paket_adi[y][0] + "/" + "PACKAGES"
		eklenecek = []
		t = paket_adi[y][1]
		#print "[" + paket_adi[y][0] + "] - " + paket_adi[y][1]
		eklenecek.append(t)
		#print eklenecek
		eklenecek.sort()
		if not os.path.exists(dosya):
			open(dosya,"w").writelines(eklenecek)
		else: 
			open(dosya,"a").writelines(eklenecek)
		say = say + 1
		os.remove(dosya)
	print "\n"
	print "%s adet paket eklendi\n"%say
	
	print "----------------------------------------\n"
	print "Geliştirici	: %s" %AUTHOR
	print "Program		: %s" %FILE
	print "Versiyon	: %s" %DESC

# Paketlerin okunmasi ve Ana pencerenin calistirilmasi
if __name__ == '__main__':
    oku=paketleri_oku()