import pytumblr
import json
from datetime import datetime
from time import time
import re

# Autenticación, los clientes utilizados
client = pytumblr.TumblrRestClient (
  'aQTecxniC7WRTaPfnwAiDLSnNSBcaUNdLKO4BjMPbKsPyPcAh8',
  'aftgShEeRCmsuTKvu79LZfeSO8XnjTAtKFkzPiaO4MkSIG9f9g',
  'ndaNcZxCuIXhIkoRm3RJv8lGELlYLUpw6SzTyTWIhzHbLGIQNf',
  'btfNfXyFqMhgtWD95V63P93dfRa42d766gw5NKVdzNeCHoyTKr'
)
client1 = pytumblr.TumblrRestClient (
  'zOSy4MOVyoMqcrOMoPnPWIZPYu7LLpg0IeuPXuDeaLMXORPLkt',
  'kMVnq5aP93YCKj583AUUeOr93SACMl1JDiYCMSmAwkq5AhUxm6',
  'ndaNcZxCuIXhIkoRm3RJv8lGELlYLUpw6SzTyTWIhzHbLGIQNf',
  'btfNfXyFqMhgtWD95V63P93dfRa42d766gw5NKVdzNeCHoyTKr'
)

client2 = pytumblr.TumblrRestClient(
  '9Fd4oPYTuOa65tvYQbcGkBYEOXYCrKV6j2pXsCGYAI9yvGCrUQ',
  'ZTpJ5rPa6MVB9MrzCay3w8XvSCYP0dWOilxH1FalelAjoS6Ssv',
  'ndaNcZxCuIXhIkoRm3RJv8lGELlYLUpw6SzTyTWIhzHbLGIQNf',
  'btfNfXyFqMhgtWD95V63P93dfRa42d766gw5NKVdzNeCHoyTKr'
)


file= 'fandometric.txt' #Archivo generado en el primer script
list1 = []
list2 = []
list3 = []
#tags ya recolectados
tags = ['Artists on Tumblr','Marvel','Pokemon','Game of Thrones','Taylor Swift','Sport','Avengers', 'Harry Potter','Harry Styles','Star Wars','Health','BTS','Boku','Druk','Writers on Tumblr','Studyblr','Artist on Tumblr','Sarah J. Maas']
days = 365  #Dias consultados
timestamp=int(time()) # timestamp referencia la fecha en que se inicia la consulta

with open(file, 'r') as f:
	list1 = f.readlines()
f.close()

for i in range(len(list1)):
	word = re.sub(r'[|,\n]', '',list1[i])
	if word not in tags:
		list2.append (word)
		
list3 = list(set(list2)) #Eliminar tags repetidos



for i in range(days):
	print(i)
	for index,j in enumerate(list3[20:]):
		if index < 4:
			print("Tags" , j)
			out_file= open("Tag_"+str(j[0:5])+str(i)+".json","w+")
			json.dump(client.tagged(str(j),before=timestamp),out_file, indent=4)
		else: 
			if index < 8:
				print("Tags_1" , j)
				out_file= open("Tag1_"+str(j[0:5])+str(i)+".json","w+")
				json.dump(client1.tagged(str(j),before=timestamp),out_file, indent=4)
			else:
				print("Tags_2" , j)
				out_file= open("Tag2_"+str(j[0:5])+str(i)+".json","w+")
				json.dump(client2.tagged(str(j),before=timestamp),out_file, indent=4)
	timestamp-=86400

out_file.close()
