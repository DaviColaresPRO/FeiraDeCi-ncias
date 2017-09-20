# -*- encoding utf-8 -*-                                        #
# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

#Importando da biblioteca math o sqrt                           #
from math import sqrt

#Pedindo os valores e convertendo em flutuantes                 #
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

#Calculando o Delta                                       #
D = b**2 - 4 * a * c

#Calculando o x                                                 #
x1 = (-(b) + sqrt(D))/2*a
x2 = (-(b) - sqrt(D))/2*a

#Possiveis raízes reais                                         #
if D == 0:
    print("Delta = %d = 0" %D)
    print("Possui 1 raiz real")
    print("x = %d" %x1)
elif D > 0:
    print("Delta = %d > 0" %D)
    print("Possui 2 raizes reais")
    print("x1 = %d \nx2 = %d " %(x1,x2))
elif D < 0:
    print("Delta = %d > 0" %D)
    print("Não possui raízes reais")

    









