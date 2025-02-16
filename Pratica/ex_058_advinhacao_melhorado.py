from random import randrange

num_escolhido = randrange(1,10)
advinhacao = int(input('Chute um número de 1 a 10: '))
chances = 5
acerto = True

while advinhacao != num_escolhido:
    chances -= 1
    if chances == 0:
        acerto = False
        break
    else:
        acerto = True
    print(f'Você errou... Tem mais {chances} chances')
    advinhacao = int(input('Chute um número de 1 a 10: '))

if acerto:
    print('Você ganhou!')
else:
    print('Você perdeu...')