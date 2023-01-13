import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, 3*np.pi, 0.1)
y_sin =np.sin(x)
y_cos =np.cos(x)

x=np.linspace(-20,20,1000)

def func(x):
    y=[]
    for elem in x:
        # result=x**2
        # result=5*(elem**2)+4*elem
        result=1-(elem**2)/2
        y.append(result)
    return y
y=func(x)
plt.plot(x,y)
plt.show()