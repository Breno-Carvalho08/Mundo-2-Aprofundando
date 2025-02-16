soma = 0

for x in range(1,500):
    if x % 2 != 0 and x % 3 == 0:
        soma += x


print(f'A soma dos multiplos de 3 de 1 a 500 que são impares é {soma}')