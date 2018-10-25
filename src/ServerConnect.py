#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import json
import requests
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class ServerConnect:
	def addEntry(self, e):
		(dat,ty,dur,com) = e
		url = 'http://127.0.0.1:5000/worktime'
		(day,month,year) = dat.split('/')
		data = year+'-'+month+'-'+day+'T'+self.minutesToHours(dur) 
		dict_data = {"startDate": data, "endDate" : data,"category" : ty, "description" : com}
		dict_data = json.dumps(dict_data)
		loaded_r = json.loads(dict_data)
		r = requests.post(url, data=loaded_r)
		return
		
	def deleteEntry(self,entry):
		return
		
	def modifyEntry(self, befentry, aftentry):
		return
		
	def get_all(self):
		lis = []
		i=1
		data = self.getEntryById(i)
		while(data!=None):
			(a,b) = data['start_date'].split('T')
			(year,month,day) = a.split('-')
			lis.append([day+'/'+month+'/'+year,data['category'],self.hoursToMinutes(b),data['description']])
			i=i+1
			data = self.getEntryById(i)
		return lis

	def getEntryById(self,i):
		url = 'http://127.0.0.1:5000/worktime/'+ str(i)
		r = requests.get(url)
		if r.status_code == 200:
			return r.json()
		return

	def minutesToHours(self,minutes):
		horas = minutes//60
		minutos = minutes%60
		return str(horas) + ":" + str(minutos)
	def hoursToMinutes(self,hour_string):
		(hours,minutes) = hour_string.split(":")
		hours = int(hours)
		minutes = int(minutes)
		return (hours*60 + minutes)

