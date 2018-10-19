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
		self.showAllEntries()
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
	def onMonthResumeClicked(self,w):
		print("Month resume clicked")
	def onShowAllEntriesSelected(self,w):
		print("show all entries selected")
	def onFilterByDateSelected(self,w):
		print("filter by date selected")
	def showAllEntries(self):
		#entries es una lista que se le pasa la vista
		entries = self.model.getAllEntries()
		for entry in entries:
			self.view.viewer.append(entry)
	def onKeyPressed(self,widget,event):
		if event.keyval == 65535:
			self.onRemoveButtonClicked(widget)
