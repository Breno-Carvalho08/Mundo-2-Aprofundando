n = int(input('Informe um número: '))
fat = 1

#fatorial WHILE
while n > 0:
    fat = fat * n
    n -= 1
print(fat)

#fatorial FOR
for i in range(1,n + 1, -1):
    fat = fat * i
print(fat)
