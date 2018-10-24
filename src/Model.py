#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Mock
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
			self.mock.deleteEntry(selected_entry)
			#main_view.viewer.remove(tree_iter)
			model, filteriter = tree_selection.get_selected()
			treeiter = model.convert_iter_to_child_iter(filteriter)
			model.get_model().remove(treeiter)
			print("Deleted!")
		elif response == Gtk.ResponseType.CANCEL:
			print("Deletion aborted")
		dialog.destroy()
	def showCalendar(self,view):
		calendario = calendar.CalendarDialog(view,self.mock.get_all())
		a = calendario.run()

	def getDate(self,view):
		entry = MonthlyResumeDialog.MonthlyResumeDialog(view).run()
		if entry is None:
			return
		return entry

	def monthResume(self, parent, month, year):
		entries = self.getAllEntries()
		total_min = 0
		month_list = Gtk.ListStore(str, str, int, str)
		for entry in entries: # detecta las actividades en el mes seleccionado
			(date, a, b, c) = entry
			adate = datetime.datetime.strptime(date,'%d/%m/%Y')
			if adate.month ==month and adate.year==year:
				total_min = total_min + b
				month_list.append(entry)
		tree = Gtk.TreeView(month_list, headers_visible=True)
		
		renderer0 = Gtk.CellRendererText()
		column0 = Gtk.TreeViewColumn("Date", renderer0, text=0)
		column0.set_alignment(0.5)
		renderer1 = Gtk.CellRendererText()
		column1 = Gtk.TreeViewColumn("Type", renderer1, text=1)
		column1.set_alignment(0.5)
		renderer2 = Gtk.CellRendererText()
		column2 = Gtk.TreeViewColumn("Duration (minutes)", renderer2, text=2)
		column2.set_alignment(0.5)
		renderer3 = Gtk.CellRendererText()
		column3 = Gtk.TreeViewColumn("Comment", renderer3, text=3)
		column3.set_alignment(0.5)
		tree.append_column(column0)
		tree.append_column(column1)
		tree.append_column(column2)
		tree.append_column(column3)
		scrolled_window = Gtk.ScrolledWindow(expand=True)
		scrolled_window.add(tree)
		
		ShowDialog.ShowDialog(parent, total_min, scrolled_window).run()
