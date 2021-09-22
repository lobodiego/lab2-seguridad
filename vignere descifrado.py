import sys

abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje_c = str(input("Introduzca el mensaje a descifrar: "))
clave_original = str(input("Introduzca la palabra clave: "))
descifrado = ''
clave = ''

if len(mensaje_c)>len(clave_original):	
	for i in range(int(len(mensaje_c)/len(clave_original))):		
		clave += clave_original									
	clave += clave_original[:len(mensaje_c)%len(clave_original)]	
elif len(mensaje_c)<len(clave_original):	
	clave = clave_original[:len(mensaje_c)]	
elif len(mensaje_c)==len(clave_original):	
        clave = clave_original	
else:
	print ('Ha ocurrido un error inesperado. Terminando ejecución...')
	sys.exit(1)

	
print ('Descifrando...')
for i in range(len(mensaje_c)):
	x = abecedario.find(mensaje_c[i])	
	y = abecedario.find(clave[i])	
	resta = x-y	
	modulo = resta%len(abecedario)	
	descifrado += abecedario[modulo]	
print ('Mensaje descifrado: ' + descifrado)
