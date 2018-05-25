# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/25 17:18
# @Author  :  wanghuodong  
# @note    : 

# -*- encoding: utf-8 -*-
# @Version : 1.0
# @Time    : 2018/5/25 11:33
# @Author  :  wanghuodong
# @note    :

import numpy as np
from sklearn import neighbors
from sklearn import datasets
from sklearn import model_selection
import pyecharts as pe

def create_regression_data(n):
    X = 5 * np.random.rand(n,1)
    y = np.sin(X).ravel()
    y[::5] += 1 * (0.5 - np.random.rand(int(n/5)))
    return model_selection.train_test_split(X,y,test_size=0.25,random_state=0)

def test_KNeighborsRegressor(*data):
    X_train, X_test,y_train,y_test = data
    regr = neighbors.KNeighborsRegressor()
    regr.fit(X_train,y_train)
    print("Training Score:{:f}".format(regr.score(X_train,y_train)))
    print("Testing Score:{:f}".format(regr.score(X_test,y_test)))


def test_KNeighborsRegressor_k_w(*data):
    X_train, X_test, y_train, y_test = data
    ks = np.linspace(1,y_train.size,num =100 ,endpoint=False,dtype='int' )
    weights = ["uniform","distance"]
    line = pe.Line("KNN_Regressor_k_w",page_title="KNN_Regressor_k_w")
    for weight in weights:
        training_scores = []
        testing_scores = []
        for k in ks:
            regr = neighbors.KNeighborsRegressor(weights=weight,n_neighbors=k)
            regr.fit(X_train,y_train)
            training_scores.append(regr.score(X_train,y_train))
            testing_scores.append(regr.score(X_test,y_test))
        line.add("--{weight:}--training".format(weight=weight),ks,training_scores)
        line.add("--{weight:}--testing".format(weight=weight),ks,testing_scores,xaxis_name="K值",
                 yaxis_name="Scores",yaxis_name_gap=50,legend_top='bottom')
    line.render("../output/KNeighborsRegressor_k_w.html")

def test_KNeighborsRegressor_k_p(*data):
    X_train, X_test, y_train, y_test = data
    # X_train, X_test, y_train, y_test = X_train[1:100], X_test[1:100], y_train[1:100], y_test[1:100]
    ks = np.linspace(1,y_train.size,num =100 ,endpoint=False,dtype='int' )
    ps = [1,2,10]
    line = pe.Line("KNN_Regressor_k_p",page_title="KNN_Regressor_k_p")
    for p in ps:
        training_scores = []
        testing_scores = []
        for k in ks:
            regr = neighbors.KNeighborsRegressor(p=p,n_neighbors=k,n_jobs=-1)
            regr.fit(X_train,y_train)
            training_scores.append(regr.score(X_train,y_train))
            testing_scores.append(regr.score(X_test,y_test))
        line.add("--p:{p:}--training".format(p=p),ks,training_scores)
        line.add("--p:{p:}--testing".format(p=p),ks,testing_scores,xaxis_name="K值",
                 yaxis_name="Scores",yaxis_name_gap=50,legend_top='bottom')
    line.render("../output/KNeighborsRegressor_k_p.html")



if __name__ == '__main__':
    X_train, X_test, y_train, y_test = create_regression_data(1000)
    test_KNeighborsRegressor(X_train, X_test,y_train,y_test)
    # test_KNeighborsRegressor_k_w(X_train, X_test,y_train,y_test)
    test_KNeighborsRegressor_k_p(X_train, X_test,y_train,y_test)