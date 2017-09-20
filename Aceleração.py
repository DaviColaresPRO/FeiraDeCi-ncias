# -*- encoding utf-8 -*-                                        #
# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

#Pedindo os valores e convertendo em flutuantes                 #
v0 = float(input("Insira a velocidade inicial(km/h): "))
v = float(input("Insira a posição final(km/h): "))
t0 = float(input("Insira o tempo inicial(h): "))
t = float(input("Insira o tempo final(h): "))

#Calculando a variação                                          #
Vs = v - v0
Vt = t - t0

#Calculando a aceleração                                        #
a = Vs/Vt

print("A aceleração é igual a %.2f km/h²" %a)
