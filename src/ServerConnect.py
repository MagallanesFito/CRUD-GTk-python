#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gi
import json
import requests
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk

class ServerConnect:
	
	def addEntry(self, entry):
		(dat,ty,dur,com) = entry
		url = 'http://127.0.0.1:5000/worktime'
		(day,month,year) = dat.split('/')
		data = year+'-'+month+'-'+day+'T'+self.minutesToHours(dur) 
		dict_data = {"startDate": data, "endDate" : data,"category" : ty, "description" : com}
		dict_data = json.dumps(dict_data)
		loaded_r = json.loads(dict_data)
		r = requests.post(url, data=loaded_r)
		myid = r.json()['id']
		if r.status_code == 200:
			e = (myid, entry)
			self.hash.append(e)
			return
		return -1
	
	def getId(self, entry):
		for e in self.hash:
			(myid,ent) = e
			if ent==entry:
				return myid
		return
	
	def updateId(self, myid, bef, entry):
		ind = self.hash.index((myid,bef))
		self.hash.remove((myid,bef))
		self.hash.insert((myid,entry))
		
	def deleteEntry(self,entry):
		url = 'http://127.0.0.1:5000/worktime/' + str(self.getId(entry))
		r = requests.delete(url) # falta eliminar en la hash table
		if r.status_code == 200:
			return
		return -1
		
	def modifyEntry(self, befentry, aftentry):
		myid = self.getId(befentry)
		url = 'http://127.0.0.1:5000/worktime/' + str(myid)
		(dat,ty,dur,com) = aftentry
		(day,month,year) = dat.split('/')
		data = year+'-'+month+'-'+day+'T'+self.minutesToHours(dur) 
		dict_data = {"startDate": data, "endDate" : data,"category" : ty, "description" : com}
		dict_data = json.dumps(dict_data)
		loaded_r = json.loads(dict_data)
		r = requests.put(url, data=loaded_r)
		if r.status_code == 200:
			self.updateId(myid,befentry,aftentry)
			return
		return -1 
		
	def get_all(self):
		self.hash = []
		lis = []
		i=1
		while(i<100): #max id -- más alto implica más espacio y más tiempo de carga
			data = self.getEntryById(i)
			if data != None:
				(a,b) = data['start_date'].split('T')
				(year,month,day) = a.split('-')
				entry = [day+'/'+month+'/'+year,data['category'],self.hoursToMinutes(b),data['description']]
				lis.append(entry)
				e = (i,entry)
				self.hash.append(e)
			i=i+1
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

