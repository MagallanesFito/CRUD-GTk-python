#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Controller:

	def __init__(self, view):
		self.view = view
		view.connect(self)
	
	def onAddButtonClicked(self, w):
		print("Not implemented")

	def onModifyButtonClicked(self, w):
		print("Not implemented")

	def onRemoveButtonClicked(self, w):
		print("Not implemented")

	def onEntrySelectedChanged(self, selection):
		print("Not implemented")
