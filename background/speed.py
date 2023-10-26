from utilities.funcoes_pertinencia import gaussiana
from utilities.plot import plot

def speed(subplot,x):

    speed_k = 1/1500

    slow = [0,speed_k]
    normal = [75,speed_k]
    fast = [150,speed_k]

    perts = [slow,normal,fast]
    arraysx = []
    arraysy = []

    for pert in perts:
        arrayx = [0]
        arrayy = [gaussiana(arrayx[0],pert)]

        for cont in range(200000):
            arrayx.append(arrayx[cont-1] + 0.005)
            arrayy.append(gaussiana(arrayx[cont],pert))
        
        arraysx.append(arrayx)
        arraysy.append(arrayy)

    return [plot(subplot,[arraysx[0],arraysx[1],arraysx[2]],
        [arraysy[0],arraysy[1],arraysy[2]],
        ["Velocidade (Km/h)","Lento","Médio","Rápido"]
        ,["red","orange","green"],0,150,
        x,
        [gaussiana(x,slow),gaussiana(x,normal),gaussiana(x,fast)]),
        [gaussiana(x,slow),gaussiana(x,normal),gaussiana(x,fast)]]
        