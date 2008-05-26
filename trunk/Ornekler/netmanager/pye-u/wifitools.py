#!/usr/bin/env python
# -*- coding: utf-8 -*-

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#  Wireless Interface Module
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
import time

# Outras bibliotecas externas
import netlib
import wpalib
import wiflib
from subprocess import Popen, PIPE

# User information
uid		= os.getuid()

# Wireless Devices
wifi_devs	= []

#-------------------------------------------------------------------------------------------------
def version():
	"""Versao da Libraria"""

	return "wifiTools v0.2.1 Beta (20070221)"
#-------------------------------------------------------------------------------------------------
# TESTING - #(Preciso fazer testes)#
#
#		- Usando o rt2x00 não temos os valores todos que o ndiswrapper dá
#			temos utilizar os dados obtidos não supondo as posicoes dos mesmos
def getAllDevState(dev):
	"""Determina o estado do dispositivo"""

	DevState	= {}
	DevTemp		= {}
	temp		= []

	print " * A determinar o estado do dispositivo "+str(dev)
	#----------------------------------------------------Device Stat (up or down)
	DevState["state"]=netlib.getDevState(dev)
	#----------------------------------------------------Tem wireless extensions
	if not( wiflib.getWext(dev) ):
		return False
	#----------------------------------------------------WPA Client status
	temp = wpalib.getWpaStatus()
	DevState["wpa"] = temp[0]
	DevState["key_mgmt"]=temp[1]
	DevState["wpa_state"]=temp[2]
	#---------------------------------------------------- WIFI Params
	DevTemp=wiflib.getWParams(dev)
	for elem in ["beacon","crypt","fragment","level","link","misc","noise","nwid","retries"]:
		DevState[elem]=DevTemp[elem]
	#---------------------------------------------------- IWCONFIG Status
	DevTemp=wiflib.getWSet(dev)
	for elem in ["Protocolo","ESSID","Modo","Freq","AP","BitRate"]:
		DevState[elem]=DevTemp[elem]
	#---------------------------------------------------- IFCONFIG Status
	DevState["IPaddr"] = netlib.getIP(dev)
	#---------------------------------------------------- ROUTER Status
	DevState["Router"] = netlib.getRoute(dev)
	#---------------------------------------------------- DNS Status
	DevState["DNS"] = netlib.getDNS()
#	DevTemp=netlib.getIfStatus(dev)
#	for elem in ["IPaddr","Router","DNS"]:
#		DevState[elem]=DevTemp[elem]
	print "-------------------------------------------------------"
	print " * Ligado a"
	print "\t> AP: "+str(DevState["AP"])
	print "\t> ESSID: "+str(DevState["ESSID"])
	print "\t> Protocolo: "+str(DevState["Protocolo"])
	print "\t> Modo: "+str(DevState["Modo"])
	print "\t> Frequencia: "+str(DevState["Freq"])
	print "\t> Velocidade: "+str(DevState["BitRate"])
	print "\t> Qualidade: "+str(DevState["link"])
	print "\t> Sinal: "+str(DevState["level"])
	print "\t> Ruido: "+str(DevState["noise"])
	print " * Autenticacao"
	print "\t> Tipo: "+str(DevState["key_mgmt"])
	print "\t> Activa: "+str(DevState["wpa"])
	print "\t> Estado: "+str(DevState["wpa_state"])	
	print " * Configuracao"
	print "\t> IP: "+str(DevState["IPaddr"])
	print "\t> Router: "+str(DevState["Router"])
	print "\t> DNS: "+str(DevState["DNS"])
	print "-------------------------------------------------------"	

	return DevState	
#-------------------------------------------------------------------------------------------------
# DONE
def connect_e_U(dev,username="",password=""):
	""" Funcao para conectar a rede e-U args:(dev,*username,*password) ret:"ERRO" """

	wpalib.WpaKill()

	#------------------------------------------------------------- Verificacao da existencia de redes
	print " * A procurar redes ao alcance"
	if wiflib.getWNet(dev)[0] == 0:
		print " * Não existem redes wireless ao alcance"
		return "WIFI"
	print " * A conectar à e-U pelo dispositivo: "+str(dev)	
	#------------------------------------------------------------- Username e Password
	if username!="":
		if wpalib.setWpaConf(username,password)==False:
			print " * Falha na configuração do username e password"
			return "CONF"
	#------------------------------------------------------------- Desactivar OpenDNS (nao funciona na e-U)
	if netlib.getODStatus():
		netlib.OpenDNS("unset")
	#------------------------------------------------------------- Conectar a rede
	if wpalib.WpaConnect(dev)==False:
		print " * Falha na autenticação ao servidor"
		return "AUTH"
	#------------------------------------------------------------- Obter IP via DHCP
	time.sleep(1)
	if netlib.setDev(dev,"dhcp")==False:
		print " * Falha na obtenção de IP via DHCP"
		return "DHCP"
	#------------------------------------------------------------- Desactivar placa de rede para nao causar conflitos
	if dev != "eth0":
		netlib.setDev("eth0",ip="down")
	#------------------------------------------------------------- Conectado
	print " * Connectado a rede e-U"
	return "OK"
