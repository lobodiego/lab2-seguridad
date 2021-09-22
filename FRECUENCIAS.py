import sys
import operator

abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje = str(input("Introduzca el mensaje a cifrar: "))
mensaje_c = mensaje.maketrans("áéíóúüñÁÉÍÓÚÜ", "aeiouunAEIOUU"," .¡!,;:\n")
mensaje = mensaje.translate(mensaje_c).upper()
clave_original = str(input("Introduzca la palabra clave: "))
clave_o = clave_original.maketrans("áéíóúüñÁÉÍÓÚÜ", "aeiouunAEIOUU"," .¡!,;:\n")
clave_original = clave_original.translate(clave_o ).upper()

clave = ''
cifrado = ''
descifrado = ''

if len(mensaje)>len(clave_original):	
	for i in range(int(len(mensaje)/len(clave_original))):		
		clave += clave_original									
	clave += clave_original[:len(mensaje)%len(clave_original)]	
elif len(mensaje)<len(clave_original):	
	clave = clave_original[:len(mensaje)]	
elif len(mensaje)==len(clave_original):	
        clave = clave_original	
else:
	print ('Ha ocurrido un error inesperado. Terminando ejecución...')
	sys.exit(1)
	
print()

print ('Cifrando...')
for i in range(len(mensaje)):
	x = abecedario.find(mensaje[i])	
	y = abecedario.find(clave[i])	
	suma = x+y	
	modulo = suma%len(abecedario)	
	cifrado += abecedario[modulo]
	
print ('Mensaje cifrado: ' + cifrado)

##FRECUENCIAS
total_frec ={}
for i in cifrado:
    if i in total_frec:
        total_frec[i] +=1
    else:
        total_frec[i]=1
total_frec = sorted(total_frec.items(), key=operator.itemgetter(0))

print('\nFrecuencias : ')
print(total_frec)
	
sys.exit(0)
