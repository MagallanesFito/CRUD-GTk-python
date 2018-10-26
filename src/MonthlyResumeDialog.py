#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk, Gdk

import gettext 

t = gettext.translation('month_resume_domain','locale',fallback=True)
_ = t.gettext
class MonthlyResumeDialog:
	def __init__(self, parent):
		dialog = Gtk.Dialog(_("Monthly Resume"), parent, Gtk.DialogFlags.DESTROY_WITH_PARENT, (Gtk.STOCK_OK, Gtk.ResponseType.OK,Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, ))
		dialog.set_default_response(Gtk.ResponseType.OK)
		dialog.set_response_sensitive(Gtk.ResponseType.OK, False)
		self.dialog = dialog
		box = dialog.get_content_area()
		grid = Gtk.Grid(margin=18, column_spacing=12, row_spacing=12)
		
		month = Gtk.Entry(activates_default=True)
		month.connect('changed', self._entry_changed)
		month.set_placeholder_text('MM')
		self.month = month
		year = Gtk.Entry(activates_default=True)
		year.connect('changed', self._entry_changed)
		year.set_placeholder_text('YYYY')
		self.year = year
		lbl_month = Gtk.Label(_("Month"))
		month.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_month.get_accessible())
		lbl_year = Gtk.Label(_("Year"))
		year.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_year.get_accessible())
		
		grid.attach(lbl_month, 0, 0, 1, 1)
		grid.attach(month, 0, 1, 1, 1)
		grid.attach(lbl_year, 1, 0, 1, 1)
		grid.attach(year, 1, 1, 1, 1)
		
		box.pack_start(grid, True, True, 0)
		box.show_all()
		
	def run(self):
		response = self.dialog.run()
		if response == Gtk.ResponseType.OK:
			result = (int(self.month.get_text().strip()), int(self.year.get_text().strip()))
		else:
			result = None
		self.dialog.destroy()
		return result

	def _entry_changed(self,entry):
		valid_month = Model.Model().isValidMonth(self.month.get_text().strip())
		valid_year = Model.Model().isValidYear(self.year.get_text().strip())

		isFilled = (valid_month) and (valid_year)
		if not valid_month:
			self.month.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))
		else:
			self.month.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 0.0, 1.0))

		if not valid_year:
			self.year.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))
		else:
			self.year.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 0.0, 1.0))
		
		self.dialog.set_response_sensitive(Gtk.ResponseType.OK, isFilled)
