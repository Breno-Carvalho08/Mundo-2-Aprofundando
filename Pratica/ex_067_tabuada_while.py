cont = 0
while True:
    print('-------------------------')
    tab = int(input('Qual numero deseja ver a tabuada (número negativo encerra o programa)? '))
    print('-------------------------')
    if tab < 0:
        break
    while cont <= 9:
        cont += 1
        print(f' {tab} x {cont:2} = {tab * cont}')
    cont = 0
print('Programa encerrado')
