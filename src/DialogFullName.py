#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Mock
import Model
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk, Gdk

import gettext 

t = gettext.translation('dialog_fullname_domain','locale',fallback=True)
_ = t.gettext

class DialogFullName:
	def __init__(self, parent, title, data=None):
		dialog = Gtk.Dialog(title, parent, Gtk.DialogFlags.DESTROY_WITH_PARENT, (Gtk.STOCK_OK, Gtk.ResponseType.OK,Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, ))
		dialog.set_default_response(Gtk.ResponseType.OK)
		dialog.set_response_sensitive(Gtk.ResponseType.OK, False)
		self.dialog = dialog
		self.valid_duration = False
		self.valid_date = False
		box = dialog.get_content_area()
		grid = Gtk.Grid(margin=18, column_spacing=12, row_spacing=12)

		dat = Gtk.Entry(activates_default=True)
		#dat.set_placeholder_text("DD/MM/YYYY")
		dat.set_text("DD/MM/YYYY")
		dat.connect('changed', self._entry_changed)
		self.dat = dat
		self.tp_text = ""
		'''tp = Gtk.Entry(activates_default=True)
		tp.connect('changed', self._entry_changed)
		tp.set_placeholder_text('Type of exercise')'''
		tp = Gtk.ComboBoxText()
		categories = [_("Karate"),_("Kick Boxing"),_("Gym"),_("Fitness"),_("Swimming"),_("Dancing")]
		tp.set_entry_text_column(0)
		tp.connect("changed", self.on_tp_changed)
		for category in categories:
			tp.append_text(category)
		self.tp = tp
		dur = Gtk.Entry(activates_default=True)
		dur.connect('changed', self._entry_changed)
		dur.set_placeholder_text(_('Only numeric values'))
		self.dur = dur
		cm = Gtk.Entry(activates_default=True)
		cm.connect('changed', self._entry_changed)
		cm.set_placeholder_text(_('Write a short description :)'))
		self.cm = cm

		if data is not None:
			dat.set_text(data[0])
			#tp.set_text(data[1])
			tp.set_active(categories.index(data[1]))
			dur.set_text(str(data[2]))
			cm.set_text(data[3])
		lbl_dat = Gtk.Label(_("Date"))
		dat.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_dat.get_accessible())
		lbl_tp = Gtk.Label(_("Type"))
		tp.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_tp.get_accessible())
		lbl_dur = Gtk.Label(_("Duration (minutes)"))
		dur.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_dur.get_accessible())
		lbl_cm = Gtk.Label(_("Comment"))
		cm.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY, lbl_cm.get_accessible())

		grid.attach(lbl_dat, 0, 0, 1, 1)
		grid.attach(dat, 0, 1, 1, 1)
		grid.attach(lbl_tp, 1, 0, 1, 1)
		grid.attach(tp, 1, 1, 1, 1)
		grid.attach(lbl_dur, 0, 2, 1, 1)
		grid.attach(dur, 0, 3, 1, 1)
		grid.attach(lbl_cm, 1, 2, 1, 1)
		grid.attach(cm, 1, 3, 1, 1)
		box.pack_start(grid, True, True, 0)
		box.show_all()

	def run(self):
		response = self.dialog.run()

		''' Validacion con el modelo ''' 
		if response == Gtk.ResponseType.OK:
			result = (self.dat.get_text().strip(), self.tp_text, int(self.dur.get_text().strip()), self.cm.get_text().strip())
		else:
			result = None
		self.dialog.destroy()
		return result

	def _entry_changed(self, entry):
		self.valid_duration = Model.Model().isValidDuration(self.dur.get_text().strip())
		self.valid_date = Model.Model().isValidDate(self.dat.get_text().strip())
		#selected_category = (self.tp_text!= "")

		isFilled = (self.valid_duration) and (self.valid_date) and (self.dat.get_text().strip() != "") and (self.tp_text != "") and (self.dur.get_text().strip() != "") and (self.cm.get_text().strip() != "")
		if not self.valid_date:
			self.dat.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))
		else:
			self.dat.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 0.0, 1.0))

		if not self.valid_duration:
			self.dur.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))
		else:
			self.dur.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 0.0, 1.0))
		#if not selected_category:
		#	self.tp.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(1.0, 0.0, 0.0, 1.0))
		#else:
		#	self.tp.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.0, 0.0, 0.0, 1.0))
		
		self.dialog.set_response_sensitive(Gtk.ResponseType.OK, isFilled)
	def on_tp_changed(self,combo):
		text = combo.get_active_text()
		if text is not None:
			self.tp_text = text
		isFilled = (self.valid_duration) and (self.valid_date) and (self.dat.get_text().strip() != "") and (self.tp_text != "") and (self.dur.get_text().strip() != "") and (self.cm.get_text().strip() != "")
		self.dialog.set_response_sensitive(Gtk.ResponseType.OK, isFilled)
