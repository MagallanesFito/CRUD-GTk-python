#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CalendarDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Fitness App", parent, Gtk.DialogFlags.DESTROY_WITH_PARENT)

        self.set_default_size(150, 100)

        self.calendar = Gtk.Calendar()
        self.calendar.select_day(0)
        self.calendar.mark_day(6)
        box = self.get_content_area()
        box.add(self.calendar)
        self.show_all()