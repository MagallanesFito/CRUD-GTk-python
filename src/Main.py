#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Controller
import View
import Model
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    controller = Controller.Controller(View.View(),Model.Model())
    Gtk.main()

