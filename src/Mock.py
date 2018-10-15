#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class Mock:
	def __init__(self):
		'''list = Gtk.ListStore(str,str,int,str)
		#Una dummy list, corregir después
		list.append(["14/09/2019","Karate",60,"Agressive!"])
		list.append(["13/10/2018","Tae Kwon Do",120,"Nice"])'''

		#entradas dummy
		self.list = [["14/09/2019","Karate",60,"Agressive!"],["13/10/2018","Tae Kwon Do",120,"Nice"]]
	def addEntry(self, e):
		self.list.append(list(e))
	def deleteEntry(self,entry):
		self.list.remove(entry)
	def modifyEntry(self, befentry, aftentry):
		a=self.list.index(befentry)
		self.list.remove(befentry)
		self.list.insert(a,aftentry)
