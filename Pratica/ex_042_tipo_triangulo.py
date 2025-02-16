from random import randrange

a = randrange(1, 10)
b = randrange(1, 10)
c = randrange(1, 10)
print(a,b,c)

if a < b + c and b < a + c and c < a + b:
    print('O triângulo existe')
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b != c or a != b == c or a == c != b:
        print('Triangulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('0')