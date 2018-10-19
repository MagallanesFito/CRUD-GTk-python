#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Mock
import DialogFullName as generic_dialog
import datetime
import ConfirmationDialog as delete_dialog
import CalendarDialog as calendar
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Model:
	def __init__(self):
		self.mock = Mock.Mock()
	def addEntry(self, w):
		entry = generic_dialog.DialogFullName(w,"Add Entry",None).run()
		''' Por lo pronto solo se hace la validacion de la fecha''' 
		if entry is not None:
			if(self.isValidDate(entry[0])):
				self.mock.addEntry(list(entry))
				return list(entry)
		return None
	def getAllEntries(self):
		#es un objeto Gtk.ListStore
		return self.mock.list
	''' Por ahora solo se valida la fecha DD/MM/YYYY''' 
	def isValidDate(self,date):
		valid = True
		try:
			datetime.datetime.strptime(date,'%d/%m/%Y')
			#En la internacionalizacion hay que cambiar la expresion regular
		except ValueError:
			valid = False
		return valid
	def isValidDuration(self,number):
		if number.isnumeric():
			integer_number = int(number)
			#No puede entrenar menos de 0 minutos ni mas de 100 horas
			return integer_number > 0 and integer_number < 6000
		return False
	def modifyEntry(self,w,tree_selection):
		(model_selection,pathlist) = tree_selection.get_selected_rows()
		tree_iter = model_selection.get_iter(pathlist)
		selected_entry = []
		for i in range(4):
			value = model_selection.get_value(tree_iter,i)
			selected_entry.append(value)
		print(selected_entry)
		dialog = generic_dialog.DialogFullName(w,"Modify Entry",selected_entry)
		entry = dialog.run()
		if entry is not None:
			if(self.isValidDate(entry[0])):
				self.mock.modifyEntry(selected_entry, list(entry))
				return (tree_iter,list(entry))
		return None
		
	def removeEntry(self,w,tree_selection):
		(model_selection,pathlist) = tree_selection.get_selected_rows()
		tree_iter = model_selection.get_iter(pathlist)
		selected_entry = []
		for i in range(4):
			value = model_selection.get_value(tree_iter,i)
			selected_entry.append(value)

		dialog = delete_dialog.ConfirmationDialog(w)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			self.mock.deleteEntry(selected_entry)
			model_selection.remove(tree_iter)
			print("Deleted!")
		elif response == Gtk.ResponseType.CANCEL:
			print("Deletion aborted")
		dialog.destroy()
	def showCalendar(self,view):
		calendario = calendar.CalendarDialog(view)
		a = calendario.run()

	#def getInformation():