#-------------------------------------------------------------------------------------------------
# DONE
def getConStatus():
	""" Verificacao da ligacao a internet """

	p = Popen("wget --spider --timeout=2 www.google.com -t 1  2> /dev/null; echo $?",shell=True, stdout=PIPE)
	out=p.stdout.read()
	p.stdout.close()	
	try:
		if int(out)==0:
			print " * Tem ligacao a internet"
			return True
		else:
			print " * NAO tem ligacao a internet"
	except:
		print " * NAO tem ligacao a internet"
		return False
	return False
#-------------------------------------------------------------------------------------------------
def WirelessConnect(dev, IGNORE_LIST):

	Estado = False

	print " * Verificando redes wireless ao alcance..."
	wifi_nets = wiflib.getWNet(dev)
	
	#[nCells, WAddr, WEssid, WProt, WMode, WFreq, WChan, WQual, WSig, WNoise, WEnc ]
	print " * Ignoradas: "+" ".join(IGNORE_LIST)
	print "\t > Verificando a melhor ligacao"
	Indice = []
	Qualidade = 00

	for a in range ( wifi_nets[0] ):
		if int( wifi_nets[7][a].split("/")[0] ) > Qualidade and not( wifi_nets[2][a] in IGNORE_LIST):
			Qualidade = int ( wifi_nets[7][a].split("/")[0] )
			Indice.append(a)
			print "\t > "+wifi_nets[2][a]+" selecionada"
	
	print " * Conectando..."
	for a in Indice:
		print "\t > Tentando ligacao a rede "+wifi_nets[2][a]+" de "+str(wifi_nets[0]+1)
		if "on" in wifi_nets[10][a]:
			print "\t > Esta rede esta encriptada, tem a palavra passe?"
			RESP=raw_input("\t\t > [s,N]: ")
			if 's' in RESP:
				TIPO = raw_input("\t\t > Tipo [HEX,ASCII]: ")
				KEY  = raw_input("\t\t > Key: ")
				if "HEX" in TIPO:
					wiflib.setWNetwork(dev, wifi_nets[2][a],KEY,"Managed")
				if "ASCII" in TIPO:
					wiflib.setWNetwork(dev, wifi_nets[2][a],"s:"+KEY,"Managed")
				netlib.getDHCP(dev)
				time.sleep(2)
				Estado = getConStatus()
				if Estado == True:
					break
		else:
			print "\t > Rede sem proteccao, a tentar ligacao..."
			wiflib.setWNetwork(dev, wifi_nets[2][a],"","Managed")
			netlib.getDHCP(dev)
			Estado = getConStatus()
			if Estado == True:
				break

	if Estado == False:
		print " * Nao existe mais nenhuma rede disponivel.\n\t > Nao foi possivel estabelecer nenhuma ligacao"
	return Estado
#-------------------------------------------------------------------------------------------------
# Funcao de teste da libraria
if __name__ == '__main__':

	wifi_devs = []

	print " * "+version()
	print "\t> WPAlib: "+wpalib.version()
	print "\t> NETlib: "+netlib.version()
	print "\t> WIFlib: "+wiflib.version()	

	# TESTE - detectar dispositivos
	wifi_devs=wiflib.getWDevs()
	
#	print wiflib.returnESSID( wifi_devs[0] )
#	print wiflib.returnBitrate( wifi_devs[0] )
#	print wiflib.returnMode( wifi_devs[0] )
	
#	print wiflib.getWSet( wifi_devs[0] )
#	print wiflib.getWSettings( wifi_devs[0] )
#	sys.exit(0)
	IGNORE_LIST = ["PT-WIFI", "TVTEL4A", "TVTEL5", "uniX" ]
	
	if wifi_devs:
		
		# TESTE - Automagicamente ligar a redes wireless
		WirelessConnect( wifi_devs[0], IGNORE_LIST )
		netlib.getByteCount( wifi_devs[0] )
		
		getAllDevState(wifi_devs[0])

	sys.exit(0)

	# TESTE - Determinar se ja existe uma configuracao activa
	if not( wpalib.getWpaConf() ):
		username=raw_input("Username: ")
		password=raw_input("Password: ")
		setWpaConf(username,password)

	# TESTE - Fechar processo wpa_supplicant
	wpalib.WpaKill()

	# TESTE - Proceder a ligacao a e-U
	if len(wifi_devs) > 0:
		inp = raw_input(" * Conectar a e-U? (S/N) ")
		if inp=="S":
			connect_e_U(wifi_devs[0])
	sys.exit(0)

#EOF
