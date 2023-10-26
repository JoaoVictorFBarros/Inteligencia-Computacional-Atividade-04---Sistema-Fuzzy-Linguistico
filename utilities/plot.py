import matplotlib.pyplot as plt

def plot(subplot,domains,y,names,colors,min,max,x,out):

    yticks = [0]
    cont = 0
    for domain in domains:
        plt.sca(subplot)
        plt.plot(domain,y[cont],label=names[cont+1],color=colors[cont])
        plt.scatter(x,out[cont],color=colors[cont])
        yticks.append(out[cont])
        cont+=1
    yticks.append(1)
    plt.yticks(yticks)
    plt.xlim(min,max)
    plt.ylim(-0.01,1.05)
    plt.title(names[0])
    plt.legend(loc="lower right")


    return plt
