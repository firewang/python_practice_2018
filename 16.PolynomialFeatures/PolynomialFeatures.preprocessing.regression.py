# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/9/3 17:49
# @Author  :  wanghuodong  
# @note    :

import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets
'''https://www.cnblogs.com/Lin-Yi/p/8975638.html'''

def load_data():
    diabetes = datasets.load_diabetes()
    print(type(diabetes))
    print(diabetes.data.shape)
    print(diabetes.target.shape)
    return model_selection.train_test_split(diabetes.data,diabetes.target,test_size=0.25,random_state=0)


def test_poly(*data):
    # 单纯使用岭回归
    X_train, X_test, y_train, y_test = data
    rg = Ridge()
    rg.fit(X_train,y_train)
    print("rg.train.score:",rg.score(X_train,y_train))
    print("rg.test.score:",rg.score(X_test,y_test))
    
    # 构建多项式生成器
    poly = PolynomialFeatures()
    # 使用多项式生成器对训练数据生成 多项式
    X_poly = poly.fit_transform(X_train)
    # 查看多项式各项
    print(poly.get_feature_names())
    # 用训练好的多项式生成器将X_test也转化为多项式形式
    Xt_poly = poly.transform(X_test)
    #新构建一个岭回归
    rg1= Ridge()
    rg1.fit(X_poly,y_train)
    print("rg.train.score:",rg1.score(X_poly,y_train))
    print("rg.test.score:",rg1.score(Xt_poly,y_test))

if __name__ == '__main__':
    X_train,X_test,y_train,y_test=load_data()
    test_poly(X_train,X_test,y_train,y_test)


