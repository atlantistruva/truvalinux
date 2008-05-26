#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pye-u - simple program to connect to wireless network e-U (http://www.e-u.pt).
#Copyright (C) 2007 Carlos Lisboa (carloslisboa _at_ gmail _dot_ com)

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import dbus

class Notificacao:
	def __init__(self):

                BUS_NAME = 'org.freedesktop.Notifications'
                OBJ_PATH = '/org/freedesktop/Notifications'
                IFACE_NAME = 'org.freedesktop.Notifications'
                bus = dbus.SessionBus()
	        notify_obj = bus.get_object(BUS_NAME,OBJ_PATH)
	        self.notifications = dbus.Interface(notify_obj,IFACE_NAME)

	def notifica(self, Titulo, Mensagem):

		#BUS_NAME = 'org.freedesktop.Notifications'
		#OBJ_PATH = '/org/freedesktop/Notifications'
		#IFACE_NAME = 'org.freedesktop.Notifications'
		#bus = dbus.SessionBus()
		#notify_obj = bus.get_object(BUS_NAME,OBJ_PATH)
		#notifications = dbus.Interface(notify_obj,IFACE_NAME)
		self.notifications.Notify('HelloWorld',0,'',Titulo,Mensagem,[],{},-1)
