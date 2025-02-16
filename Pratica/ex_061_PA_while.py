a1 = int(input('informe o primeiro termo: '))
r = int(input('Razão: '))
n = int(input('Quantidade de termos: '))

cont = 0
while cont < n:
    a1 += r
    cont += 1
    print(a1,end=' -> ')
print('Acabou')