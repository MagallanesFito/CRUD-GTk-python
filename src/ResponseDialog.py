#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk, Gdk

class ResponseDialog:
	def __init__(self, parent, response_text):
		dialog = Gtk.Dialog("Fitness App", parent, Gtk.DialogFlags.DESTROY_WITH_PARENT, (Gtk.STOCK_OK, Gtk.ResponseType.OK, ))
		dialog.set_default_response(Gtk.ResponseType.OK)
		dialog.set_default_size(200,30)
		self.dialog = dialog
		box = dialog.get_content_area()
		grid = Gtk.Grid(margin=18, column_spacing=12, row_spacing=12)
		label = Gtk.Label(response_text)
		grid.attach(label, 1, 3, 1, 1)
		box.pack_start(grid, True, True, 0)
		box.show_all()
		
	def run(self):
		response = self.dialog.run()
		self.dialog.destroy()
