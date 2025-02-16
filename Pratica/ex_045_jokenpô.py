from time import sleep
from random import choice

p1 = input('1 - Pedra\n2 - Papel\n3 - Tesoura\n')
p2 = choice(['Pedra', 'Papel', 'Tesoura'])
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print(p2)

if p1 == 'Pedra' and p2 == 'Tesoura':
    print('Vitória p1')
elif p1 == 'Pedra' and p2 == 'Papel':
    print('Vitória p2')
elif p1 == 'Papel' and p2 == 'Pedra':
    print('Vitória p1')
elif p1 == 'Papel' and p2 == 'Tesoura':
    print('Vitória p2')
elif p1 == 'Tesoura' and p2 == 'Papel':
    print('Vitória p1')
elif p1 == 'Tesoura' and p2 == 'Pedra':
    print('Vitória p2')
else:
    print('Empate')