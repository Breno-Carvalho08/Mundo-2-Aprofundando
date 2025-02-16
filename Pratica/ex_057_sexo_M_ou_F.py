sexo = str(input('Digite seu sexo [M/F]:')).upper()

while sexo != 'M' and sexo != 'F':
    print('Inválido! Digite novamente')
    sexo = str(input('Digite seu sexo [M/F]:')).upper()

if sexo == 'M':
    print('Masculino')
else:
    print('Feminino')