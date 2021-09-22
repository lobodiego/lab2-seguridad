import sys

abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje_c = str(input("Introduzca el mensaje a descifrar: "))
clave_original = str(input("Introduzca la palabra clave: "))
descifrado = ''
clave = ''

clave = clave_original
	
print ('Descifrando...')
for i in range(len(mensaje_c)):
	x = abecedario.find(mensaje_c[i])	
	y = abecedario.find(clave[i])	
	resta = x-y	
	modulo = resta%len(abecedario)	
	clave += abecedario[modulo]
	descifrado += abecedario[modulo]

print ('Mensaje descifrado: ' + descifrado)