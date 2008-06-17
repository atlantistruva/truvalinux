# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi uygulaması
# Temel bileşenler modülü
#  Copyright (C) 2008  Truva Linux
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import shelve

db = shelve.open("%s/.servisy.db" % os.environ["HOME"])
servis_dizin = "/etc/rc.d/"

class Yonetici:
	def __init__(self):
		self.db = db
		self.servis_dizin = servis_dizin

	def calistir(self, servisadi, s_komut):
		print "%s%s" % (self.servis_dizin, "rc." + servisadi)
		if os.path.exists("%s%s" % (self.servis_dizin, "rc." + servisadi)):
			print "..."
			os.system("sh %s%s %s > /dev/null" % (self.servis_dizin, "rc." + servisadi, s_komut))
		else:
			print "Servis bulunamadı!"

	def servis_baslat_acilis(self):
		for i in self.db["acilis"]:
			print i

	def acilis_ekle(self, servisadi):
		self.db["acilis"].append("rc." + servisadi)

	def servis_baslat(self, servisadi):
		self.calistir(servisadi, "start")
		print "rc." + servisadi + " servisi başlatıldı."

	def servis_aktif(self, servisadi):
		os.chmod(self.servis_dizin + "rc." + servisadi, 0777)
		print "rc." + servisadi + " servisi açılışta başlatılacak."

	def servis_deaktif(self, servisadi):
		os.chmod(self.servis_dizin + "rc." + servisadi, 777)
		print "rc." + servisadi + " servisi açılışta başlatılmayacak."

	def servis_durdur(self, servisadi):
		self.calistir(servisadi, "stop")
		print "rc." + servisadi + " servisi durduruldu."

	def listele(self):
		return os.listdir(self.servis_dizin)

	def durum(self, servisadi):
		return os.popen("ps -e|grep -c %s" % servisadi).read().replace("\n", "")

	def restart(self, servisadi):
		self.servis_durdur("rc." + servisadi)
		self.servis_baslat("rc." + servisadi)

	def listele_goster(self):
		self.listeleg = self.listele()
		print "Tüm servisler:"
		print "|    Servis Adı    |    Durum    |"
		for i in self.listeleg:
			if self.durum(i) == "0":
				print "\033[01;34m" + i, "\033[01;0m   (Çalışmıyor)"
			else:
				print "\033[01;34m" + i, "\033[01;0m   (Çalışıyor)"