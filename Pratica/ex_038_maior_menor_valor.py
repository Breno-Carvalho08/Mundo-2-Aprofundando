from random import randrange

num1 = randrange(1,10)
num2 = randrange(1,10)

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print(f'{num1} e {num2} são iguais')