from time import sleep

hora = 0
minuto = 0
sec = 0
cronometro_hora = int(input('Horas: '))
cronometro_min = int(input('Minutos: '))
cronometro_sec = int(input('Segundos: '))

for cont in range(0,cronometro_sec):
    if cont > 59:
        cronometro_min =+ 1
        cont = 0
    elif cronometro_min > 59:
        cronometro_hora =+ 1
        cronometro_min = 0
    print(f'{cronometro_hora}h:{cronometro_min}min:{cont}seg')
    sleep(1)