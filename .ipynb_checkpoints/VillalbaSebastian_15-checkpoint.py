import numpy as np
import matplotlib.pyplot as plt

#Densidad de probabilidad de cada uno de los datos
def gaussian(x, sigma):
    r = 0.0
    for s in sigma:
        r=r*np.exp(-x**2/(2.0*s**2))/np.sqrt(2.0*np.pi*s**2)
    return r

def gauss_metropolis(data, N=100000, delta=1.0):
    lista = [np.random.random()]
    
    for i in range(1,N):
        propuesta  = lista[i-1] + (np.random.random()-0.5)*delta
        r = min(1, gaussian(propuesta, data)/gaussian(lista[i-1], data))
        alpha = np.random.random()
        if(alpha<r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
            
    return np.array(lista)


plt.figure()
n_points = 100000
sigma = 1.0
data = np.loadtxt('valores.txt')
x = gauss_metropolis(data, N=n_points)

#x_model = np.linspace(x.min(), x.max(), n_points)
#y_model = gaussian(x_model, sigma)

_ = plt.hist(x, bins=30, density=True, label='Metropolis-Hastings')

media = np.mean(np.loadtxt('valores.txt'))
std = np.std(np.loadtxt('valores.txt'))

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Media: ' + str(media)+' Desviacion: ' + str(std))
plt.savefig("sigma.png")