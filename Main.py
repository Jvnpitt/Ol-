from Funcoes import bemVindo
from Funcoes import tchau
from Funcoes import calDia
from Funcoes import menu
from datetime import date
from datetime import datetime
from Funcoes import listMusic
from Funcoes import atencion
from Funcoes import numSortido
import os

bemVindo()
loop = 1
while(loop == 1):
    print(' ')
    menu()
    resp = input()
    if resp == '1':
        hoje = date.today()#Função que retorna a data
        print("A data de hoje é - ", hoje)
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim':
            loop = 1
        else:
            print("Finalizando...")
            tchau()
            loop = 2

    elif resp == '1.1' or resp == '1,1':
        hoje = date.today()
        dia = hoje.weekday()#função que retorna um número que indica o dia da semana
        calDia(dia)#Chama um procedimento para printar o dia da semana
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim' or resp == 'Sim' or resp == 'S':
            loop = 1
        else:
            print("Finalizando...")
            tchau()
            loop = 2

    elif resp == '1,2' or resp == '1.2':
        hora = datetime.now()#objeto da classe datetime
        print(hora.hour,":",hora.minute,",",hora.second )#Métodos dá classe
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim'or resp == 'Sim' or resp == 'S':
            loop = 1
        else:
            print("Finalizando...")
            tchau()
            loop = 2

    elif  resp == '2':
        while(loop == 1):
            print("Informe o diretório onde suas músicas estão:")
            diretorio = input()#Diretório de músicas
            verifica = listMusic(diretorio)#Verifica se o diretório existe
            diretorio2 = (os.getcwd(),"/",diretorio)
            print("Verificando...")
            if (verifica == True):
                print("O diretório existe")
                print("")
                nome = os.path.expanduser('~') #Verifica o diretório do usuário
                v =(os.listdir(nome+"/"+diretorio)) #Transforma os nomes dos arquivos em uma lista
                num = 0
                for i in v:
                    print(num, i)#Printa um embaixo do outro e com a ordem númerica
                    num +=1
                print("Escolha uma música, ou digite -1 para uma música aleatória")
                music = int(input())
                if music == -1:
                    print()
                    print("Escolherei uma música, espero que goste")
                    print()
                    sort = numSortido(v)#Chama a função para escolher um número aleatório
                    os.system('xdg-open'+' '+nome+'/'+diretorio+'/'+v[sort].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))#Abri o software padrão do sistema operacional
                    print("Gostaria que eu escolhesse outra música?")
                    resp = input()
                    if resp == 'sim' or resp == 's' or resp == 'Sim':
                        loop = 1
                        confi = sort
                        while loop == 1:
                            try:
                                print()
                                print("Simboraaa, espero que goste")
                                print()
                                sort = numSortido(v)#Chama a função para escolher um número aleatório
                                if sort == confi:
                                    sort = numSortido(v)
                                os.system('xdg-open'+' '+nome+'/'+diretorio+'/'+v[sort].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))#Abri o software padrão do sistema operacional, substituindo alguns caracteres especiais por questôes do shell
                                print("Gostaria que eu escolhesse outra música?")
                                resp = input()
                                if resp == 'n' or  resp == 'Não' or resp == 'nao' or resp == 'não':
                                    loop = 0
                                elif resp == 'sim' or resp == 's' or resp == 'Sim':
                                    loop = 1
                                    confi = sort
                            except IndexError:
                                print("Número sem música")
                    loop = 0 #Quando sair do while ele tmb sairá do while principal
                else:
                    try:
                        os.system('xdg-open'+' '+nome+'/'+diretorio+'/'+v[music].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))#Abri o software padrão do sistema operacional
                        loop == 0
                    except IndexError:
                        print('Número sem música')
                    print("Deseja escolher outra música? ")
                    resp = input()
                    if resp == 'sim' or resp == 's' or resp == 'Sim':
                        print()
                        while loop == 1:
                            num = 0
                            for i in v:
                                print(num, i)#Printa um embaixo do outro e com a ordem númerica
                                num +=1
                            print("Escolha uma música")
                            music = int(input())
                            os.system('xdg-open'+' '+nome+'/'+diretorio+'/'+v[music].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))#Abri o software padrão do sistema operacional
                            loop == 0
                            print("Deseja escolher outra música? ")
                            resp = input()
                            if resp == 'sim' or resp == 's' or resp == 'Sim':
                                loop = 1
                            elif resp == 'n' or  resp == 'Não' or resp == 'nao' or resp == 'não':
                                loop = 0
                            else:
                                print("Desculpa ainda não conheço esse comando")
                                loop = 0
                    loop = 0#Quando sair do while ele tmb sairá do while principal
            else:
                print("Desculpe diretório não encontrado")
                atencion()
                print()
                print("Quer informa outro diretório? ")
                resp = input()
                if resp == 's' or resp == 'sim' or resp == 'Sim':
                    loop = 1
                else:
                    loop = 2 # Se diretório não existir
        print('')
        print("Gostaria de ficar um pouco mais? ")
        resp = input()
        if resp == 's' or resp == 'sim'or resp == 'Sim' or resp == 'S':
            loop = 1
        else:
            print("Finalizando...")
            tchau()
            loop = 2

    else:
        print("Desculpa ainda não conheço esse comando")
        print('você gostaria de ficar mais um pouco? ')
        resp = input()
        if resp == 's' or resp == 'sim' or resp == 'Sim' or resp == 'S':
            loop = 1
        else:
            loop = 2
            print("Finalizando...")
            tchau()
