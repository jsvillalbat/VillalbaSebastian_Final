import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def grafica(datafile):
    data = np.loadtxt(datafile)
    
    s = np.shape(data)
    #print(s)
    n_x = s[1]
    n_t = s[0]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.linspace(0,1,n_x)
    t = np.linspace(0,0.1,n_t)
    X,T = np.meshgrid(x,t)

    ax.plot_surface(X, T, data)

    fig.savefig("resultado.png", bbox_inches='tight')

grafica("ode.dat")