#!/usr/bin/python
# -*- coding: utf-8 -*-

#Adem Dedebali
#Lisans : GPL
#Editor : Kate
#Tarih : 06.05.2009

#Truva Paket Kayıtçı
#Sürüm : 0.2

############################################################################
#                                                                          #
#                     PROGRAMIN GENEL ÇALIŞMA YAPISI                       #
# Program patika değişkeninin içerisindeki dosyalarda işlem yapar.         #
# Hızlı çalışabilmesi için hiçbir hata kontrolü yapılmamıştır.             #
# Truva Linux paketlerinin kategorilenmiş olarak tutulduğu dizin patika    #
# değişkenine verilmelidir. Argüman alarak çalışan program eğer yanlış bir #
# argüman girilirse veya program argümansız başlatılmaya çalışılırsa       #
# nasıl kullanılacağına dair ufak bir yardım belgesiyle karşılaşaşılır.    #
#                                                                          #
# *********Oluşturulacak dosya aynı dizinde varsa üzerine yazılır********* #
#                          ***changelog hariç***                           #
############################################################################

# /home/user/truva patikasında çalışıldığı düşünülürse
# patika değişkenine "/home/user/truva" girilmelidir.

# http://www.truvalinux.org.tr/wiki/index.php/Truva_Linux_Kurulum_ve_Kullan%C4%B1m_Rehberi
# adresinde "Paket Serileri ve Açıklamaları" başlığında açıklandığı gibi çalışılan
# dizinde "/a", "xorg-util" gibi alt klasörler ve bu klasörlerin içerisinde
# paketlerin olması gerekir. Program sadece bu yapıyı destekler.

#Kullanılan kütüphaneler programa dahil edilir
import os
import time
import re
import tarfile
import md5
import sys

#Programın tamamında kullanılacak bazı değişkenler tanımlanıyor

#Programın çalışacağı patika
patika = "/home/adem/Desktop/truvapaketler"

kok = "/"

