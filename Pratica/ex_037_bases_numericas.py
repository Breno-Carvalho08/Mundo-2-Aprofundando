num = int(input('Digite um número: '))
escolha = int(input('Qual conversão de base você quer:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if escolha == 1:
    conversao = bin(num)
    print(f'O valor {num} em binário é {conversao[2:]}')
elif escolha == 2:
    conversao = oct(num)
    print(f'O valor {num} em octal é {conversao[2:]}')
else:
    conversao = hex(num)
    print(f'O valor {num} em hexadecimal é {conversao[2:]}')
