#IF, ELIF, ELSE (ANINHADA)
nome = input("Nome: ")

#Estrutura condiconal aninhada
if nome == 'Breno':
    print('Belo nome')
elif nome in 'Jonas Caio Lucas Pedro Rafael':
    print('Seja bem vindo {}'.format(nome))
else:
    print('Seu nome é bem normal')


