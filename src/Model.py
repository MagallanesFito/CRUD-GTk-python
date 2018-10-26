#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
#import Mock
import ServerConnect
import DialogFullName as generic_dialog
import ShowDialog
import datetime
import ConfirmationDialog as delete_dialog
import CalendarDialog as calendar
import MonthlyResumeDialog
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Model:
	def __init__(self):
		self.mock = ServerConnect.ServerConnect()
	def addEntry(self, w):
		entry = generic_dialog.DialogFullName(w,"Add Entry",None).run()
		''' Por lo pronto solo se hace la validacion de la fecha''' 
		if entry is not None:
			if(self.isValidDate(entry[0])):
				if self.mock.addEntry(list(entry),w) != None:
					return None
				return list(entry)
		return None
	def getAllEntries(self):
		#es un objeto Gtk.ListStore
		return self.mock.get_all()
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
		
	def isValidMonth(self,month):
		if month.isnumeric():
			integer_number = int(month)
			return integer_number > 0 and integer_number < 13
		return False
		
	def isValidYear(self,year):
		if year.isnumeric():
			integer_number = int(year)
			#Numeros positivos de maximo 4 cifras
			return integer_number > 0 and integer_number < 9999
		return False
		
	def modifyEntry(self,w,tree_selection):
		(model_selection,pathlist) = tree_selection.get_selected_rows()
		if pathlist == []:
			return
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
				if self.mock.modifyEntry(selected_entry, list(entry),w) != None:
					return None
				return entry
		return None
		
	def removeEntry(self,main_view,tree_selection):
		(model_selection,pathlist) = tree_selection.get_selected_rows()
		if pathlist == []:
			return 
		tree_iter = model_selection.get_iter(pathlist)
		selected_entry = []
		for i in range(4):
			value = model_selection.get_value(tree_iter,i)
			selected_entry.append(value)

		dialog = delete_dialog.ConfirmationDialog(main_view)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			if self.mock.deleteEntry(selected_entry) == None:
				#main_view.viewer.remove(tree_iter)
				model, filteriter = tree_selection.get_selected()
				treeiter = model.convert_iter_to_child_iter(filteriter)
				model.get_model().remove(treeiter)
				print("Deleted!")
			else:
				print("Connection problems")
				return -1
		elif response == Gtk.ResponseType.CANCEL:
			print("Deletion aborted")
		dialog.destroy()
		return
	def showCalendar(self,view):
		calendario = calendar.CalendarDialog(view,self.mock.get_all())
		a = calendario.run()

	def getDate(self,view):
		entry = MonthlyResumeDialog.MonthlyResumeDialog(view).run()
		if entry is None:
			return
		return entry
	def showResume(self, parent, minutes):
		ShowDialog.ShowDialog(parent, minutes).run()
	def monthResume(self, parent, month, year):
		entries = self.getAllEntries()
		print(entries)
		entries_shown = []
		total_min = 0
		month_list = Gtk.ListStore(str, str, int, str)
		if entries==None:
			return
		for entry in entries: # detecta las actividades en el mes seleccionado
			(date, a, b, c) = entry
			adate = datetime.datetime.strptime(date,'%d/%m/%Y')
			if adate.month ==month and adate.year==year:
				entries_shown.append([date,a,b,c])
				total_min = total_min + b
		#self.showResume(parent, total_min)
		return entries_shown