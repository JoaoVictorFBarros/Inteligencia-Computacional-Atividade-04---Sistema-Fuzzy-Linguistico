def deffuzyfy(activations,values):

    cont = 0
    num = 0.0
    den = 0.0
    for activation in activations:
        num += float(activation * values[cont])
        den += activation
        cont+=1
        
    return num/den


