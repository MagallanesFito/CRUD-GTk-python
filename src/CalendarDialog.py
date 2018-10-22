#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CalendarDialog(Gtk.Dialog):

    def __init__(self, parent,all_entries):
    	#["14/09/2019","Karate",60,"Agressive!"]
        Gtk.Dialog.__init__(self, "Fitness App", parent, Gtk.DialogFlags.DESTROY_WITH_PARENT)
        self.dates = self.get_all_dates(all_entries)
        self.set_default_size(150, 100)
        self.calendar = Gtk.Calendar()
        self.calendar.connect('month_changed',self.month_changed_func)
        self.calendar.select_day(3)
        self.calendar.select_month(10,2020)

        box = self.get_content_area()
        box.add(self.calendar)
        self.show_all()
    def month_changed_func(self,widget):
    	print(self.calendar.get_date())
    def get_all_dates(self,entries):
    	mylist = []
    	for entry in entries:
    		mylist.append(entry[0])
    	return mylist
