from background.level import level
from background.gear import gear
from background.speed import speed
from background.consumption import consumption
from output_Activation import high_activation, mid_activation,low_activation
from deffuzification import deffuzyfy

import matplotlib.pyplot as plt


def evaluate(speed_value,march_value,level_value):
    fig, axs = plt.subplots(4, 1,figsize=[9,9])

    level_activation = level(axs[0],level_value)[1]
    speed_activation = speed(axs[1],speed_value)[1]
    gear_activation = gear(axs[2],march_value)[1]


    plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05, hspace=0.3)

    level_print       = "Inclinação: "
    speed_print       = "Velocidade: "
    gear_print        = "Marcha:     "
    consumption_print = "Consumo:    "

    for elem in level_activation:
        level_print += "{:.2f}".format(elem) + "   "

    for elem in speed_activation:
        speed_print += "{:.2f}".format(elem) + "   "

    for elem in gear_activation:
        gear_print += "{:.2f}".format(elem) + "   "

    activation = [high_activation(level_activation,speed_activation,gear_activation),
                                mid_activation(level_activation,speed_activation,gear_activation),
                                low_activation(level_activation,speed_activation,gear_activation)]

    consumption(axs[3],activation)
    for elem in activation:
        consumption_print += "{:.2f}".format(elem) + "   "
        
    consumption_print += "-> " + "{:.2f}".format(deffuzyfy(activation,[0,10,20]))

    print(level_print + "\n" + speed_print + "\n" + gear_print + "\n" + consumption_print + "\n------------------------------------------------------------------")

    plt.show() 

print("\nEntrada: velocidade = 130, marcha = 2, inclinação= 40\n")
evaluate(130,2,40)

print("\nEntrada: velocidade = 60, marcha = 2, inclinação= -12\n")
evaluate(60,2,-12)

print("\nEntrada: velocidade = 30, marcha = 3, inclinação= -40\n")
evaluate(30,3,-40)
