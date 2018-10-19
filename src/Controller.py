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
			(a,b) = entry
			self.view.viewer.remove(a)
			self.view.viewer.append(b)

	def onRemoveButtonClicked(self, w):
		#No se puede borrar cuando no hay nada en el viewer de la vista
		if len(self.view.viewer) > 0:
			selection = self.view.entries.get_selection()
			self.model.removeEntry(self.view,selection)
	def onEntrySelectedChanged(self, selection):
		print("Cambiado")
	def onShowCalendarClicked(self,w):
		print("show calendar clicked")
	'''La señal toggle de los radio buttons se activa tanto cuando
	un boton se activa como cuando se desactiva. Se tiene que preguntar el
	estado del boton para poder realizar la accion, de otra forma cada funcion
	del controlador se llamaría dos veces, una cuando se activa y otra cuando se 
	desactiva. '''
	def onMonthResumeClicked(self,w):
		if self.view.month_resume.get_active():
			print("Month resume clicked, se borro todo el list store")
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
