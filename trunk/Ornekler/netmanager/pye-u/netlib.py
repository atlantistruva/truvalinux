#!/usr/bin/env python
# -*- coding: utf-8 -*-

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#  Network Interface Module
#
#  Developed by Joao Rodrigues - gothicknight@gmail.com
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#    This file is part of wifiTools.
#
#    wifiTools is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    any later version.
#
#    wifiTools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with wifiTools; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Bibliotecas de sistema
import os
import sys
from subprocess import Popen, PIPE

# User information
uid		= os.getuid()

#-------------------------------------------------------------------------------------------------
def version():
	"""Versao da Libraria"""

	return "v.20061017"

#-------------------------------------------------------------------------------------------------
def getByteCount(dev):

	if os.access('/proc/net/dev', os.F_OK|os.R_OK):
		file_io=open( '/proc/net/dev' )
		temp = file_io.read().splitlines()
		file_io.close()
	else:
		return []	
	temp = [[elem.split(":")[1].split()[0],elem.split(":")[1].split()[8]] for elem in temp if str(dev) in elem ][0]
	print " * Quantidade de informacao - Rec: "+temp[0]+" Env: "+temp[1]+" (Bytes)"
	return temp
#-------------------------------------------------------------------------------------------------
def getIP(dev):
	p = Popen("ifconfig "+str(dev),shell=True, stdout=PIPE)
	out = p.stdout.read().splitlines()
	p.stdout.close()
	if "inet" in out[1]:

		# Ubuntu
		temp = str(out[1].split(":")[1]).split(" ")[1]
		if len(temp.split(".")) == 4:
			return temp

		# Archlinux
		temp = str(out[1].split(":")[1]).split(" ")[0]
		if len(temp.split(".")) == 4:
			return temp

		return False
	else:
		return False
#-------------------------------------------------------------------------------------------------
def getDNS():
	if os.access("/etc/resolv.conf", os.F_OK|os.R_OK):
		file_io=open("/etc/resolv.conf")
		out= file_io.readlines()
		file_io.close()
		return [ str(elem.split(" ")[1]).split("\n")[0] for elem in out if "nameserver" in elem ]
	else:
		return False
#-------------------------------------------------------------------------------------------------
def getRoute(dev):
	p = Popen("route -en",shell=True, stdout=PIPE)
	out = p.stdout.read().splitlines()
	p.stdout.close()
	try:
		return [ elem.split(" ")[9] for elem in out if str(dev) in elem and "UG" in elem ][0]
	except:
		return False
#-------------------------------------------------------------------------------------------------
# DONE
def getDevState(dev):
	DevStatFile="/sys/class/net/"+str(dev)+"/operstate"
	if os.access(DevStatFile, os.F_OK|os.R_OK):
		file_io=open(DevStatFile)
		out = file_io.read()
		file_io.close()
		return str(out).split("\n")[0]
	else:
		print >>sys.stderr.write("\tE Nao consigo aceder a: "+DevStatFile)
		return "ERRO"
#-------------------------------------------------------------------------------------------------
#TESTING - #(Preciso fazer testes)#
def setDev(dev,ip="dhcp",mask="",route="",dns=""):
	"""Configura o dispositivo com os dados fornecidos"""

	if uid != 0:
		print >>sys.stderr.write(" E Nao tens permissoes para configurar redes")
		return False

	if ip == "dhcp":
		getDHCP(dev)
		return True
	if ip == "down":
		cfgstr="ifconfig "+str(dev)+" down"
	else:
		cfgstr="ifconfig "+str(dev)+" "+ip+" netmask "+mask+"; route add default gw "+route+"; echo \"nameserver "+dns+"\" > /etc/resolv.conf"
	os.system(cfgstr)	

	return True
#-------------------------------------------------------------------------------------------------
# DONE
def getDHCP(dev):
	"""Funcao para obter as definicoes de rede por DHCP e detectar os programas para tal"""

	dhcpStatFile	= "/var/run/dhcpcd-"+str(dev)+".pid"
	DHCP		= ""
	out		= []

	print " * Verificando por clientes DHCP"


	# DHCPCD FIXME: é preciso verificar o que se passa com a obtenção da gateway
	p = Popen("which dhcpcd", shell=True, stdout=PIPE,stderr=PIPE)
	out = p.stdout.read()
	p.stdout.close()
	if len(out) == 0:
		print "\tW Sem dhcpcd"
	else:
		DHCP=str(out).split("\n")[0]

	# DHCLIENT
	p = Popen("which dhclient", shell=True, stdout=PIPE,stderr=PIPE)
	out = p.stdout.read()
	p.stdout.close()
	if len(out) == 0:
		print "\tW Sem dhclient"
	else:
		DHCP=str(out).split("\n")[0]

	# Caso nao haja programas sai
	if DHCP == "":
		print >>sys.stderr.write(" E Sem programa para gerir o protocolo DHCP")
		return False
	
	print " * A usar "+DHCP+" para o protocolo DHCP"
	
	#Verificar se ja n esta um daemon a correr (so para o dhcpcd)
	if "dhcpcd" in DHCP:
		if os.access(dhcpStatFile, os.F_OK|os.R_OK):
			print " W dhcpcd a correr... matando o processo"
			os.system("dhcpcd -k "+str(dev))
	print "-------------------------------------------------------"	
	os.system(DHCP+" "+str(dev))
	print "-------------------------------------------------------"	
	print "\t > Obtido o IP: "+str(getIP(dev))
	print "\t > Obtido a route: "+str(getRoute(dev))
	print "\t > Obtido os DNS: "+str(getDNS())
	return True
#-------------------------------------------------------------------------------------------------
#TESTING - #(Preciso fazer testes)#
def OpenDNS(opt="set"):
	"""Activa/Desactivar o OpenDNS"""

	config		= []
	ResolvFile	= "/etc/resolv.conf"
	ResolvBKP	= "/etc/resolv.conf-BKP"
	
	if uid != 0:
		print >>sys.stderr.write(" E Nao tens permissoes para configurar redes")
		return False
		
	if opt=="set":
		if not ( os.access(ResolvFile, os.F_OK) ):
			print " * Criando novo "+ResolvFile
			os.system("touch "+ResolvFile)
		else:
			os.system("cp "+ResolvFile+" "+ResolvBKP)
	
		if not ( os.access(ResolvFile, os.W_OK) ):
			print >>sys.stderr.write(" E Nao consegui escrever em "+wpaconFILE)
			return False

		config.append("# Criado por pye-U\n")
		config.append("nameserver 208.67.222.222\n")
		config.append("nameserver 208.67.220.220\n")

		file_io = open(ResolvFile,"w")
		file_io.writelines(config)
		file_io.close()
		print " * Activado OpenDNS em "+ResolvFile
		return True
	else:
		if os.access(ResolvBKP, os.F_OK):
			os.system("cp "+ResolvBKP+" "+ResolvFile)
			print " * Usando o DNS dado por DHCP"
		else:
			print " W Sem backup. Criando uma configuracao vazia"
			os.system("cat /dev/null > "+ResolvFile)
#-------------------------------------------------------------------------------------------------
def getODStatus():
	if "208.67.222.222" in getDNS():
		return True
	else:
		return False


#EOF
