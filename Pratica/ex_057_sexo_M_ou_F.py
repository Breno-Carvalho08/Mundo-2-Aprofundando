sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()

while sexo != 'M' and sexo != 'F': #sexo not in 'MmFf'
    print('Inválido! Digite novamente')
    sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()

if sexo == 'M':
    print('Masculino')
else:
    print('Feminino')