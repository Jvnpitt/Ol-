import random
import os

def bemVindo():
    f = open("this.txt")
    print(f.read())
    print("Eu sou a Jacy sua assistente pessoal feito para te ajudar.")
    print("Isso é oque eu sei fazer: ")

def tchau():
    print("Sentirei muitas saudades, até logo.")

def menu():
    print("1 - Data atual")
    print("1.1 - Dia da semana")
    print("1.2 - Horário")
    print("2 - Tocar música")
    print("Como posso te ajudar? ")

def calDia(dia):
    if dia == 0:
        print("Hoje é Segunda-feira")
    elif dia == 1:
        print("Hoje é Terça-feira")
    elif dia == 2:
        print("Hoje é Quarta-feira")
    elif dia == 3:
        print("Hoje é Quinta-feira")
    elif dia == 4:
        print("Hoje é Sexta-feira")
    elif dia == 5:
        print("Hoje é Sábado")
    else:
        print("Hoje é Domingo")

def listMusic(diret):
    nome = os.path.expanduser('~') #Verifica o diretório home do usuário
    verifica = os.path.isdir(nome+"/"+diret) #Verifica se o diretório existe
    if (verifica == True):
        return True
    else:
        return False

def atencion():
    print("Verifique existe letra maiúscula no diretório, acentuação...")

def numSortido(vet):
    n = 0
    for i in vet:
        n += 1
    num = random.randrange(0, n+1)
    return num
