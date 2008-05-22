# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi uygulaması
# Konsol arayüzü...
# Author: Oğuzhan Eroğlu (oguzhan@oguzhaneroglu.com)

import sys
from servisy_core import Yonetici
import os

yardim_metni = """Kullanım: service [servisadi] veya (list) (start, stop, status, restart, active, deactive)"""
ytc = Yonetici()

if os.geteuid() != 0:
	print "Servis yönetici root olarak çalıştırılmalıdır."
	sys.exit()

if len(sys.argv) < 3:
	if "--help" in sys.argv:
		print yardim_metni
	else:
		print "Yanlış kullanım. (--help komutuna bakın.)"
else:
	if sys.argv[2] == "start":
		ytc.servis_baslat(sys.argv[1])
	elif sys.argv[2] == "stop":
		ytc.servis_durdur(sys.argv[1])
	elif sys.argv[2] == "status":
		if ytc.durum(sys.argv[1]) != "0":
			print sys.argv[1] + " servisi çalışıyor."
		else:
			print sys.argv[1] + " servisi çalışmıyor."
	elif sys.argv[2] == "restart":
		ytc.restart(sys.argv[1])
	elif sys.argv[2] == "list":
		ytc.listele_goster()
	elif sys.argv[2] == "active":
		ytc.servis_aktif(sys.argv[1])
	elif sys.argv[2] == "deactive":
		ytc.servis_deaktif(sys.argv[1])
	else:
		print "Yanlış kullanım. (--help komutuna bakın.)"