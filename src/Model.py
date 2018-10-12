#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import Mock
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Model:
	def __init__(self):
		self.mock = Mock.Mock()
	#def addEntry():
	#def modifyEntry():
	#def removeEntry():
	#def getInformation():
