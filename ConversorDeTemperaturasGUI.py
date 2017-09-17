# -*- encoding utf-8 -*-                                        #

# Creator: Davi_Colares                                         #
# Contact: (85) 989305416                                       #
#          https://www.facebook.com/willy.tru.39                #  
#          https://www.linkedin.com/in/davi-colares-371bb3146/  #

#Opções de conversão:
def convert():
    if convertede.get() == "°C (Celsius)" and convertepara.get() == "K (Kelvin)":
        vartemp = float(valortemp.get()) + 273
        temper.set(vartemp)
    elif convertede.get() == "K (Kelvin)" and convertepara.get() == "°C (Celsius)":
        vartemp = float(valortemp.get()) - 273
        temper.set(vartemp)
    elif convertede.get() == "°C (Celsius)" and convertepara.get() == "°F (Fahrnheit)":
        vartemp = 1.8 * float(valortemp.get()) + 32
        temper.set(vartemp)
    elif convertede.get() == "°F (Fahrnheit)" and convertepara.get() == "°C (Celsius)":
        vartemp = (float(valortemp.get()) - 32) / 1.8
        temper.set(vartemp)
    elif convertede.get() == "K (Kelvin)" and convertepara.get() == "°F (Fahrnheit)":
        vartemp = (((float(valortemp.get()) - 273) / 5 ) * 9) + 32
        temper.set(vartemp)
    elif convertede.get() == "°F (Fahrnheit)" and convertepara.get() == "K (Kelvin)":
        vartemp = (((float(valortemp.get()) - 32) / 9 ) * 5) + 273
        temper.set(vartemp)
    elif convertede.get() == convertepara.get():
        messagebox.showerror('Erro!',
        'Não é possível converter duas unidades iguais')
 
 #Importando a biblioteca                                   # 
from tkinter import *

temperatura = Tk()

temperatura.title("Conversor de Temperaturas")

#Unidades de medida de temperatura                          #
conversoes = "°C (Celsius)", "K (Kelvin)", "°F (Fahrnheit)"


valortemp = Entry(temperatura) 
valortemp.pack(side = 'left')

convertede = StringVar()
convertede.set("°C (Celsius)")
OptionMenu(temperatura, convertede, *conversoes).pack(side = 'left', padx = 10, pady = 10)

convertepara = StringVar()
convertepara.set("K (Kelvin)")
OptionMenu(temperatura, convertepara, *conversoes).pack(side = 'right', padx = 10, pady = 10)

temper = IntVar()
temper.set(0)
Label(temperatura, textvariable = temper).pack(side = 'right')

converta = Button(temperatura, text = "Converta", width = 10, command = convert)
converta.pack(pady = 50)

temperatura.mainloop()