class paketleri_adam_et (object):
	def __init__ (self):
		self.desteklenen_uzantilar = []
		
		self.desteklenen_uzantilar.append ("tgz")
		self.desteklenen_uzantilar.append ("txz")
		
		self.desteklenen_mimariler = []
		
		self.desteklenen_mimariler.append ("i386")
		self.desteklenen_mimariler.append ("i486")
		self.desteklenen_mimariler.append ("i586")
		self.desteklenen_mimariler.append ("i686")
		self.desteklenen_mimariler.append ("noarch")
		self.desteklenen_mimariler.append ("x86")
	
	def paketleri_al (self):
		#changelog oluşturulurken veriler paketin isminden yola çıkılarak bulunur.
		#Eğer paketin isminde bir bozukluk varsa, düzeltilebiliyorsa düzeltilir
		#düzeltilemiyorsa uyarı olarak bildirilip, elle düzeltilmesi istenir.
		klasorler = os.listdir (patika)
	
		for klasor in klasorler:
			if os.path.isdir (patika + kok + klasor):
				paketler = os.listdir (patika + kok + klasor)
				
				for paket in paketler:				
					#Paketi aldık, şimdi kontrol edilmeli
					paket2 = self.duzgununu_iste (paket)
					
					if paket <> paket2:
						os.chdir (patika + kok + klasor)
						os.rename (paket, paket2)
						
						print paket + " paketi"
						print paket2 + " adiyla degistirildi...\n"
						
		print "Tum paketler gozden gecirildi..."
					
	def duzgununu_iste (self, paket):
		#Paketin ismi örnek olarak şu şekilde olmalıdır.
		#most-4.10.2-i486-2.tgz
		#Sağdan gelinirse ilk noktadan sonra paketin uzantısı
		#İlk nokta ile ilk çizgi arasında derlenme numarası
		#İlk çizgi ile ikinci çizgi arasında mimarisi
		#İkinci çizgi ile üçüncü çizgi arasında sürümü
		#Üçüncü çizgiden geri kalan adı olmalıdır.
		
		#Paket ayıklanır ve 5 elemanlı dizi döner
		
		#0. eleman adı
		#1. eleman sürümü
		#2. eleman mimarisi
		#3. eleman derlenme numarası
		#4. eleman uzantısıdır
			
		paket = self.paketi_ayikla (paket)
		
		#Kontrole sok
		paket[0] = self.ad_kontrol (paket)
		paket[1] = self.surum_kontrol (paket)
		paket[2] = self.mimari_kontrol (paket)
		paket[3] = self.derlenme_no_kontrol (paket)
		paket[4] = self.uzanti_kontrol (paket)
		
		#Yeni değerler birleştirilir.
		paket = self.ayrigi_birlestir (paket)
		
		return paket
		
	def ayrigi_birlestir (self, x):
		return x[0] + "-" + x[1] + "-" + x[2] + "-" + str (x[3]) + "." + x[4]
		
	def ad_kontrol (self, ad):
		#Henüz hiçbir kontrol yok
		return ad[0]
	
	def surum_kontrol (self, surum):
		#Henüz hiçbir kontrol yok
		return surum[1]
	
	def mimari_kontrol (self, mimari):
		for x in self.desteklenen_mimariler :
			if x == mimari[2]:
				return mimari[2]
			
		print self.ayrigi_birlestir (mimari) + " paketinin mimarisi desteklenenler listesinde yok"
		print "Program mudahele edemedi, elle yapilandirilmasi gerekiyor"
		print "Cikiliyor..."
		sys.exit (0)
		
	def derlenme_no_kontrol (self, d_no):
		#Bazen derleme numaralarına harf karışmış olabiliyor.
		#Fonksiyon bunu tespit edip silmeye çalışır.
		try:
			return int (d_no[3])
		
		except:
			donecek = ""
			for a in d_no[3]:
				try:
					donecek = donecek + str (int (a))
					
				except:
					pass
				
		try:
			return int (donecek)
		
		except:
			print self.ayrigi_birlestir (d_no) + " paketinin derlenme numarası hatalı."
			print "Program mudahele edemedi. Elle duzeltilmesi gerek"
			print "Cikiliyor..."
			sys.exit (0)
			
	def uzanti_kontrol (self, uzanti):
		#Eğer desteklenen uzantılar listesinde varsa değişmez
		for x in self.desteklenen_uzantilar:
			if x == uzanti[4]:
				return uzanti[4]
		
		print self.ayrigi_birlestir (uzanti) + " paketinin uzantisi desteklenenler listesinde yok."
		print "Program mudahele edemedi. Elle duzeltilmesi gerek"
		print "Cikiliyor..."
		sys.exit (0)
			
	def paketi_ayikla (self, paket):
		ayrik = []
		
		sayacnokta = False
		sayac = 0
		im1 = 0
		im2 = 0
		im3 = 0
		imnokta = 0
		for i in range (len (paket) - 1, 0, -1):
			
			if i == 0:
				print paket + " paketi ayiklanamiyor"
				print "elle mudahele gerekiyor. Program bir sey yapamadi..."
				print "Cikiliyor..."
				sys.exit (0)
					
			if paket[i] == ".":
				if not sayacnokta:
					imnokta = i
					sayacnokta = True
						
			if paket[i] == "-":
				if sayac == 0:
					im1 = i
					
				elif sayac == 1:
					im2 = i
						
				elif sayac == 2:
					im3 = i
					
				sayac = sayac + 1
				if sayac == 3:
					break
					
		#Paketin adi
		ayrik.append (paket[ : im3])
				
		#Paketin sürümü
		ayrik.append (paket[im3 + 1 : im2])
				
		#Paketin mimarisi
		ayrik.append (paket[im2 + 1 : im1])
				
		#Paketin derlenme numarası
		ayrik.append (paket[im1 + 1 : imnokta])
				
		#paketin uzantısı
		ayrik.append (paket[imnokta + 1 : ])

		if len (ayrik) == 5:
			return ayrik
			
		else:
			print paket + " paketi ayiklanamiyor"
			print "elle mudahele gerekiyor. Program bir sey yapamadi..."
			print "Cikiliyor..."
			sys.exit (0)

