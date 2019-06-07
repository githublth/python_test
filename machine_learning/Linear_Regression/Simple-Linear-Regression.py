
"""
@Time: 6th May 2019
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([1,3,2,3,5])

plt.scatter(x,y)
plt.axis([0,6,0,6])
plt.show()

x_mean=np.mean(x)
y_mean=np.mean(y)

num=0.0
d=0.0
for x_i,y_i in zip(x,y):
    num+=(x_i-x_mean)*(y_i-y_mean)
    d+=(x_i-x_mean)**2

a=num/d
b=y_mean-a*x_mean

y_hat=a*x+b
plt.scatter(x,y)
plt.plot(x,y_hat,color='r')
plt.axis([0,6,0,6])
plt.show()

x_predict=6
y_predict=a*x_predict+b


#使用我们自己的SimpleLinearRegression
from machine_learning.Linear_Regression.SimpleLinearRegression import SimpleLinearRegression1
reg1=SimpleLinearRegression1()
reg1.fit(x,y)
reg1.predict(np.array([x_predict]))
reg1.a_
reg1.b_


from machine_learning.Linear_Regression.SimpleLinearRegression import SimpleLinearRegression2
reg2=SimpleLinearRegression2()
reg2.fit(x,y)
reg2.predict(np.array([x_predict]))

#性能测试：
m=100
big_x=np.random.random(size=m)
big_y=big_x*2.0+3.0+np.random.normal(size=m)
import timeit
#
# timeit.timeit('reg1.fit(big_x,big_y)',globals=globals())
# timeit.timeit('reg2.fit(big_x,big_y)',globals=globals())


