import datetime
ano_nasc = int(input('Qual ano você nasceu: '))
ano = datetime.date.today().year
idade_pessoa = ano - ano_nasc

if ano - ano_nasc < 18:
    print(f'Ainda não é o momento para se alistar. Faltam {18 - (ano - ano_nasc)} anos.')
elif ano - ano_nasc == 18:
    print('Idade para se alistar')
else:
    print(f'Passou o momento de se alistar. O ano correto seria {ano - (idade_pessoa - 18)}.')