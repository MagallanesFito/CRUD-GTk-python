#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Mock:
	def __init__(self):
		list = Gtk.ListStore(str,str,str,str)
		list.append(["Manuel","Adolfo","Test","Inicial"])
		list.append(["Manuel","Adolfo","Test","Inicial"])
		self.list = list
	def addEntry(self, e):
		print("")
