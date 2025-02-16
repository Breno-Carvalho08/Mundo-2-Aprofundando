from random import randint
from time import sleep

vitoria_player = True
vitoria = 0

escolha = str(input('Par ou Impar? [P/I]\n')).upper()
while escolha not in 'PI':
    print('Escolha par ou impar...')
    escolha = str(input('Par ou Impar? [P/I]\n')).upper()
match escolha:
    case 'P':
        while vitoria_player:
            player = int(input('Jogue um número de 1 a 10: '))
            while player > 10:
                print('Você não tem tudo isso de dedo...')
                player = int(input('Jogue um número de 1 a 10: '))
            pc = randint(0, 10)
            print('PAR')
            sleep(0.5)
            print('OU')
            sleep(0.5)
            print('IMPAR')
            if (player + pc) % 2 == 0:
                vitoria += 1
                print(f'Vitória do jogador (PAR). O número foi {player + pc}. Os numeros jogados foram {player} e {pc}')

            else:
                vitoria_player = False
                print(f'Vitória do pc (IMPAR). O número foi {player + pc}. Os numeros jogados foram {player} e {pc}')
                print(f'O jogo acabou. Foram {vitoria} vitória(s) seguidas para o jogador.')
                break
    case 'I':
        while vitoria_player:
            player = int(input('Jogue um número de 1 a 10: '))
            while player > 10:
                print('Você não tem tudo isso de dedo...')
                player = int(input('Jogue um número de 1 a 10: '))
            pc = randint(0, 10)
            print('PAR')
            sleep(0.5)
            print('OU')
            sleep(0.5)
            print('IMPAR')
            if (player + pc) % 2 != 0:
                vitoria += 1
                print(f'Vitória do jogador (IMPAR). O número foi {player + pc}. Os numeros jogados foram {player} e {pc}')

            else:
                vitoria_player = False
                print(f'Vitória do pc (PAR). O número foi {player + pc}. Os numeros jogados foram {player} e {pc}')
                print(f'O jogo acabou. Foram {vitoria} vitória(s) seguidas para o jogador.')
                break