import os
import time
import re
import tarfile
import md5
import sys

#####################################################################
####################### CHANGELOG.TXT ###############################
##################################################################### 
class changelog:
	def __init__ (self, gpatika = "/home/adem/truva"): #Bu kisim istege gore degisebilir.
		self.patika = gpatika
	
	def changelogolustur (self):
		gpatika = self.patika + "/" + "ChangeLog.txt"

		x = os.path.exists (gpatika)
		
		if x == 1:
			self.log_var (gpatika)
		else:
			self.log_yok (gpatika)

	def log_yok (self, gpatika):
		safzaman = time.time ()
		zaman = time.localtime (safzaman)
		zaman = str(zaman[0]) + "/" + str(zaman[1]) + "/" + str(zaman[2]) + "," + str(zaman[3]) + ":" + str(zaman[4]) + ":" + str(zaman[5])

		ff = open (gpatika, "w")
		
		ff.write (zaman + "\n")

		dosyalar = os.listdir (self.patika)

		for dosya in dosyalar:

			gpatika = self.patika + "/" + dosya

			if os.path.isdir (gpatika) <> 1:
				continue

			else:
				tgzler = os.listdir (gpatika)

				for tgz in tgzler:
					ff.write ("Eklendi : " + tgz + "\n")

		ff.write ("|||---|||---|||---|||---|||---|||")
		ff.close ()

	def log_var (self, gpatika):
		print "Bu fonksiyon yapim asamasinda...\n"


##################################################################
####################### PACKAGES.TXT #############################
##################################################################


class paketliste:
	def __init__ (self, gpatika = "/home/adem/truva"): #Bu kisim uygun sekilde degistirilmelidir.
		self.patika = gpatika


	def plistolustur (self):
		gpatika = self.patika + "/" + "PACKAGES.TXT" #Bu kisim istege gore degistirilebilir.
		os.chdir (self.patika)
		dosyalar = os.listdir (self.patika)

		x = self.dosya_var_mi ()
		if (x == 0):
			self.iletisim (1)
			return;

		x = self.txt_var_mi (gpatika)
		if x == 0:
			self.iletisim (2)
			return
		
		ff = open (gpatika, "w")
		
		for dosya in dosyalar:
			os.chdir (self.patika)
			gpatika = self.patika + "/" + dosya

			if os.path.isdir (gpatika) <> 1:
				continue
			else:
				tgzler = os.listdir (gpatika)

				for tgz in tgzler:
					gpatika = self.patika + "/" + dosya + "/" + tgz
					self.paketiyaz (dosya, ff, tgz, gpatika)

		ff.close ()
		self.iletisim (3)
	
	
	def dosya_var_mi (self):    #Dosya varsa 1, yoksa 0 dondurur
		os.chdir (self.patika)
		dosyalar = os.listdir (self.patika)
		
		for dosya in dosyalar:
			gpatika = self.patika + "/" + dosya
			if (os.path.isdir(gpatika) <> 1):
				continue
			else:
				tgzler = os.listdir (gpatika)
				
				for tgz in tgzler:
					gpatika = self.patika + "/" + dosya + "/" + tgz

					if os.path.exists (gpatika):
						return 1;
		
		return 0


	def iletisim (self, no):
		print ("\n")
		if no == 1:
			print ("Listelenecek dosya yok...")
		elif no == 2:
			print ("Programdan cikildi. Dosya olusturulmadi...")
		elif no == 3:
			print ("Dosya basariyla olusturuldu...")
		
		print ("\n")


	def txt_var_mi (self, patika):
		x = os.path.exists (patika)

		if x == 1:
			patika = re.sub (self.patika + "/", "", patika)
			yanit = raw_input ("%s dosyasi zaten var. Uzerine yazmak ister misin (E-H)" %(patika))

			if (yanit == "E" or yanit == "e"):
				return 1
		else:
			return 1
		
		return 0


	def paketiyaz (self, klasor, ff, tgz, patika):
		#PACKAGE NAME
		ff.write ("\n")
		ff.write ("PACKAGE NAME:  %s\n" %(tgz))
		
		#PACKAGE LOCATION
		klasor = "./" + klasor
		ff.write ("PACKAGE LOCATION:  %s\n" %(klasor))
		
		#PACKAGE SIZE CS
		x = os.path.getsize (patika) / 1024
		ff.write ("PACKAGE SIZE (compressed):  %d K\n" %(x))
		
		tg = tarfile.open (patika, "r")

		#PACKAGE SIZE U CS
		x = self.boyut_bul (patika, tg)
		ff.write ("PACKAGE SIZE (uncompressed):  %d K\n" %(x))

		bbagimli = 0
		bconf = 0
		bsugg = 0
		bdesc = 0
		
		for dosyalar in tg.getnames ():
		
			#PACKAGE REQUIRED (bagimli)
			if dosyalar == "install/slack-required":

				bagimli = tg.extractfile (dosyalar)
				bagimli = bagimli.read ()
				bagimli = re.sub ("\n", ",", bagimli)
				bbagimli = 1

			#PACKAGE CONFLICTS (conf)
			elif dosyalar == "install/slack-conflicts":

				conf = tg.extractfile (dosyalar)
				conf = conf.read ()
				conf = re.sub ("\n", ",", conf)
				bconf = 1
		
			#PACKAGE SUGGESTS (sugg)
			elif dosyalar == "install/slack-suggests":
				
				sugg = tg.extractfile (dosyalar)
				sugg = sugg.read ()
				sugg = re.sub ("\n", ",", sugg)
				bsugg = 1
			
			#PACKAGE DESCRIPTION (desc)
			elif dosyalar == "install/slack-desc":

				desc = tg.extractfile (dosyalar)
				desc = desc.read ()
				bdesc = 1
				
				sayac = 0
				sayac2 = 0
				
				for x in desc:
					
					sayac2 = sayac2 + 1
					if x == "|":

						sayac = sayac + 1

						if sayac == 4:
							break
				if sayac < 4:
					pass
				else:
					sayac2 = sayac2 + 1 
					desc = desc[sayac2:]
				
				
				
				sayac = 0
				sayac2 = 0
				for x in desc:
					
					sayac2 = sayac2 + 1					
					if x == "\n":
						sayac = sayac + 1
						
						if sayac == 11:
							desc = desc[0:sayac2]
							desc = desc[:-1]
							break
					
		
		yazilacak = "PACKAGE REQUIRED:  "
		if bbagimli == 1:
			yazilacak = yazilacak + bagimli
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE CONFLICTS:  "
		if bconf == 1:
			yazilacak = yazilacak + conf
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE SUGGESTS:  "
		if bsugg == 1:
			yazilacak = yazilacak + sugg
		yazilacak = yazilacak + "\n"

		yazilacak = yazilacak + "PACKAGE DESCRIPTION:\n"
		if bdesc <> 1:
			print patika + " dosyasinin slack-desc dosyasi bulunamadi..."
			yazilacak = yazilacak + "x:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:\nx:"
		else:
			yazilacak = yazilacak + desc

		yazilacak = yazilacak + "\n"

		ff.write (yazilacak)
		tg.close ()
		
		
	def boyut_bul (self, patika, tg):
		y = 0
		try:
			for r in tg:
				y = y + r.size
			return y / 1024
		except:
			print "%s yolundaki dosyanin boyutu yazilamadi...\n" %(patika)
			return 0



