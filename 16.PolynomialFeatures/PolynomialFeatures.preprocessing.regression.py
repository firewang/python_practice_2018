# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/9/3 17:49
# @Author  :  wanghuodong  
# @note    :

import pyecharts as pe
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
    X_train, X_test, y_train, y_test = data
    # 构建多项式生成器
    poly2 = PolynomialFeatures(degree=2)
    # 使用多项式生成器对训练数据生成 多项式
    X_train_poly2 = poly2.fit_transform(X_train)
    # 构建线性回归 生成器
    lg = LinearRegression()
    # 进行线性回归
    lg.fit(X_train_poly2,y_train)

    X_test_poly2 = poly2.transform(X_test)
    y_test_poly2 = lg.predict(X_test_poly2)

    print("训练等分：",lg.score(X_train_poly2,y_train))
    print("测试等分：",lg.score(X_test_poly2,y_test))

'''
# 2次线性回归进行预测
poly2 = PolynomialFeatures(degree=2)    # 2次多项式特征生成器
x_train_poly2 = poly2.fit_transform(x_train)
# 建立模型预测
regressor_poly2 = LinearRegression()
regressor_poly2.fit(x_train_poly2, y_train)
# 画出2次线性回归的图
xx_poly2 = poly2.transform(xx)
yy_poly2 = regressor_poly2.predict(xx_poly2)
plt.scatter(x_train, y_train)
plt1, = plt.plot(xx, yy, label="Degree1")
plt2, = plt.plot(xx, yy_poly2, label="Degree2")
plt.axis([0, 25, 0, 25])
plt.xlabel("Diameter")
plt.ylabel("Price")
plt.legend(handles=[plt1, plt2])
plt.show()
# 输出二次回归模型的预测样本评分
print("二次线性模型在训练数据上得分:", regressor_poly2.score(x_train_poly2, y_train))     # 0.9816421639597427'''






if __name__ == '__main__':
    X_train,X_test,y_train,y_test=load_data()
    test_poly(X_train,X_test,y_train,y_test)


