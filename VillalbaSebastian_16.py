import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos.txt')

#print(datos[:,0])

def DFT(x):
    
    N = x.size
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    w = 2*np.pi*k*n
    return w,np.dot(e, x)

e,dft = DFT(datos[:,3])
plt.figure()
plt.plot(datos[:,0],datos[:,3],label= 'Variación') 
plt.plot(datos[:,0],np.abs(dft),label = 'DFT')
plt.xlabel('Tiempo (años)')
plt.ylabel('Variacion')
plt.legend()
plt.savefig('solar.png')

print(np.max(np.abs(dft))/2*np.pi)