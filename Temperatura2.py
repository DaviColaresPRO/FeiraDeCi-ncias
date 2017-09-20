# -*- encoding utf-8 -*-                                        #
# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

#Tipo de conversão                                              #
print("Tipos de conversão \n1.C° -> F° \n2.Fº->Cº")
o = input("Tipo de conversão(1|2): ")
if o == "1":
    C = float(input("Valor da temperatura(Cº): "))
#Calculando O Fº                                                #
    F = (C/5) * 9 + 32
    print("O valor %2.f ºC em Fahrenheit é %2.f ºF" %(C, F))
elif o == "2":
    F = float(input("Valor da temperatura(Fº): "))
#Calculando O Cº                                                #
    C = ((F-32)/9) * 5
    print("O valor %2.f ºF em Celsius é %2.f ºC" %(F, C))
    
    
    

