# -*- coding: utf-8 -*-
# a python wireless module
 # Copyright (C) Oğuzhan Eroğlu <oguzhan@oguzhaneroglu.com>
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
import re

def listInterfaces():
	wlan_ifaces = []
	ifaces_dir = "/sys/class/net"
	ifaces = os.listdir(ifaces_dir)
	for iface in ifaces:
		if os.path.exists("%s/%s/wireless" % (ifaces_dir, iface)):
			wlan_ifaces.append(iface)
	return wlan_ifaces

def getConnected(iface):
	return re.compile('ESSID:"(.*?)"').findall(os.popen("sudo iwconfig %s" % iface).read())[0]

class wlan_tools:
	def iwconfig_read(self):
		return os.popen("sudo iwconfig %s" % self.wlan).read()

	def iwlist_scan(self, wlaniface):
		self.wlanlist = os.popen("sudo iwlist %s scanning" % self.wlaniface).read().split("Cell")
		del self.wlanlist[0]
		return self.wlanlist

	def get_essid(self, wlan):
		return re.compile('ESSID:"(.*?)"').findall(wlan)[0]

class Wireless(wlan_tools):
	def __init__(self, wlaniface):
		self.wlaniface = wlaniface

	def scanning(self):
		self.results = []
		for wlan in self.iwlist_scan(self.wlaniface):
			self.results.append(self.get_essid(wlan))
		return self.results

	def enterPasswd(self, passwd):
		os.popen("sudo iwconfig %s key %s" % (self.wlaniface, passwd))

	def connect(self):
		os.popen("sudo dhclient %s" % self.wlaniface)

class wlanInfo(wlan_tools):
	def __init__(self, iface, gateway):
		self.wlaniface= iface
		self.gateway = gateway
		self.wireless_class = Wireless(self.wlaniface)

	def gateway_refresh(self):
		if self.gateway in self.wireless_class.scanning():
			for wlan in self.iwlist_scan(self.wlaniface):
				if self.get_essid(wlan) == self.gateway:
					return wlan

	def isEncryption(self):
		if "Encryption key:off" not in self.gateway_refresh():
			return True
		else:
			return False

	def getEssid(self):
		return self.get_essid(self.gateway_refresh())

	def getQuality(self):
		return re.compile("Quality=(.*?)/").findall(self.gateway_refresh())[0]

	def getBssid(self):
		return re.compile("Address: (.*?)\n").findall(self.gateway_refresh())[0]