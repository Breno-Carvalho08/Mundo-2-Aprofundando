valor = float(input('Valor do produto: '))
pagamento = int(input('1 - Á vista (dinheiro)\n2 - Á vista (cartão)\n3 - Parcelado\n'))

if pagamento == 1:
    valor_final = valor - (valor * 0.10)
    print(f'Valor a ser pago com 10% de desconto: R${valor_final}')
elif pagamento == 2:
    valor_final = valor - (valor * 0.05)
    print(f'Valor a ser  com 5% de desconto: R${valor_final}')
else:
    parcelas = int(input('Quantas vezes deseja parcelar: '))
    if parcelas == 2:
        valor_parcelas = valor / 2
        print(f'Valor das parcelas é de R${valor_parcelas}')
    else:
        valor_parcelas = (valor + (valor * 0.2)) / parcelas
        print(f'Valor das parcelas com 20% de juros é de R${valor_parcelas}')