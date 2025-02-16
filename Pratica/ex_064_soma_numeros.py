soma = 0
num = 0
cont_num = 0

while num != 999: #flag
    num = float(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont_num += 1

print(f'A soma de todos os números foi de {soma} e foram um total de {cont_num } números')