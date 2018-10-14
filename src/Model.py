#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Mock
import DialogFullName as generic_dialog
import datetime
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Model:
	def __init__(self):
		self.mock = Mock.Mock()
	def addEntry(self, w):
		entry = generic_dialog.DialogFullName(w,"Add",None).run()

		''' La validacion se hace en el modelo ''' 
		#result = self.validateDateTime(entry)
		#if result:
		self.mock.addEntry(entry)
	def getAllEntries(self):
		#es un objeto Gtk.ListStore
		return self.mock.list
	''' Por ahora solo se valida la fecha DD/MM/YYYY y la longitud del comentario < 50 caracteres''' 
	def validateDateTime(self,data):
		date_text = data[0] #Fecha 
		comment_text = data[3]
		valid = True
		try:
			datetime.datetime.strptime(date_text,'%d/%m/%Y')
		except ValueError:
			valid = False
		if(len(comment_text) > 50):
			valid = False
		return valid
	#def modifyEntry():
	#def removeEntry():
	#def getInformation():

