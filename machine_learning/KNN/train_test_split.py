# -*- coding:utf-8 -*-
"""
@Time: 3th May 2019
"""

import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets

iris=datasets.load_iris()
X=iris.data
y=iris.target

import sys,os
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from machine_learning.KNN import model_selection, kNN, metrics

X_train,X_test,y_train,y_test= model_selection.train_test_split(X, y)

knn_clf= kNN.KNNClassifier(k=3)
knn_clf.fit(X_train,y_train)
y_predict=knn_clf.predict(X_test)

sum(y_predict==y_test)/len(y_test)


#sklearn中的train_test_split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=666)
from sklearn.neighbors import KNeighborsClassifier
my_knn_clf=KNeighborsClassifier(n_neighbors=3)
my_knn_clf.fit(X_train,y_train)
y_predict=my_knn_clf.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_predict)






digits=datasets.load_digits()
digits.keys()
# digits['DESCR']
X=digits.data
y=digits.target

some_digit=X[666]
y[666]
some_digit_image=some_digit.reshape(8,8)
plt.imshow(some_digit_image,cmap=matplotlib.cm.binary)
plt.show()


X_train,X_test,y_train,y_test= model_selection.train_test_split(X, y, test_ratio=0.2)
knn_clf= kNN.KNNClassifier(k=3)
knn_clf.fit(X_train,y_train)
y_predict=knn_clf.predict(X_test)
sum(y_predict==y_test)/len(y_test)

metrics.accuracy_score(y_test, y_predict)
knn_clf.score(X_test,y_test)




#超参数
digits=datasets.load_digits()
X=digits.data
y=digits.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=666)
from sklearn.neighbors import KNeighborsClassifier
knn_clf=KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X_train,y_train)
knn_clf.score(X_test,y_test)

#寻找最好的k
#考虑距离与否
best_method=""
best_score=0.0
best_k=-1
for method in ["uniform","distance"]:
    for k in range(1,11):
        knn_clf=KNeighborsClassifier(n_neighbors=k,weights=method)
        knn_clf.fit(X_train,y_train)
        score=knn_clf.score(X_test,y_test)
        if score>best_score:
            best_k=k
            best_score=score
            best_method=method
print("best_method=",best_method)
print("best_k=",best_k)
print("best_score=",best_score)

#搜索明可弗斯距离相应的p
best_p=-1
best_score=0.0
best_k=-1

for k in range(1,11):
    for p in range(1,6):
        knn_clf=KNeighborsClassifier(n_neighbors=k,weights="distance",p=p)
        knn_clf.fit(X_train,y_train)
        score=knn_clf.score(X_test,y_test)
        if score>best_score:
            best_k=k
            best_score=score
            best_p=p
print("best_p=",p)
print("best_k=",best_k)
print("best_score=",best_score)


# # Grid Search
# param_grid=[
#     {
#         'weights':['uniform'],
#         'n_neighbors':[i for i in range(1,11)]
#     },
#     {
#         'weights':['distance'],
#         'n_neighbors':[i for i in range(1,11)],
#         'p':[i for i in range(1,6)]
#     }
# ]
#
#
# knn_clf=KNeighborsClassifier()
# from sklearn.model_selection  import GridSearchCV
# grid_search=GridSearchCV(knn_clf,param_grid,n_jobs=-1)
# grid_search.fit(X_train,y_train)



