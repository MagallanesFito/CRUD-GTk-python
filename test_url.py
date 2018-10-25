import requests
import json

#ADD NEW ENTRY
'''
url = 'http://127.0.0.1:5000/worktime'
dict_data = {"startDate": "2020-01-01T10:30", "endDate" : "2020-01-01T11:30","category" : "Dancing", "description" : "Wake me up, before you go go!"}
dict_data = json.dumps(dict_data)
loaded_r = json.loads(dict_data)
r = requests.post(url, data=loaded_r)
print(r.json())
'''

#---------------------------------------------------------------------------------

#GET ENTRY WITH ID
'''myid = "7"
url = 'http://127.0.0.1:5000/worktime/'+myid
r = requests.get(url)
print(r.json())'''


#---------------------------------------------------------------------------------

#ENTRIES IN RANGE OF DATES
'''url  = 'http://127.0.0.1:5000/worktime?startDate=2018-01-01T10:30&endDate=2018-01-01T11:30'
r = requests.get(url)
respuestas = r.json()
for respuesta in respuestas:
	print(respuesta)
	print("-"*10)'''


#---------------------------------------------------------------------------------

#UPDATE ENTRY WITH ID
'''url = 'http://127.0.0.1:5000/worktime/3' #actualizamos el id 3
dict_data = {"startDate": "2018-01-01T10:30", "endDate" : "2018-01-01T11:30","category" : "Kick Boxing", "description" : "Working in my time tracker project"}
dict_data = json.dumps(dict_data)
loaded_r = json.loads(dict_data)
r = requests.put(url, data=loaded_r)
print(r.json())'''


#---------------------------------------------------------------------------------

#DELETE ENTRY
'''myid = "7"
url = 'http://127.0.0.1:5000/worktime/'+myid
r = requests.delete(url)
print(r.json())'''


#---------------------------------------------------------------------------------