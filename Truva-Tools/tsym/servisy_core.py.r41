# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi uygulaması
# Temel bileşenler modülü
# Author: Oğuzhan Eroğlu (oguzhan@oguzhaneroglu.com)

import os
import sys
import shelve

db = shelve.open("%s/.servisy.db" % os.environ["HOME"])
servis_dizin = "/etc/init.d/"

class Yonetici:
	def __init__(self):
		self.db = db
		self.servis_dizin = servis_dizin

	def calistir(self, servis_adi, s_komut):
		if os.path.exists("%s%s" % (self.servis_dizin, servis_adi)):
			os.system("sh %s %s %s > /dev/null" % (self.servis_dizin, servis_adi, s_komut))
		else:
			print "Servis bulunamadı!"

	def servis_baslat_acilis(self):
		for i in self.db["acilis"]:
			print i

	def acilis_ekle(self, servis_adi):
		self.db["acilis"].append(servis_adi)

	def servis_baslat(self, servis_adi):
		self.calistir(servis_adi, "start")
		print servis_adi + " servisi başlatıldı."

	def servis_aktif(self, servis_adi):
		os.chmod(self.servis_dizin + servis_adi, 0777)
		print servis_adi + " servisi açılışta başlatılacak."

	def servis_deaktif(self, servis_adi):
		os.chmod(self.servis_dizin + servis_adi, 777)
		print servis_adi + " servisi açılışta başlatılmayacak."

	def servis_durdur(self, servis_adi):
		self.calistir(servis_adi, "stop")
		print servis_adi + " servisi durduruldu."

	def listele(self):
		return os.listdir(self.servis_dizin)

	def durum(self, servis_adi):
		return os.popen("ps -e|grep -c %s" % servis_adi).read().replace("\n", "")

	def restart(self, servis_adi):
		self.servis_durdur(servis_adi)
		self.servis_baslat(servis_adi)

	def listele_goster(self):
		self.listeleg = self.listele()
		print "Tüm servisler:"
		print "|    Servis Adı    |    Durum    |"
		for i in self.listeleg:
			if self.durum(i) != "0":
				print "\033[01;34m" + i, "\033[01;0m   (Çalışıyor)"
			else:
				print "\033[01;34m" + i, "\033[01;0m   (Çalışmıyor)"