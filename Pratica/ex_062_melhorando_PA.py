a1 = int(input('informe o primeiro termo: '))
p = a1
r = int(input('Razão: '))
parar = False
termo = 0

while not parar:
    escolha = int(input('Deseja ver até qual termo: '))
    termo += escolha
    cont = 0
    while cont < escolha:
        cont += 1
        a1 += r
        print(a1)
    escolha2 = str(input('Deseja parar? [S/N]\n').upper())
    if escolha2 == 'S':
        parar = True
    else:
        parar = False
print(f'Acabou. Você viu até o {termo}°termo começando pelo número {p} e com uma razão de {r}')