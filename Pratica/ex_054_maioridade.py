from datetime import date

maioridade = 0
menor_de_idade = 0
for i in range (1,8):
    ano_nasc = int(input('Ano de nascimento: '))
    if date.today().year - ano_nasc >= 21:
        maioridade += 1
    else:
        menor_de_idade += 1
print(f'Maiores de idade: {maioridade}\nMenor de idade: {menor_de_idade}')