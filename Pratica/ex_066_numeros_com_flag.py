soma = cont = 0
while True:
    num = int(input("Digite um número (parar 999): "))
    if num == 999: #flag
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} numeros foi de {soma}')