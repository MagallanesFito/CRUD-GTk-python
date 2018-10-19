#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ConfirmationDialog(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Fitness App", parent, 0,
            (Gtk.STOCK_OK, Gtk.ResponseType.OK,Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        self.set_default_size(150, 100)

        label = Gtk.Label("Are you sure you want to delete this entry?",margin=18)

        box = self.get_content_area()
        box.add(label)
        self.show_all()