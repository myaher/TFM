import pytumblr
import json
from datetime import datetime
from time import time
import re

# Autenticación, los clientes utilizados
client = pytumblr.TumblrRestClient (
)
client1 = pytumblr.TumblrRestClient (
)
client2 = pytumblr.TumblrRestClient(
)


file= 'fandometric.txt' #Archivo generado en el primer script
list1 = []
list2 = []
list3 = []
#tags ya recolectados

days = 365  #Dias consultados
timestamp=int(time()) # timestamp referencia la fecha en que se inicia la consulta

with open(file, 'r') as f:
	list1 = f.readlines()
f.close()

for i in range(len(list1)):
	word = re.sub(r'[|,\n]', '',list1[i])
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
