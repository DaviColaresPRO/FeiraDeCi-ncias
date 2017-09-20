# -*- encoding utf-8 -*-                                        #
# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

def escolhedor:
    
#Importando e criando aba                                       #
from tkinter import *
aba = Tk()
temperatura.title("Calculadora Velocidade/Aceleração")

#Criando barra de opções                                        #
options = "Velocidade", "Aceleração"
escolha = StringVar()
escolha.set("Velocidade")
OptionMenu(temperatura, escolha, *options).pack(padx = 10, pady = 10)

#Criando botão para escolher                                    #
escolher = Button(aba, text = "Ok", width = 10, command = escolhedor)
escolher.pack(pady = 50)

ini1 = StringVar()
temper.set("")
Label(temperatura, textvariable = temper).pack(side = 'right')
