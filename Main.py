from Funcoes import bemVindo
from Funcoes import tchau
from Funcoes import calDia
from Funcoes import menu
from datetime import date
from datetime import datetime


bemVindo()
loop = 1
while(loop == 1):
    print(' ')
    menu()
    resp = input()
    if resp == '1':
        hoje = date.today()
        print("A data de hoje é - ", hoje)
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim':
            loop = 1
        else:
            loop = 2

    elif resp == '1.1' or resp == '1,1':
        hoje = date.today()
        dia = hoje.weekday()
        calDia(dia)
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim':
            loop = 1
        else:
            loop = 2

    elif resp == '1,2' or resp == '1.2':
        hora = datetime.now()
        print(hora.hour,":",hora.minute,",",hora.second )
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim':
            loop = 1
        else:
            loop = 2

    else:
        print("Desculpa ainda não conheço esse comando")
        print('você gostaria de ficar mais um pouco? ')
        resp = input()
        if resp == 's' or resp == 'sim':
            loop = 1

        else:
            loop = 2
            print("Finalizando...")
            tchau()
