seq = int(input('Até qual sequência você deseja ver: '))

def fibonacci(x):
    cont = 0
    ant = 0
    atual = 1
    prox = 0
    while cont < x:
        prox = atual + ant
        ant = atual
        atual = prox
        cont = cont + 1
        print (prox,end = ' - ')

fibonacci(seq)
print('Fim')