n1 = float(input('Informe um número: '))
n2 = float(input('Informe um número: '))
escolha = 0

while escolha != 5:
    escolha = int(input('[1] Soma\n[2] Multiplicar\n[3] Maior valor\n[4] Novos números\n[5] Sair do programa\n'))
    match escolha:
        case 1:
            print(n1 + n2)
        case 2:
            print(n1 * n2)
        case 3:
            if n1 > n2:
                print(n1)
            else:
                print(n2)
        case 4:
            n1 = float(input('Informe um número: '))
            n2 = float(input('Informe um número: '))