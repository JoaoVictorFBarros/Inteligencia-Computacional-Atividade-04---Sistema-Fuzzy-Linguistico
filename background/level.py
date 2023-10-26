from utilities.funcoes_pertinencia import gaussiana
from utilities.plot import plot

def level (subplot,x):

    level_k = 1/500

    descent = [-45,level_k]
    flat = [0,level_k]
    ascent = [45,level_k]

    perts = [descent,flat,ascent]
    arraysx = []
    arraysy = []

    for pert in perts:
        arrayx = [-45]
        arrayy = [gaussiana(arrayx[0],pert)]

        for cont in range(200000):
            arrayx.append(arrayx[cont-1] + 0.005)
            arrayy.append(gaussiana(arrayx[cont],pert))
        
        arraysx.append(arrayx)
        arraysy.append(arrayy)

    return [plot(subplot,[arraysx[0],arraysx[1],arraysx[2]],
        [arraysy[0],arraysy[1],arraysy[2]],
        ["Inclinação (Graus)","Descida","Plano","Subida"]
        ,["blue","green","red"],-45,45,
        x,
        [gaussiana(x,descent),gaussiana(x,flat),gaussiana(x,ascent)]),
        [gaussiana(x,descent),gaussiana(x,flat),gaussiana(x,ascent)]]