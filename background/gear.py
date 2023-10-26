from utilities.plot import plot
from utilities.funcoes_pertinencia import triangular

def gear(subplot,x):

    low = [0.999,1,1.001]
    mid = [1.999,2,2.001]
    high = [2.999,3,3.001]

    return [plot(subplot,[low,mid,high],[[0,1,0],[0,1,0],[0,1,0]],
        ["Marcha","Lenta","Média","Rápida"],["red","orange","green"],0,3.1,
        x,
        [triangular(x,low),triangular(x,mid),triangular(x,high)]),
        [triangular(x,low),triangular(x,mid),triangular(x,high)]]