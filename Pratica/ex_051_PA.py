
a1 = int(input('informe o primeiro termo: '))
r = int(input('Razão: '))
n = int(input('Quantidade de termos: '))
an = a1 + (n - 1) * r
somaPA = 0

for i in range (a1, an + 1, r):
    print(i, end=' -> ')
    somaPA += i
print('Acabou!')
print(f'Soma de todos os termos da PA: {somaPA}')
