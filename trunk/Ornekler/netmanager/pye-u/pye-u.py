#!/usr/bin/env python
# -*- coding: utf-8 -*-

#pye-u - simple program to connect to wireless network e-U (http://www.e-u.pt).
#Copyright (C) 2006 Carlos Lisboa (carloslisboa _at_ gmail _dot_ com)

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

#DEBUG = True

VERSION = '0.1.3'


import os
import sys
from subprocess import Popen, PIPE

try:
	import gobject
	import pygtk
	pygtk.require("2.0")
	import gtk
	import gtk.glade
except ImportError:
	print >>sys.stderr.write("\n\n E Para correr verifica se tens os pacotes gtk, pygtk, gobject e gtk-glade.\n\nSaindo...\n")
	sys.exit(1)

try:
	import wifitools
	import wpalib
	import netlib
	import wiflib
	import trayicon
	import config
except ImportError:
	print >>sys.stderr.write("\n\n E Nao foi possivel carregar bibliotecas internas\n\nSaindo...\n")
	sys.exit(1)

#verificar de onde foi chamada a aplicação
APP_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))

class pyeu:
	"""Classe para o GUI"""
	
	def __init__(self):
		#verificar utilizador
		self.verificar_utilizador()
		
		#iniciar o trayicon
		self.init_tray()
		
		#iniciar o gladefile
		self.gladefile = APP_PATH + '/pye-u.glade'
		self.wTree = gtk.glade.XML(self.gladefile)
		
		#ligação dos callbacks
		dic = {	"on_btn_aplicar_released"	: self.btn_aplicar_released,
			"on_btn_limpar_released"	: self.btn_limpar_released,
			"on_btn_sair_released"		: self.btn_sair_released,
			"on_btn_refresh_released"	: self.btn_refresh_released,
			"on_btn_connect_wifi_released"	: self.btn_connect_wifi_released,
			#"on_chk_opendns_toggled" 	: self.chk_opendns_toggled,
			"on_btn_ligar_released"		: self.btn_ligar_released,
			"on_btn_aplicar_opcoes_released": self.btn_aplicar_opcoes_released }
		
		#ligar os callbacks
		self.wTree.signal_autoconnect(dic)
		
		##obtenção dos diversos widgets
		self.MainWindow = self.wTree.get_widget('MainWindow')
		
		#tab_inicio
		self.edit_user = self.wTree.get_widget('edit_username')
		self.edit_password = self.wTree.get_widget('edit_password')
		self.combo = self.wTree.get_widget('combo_dispositivo')
		self.btn_limpar = self.wTree.get_widget('btn_limpar')
		self.btn_aplicar = self.wTree.get_widget('btn_aplicar')
		self.btn_ligar_eu = self.wTree.get_widget('btn_ligar_eu')
		#tab_estados
                self.essid = self.wTree.get_widget('lbl_essid_texto')
                self.protocolo = self.wTree.get_widget('lbl_protocolo_texto')
		self.IP = self.wTree.get_widget('lbl_endereco_texto')
                self.velocidade = self.wTree.get_widget('lbl_velocidade_texto')
                self.router = self.wTree.get_widget('img_router')
                self.dns = self.wTree.get_widget('img_dns')
                self.www = self.wTree.get_widget('img_web')
                self.sinal = self.wTree.get_widget('progressbar_sinal')
                #tab_redes
                self.tab_redes = self.wTree.get_widget('tv_redes')
                self.notebook = self.wTree.get_widget('notebook')
                self.btn_refresh = self.wTree.get_widget('btn_refresh')
                self.btn_connect_wifi = self.wTree.get_widget('btn_connect_wifi')
                #tab_opcoes
                self.fechar_tray = self.wTree.get_widget('chk_tray')
                self.chk_opendns = self.wTree.get_widget('chk_opendns')
                self.btn_aplicar_opcoes = self.wTree.get_widget('btn_aplicar_opcoes')
	
		#verificar quando a aplicação está para ser encerrada
		self.MainWindow.connect('delete_event', self.MainWindow_delete_event )
		
		#obter a imagem do logotipo e mostrar a versão do pye-u
		self.logo = self.wTree.get_widget('logo')
		self.logo.set_from_file(APP_PATH + '/logo.png')
		self.sobre = self.wTree.get_widget('lbl_sobre')
		self.sobre.set_text('pye-U '+VERSION)
		
		#preencher os diversos campos se já estiver configurado
		self.preencher_edit(self.edit_user, self.edit_password)
		self.preencher_combo(self.combo)
	
		#adequar o botão ligar_eu para a situação de haver ou não ligação em curso
		if wpalib.getWpaStatus()[0]:
			self.btn_ligar_eu.set_label('Desligar')
		else:
			self.btn_ligar_eu.set_label('Ligar')
		
		#iniciar os dados a introduzir nas tab_redes e tab_estados
		self.init_estados()
		self.init_redes()
			
		#timer para actualizar a tab_estados a cada 5 segundos
		self.t_estados = gobject.timeout_add(5000, self.estados)
		
		#obter imagens para a indicação visual da encriptação de uma determinada rede wireless
		self.enc = gtk.gdk.pixbuf_new_from_file(APP_PATH +"/enc.png")
		self.non_enc = gtk.gdk.pixbuf_new_from_file(APP_PATH +"/non_enc.png")
		
		#iniciar ficheiro config
		self.config = config.PyeuConfig()
		self.config.load_config()
		#self.config.save_config()
		#print self.config
		self.init_opcoes()
		
	def init_opcoes(self):
	
		if self.config.get_option(0):
			self.fechar_tray.set_active(True)
		
		if self.config.get_option(1):
			self.chk_opendns.set_active(True)
			netlib.OpenDNS()
		elif netlib.getODStatus():
			netlib.OpenDNS('unset')
			
	
	#função para verificar se o utilizador possui poderes de super-vaca
	def verificar_utilizador(self):
                if os.getuid() != 0:
			SUDOPRG = []

			# GKSU
			p = Popen("which gksu", shell=True, stdout=PIPE)
			out = p.stdout.read()
			p.stdout.close()
			if len(out) == 0:
				print "\tW Sem gksu"

				# KDESU
				p = Popen("which kdesu", shell=True, stdout=PIPE)
				out = p.stdout.read()
				print out
				p.stdout.close()
				if len(out) == 0:
					print "\tW Sem kdesu"
					print >>sys.stderr.write(" E Nao tens permissoes para executar este programa")
					sys.exit(1)
				else:
					SUDOPRG=[ 2, str(out).split("\n")[0] ]
					print SUDOPRG
			else:
				SUDOPRG=[ 1, str(out).split("\n")[0] ]
				
				
				
			if SUDOPRG[0] == 1:
				os.execv(SUDOPRG[1],["gksu","python "+APP_PATH +"/pye-u.py"])
			if SUDOPRG[0] == 2:
				print SUDOPRG[1]
				os.execv(SUDOPRG[1],["kdesu","python "+APP_PATH +"/pye-u.py"])

	#função iniciar o trayicon
	def init_tray(self):
		self.tray_icon = trayicon.TrayIcon(self.on_trayicon_click)
		self.tray_icon.set_icon(APP_PATH +'/tray.png')

	#quando se clica no trayicon comuta o estado da aplicação: visivel/escondido
	def on_trayicon_click(self, signal, event):
		if event.button==1:
			if self.MainWindow.flags() & gtk.VISIBLE:
				self.MainWindow.hide()
			else:
				self.MainWindow.show()
		else:
			pass
	
	#preencher as entry com os dados se já se encontrar configurado
	def preencher_edit(self, edit_user, edit_password):
		dados = wpalib.getWpaConf()
		
		if dados:
			self.edit_user.set_text(dados[0])
			self.edit_password.set_text(dados[1])
		else:
			pass	
			
	#colocar na combo os dispositivos que se encontrem no sistema
	def preencher_combo(self, combo):
		dispositivos = wiflib.getWDevs()
		
		if dispositivos:
			#encontramos dispositivos, vamos colocá-los na combo
			for i in dispositivos:
				combo.append_text(i)
				combo.set_active(0)				
		else:
			#não encontramos nenhum dispositivo, desactivamos 
			#os botões já q n fazem sentido
			combo.append_text('Nenhum')
			combo.set_active(0)
			#tab_inicio
			self.btn_aplicar.set_sensitive(False)
			self.btn_ligar_eu.set_sensitive(False)
			self.btn_limpar.set_sensitive(False)
			self.edit_user.set_sensitive(False)
			self.edit_password.set_sensitive(False)
			#tab_redes
			self.btn_refresh.set_sensitive(False)
			self.btn_connect_wifi.set_sensitive(False)
			self.tab_redes.set_sensitive(False)
	
	#callback para esconder a janela
	def MainWindow_delete_event(self, *args):
		if self.fechar_tray.get_active():
			self.MainWindow.hide()
			return True
		else:
			gobject.source_remove(self.t_estados)
			self.t_estados = 0
			gtk.main_quit()
	
	#callback para gravar os dados 
	def btn_aplicar_released(self, widget):
		#dispositivo = self.combo.get_active_text()
		self.user = self.edit_user.get_text()
		self.password = self.edit_password.get_text()

		#enviar os dados para fazer o conf
		wpalib.setWpaConf(self.user, self.password)

	#callback para limpar os widgets
	def btn_limpar_released(self, widget):
		self.combo.set_active(-1)
		self.edit_user.set_text('')
		self.edit_password.set_text('')

	#callback do botão sair 
	def btn_sair_released(self, widget):
		gobject.source_remove(self.t_estados)
		self.t_estados = 0
		gtk.main_quit()

	#callback do botão ligar_eu
	def btn_ligar_released(self, widget):
		if not wpalib.getWpaStatus()[0]:
			#não existe ligação, vamos ligar agora
			if wifitools.connect_e_U(self.combo.get_active_text()) != "OK":
				# Caso o output da função não seja 'OK'
				return
			#Na e-U não se consegue usar OpenDNS
			if self.chk_opendns.get_active():
				self.config.set_option(1, 0)
				self.chk_opendns.set_active(False)
			#este botão passa agora para a função desligar ligação
			self.btn_ligar_eu.set_label('Desligar')
		else:
			#desligar as ligações que possam haver
			wpalib.WpaKill()
			#uma vez desligadas as ligações, passa a ter a função ligar 
			self.btn_ligar_eu.set_label('Ligar')
		
	def btn_aplicar_opcoes_released(self, widget):

		if self.fechar_tray.get_active():
			self.config.set_option(0, 1)
		else:
			self.config.set_option(0, 0)

		if self.chk_opendns.get_active():
			self.config.set_option(1, 1)
			if not netlib.getODStatus():
				netlib.OpenDNS()
		else:
			self.config.set_option(1, 0)
			if netlib.getODStatus():
				netlib.OpenDNS('unset')

		self.config.save_config()
		
	#função para actualizar a tab_estados
	def estados(self):
		#Actualizar os indicadores do estado da ligação
		dispositivo = self.combo.get_active_text()
		
		#se não houver nenhum dispositivo, não há nada para verificar
		if dispositivo == 'Nenhum':
			print " W Sem estados para observar"
			return False

		#obter as informações do dispositivo seleccionado
		if netlib.getDevState(dispositivo) == "up":
			estados = wifitools.getAllDevState(dispositivo)
	                self.essid.set_text(estados['ESSID'])
	                self.protocolo.set_text(estados['key_mgmt'])
        	        self.IP.set_text(netlib.getIP(dispositivo))
	                self.velocidade.set_text(estados['BitRate'])
	                if netlib.getRoute(dispositivo) != False:
			        self.router.set_from_stock( gtk.STOCK_YES, gtk.ICON_SIZE_BUTTON )
			if netlib.getDNS() != False:
	        	        self.dns.set_from_stock( gtk.STOCK_YES, gtk.ICON_SIZE_BUTTON )
        	        if wifitools.getConStatus():
		                self.www.set_from_stock( gtk.STOCK_YES, gtk.ICON_SIZE_BUTTON ) 
	                self.sinal.set_fraction(int(estados['link'])/100.0)
			self.sinal.set_text(str(estados['link'])+" %")
			self.tray_icon.set_tooltip('SSID: %s \nBitRate: %s \nSinal: %s' % (estados['ESSID'], estados['BitRate'], estados['link']))
		else:
			self.tray_icon.set_tooltip('Sem ligação wireless')
						
		#necessário para o timer continuar a correr
		return True 

	#função para inicializar os dados da tab_estados
	def init_estados(self):
	        self.essid.set_text('N/A')
        	self.protocolo.set_text('N/A')
                self.IP.set_text('127.0.0.1')
                self.velocidade.set_text('N/A')
                self.router.set_from_stock( gtk.STOCK_NO, gtk.ICON_SIZE_BUTTON )
                self.dns.set_from_stock( gtk.STOCK_NO, gtk.ICON_SIZE_BUTTON )
                self.www.set_from_stock( gtk.STOCK_NO, gtk.ICON_SIZE_BUTTON )
                self.sinal.set_fraction(0)
                self.sinal.set_text('N/A')

	#função para inicializar os dados da tab_redes
	def init_redes(self):
		#queremos uma tabela com 3 campos para dados em string e um outro
		#para indicar visualmente a encriptação ou não de uma rede.
		self.redes_treestore = gtk.TreeStore(gtk.gdk.Pixbuf,str,str,str)
		self.tab_redes.set_model(self.redes_treestore)
		
		#queremos que os cabeçalhos sejam visiveis
		self.tab_redes.set_headers_visible(True)

		#criar um renderer para o texto
		renderer = gtk.CellRendererText()
		#criar um renderer para as imagens de encriptação
		renderer_pixbuf = gtk.CellRendererPixbuf()
		#criamos uma coluna
		column = gtk.TreeViewColumn()
		column.set_title('SSID')
		#queremos que seja possivel alterar a largura das colunas
		column.set_resizable(True)
		#adicionamos a coluna ao modelo
		self.tab_redes.append_column(column)
		#atribuimos a posição da imagem na coluna - 0
		column.pack_start(renderer_pixbuf, expand=False)
		column.add_attribute(renderer_pixbuf, 'pixbuf', 0)
		#atribuimos a posição do texto - 1
		column.pack_start(renderer, expand=True)
		column.add_attribute(renderer, 'text', 1)
		
		#restantes colunas com as respectivas posições
		column=gtk.TreeViewColumn("Protocolo", renderer, text=2)
		column.set_resizable(True)
		self.tab_redes.append_column(column)
				
		column=gtk.TreeViewColumn("AP", renderer, text=3)
		column.set_resizable(True)
		self.tab_redes.append_column(column)
		
	def redes(self):
		#obtemos o dispositivo actual
		dispositivo = self.combo.get_active_text()
		#obtemos a lista de redes no alcance do dispositivo
		lista_redes = wiflib.getWNet(dispositivo)
		
		#limpar a lista de redes, para actualizar as redes possiveis
		self.redes_treestore.clear()
		
		#para cada célula encontrada colocamos os valores na tabela
		for cell in xrange(lista_redes[0]) :
		
			linha = []

			#se a rede for encriptada colocamos a indicação visual para tal
			if lista_redes[10][cell] == 'on':
				linha.append(self.enc)
			else:
				linha.append(self.non_enc)
			
			#colocamos os restantes dados dessa célula
			linha.append(lista_redes[2][cell])
			linha.append(lista_redes[3][cell])
			linha.append(lista_redes[1][cell])
			
			#finalmente introduzimos os dados na tabela
			self.redes_treestore.append(None, linha)
		
	#callback para o botão refresh da tab_redes
	def btn_refresh_released(self, widget):
		dispositivo = self.combo.get_active_text()
		#Se n existir nenhum dispositivo de rede wireless não podemos verificar as redes...		
		if 'Nenhum' not in dispositivo:
			self.redes()			
		else:
			print >>sys.stderr.write(" E Não possui dispositivos para verificar redes wireless")
			pass	
			
	#callback para o botão ligar da tab_redes
	def btn_connect_wifi_released(self, widget):
		print "connect wifi released - por implementar"

#função principal
if __name__ == '__main__':
	pyeu_GUI = pyeu()
	gtk.main()
