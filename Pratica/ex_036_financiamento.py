valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
quant_anos = float(input('Em quantos anos deseja pagar: '))
parcelas = (valor_casa /(12 * quant_anos))

if parcelas > salario * 0.3:
    print(f'Empréstimo negado! O valor da parcela compromete \033[1;31m{((parcelas/salario) * 100):.2f}%\033[m do seu salário: \nParcelas: R${parcelas:.2f}\nSalário: R${salario}')
else:
    print(f'Empréstimo concedido! O valor da parcela : \033[0;32mR${parcelas:.2f}\033[m')

'''Sintaxe para colocar texto colorido no python: \033 [0 (estilo do texto); 31 (cor do texto); 44 (cor do background do texto) \033[m'''
'''
Estilo do texto: 
1 = Bolde (Negrito)

2 = Fraco

3 = Itálico

4 = Underline (Sublinhado)

Cores do texto

30 = Branco

31 = Vermelho

32 = Verde

33 = Amarelo

34 = Azul

35 = Magenta

36 = Ciano (*imagine ciano aqui, não tem pra por no texto ^.^')

37 = Cinza

Cores do background

40 = Branco

41 = Vermelho

42 = Verde

43 = Amarelo

44 = Azul

45 = Magenta

46 = Ciano

47 = Cinza
'''