#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Controller
import View
import Model
import gi
import locale
import os
import gettext
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

if __name__ == '__main__':
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    locale.setlocale(locale.LC_ALL,'')

    LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locale")
    locale.bindtextdomain('FlightBooker', LOCALE_DIR)
    gettext.bindtextdomain('FlightBooker', LOCALE_DIR)
    gettext.textdomain('FlightBooker')

    controller = Controller.Controller(View.View(),Model.Model())
    controller.run_application()

