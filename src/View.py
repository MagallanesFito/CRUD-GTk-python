#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Atk

class View(Gtk.Window):
	def __init__(self):
		prefix = Gtk.Entry(width_chars=10)
		self.prefix = prefix
		lbl_prefix = Gtk.Label(label="_Filtrar:", use_underline=True, mnemonic_widget=self.prefix)
		prefix.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_prefix.get_accessible())
		Gtk.Window.__init__(self,title="Fitness App")
		self.set_default_size(680,680)
		self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
		self.set_icon_from_file('img/app_icon.ico')
		self.viewer = Gtk.ListStore(str, str, int, str)
		grid = Gtk.Grid(margin=18)
		self.add(grid)
		self.add = Gtk.Button(label="_Add", use_underline=True)
		self.remove = Gtk.Button(label="_Remove", use_underline=True)
		self.modify = Gtk.Button(label="_Modify", use_underline=True)

		filter = self.viewer.filter_new()
		filter.set_visible_func(self._entries_visible_func)
		self.filter = filter
		self.filter_prefix = ""
		self.entries = Gtk.TreeView(filter, headers_visible=True)

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

		self.entries.append_column(column0)
		self.entries.append_column(column1)
		self.entries.append_column(column2)
		self.entries.append_column(column3)

		scrolled_window = Gtk.ScrolledWindow(expand=True)
		scrolled_window.add(self.entries)

		bottomBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=18, margin_top=18)
		boxButtons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		filterButtons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6,margin_right=0) 

		bottomBox.pack_start(boxButtons,False,False,0)
		bottomBox.pack_start(filterButtons,False,False,0)

		self.show_all_entries = Gtk.Button("Show all")
		self.month_resume  = Gtk.Button("Month resume")
		self.prefix.set_placeholder_text("DD/MM/YYYY")
		boxButtons.pack_start(self.add, False, False, 0)
		boxButtons.pack_start(self.modify, False, False, 0)
		boxButtons.pack_start(self.remove, False, False, 0)
		boxButtons.pack_start(self.month_resume, False, False, 0)
		boxButtons.pack_start(self.show_all_entries,False,False,0)
		boxButtons.pack_start(Gtk.Label("Filter by day: "), False, False, 0)
		boxButtons.pack_start(self.prefix, False, False, 0)

		grid.attach(scrolled_window, 0, 1, 1, 1)
		grid.attach(bottomBox, 0, 2, 3, 1)
		self.prefix.connect('changed', self.on_prefix_changed)

	def _connect(self, vc):
		self.connect("destroy",Gtk.main_quit)
		self.connect("key-press-event",vc.onKeyPressed)
		self.add.connect('clicked', vc.onAddButtonClicked)
		self.modify.connect('clicked', vc.onModifyButtonClicked)
		self.remove.connect('clicked', vc.onRemoveButtonClicked)
		#self.show_calendar.connect('clicked',vc.onShowCalendarClicked)
		self.month_resume.connect('clicked',vc.onMonthResumeClicked)
		self.show_all_entries.connect('clicked',vc.onShowAllEntriesSelected)

	def _entries_visible_func(self, model, iter, data):
		if (self.filter_prefix == ""):
			return True
		else:
			return self._full(model[iter]).startswith(self.filter_prefix)

	def _full(self, item):
		return "{}, {}, {}, {}".format(*item)

	def on_prefix_changed(self, entry):
		self.filter_prefix = entry.get_text()
		self.entries.get_model().refilter()       
