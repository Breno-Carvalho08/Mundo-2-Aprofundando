inverso = ''
frase = input('')
frase_minuscula = frase.lower()
frase_invertida = frase_minuscula[::-1] #Inverter uma frase
print(frase_minuscula.replace(' ',''))
print(frase_invertida.replace(' ',''))

if frase_minuscula.replace(' ','') == frase_invertida.replace(' ',''):
    print('Palindromo')


