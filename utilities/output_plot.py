import matplotlib.pyplot as plt

def plot(subplot,domains,y,names,colors,min,max,out,a):

    yticks = [0]
    cont = 0
    for domain in domains:
        plt.sca(subplot)
        plt.plot(domain,y[cont],label=names[cont+1],color=colors[cont])
        yticks.append(out[cont])    
        plt.fill([domain[0],domain[0] + a*out[cont],domain[2] -a*out[cont],domain[2]], [0,out[cont],out[cont],0],color=colors[cont],alpha=0.5)
        cont+=1

    yticks.append(1)
    plt.yticks(yticks)
    plt.xlim(min,max)
    plt.ylim(-0.01,1.05)
    plt.title(names[0])
    plt.legend(loc="lower right")

    return plt
