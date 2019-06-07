
import numpy as np
from sklearn import datasets

iris=datasets.load_iris()

X=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=666)

# scikit-learn中的StandardScaler
from sklearn.preprocessing import StandardScaler
standardScaler=StandardScaler()
standardScaler.fit(X_train)

standardScaler.mean_
X_train=standardScaler.transform(X_train)
X_test_standard=standardScaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
knn_clf=KNeighborsClassifier(n_neighbors=3)
knn_clf.fit(X_train,y_train)
knn_clf.score(X_test_standard,y_test)
