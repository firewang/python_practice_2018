# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/28 9:58
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
import pyecharts as pe
from sklearn import datasets
from sklearn import decomposition

def load_data():
    iris = datasets.load_iris()
    return iris.data,iris.target

def test_PCA(*data):
    X,y =data
    pca = decomposition.PCA()
    pca.fit(X)
    print("explained variance ratio : {ratio:}".format(ratio=str(pca.explained_variance_ratio_)))
    print("explained variance : {variance:}".format(variance=str(pca.explained_variance_)))
    print("components : {components:}".format(components= str(pca.components_)))
    print("n_components : {n_components:}".format(n_components= str(pca.n_components_)))

def plot_PCA(*data):
    X,y = data
    pca = decomposition.PCA(n_components=2)      # 如何判断是哪两个特征？？
    pca.fit(X)
    X_r = pca.transform(X)
    # print(X_r.shape)
    scatter = pe.Scatter("PCA",page_title='PCA')
    scatter.add("Y:0",X_r[y==0,0],X_r[y==0,1])
    scatter.add("Y:1".format(Y=1),X_r[y==1,0],X_r[y==1,1])
    scatter.add("Y:2".format(Y=2),X_r[y==2,0],X_r[y==2,1])
    scatter.render("../output/PCA_scatter.html")


if __name__ == '__main__':
    X, y = load_data()
    test_PCA(X,y)
    #[ 0.92461621  0.05301557  0.01718514  0.00518309] 可以降维为2维
    plot_PCA(X,y)
