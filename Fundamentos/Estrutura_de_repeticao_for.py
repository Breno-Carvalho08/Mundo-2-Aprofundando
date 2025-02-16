#Estrutura for: for x (variável) in range (começo do intervalo, fim do intervalo, passo):
soma_par = 0
soma_impar = 0
for i in range (1,200):
    if i % 2 == 0:
        soma_par += i
    elif i % 2 != 0:
        soma_impar += i

print(f'Soma pares: {soma_par}\nSoma impares: {soma_impar}')



