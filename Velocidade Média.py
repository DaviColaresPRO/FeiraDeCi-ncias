# -*- encoding utf-8 -*-                                        #
# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

#Pedindo os valores e convertendo em flutuantes                 #
s0 = float(input("Insira a posição inicial(m): "))
s = float(input("Insira a posição final(m): "))
t0 = float(input("Insira o tempo inicial(s): "))
t = float(input("Insira o tempo final(s): "))

#Calculando a variação                                          #
Vs = s - s0
Vt = s - s0

#Calculando a velocidade média                                  #
Vm = Vs/Vt

print("A velocidade média é igual a %.2f m/s" %Vm)