class changelog (object):
	def __init__ (self):
		self.dosyaadi = "ChangeLog.txt"
		
		self.mimari = []
		self.mimari.append ("i386")
		self.mimari.append ("i486")
		self.mimari.append ("i586")
		self.mimari.append ("i686")
		self.mimari.append ("noarch")
		self.mimari.append ("x86")
		
		self.modlar = []
		self.modlar.append ("eklendi :: ")
		self.modlar.append ("guncellendi :: ")
		self.modlar.append ("yeniden :: ")
		self.modlar.append ("kaldirildi :: ")
		
		self.ff = open (patika + kok + self.dosyaadi, "r+")
		
	def changelog_txt_olustur (self):
		islenmis_changelog = []
			
		#Bütün paketlerin listesi alınır.
		tumpaketler = self.paket_listesini_al ()
		
		#changelog dosyasının içeriği okunur.
		changelog_veriler = self.ff.read ()
		
		#changelog dosyasındaki veriler her satır bir dizi elemanı olacak
		#şekilde diziye aktarılır
		changelog_veriler = self.diziye_at_changelog_txt (changelog_veriler)
		
		#Paketlerin adı, sürümü, son durumu, uzantısı gibi bilgiler alınır.
		changelog_veriler = self.kaydi_ayikla_changelog_txt (changelog_veriler)
		
		#Yukarıdaki işlem depodaki paketler için de yapılır
		tumpaketler = self.kaydi_ayikla_paketler (tumpaketler)
		
		#Elde paket listesi ve changelog dosyası işlenmiş şekilde var
		#Gerekli değerlendirmeyi yapıp yazdırmak kaldı.
		degisiklikler = self.degisiklik_listesi_cikar (changelog_veriler, tumpaketler)

		self.degisiklikleri_yaz (degisiklikler)
		
		self.ff.close ()
		
	def degisiklikleri_yaz (self, veriler):
		#Değişiklikler başka bir dosyaya yazılır ve diğer dosyadaki veriler
		#bu dosyanın altına eklenir. Son olarak dosyanın adi değiştirilir.
		
		dd = open (patika + kok + "tesadufen_kullanilmaz_ins", "w")
		
		dd.write ("+------------------------------------------------------------------------+\n")
		#Tarih bilgisi eklenir
		tarih = time.localtime ()
		tarih = str (tarih[2]) + "." +  str (tarih[1]) + "." + str (tarih[0]) + "  " + str (tarih[3]) + "." + str (tarih[4]) + "." + str (tarih[5])
		
		#Eğer değişiklik yoksa uyarir ve dosyaya bir sey yazilmaz
		if len (veriler) == 0:
			print tarih
			print "Paketlerde bir degisiklikle karsilasilmadi, changelog degismedi"
			
			return
		
		#Tarih dosyaya yazılır
		tarih = "Olusturulma tarihi --->  " + tarih + "\n"
		dd.write ("+" + "-" * 80 + "+" + "\n")
		dd. write (tarih)
		dd.write ("+" + "-" * 80 + "+" + "\n")
	
		#Değişiklik kayıtları eklenir
		for veri in veriler:
			dd.write (veri + "\n")
			
		#Diğer dosya eklenir.
		self.ff.seek (0)
		dd.write (self.ff.read ())
		
		#Dosyanın ismi degistirilir
		os.chdir (patika)
		os.rename ("tesadufen_kullanilmaz_ins", self.dosyaadi)
		
	def kaydi_ayikla_paketler (self, paketler):
		islenmis = []
		
		for paket in paketler:	
			islenmis.append (self.kaydi_ayikla (paket))
			
		return islenmis
		
		
	def degisiklik_listesi_cikar (self, changepaketler, paketler):
		degisiklikler = []
		
		for i in range (0, len (changepaketler) - 1, 1):
			j = i
			while j < len (changepaketler) - 1:
				j = j + 1
				
				if changepaketler[i][0] == changepaketler[j][0]:
					changepaketler.pop (j)
					j = j - 1
				
		#Bir paket alınır.
		for paket in paketler:
			paket_islemi_yapildi = False
			
			#Changelogdaki son durumuna bakılır.
			for changepaket in changepaketler:
				#Eğer varsa
				if paket[0] == changepaket[0]:
					#İlkin moduna bakılır. Paket daha önceden kaldırıldı olarak işaretlenmişse
					#Direk eklendi olarak geçer. Aksi durumda işleme bakılır
					if changepaket[5] == 4:
						degisiklikler.append (self.modlar[0] + self.gercek_isim (paket))
						
					#Eğer silinmiş değilse
					else:
						#Sürümüne bakılır. Sürümler farklı ise güncellendi olarak eklenir.
						if paket[1] <> changepaket[1]:
							degisiklikler.append (self.modlar[1] + self.gercek_isim (paket))
						
						#Mimari ve derlenme sayılarına bakılır. Eğer biri farklıysa
						#yeniden olarak işaretlenir.
						elif paket[2] <> changepaket[2] or paket[3] <> changepaket[3]:
							print str (paket)
							print str (changepaket)
							print str (paket[2]) + " -->> " + str (changepaket[2]) + "\n"
							degisiklikler.append (self.modlar[2] + self.gercek_isim (paket))
							
					#Eğer paket ismi changelogda bulunduysa, silinmiş değilse ve bir değişiklik
					#varsa bu listeye eklendi. Artık bu paketle işimiz kalmadı
					paket_islemi_yapildi = True
						
				if paket_islemi_yapildi:
					break
		
			#Döngüde paket bulunamamişsa paket daha önce yoktur demektir ve eklenir.
			else:
				degisiklikler.append (self.modlar[0] + self.gercek_isim (paket))
			
		#Bellekte yer kaplayan somut paketlerle iş bitti. Sırada changelog dosyasında bulunan verilerden
		#silinenler var mı ona bakmak kaldı
		
		#Fonksiyonun ilk işleminde yapıldığı üzere changepaket dizisinde
		#aynı ismi taşıyan eleman yok, hep en güncelleri var
		#Bunun için rahat rahat bakabiliriz.
		
		for changepaket in changepaketler:
			paketle_karsilasildi = False
			
			#Eğer kaldirildi olarak gorunmuyorsa bu paket depoda var goruluyor demektir.
			if changepaket[5] == 4:
				continue
			paketin_adi = self.gercek_isim (changepaket)
			
			#Depodaki paketler içerisinde geziye çıkılır.
			klasorler = os.listdir (patika)
	
			for klasor in klasorler:
				if os.path.isdir (patika + kok + klasor):
					paketler = os.listdir (patika + kok + klasor)
					
					#Eğer changelogdaki paket gercekten varsa donguden break ile cikilir
					#break ile cikilan dongunun else bloguna girilmez
					for paket in paketler:
						if paket == paketin_adi:
							paketle_karsilasildi = True
							break
						
						
				if paketle_karsilasildi:
					break
				
			else:
				#Eğer changelogdaki paket yoksa eklendi, guncellende veya
				#yeniden olarak birazdan kayda gecirilecek olabilir
				#Eğer öyleyse silindi olarak gorunmez, aksi takditde görünür.
				for degisiklik in degisiklikler:
					if degisiklik.find (changepaket[0]) <> -1:
						break
					
				else:	
					degisiklikler.append (self.modlar[3] + changepaket[0])
					
		return degisiklikler
	def gercek_isim (self, paket):
		#Ayıklanmış paketin gerçek ismini döndürür
		return paket[0] + "-" + paket[1] + "-" + paket[3] + "-" + str (paket[2]) + "." + paket[4]
	
	def kaydi_ayikla_changelog_txt (self, veriler):
		islenmis = []
		
		for veri in veriler:	
			islenmis.append (self.kaydi_ayikla (veri))
			
		return islenmis
				
	def kaydi_ayikla (self, paket):
		#"eklendi", yapısı aşağıdaki gibi olmalıdır.
		#Paket daha önce depoda yoksa veya son işlem olarak kaldırıldı görünüyorsa eklendi...
		#"eklendi :: xeyes-1.0.1-i486-1.tgz"
		#"eklendi :: xkill-1.0.1-i486-1.tgz"
		
		#"guncellendi", yapısı aşağıdaki gibi olmalıdır.
		# Paketin ismi aynı, sürüm numarası farklı ise güncellendi olarak işaretlenir.
		#"guncellendi :: cairo-1.4.10-i486-1.tgz"
		#"guncellendi :: hal-info-20070618-noarch-1.tgz"
		
		#"yeniden", paketin ismi ve sürümü aynı, derleme numarası farklı ise işaretlenir.
		#Yapısı aşağıdaki gibi olmalıdır.
		#"yeniden :: glibc-zoneinfo-2.5-noarch-4.tgz"
		#"yeniden :: oprofile-0.9.2-i486-5.tgz"
		
		#"kaldırıldı", paket daha önceden depodaysa, program işlediği anda yoksa işaretlenir.
		#Yapısı aşağıdaki gibi olmalıdır.
		#kaldirildi :: x11-docs-html
		#kaldirildi :: x11-fonts-100dpi
		
		#changelog dosyasında bu anahtarlardan biriyle başlayan satırlar
		#changelog_veri dizisine aktarılır.

		ayrik = []
		#İlk eleman paketin adı
		#İkinci eleman sürümü
		#Üçüncü eleman derlenme sayısı
		#Dördüncü eleman hangi işlemci için derlendiğini 
		#Beşinci eleman uzantısını tutar.
		#Altıncı eleman modunu tutar
		
		#MODLAR		
		# 1 eklendi
		# 2 güncellendi
		# 3 yeniden
		# 4 kaldırıldı
		# 5 yeni paket
		
		#Mod bulunur
		if paket.find ("eklendi") <> -1:
			mod = 1
			
		elif paket.find ("guncellendi") <> -1:
			mod = 2
			
		elif paket.find ("yeniden") <> -1:
			mod = 3
			
		elif paket.find ("kaldirildi") <> -1:
			mod = 4
		
		else:
			#Kayde gecirilmemis paketler icin
			mod = 5
			
		#Changelog dosyasından okunmuşsa başında eklendi :: gibi ibare bulunur.
		#String üzerinde daha rahat çalışabilmek için bu silinir.
		if paket.find ("::") <> -1:
			paket = paket[paket.find ("::") + 3 : ]
			
		#Eğer kaldirildi modunda ise sadece paket adi ve modu dondurulur
		if mod == 4:
			ayrik.append (paket)
			ayrik.append ("")
			ayrik.append ("")
			ayrik.append ("")
			ayrik.append ("")
			ayrik.append (mod)
			
			return ayrik
		
		#Ayırıcı çizgilerin yeri belirleniyor.
		sayac = 0
		for i in range (len (paket) - 1, 0, -1):
			if paket[i] == "-":
				if sayac == 0:
					im1 = i
					
				elif sayac == 1:
					im2 = i
				
				elif sayac == 2:
					im3 = i
					
				sayac = sayac + 1
				
				if sayac == 3:
					break
		
		#Paketin adı eklenir
		ayrik.append (paket[ : im3])
				
		#Paketin sürümü alınır.
		ayrik.append (paket[im3 + 1: im2])
		
		#Derlenme sayısı alınır
		ayrik.append (paket[im1 + 1 : paket.rfind (".")])
		
		#Hangi mimari için derlendiğine bakılır.
		ayrik.append (paket[im2 + 1: im1])
				
		#Uzantısı alınır.
		#Son üç karakteri alır.
		
		ayrik.append (paket[-3 : ])
		
		ayrik.append (mod)
		
		return ayrik
		
	def diziye_at_changelog_txt (self, veriler):
		changelog_veri = []
		
		#Gelen veri yığınında satır sonu karakter görüldüğünde o satırda
		#4 anahtar kelimeden birisi varsa eklenir.
		sayac = -1
		while len (veriler) >= 0:
			sayac = sayac + 1
			
			try:
				if veriler[sayac] == "\n":
					d = veriler[ : sayac]
				
					#4 anahtar kelimeden biri aranır. find () fonksiyonundan dönen
					#sonuçlar toplanır. Eğer 4ü de yoksa ve dönen değerleri toplarsak
					#-4 olur. Eğer sonuç -4 değilse birisi vardır ve diziye eklenir.
				
					if d.find("eklendi") + d.find ("guncellendi") + d.find ("kaldirildi") + d.find ("yeniden") <> -4:
						changelog_veri.append (d[ : sayac])
					
					veriler = veriler[sayac + 1 : ]
				
					sayac = -1
					
			except:
						break
				
		return changelog_veri
				
	def paket_listesini_al (self):
		tumpaketler = []
		
		klasorler = os.listdir (patika)
		
		for klasor in klasorler:
			if os.path.isdir (patika + kok + klasor):
				paketler = os.listdir (patika + kok + klasor)
				
				for paket in paketler:
					tumpaketler.append (paket)
					
		return tumpaketler
	
