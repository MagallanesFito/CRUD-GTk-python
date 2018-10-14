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
		self.model.addEntry(self.view)
		#self.showAllEntries()

	def onModifyButtonClicked(self, w):
		print("Not implemented")

	def onRemoveButtonClicked(self, w):
		print("Not implemented")

	def onEntrySelectedChanged(self, selection):
		print("Not implemented")
	def showAllEntries(self):
		#entries es una lista que se le pasa la vista
		entries = self.model.getAllEntries()
		self.view.displayAllEntries(entries)
