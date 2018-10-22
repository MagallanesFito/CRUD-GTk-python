#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Controller:

	def __init__(self, view, model):
		self.view = view
		self.model = model
		self.view._connect(self)
	def run_application(self):
		#Por default se deja showAllEntries
		self.onShowAllEntriesSelected(None)
		self.view.show_all()
		Gtk.main()
	
	def onAddButtonClicked(self, w):
		entry = self.model.addEntry(self.view)
		if entry is not None:
			self.view.viewer.append(entry)
		#self.showAllEntries()

	def onModifyButtonClicked(self, w):
		selection = self.view.entries.get_selection()
		entry = self.model.modifyEntry(self.view,selection)
		if entry is not None:
			(a,b,c,d) = entry
		model, filteriter = self.view.entries.get_selection().get_selected()
		treeiter = model.convert_iter_to_child_iter(filteriter)
		model.get_model().set(treeiter, list(range(0,4)), [a,b,c,d])
		
	def onRemoveButtonClicked(self, w):
		#No se puede borrar cuando no hay nada en el viewer de la vista
		if len(self.view.viewer) > 0:
			selection = self.view.entries.get_selection()
			self.model.removeEntry(self.view,selection)
	def onEntrySelectedChanged(self, selection):
		print("Cambiado")
	def onShowCalendarClicked(self,w):
		self.model.showCalendar(self.view)
		print("show calendar clicked")
	'''La señal toggle de los radio buttons se activa tanto cuando
	un boton se activa como cuando se desactiva. Se tiene que preguntar el
	estado del boton para poder realizar la accion, de otra forma cada funcion
	del controlador se llamaría dos veces, una cuando se activa y otra cuando se 
	desactiva. '''
	def onMonthResumeClicked(self,w):
		entry = self.model.getDate(self.view)
		if entry is None:
			return
		(month,year) = entry
		total_min = 0
		#for ... :
		#	(a,b,c,d) = fila
		#	if fila encaja con month y year
		#		total_min = total_min + c
		self.model.showResume(self.view, total_min)
		
	def onShowAllEntriesSelected(self,w):
		'''Borra todo y muestra todo lo que está en el modelo. 
		Mejorar la implementacion de esto. '''
		if self.view.show_all_entries.get_active():
			entries = self.model.getAllEntries()
			self.view.viewer.clear()
			for entry in entries:
				self.view.viewer.append(entry)
			print("show all entries selected")
	def onFilterByDateSelected(self,w):
		if self.view.filter_by_date.get_active():
			print("filter by date selected")
	#radio /
	def onKeyPressed(self,widget,event):
		if event.keyval == 65535:
			self.onRemoveButtonClicked(widget)