class checksums (object):
	def __init__ (self):
		#Oluşacak dosyanın ismi belirlenir.
		self.dosyaadi = "CHECKSUMS.md5"
	
	def checksums_md5_olustur (self):
		
		klasorler = os.listdir (patika)
		
		ff = open (patika + kok + self.dosyaadi, "w")
		
		#Örnek dosyada ilk satır boş olduğu için:
		ff.write ("\n")
		
		#patika içerisindeki değişkenler tek tek geziliyor
		for klasor in klasorler:
			#Eğer Klasörse içerisindeki paketlerin isimleri paketler değişkenine aktarılır.
			if os.path.isdir (patika + kok + klasor):
				paketler = os.listdir (patika + kok + klasor)
					
				#Dizindeki her paketin md5 değeri alınır.
				# "1197b5a27932e371255887ea45c9b1de ./a/aaa_base-12.0.0-noarch-1.tgz"
				#Yukarıdaki formatta dosyaya yazılır.
				for paket in paketler:
					gecicipatika = patika + kok + klasor + kok + paket
					md5 = self.paketin_md5ini_oku (gecicipatika)
					
					gecicipatika = re.sub (patika, ".", gecicipatika)
					
					ff.write (md5 + " " + gecicipatika + "\n")
				
		ff.close ()
		
		print self.dosyaadi + " basariyla olusturuldu..."
	
	def paketin_md5ini_oku (self, patika):
		m = md5.new (file (patika).read())
		
		return m.hexdigest ()
	
