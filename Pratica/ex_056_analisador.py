
media_idade = 0
maioridadeHomem = 0
nomeVelho = 0
mulher_menos_20anos = 0

for i in range (1,6):
    print(f'------ {i}° Pessoa ------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip()
    media_idade += idade

    if i == 1 and sexo in 'Mm': #utilizamos dessa forma para conseguir colocar tanto as letras 'M' maiuscula e minuscula
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20anos += 1


print(f'Média de idade: {media_idade/5} anos')
print(f'O homem mais velho se chama {nomeVelho} e tem {maioridadeHomem} anos.')
print(f'Temos {mulher_menos_20anos} mulheres com menos de 20 anos')

