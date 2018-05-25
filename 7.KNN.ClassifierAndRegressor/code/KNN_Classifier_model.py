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

def load_classification_data():
    digits = datasets.load_digits()
    return model_selection.train_test_split(digits.data,digits.target,test_size=0.25,random_state=0,stratify=digits.target)

def create_regression_data(n):
    X = 5 * np.random.rand(n,1)
    y = np.sin(X).ravel()
    y[::5] += 1 * (0.5 - np.random.rand(int(n/5)))
    return model_selection.train_test_split(X,y,test_size=0.25,random_state=0)

def test_KNeighborsClassifier(*data):
    X_train, X_test,y_train,y_test = data
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)
    print("Training Score:{:f}".format(clf.score(X_train,y_train)))
    print("Testing Score:{:f}".format(clf.score(X_test,y_test)))


def test_KNeighborsClassifier_k_w(*data):
    X_train, X_test, y_train, y_test = data
    # X_train, X_test, y_train, y_test = X_train[1:100], X_test[1:100], y_train[1:100], y_test[1:100]
    ks = np.linspace(1,y_train.size,num =100 ,endpoint=False,dtype='int' )
    weights = ["uniform","distance"]
    line = pe.Line("KNN_Classifier_k_w",page_title="KNN_Classifier_k_w")
    for weight in weights:
        training_scores = []
        testing_scores = []
        for k in ks:
            clf = neighbors.KNeighborsClassifier(weights=weight,n_neighbors=k)
            clf.fit(X_train,y_train)
            training_scores.append(clf.score(X_train,y_train))
            testing_scores.append(clf.score(X_test,y_test))
        line.add("--{weight:}--training".format(weight=weight),ks,training_scores)
        line.add("--{weight:}--testing".format(weight=weight),ks,testing_scores,xaxis_name="K值",
                 yaxis_name="Scores",yaxis_name_gap=50,legend_top='bottom')
    line.render("../output/KNeighborsClassifier_k_w.html")

def test_KNeighborsClassifier_k_p(*data):
    X_train, X_test, y_train, y_test = data
    # X_train, X_test, y_train, y_test = X_train[1:100], X_test[1:100], y_train[1:100], y_test[1:100]
    ks = np.linspace(1,y_train.size,num =100 ,endpoint=False,dtype='int' )
    ps = [1,2,10]
    line = pe.Line("KNN_Classifier_k_p",page_title="KNN_Classifier_k_p")
    for p in ps:
        training_scores = []
        testing_scores = []
        for k in ks:
            clf = neighbors.KNeighborsClassifier(p=p,n_neighbors=k,n_jobs=-1)
            clf.fit(X_train,y_train)
            training_scores.append(clf.score(X_train,y_train))
            testing_scores.append(clf.score(X_test,y_test))
        line.add("--p:{p:}--training".format(p=p),ks,training_scores)
        line.add("--p:{p:}--testing".format(p=p),ks,testing_scores,xaxis_name="K值",
                 yaxis_name="Scores",yaxis_name_gap=50,legend_top='bottom')
    line.render("../output/KNeighborsClassifier_k_p.html")



if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_classification_data()
    test_KNeighborsClassifier(X_train, X_test,y_train,y_test)
    test_KNeighborsClassifier_k_w(X_train, X_test,y_train,y_test)
    test_KNeighborsClassifier_k_p(X_train, X_test,y_train,y_test)   #p值对预测性能无影响