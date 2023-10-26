from utilities.funcoes_pertinencia import triangular
from utilities.output_plot import plot

def consumption(subplot,activation):

    x = 2

    low = [-10,0,10]
    mid = [0,10,20]
    high = [10,20,30]

    return [plot(subplot,[low,mid,high],[[0,1,0],[0,1,0],[0,1,0]],
        ["Consumo","Alto","Normal","Baixo"],["red","orange","green"],0,20,
        activation,10),
        [triangular(x,low),triangular(x,mid),triangular(x,high)]]