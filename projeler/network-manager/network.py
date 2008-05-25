# -*- coding: utf-8 -*-
# Truva Linux init network modülü
 # Copyright (C) Truva Developers
 # Authors: Oğuzhan Eroğlu <oguzhan@oguzhaneroglu.com>
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.

__version__ = "0.0.1"

import os
import sys

class Networking_Info:
	def __init__(self):
		pass

	def open_read(self, address, file):
		return open("/sys/class/net/%s/%s" % (str(address), str(file))).readline().replace("\n", "")

	def isUp(self, iface):
		""" is network active and deactive.."""
		self.iface_isup = self.open_read(iface, "operstate")
		if "up" in self.iface_isup:
			return True
		else:
			return False

	def listIfaces(self):
		""" gives network interfaces in tuple"""
		ifaces = {}
		for iface in os.listdir("/sys/class/net"):
			if os.path.exists("/sys/class/net/%s/wireless" % iface):
				if self.isUp(iface):
					ifaces[iface] = (unicode(iface), u"wireless", u"Bağlı")
				else:
					ifaces[iface] = (unicode(iface), u"wireless", u"Bağlı Değil")
			else:
				if self.isUp(iface):
					ifaces[iface] = (unicode(iface), u"ethernet", u"Bağlı")
				else:
					ifaces[iface] = (unicode(iface), u"ethernet", u"Bağlı Değil")
		return ifaces

	def connect(self, iface):
		""" connect ethernet network with given interface """
		os.system("ifconfig %s up" % iface)
		if self.isUp(iface):
			return True
		else:
			return False

	def disconnect(self, iface):
		""" disconnect ethernet network with given interface """
		os.system("ifconfig %s down" % iface)
		if self.isUp(iface):
			return False
		else:
			return True