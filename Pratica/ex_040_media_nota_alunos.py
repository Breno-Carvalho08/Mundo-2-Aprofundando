quant = int(input('Quantas notas deseja colocar: '))
media = 0
soma_notas = 0

for i in range(quant):
    notas = float(input(f'{i + 1}° Nota: '))
    soma_notas = soma_notas + notas
    media = (soma_notas/quant)

if media < 5:
    print(f'REPROVADO. Média: {media:.2f}')
elif 5 <= media <= 6.9:
    print(f'RECUPERAÇÃO. Média: {media:.2f}')
else:
    print(f'APROVADO. Média: {media:.2f}')

