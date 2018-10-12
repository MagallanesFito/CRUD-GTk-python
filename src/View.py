#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class View:
	def __init__(self):
		prefix = Gtk.Entry(width_chars=10)
		self.prefix = prefix
		lbl_prefix = Gtk.Label(label="_Filtrar:", use_underline=True, mnemonic_widget=self.prefix)
		prefix.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_prefix.get_accessible())

		# Provisional, hay que implementar la carga inicial de info
		viewer = Gtk.ListStore(str, str, str, str)
		viewer.append(["Manuel","Adolfo","Belen Esteban","Test Inicial"])
		self.viewer = viewer
		#

		self.add = Gtk.Button(label="_Add", use_underline=True)
		self.remove = Gtk.Button(label="_Remove", use_underline=True)
		self.modify = Gtk.Button(label="_Modify", use_underline=True)

		filter = viewer.filter_new()
		filter.set_visible_func(self._entries_visible_func)
		self.filter = filter
		self.filter_prefix = ""

		entries = Gtk.TreeView(filter, headers_visible=False)

		renderer0 = Gtk.CellRendererText()
		column0 = Gtk.TreeViewColumn("DATE", renderer0, text=0)
		renderer1 = Gtk.CellRendererText()
		column1 = Gtk.TreeViewColumn("TYPE", renderer1, text=1)
		renderer2 = Gtk.CellRendererText()
		column2 = Gtk.TreeViewColumn("DURATION", renderer2, text=2)
		renderer3 = Gtk.CellRendererText()
		column3 = Gtk.TreeViewColumn("COMMENT", renderer3, text=3)

		entries.append_column(column0)
		entries.append_column(column1)
		entries.append_column(column2)
		entries.append_column(column3)
		self.entries = entries

		scrolled_window = Gtk.ScrolledWindow(expand=True)
		scrolled_window.set_size_request(200, 500)
		scrolled_window.add(entries)

		boxFilter = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=0)
		boxFilter.pack_start(lbl_prefix, False, False, 0)
		boxFilter.pack_start(self.prefix, False, False, 0)

		boxButtons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10, margin=10)
		boxButtons.pack_start(self.add, False, False, 0)
		boxButtons.pack_start(self.modify, False, False, 0)
		boxButtons.pack_start(self.remove, False, False, 0)

		grid = Gtk.Grid(margin=20, column_spacing=10, row_spacing=10)
		grid.attach(boxFilter, 0, 0, 1, 1)
		grid.attach(scrolled_window, 0, 1, 1, 1)
		grid.attach(boxButtons, 0, 2, 3, 1)

		self.add.set_sensitive(True)
		self.modify.set_sensitive(False)
		self.remove.set_sensitive(False)

		win = Gtk.Window(title="Fitness App")
		win.connect('delete-event', Gtk.main_quit)
		win.add(grid)
		win.show_all()
		self.win = win

	def connect(self, vc):
		self.add.connect('clicked', vc.onAddButtonClicked)
		self.modify.connect('clicked', vc.onModifyButtonClicked)
		self.remove.connect('clicked', vc.onRemoveButtonClicked)
		self.entries.get_selection().connect("changed", vc.onEntrySelectedChanged)

	def _entries_visible_func(self, model, iter, data):
		if (self.filter_prefix == ""):
			return True
		else:
			return self._full(model[iter]).startswith(self.filter_prefix)

	def _full(self, item):
		return "{}, {}, {}, {}".format(*item)


