# -*- coding:utf-8 -*-
"""
@Time: 3th May 2019
"""

import numpy as np
import matplotlib.pyplot as plt

raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]
              ]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train=np.array(raw_data_X)
y_train=np.array(raw_data_y)


plt.scatter(X_train[y_train==0,0],X_train[y_train==0,1],color='g')
plt.scatter(X_train[y_train==1,0],X_train[y_train==1,1],color='r')
plt.show()


x = np.array([8.093607318, 3.365731514])
plt.scatter(X_train[y_train==0,0],X_train[y_train==0,1],color='g')
plt.scatter(X_train[y_train==1,0],X_train[y_train==1,1],color='r')
plt.scatter(x[0],x[1],color='b')
plt.show()

# kNN的实现过程
from math import sqrt

distances = []
for x_train in X_train:
    d = sqrt(np.sum((x_train - x) ** 2))
    distances.append(d)

# distances=[sqrt(np.sum((x_train-x)**2)) for x_train in X_train]

nearest = np.argsort(distances)
k = 6
topK_y = [y_train[i] for i in nearest[:k]]

from collections import Counter
votes=Counter(topK_y)
predict_y=votes.most_common(1)[0][0]


#import模块的万金油方法
import sys, os
base_path = os.path.dirname(os.path.dirname(
                            os.path.abspath(__file__)))
sys.path.append(base_path)

from machine_learning.KNN import kNN

knn_clf= kNN.KNNClassifier(k=6)
knn_clf.fit(X_train,y_train)
y_predict=knn_clf.predict(x.reshape(1,-1))

#使用scikit-learn中的kNN
# from sklearn.neighbors import KNeighborsClassifier
# kNN_classifier=KNeighborsClassifier(n_neighbors=6)
# kNN_classifier.fit(X_train,y_train)
# kNN_classifier.predict(x.reshape(1,-1))

