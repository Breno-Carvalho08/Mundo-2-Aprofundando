
maior_nota = 0
menor_nota = 0
media_nota = 0
nome_maior_nota = ''
nome_menor_nota = ''
lista_notas = []

quant_alunos = int(input('Quantidade de alunos para lançar a nota: '))

for i in range(0,quant_alunos):
    print(f'----- {i+1}°Aluno -----')
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    media_nota += nota

    if i == 0:
        nome_maior_nota = nome
        nome_menor_nota = nome
        maior_nota = nota
        menor_nota = nota
    elif nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    elif nota < menor_nota:
        menor_nota = nota
        nome_menor_nota = nome

print(f'O aluno com a maior nota foi {nome_maior_nota} com {maior_nota}')
print(f'O aluno com a menor nota foi {nome_menor_nota} com {menor_nota}')
print(f'Média dos alunos: {media_nota/quant_alunos:.2f}')

