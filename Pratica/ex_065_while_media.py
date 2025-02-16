parar = False
soma = 0
media = 0
cont = 0
num = 0
maior = 0
menor = 0

while not parar:
    if num == 0: #Como o valor se inicia em 0, já atribuímos os valores de num às variáveis menor e maior
        num = float(input('Digite um número: '))
        maior = num
        menor = num
        cont += 1

    num = float(input('Digite um número: ')) #Aqui com os valores de menor e maior definidos começa o programa de fato
    if num == 0:
        escolha = int(input('Deseja contiunar?\n[1] Sim\n[2] Não\n'))
        if escolha == 1:
            parar = False
        else:
            parar = True
            break
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

    soma += num
    cont += 1
print(f'Média: {soma/cont:.2f}\nMaior valor: {maior}\nMenor valor: {menor}')

