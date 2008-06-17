# -*- coding: utf-8 -*-
# Truva Linux servis yöneticisi uygulaması
# Konsol arayüzü
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