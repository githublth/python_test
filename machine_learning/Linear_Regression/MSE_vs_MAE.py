
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from sklearn import datasets

boston=datasets.load_boston()

pprint(boston.DESCR)

x=boston.data[:,5]  #只使用房间数量这个特征
x.shape
y=boston.target

plt.scatter(x,y)
plt.show()

np.max(y)

x=x[y<50.0]
y=y[y<50.0]
plt.scatter(x,y)
plt.show()


#使用简单现行回归法