class packages (object):
	def __init__ (self):
		self.dosyaadi = "PACKAGES.TXT"
		self.ff = open (patika + kok + self.dosyaadi, "w")
		
	def packages_txt_olustur (self):
		klasorler = os.listdir (patika)
				
		for klasor in klasorler:
			if os.path.isdir (patika + kok + klasor):
				paketler = os.listdir (patika + kok + klasor)
				
				for paket in paketler:
					#Buradan itibaren geri kalan işi paket_incele_ve_yaz ()
					#fonksiyonu yapacağı ve o da alt fonksiyonlara aytılacağı
					#için bilgilerini alacağımız paket self.gecerlipaket
					#değişkenine alınır. (Diğer fonksiyonlarca daha rahat
					#ulaşılabilmesi için.)
					print paket + " paketi packages.txt dosyasına yazılıyor"
					self.gecerlipaket = patika + kok + klasor + kok + paket
					
					self.paketi_incele_ve_yaz (klasor, paket)
					
		print self.dosyaadi + " basariyla olusturuldu..."
		
		self.ff.close ()
					
	def acilinca_boyut (self, tg):
		y = 0
		try:
			for r in tg:
				y = y + r.size
			return y / 1024
		except:
			print "%s yolundaki dosyanin boyutu yazilamadi...\n" %(self.gecerlipaket)
			return 0
	
	def paketi_incele_ve_yaz (self, klasor, paket):
		#Packages.txt oluşturulurken model alınan yapı:
		
		#
		#PACKAGE NAME:  aaa_base-12.0.0-noarch-1.tgz
		#PACKAGE LOCATION:  ./a
		#PACKAGE SIZE (compressed):  11 K
		#PACKAGE SIZE (uncompressed):  90 K
		#PACKAGE REQUIRED:  
		#PACKAGE CONFLICTS:  
		#PACKAGE SUGGESTS:  
		#PACKAGE DESCRIPTION:
		#aaa_base: aaa_base (Basic Linux filesystem package)
		#aaa_base:
		#aaa_base: Sets up the empty directory tree for Slackware and adds an email to
		#aaa_base: root's mailbox welcoming them to Linux. :)  This package should be
		#aaa_base: installed first, and never uninstalled.
		#aaa_base:
		#aaa_base:
		#aaa_base:
		#aaa_base:
		#aaa_base:
		#aaa_base:
		
		#şeklindedir. İlkin bir satır boş bırakılır.
		
		
		#PACKAGE NAME
		self.ff.write ("\nPACKAGE NAME:  %s\n" %(paket))
			
		#PACKAGE LOCATION
		self.ff.write ("PACKAGE LOCATION:  %s\n" %("." + kok + klasor))
		
		#PACKAGE SIZE COMPRESSED
		self.ff.write ("PACKAGE SIZE (compressed):  %d K\n" %(os.path.getsize (self.gecerlipaket) / 1024))
		
		#Gzipli sıkıştırılmış (tar.gz) dosya okuma modunda açılır.
		
		tg = tarfile.open (self.gecerlipaket, "r")

		#PACKAGE SIZE (uncompressed)
		self.ff.write ("PACKAGE SIZE (uncompressed):  %d K\n" %(self.acilinca_boyut (tg)))
		
		#Paket açıldı ve içine girilecek.
		#İçine girmişten packages.txt dosyasına eklenecek ne varsa alıp çıkmak lazım
		#rcsd fonksiyonu bu işi yapar.
		#Required, conflicts, suggests, description açılımındadır.
		
		self.ff.write (self.rcsd (tg))
		
		tg.close ()
	
	def rcsd (self, tg):
		# Required, conflicts, suggests, description açılımındadır.
		
		# Eğer pakete bağımlı bir paket varsa bu paket
		# /install/slack-requried dosyasında belirtilir.
		
		# "cxxlibs >= 6.0.8-i486-4 | gcc-g++ >= 4.1.2-i486-1"
		# "gcc >= 4.1.2-i486-1"
		# "glibc-solibs >= 2.7-i486-4"
		# Yukarıdaki formattadır.

		# PACKAGE REQUIRED:  cxxlibs >= 6.0.8-i486-4 | gcc-g++ >= 4.1.2-i486-1,gcc >= 4.1.2-i486-1,glibc-solibs >= 2.7-i486-4
		# Yukarıdaki formatta yazılmalıdır.
		required = False
		
		# Eğer paketin ters bağımlılıkları varsa bu paketler
		# /install/slack-conflicts dosyasında belirtilir.
		conflicts = False
		
		# Eğer paketin önerdiği bir paket varsa
		# /install/slack-suggests dosyasında belirtilir.
		suggests = False
		
		#Paket açıklaması
		# /install/slack-desc dosyasındadır.
		description = False
		
		for dosyalar in tg.getnames ():
			#PACKAGE REQUIRED
			if dosyalar == "install/slack-required":

				required_veri = tg.extractfile (dosyalar)
				required_veri = re.sub ("\n", ",", required_veri.read ())
				required = True

			#PACKAGE CONFLICTS
			elif dosyalar == "install/slack-conflicts":

				conflicts_veri = tg.extractfile (dosyalar)
				conflicts_veri = re.sub ("\n", ",", conflicts_veri.read ())
				conflicts = True
		
			#PACKAGE SUGGESTS
			elif dosyalar == "install/slack-suggests":
				
				suggests_veri = tg.extractfile (dosyalar)
				suggests_veri = re.sub ("\n", ",", suggests_veri.read ())
				suggests = True
			
			#PACKAGE DESCRIPTION
			
			#Bazı paketlerin slack-desc formatları farklılık gösterir.
			#packages.txt dosyasında PACKAGE NAME: satırının 2, 22, 42, 32, 82
			#gibi ilerleyerek devam etmesi için ayrıca istenilen formata uygun
			#hale getirmek için desc_uygunlasır () fonksiyonuna girer
			elif dosyalar == "install/slack-desc":

				description_veri = tg.extractfile (dosyalar)
				description_veri = self.desc_uygunlastir (description_veri.read ())
				description = True
				
		#Elde edilen veriler uygun formata getiriliyor.
		yazilacak = "PACKAGE REQUIRED:  "
		if required:
			yazilacak = yazilacak + required_veri
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE CONFLICTS:  "
		if conflicts:
			yazilacak = yazilacak + conflicts_veri
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE SUGGESTS:  "
		if suggests:
			yazilacak = yazilacak + suggests_veri
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE DESCRIPTION:\n"
		if description:
			yazilacak = yazilacak + description_veri
		else:
			print patika + " dosyasinin slack-desc dosyasi bulunamadi..."
			
			yazilacak = yazilacak + "x:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:"

		yazilacak = yazilacak + "\n"
		
		return yazilacak
				
	def desc_uygunlastir (self, veriler):
		#slack-desc dosyasının içeriği aşağıdaki gibidir...
		
		# HOW TO EDIT THIS FILE:
		# The "handy ruler" below makes it easier to edit a package description.  Line
		# up the first '|' above the ':' following the base package name, and the '|'
		# on the right side marks the last column you can put a character in.  You must
		# make exactly 11 lines for the formatting to be correct.  It's also
		# customary to leave one space after the ':'.

        	#|-----handy-ruler------------------------------------------------------|
		#aaa_base: aaa_base (Basic Linux filesystem package)
		
		# aaa_base ile başlayan son satır gerekli. Bunun için 4. "|" karakterini
		# gördükten sonra döngü biter ve ordan sonrası alınır. Tabi ki satır sonu
		# karakter olduğu için bir fazlası alınır.
		
		# sayac 1. döngüde"|", 2. döngüde "\n" karakterini sayar.
		# sayac2 bütün karakterleri sayar.
		
		
		#Bazı paketlerin desclerinde handy-ruler yok.
		#Pakette handy-ruler olup olmadığı denetlenir.
		#handy-ruler yoksa direk veriler döndürülür.
		
		if veriler.find ("handy-ruler") < 0:
			sayac  = 0
			sayac2 = 0
		
			for veri in veriler:
				sayac2 = sayac2 + 1
			
				if veri == '\n':
					sayac = sayac + 1
				
				if sayac == 11:
					break
				
				return veriler
		
		sayac  = 0
		sayac2 = 0 
		
		for veri in veriler:
			sayac2 = sayac2 + 1
			
			if veri == "|":
				sayac = sayac + 1
				
			if sayac == 4:
				break
			
		veriler = veriler[sayac2 + 1: ]
		
		# Bu işlemden sonra da aaa_base satırından 11 adet olacak şekilde ayarlanmalıdır.
		# 11 tane satır sonu karakter sayılır ve daha fazla ise gerisi okunmaz.
		
		sayac  = 0
		sayac2 = 0
		
		for veri in veriler:
			sayac2 = sayac2 + 1
			
			if veri == '\n':
				sayac = sayac + 1
				
			if sayac == 11:
				break
			
		veriler = veriler[ : sayac2 - 1]
		
		return veriler
			