##################################################################
####################### CHECKSUMS.MD5 ############################
##################################################################

class checksums:
	def __init__ (self, gpatika = "/home/adem/truva"): #Burasi uygun sekilde degistirilmelidir.
							   #Fonksiyona istenirse yeni nesne olusturulurken farkli patika girilebilir.
		self.patika = gpatika

	def sum_olustur (self):
		gpatika = self.patika + "/" + "CHECKSUMS.MD5" #Istenirse farkli bir dosya adi kullanilabilir.
		os.chdir (self.patika)
		dosyalar = os.listdir (self.patika)
		
		x = self.dosya_var_mi ()
		if x == 0:
			self.iletisim (2)
			return

		x = self.sum_var_mi (gpatika)
		if x == 0:
			self.iletisim (1)
			return

		ff = open (gpatika, "w")

		for dosya in dosyalar:
			os.chdir (self.patika)
			gpatika = self.patika + "/" + dosya

			if os.path.isdir (gpatika) <> 1:
				continue;
			else:
				tgzler = os.listdir (gpatika)

				for tgz in tgzler:
					gpatika = self.patika + "/" + dosya + "/" + tgz
					m = self.md5_dosya (gpatika)
					gpatika = re.sub (self.patika, ".", gpatika)
					ff.write (m + " " + gpatika + "\n")
		ff.close ()
		self.iletisim (3)

		
	def md5_dosya (self, gpatika):  #Dosyanin md5 degerini dondurur
		m = md5.new (file (gpatika).read())
		m = m.hexdigest ()
		return m


	def sum_var_mi (self, gpatika): #Dosya olusturulmaya uygunsa 1, degilse 0 dondurur
		x = os.path.exists (gpatika)

		if x == 1:
			gpatika = re.sub (self.patika + "/", "", gpatika)
			yanit = raw_input ("%s dosyasi zaten var. Uzerine yazmak ister misin (E-H)" %(gpatika))

			if (yanit == "E" or yanit == "e"):
				return 1
		else:
			return 1
		
		return 0


	def dosya_var_mi (self): #Sifrelenecek dosya varsa 1, yoksa 0 dondurur
		os.chdir (self.patika)
		dosyalar = os.listdir (self.patika)

		for dosya in dosyalar:
			gpatika = self.patika + "/" + dosya

			if (os.path.isdir(gpatika) <> 1):
				continue
			else:
				tgzler = os.listdir (gpatika)

				for tgz in tgzler:
					gpatika = self.patika + "/" + dosya + "/" + tgz

					if os.path.exists (gpatika):
						return 1

		return 0

	def iletisim (self, no): #Uygun mesajlar kullaniciya iletilir
		print ("\n")

		if no == 1:
			print "Programdan cikildi. md5 dosyasi olusturulmadi..."
		elif no == 2:
			print "Patikada sifrelenecek dosya bulunamadi..."
		elif no == 3:
			print "md5 dosyasi basariyla olusturuldu..."

		print ("\n")

x = len (sys.argv)
if (x == 1):
	print "Bu program arguman alarak calisir"
	print "     -checksums  veya -c  --> CHECKSUMS.MD5  olusturur"
	print "     -packages   veya -p  --> PACKAGES.TXT   olusturur"
	print "     -changelogs veya -ch --> CHANGELOGS.TXT olusturur"
else:
	bc = 0
	bp = 0
	bch = 0
	for x in sys.argv:
		
		if (x == "-checksums" or x == "-c") and bc == 0:
			y = checksums ()
			y.sum_olustur ()
			bc = 1
		if (x == "-packages" or x == "-p") and bp == 0:
			y = paketliste ()
			y.plistolustur ()
			bp = 1
		if (x == "-changelogs" or x == "-ch") and bch == 0:
			y = changelog ()
			y.changelogolustur ()
			bch = 1
 
