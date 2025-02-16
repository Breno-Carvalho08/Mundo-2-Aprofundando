quant_nomes = int(input('Quantidade de nomes que deseja: '))
lista_nomes = [{}]

for nomes in range(1,quant_nomes+1):
    print(f'----- {nomes}°Nome -----')
    nome = input('Nome: ')
    idade= int(input('idade: '))
    lista_nomes.append({'Nome':nome, 'Idade': idade})

print(lista_nomes.sort())
print((lista_nomes.__len__()) - 1)

