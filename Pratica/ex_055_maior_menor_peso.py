maior_peso = 0
menor_peso = 0
for i in range(1,6):
    peso = float(input('Informe seu peso: '))
    if maior_peso == 0 and menor_peso == 0:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'Maior peso: {maior_peso}kg\nMenor peso: {menor_peso}kg')