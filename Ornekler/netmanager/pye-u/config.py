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

try:
	import os
	import sys
	
	import ConfigParser

except ImportError:
	print 'Erro ao importar módulos'
	sys.exit(1)
	
class PyeuConfig:
	""" Classe para as configurações"""
	
	seccao = "opcoes"
	ficheiro_config = os.path.expanduser( "~/.pye-u/pye-u.conf" )
	
	if not os.path.exists(ficheiro_config):
		caminho = os.path.split(ficheiro_config)
		os.mkdir(caminho[0])
		os.system('touch '+ ficheiro_config)
	
	opcoes = {}
	
	def load_config(self):
	
		config = ConfigParser.ConfigParser()
		config.read(self.ficheiro_config)
		
		existe_seccao = 0
		for section in config.sections():
			if section == 'opcoes': 
				existe_seccao = 1
			
			if section == 'opcoes':
				dados = [None,None]				
				for option in config.options(section):
					if option == 'fechar_tray':
						dados[0] = int(config.get(section, option))
					elif option == 'opendns':
						dados[1] = int(config.get(section, option))
				self.opcoes['opcoes'] = dados
				
		if existe_seccao == 0:
			dados = []
			dados.append(0)
			dados.append(0)
			self.opcoes['opcoes'] = dados
			
		print " * Configuracao carregada"
		
	def save_config(self):

		config = ConfigParser.ConfigParser()
		config.add_section('opcoes')
		
		iteracao = 1		
		for opcao in self.opcoes['opcoes']:

			if iteracao == 1:
				config.set('opcoes', 'fechar_tray', opcao)
			if iteracao == 2: 
				config.set('opcoes', 'opendns', opcao)
			
			iteracao+=1

		config.write(open(self.ficheiro_config, "w"))
		print " * Configuracao salva"
	
	def get_option(self, key):
	
		return self.opcoes['opcoes'][key]
	
	def set_option(self, key, value):
	
		opt = self.opcoes['opcoes']
		opt[key] = value
		self.opcoes['opcoes'] = opt
	