x = len (sys.argv)

if (x == 1):
	print "Kullanim:"
	print "Asagidaki parametrelerden biri veya birkaci girilir"
	print "Daha fazla aciklama icin kaynak koddaki aciklama satirlarina bakilabilir\n"
	
	print "     -checksums   veya -c  --> CHECKSUMS.MD5  olusturur"
	print "     -packages    veya -p  --> PACKAGES.TXT   olusturur"
	print "     -changelogs  veya -ch --> CHANGELOGS.TXT olusturur"
	print "     -isimkontrol veya -i  --> Paket isimlerini kontrol eder"
	
else:
	bc = 0
	bp = 0
	bch = 0
	bi = 0
	for x in sys.argv:
		if x == "isimkontrol" or x == "-i" and bi == 0:
			y = paketleri_adam_et ()
			y.paketleri_al ()
			
		elif x == "-checksums" or x == "-c" and bc == 0:
			y = checksums ()
			y.checksums_md5_olustur ()
			bc = 1
		elif x == "-packages" or x == "-p" and bp == 0:
			y = packages ()
			y.packages_txt_olustur ()
			bp = 1
		elif x == "-changelogs" or x == "-ch" and bch == 0:
			y = changelog ()
			y.changelog_txt_olustur ()
			bch = 1
		else:
			if x <> sys.argv[0]:
				print x + " parametresi bir ise yaramaz"