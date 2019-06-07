
import numpy as np
import matplotlib.pyplot as plt

#最值归一化
x=np.random.randint(0,100,size=100)
(x-np.min(x))/(np.max(x)-np.min(x))

X=np.random.randint(0,100,(50,2))
X=np.array(X,dtype=float)

X[:,0]=(X[:,0]-np.min(X[:,0]))/(np.max(X[:,0])-np.min(X[:,0]))
X[:,1]=(X[:,1]-np.min(X[:,1]))/(np.max(X[:,1])-np.min(X[:,1]))

plt.scatter(X[:,0],X[:,1])
plt.show()