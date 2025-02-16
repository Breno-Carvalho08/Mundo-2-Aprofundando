from datetime import date

ano_nasc = int(input('Qual o seu ano de nascimento: '))
ano = date.today().year

if ano - ano_nasc <= 9:
    print('Atleta Mirim')
elif 9 < ano - ano_nasc <= 14:
    print('Atleta Infantil')
elif 14 < ano - ano_nasc <= 19:
    print('Atleta Junior')
elif 19 < ano - ano_nasc <= 20:
    print('Atleta Sênior')
else:
    print('Atleta Master')