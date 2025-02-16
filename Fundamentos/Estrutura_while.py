# while (enquanto algo): faça algo até a condição ser FALSA
parar = False

#Limite desconhecido
while parar == False: #not parar
   continuar = int(input('Deseja continuar?\n1 - Sim\n2 - Não\n'))
   if continuar == 1:
       parar = False
   else:
       parar = True

#Limite conhecido
cont = 0
while cont <= 10:
    print(cont,end=' - ')
    cont += 1
print('FIM')
