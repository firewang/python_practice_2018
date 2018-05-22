# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/22 11:25
# @Author  :  wanghuodong  
# @note    : 
import pyecharts as pe
import numpy as np
from sklearn import linear_model,discriminant_analysis,model_selection
from sklearn import datasets

def load_data():
    diabetes = datasets.load_diabetes()
    print(type(diabetes))
    return model_selection.train_test_split(diabetes.data,diabetes.target,test_size=0.25,random_state=0)

def test_LinearRegression(*data):
    X_train,X_test,y_train,y_test=data
    regr = linear_model.LinearRegression()
    regr.fit(X_train,y_train)
    print("Coefficients:{coefficients},intercept:{intercept:.2f}".format(coefficients=regr.coef_,intercept=regr.intercept_))
    print("Residual sum of squares: {RSS:.2f}".format(RSS=np.mean((regr.predict(X_test)-y_test)**2)))
    print("Score: {score:.2f}".format(score=regr.score(X_test,y_test)))

def test_Ridge(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.Ridge()
    regr.fit(X_train,y_train)
    print("Coefficients:{coefficients},intercept:{intercept:.2f}".format(coefficients=regr.coef_,intercept=regr.intercept_))
    print("Residual sum of squares: {RSS:.2f}".format(RSS=np.mean((regr.predict(X_test)-y_test)**2)))
    print("Score: {score:.2f}".format(score=regr.score(X_test,y_test)))

def test_Ridge_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100]
    scores = [    ]
    for i,alpha in enumerate(alphas):
        regr = linear_model.Ridge(alpha=alpha)
        regr.fit(X_train,y_train)
        scores.append(regr.score(X_test,y_test))
    line = pe.Line("alpha与score")
    line.add("",alphas,scores)
    line.render("../output/test_Ridge_alpha.html")

def test_Lasso(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.Lasso()
    regr.fit(X_train, y_train)
    print("Coefficients:{coefficients},intercept:{intercept:.2f}".format(coefficients=regr.coef_,
                                                                         intercept=regr.intercept_))
    print("Residual sum of squares: {RSS:.2f}".format(RSS=np.mean((regr.predict(X_test) - y_test) ** 2)))
    print("Score: {score:.2f}".format(score=regr.score(X_test, y_test)))

def test_Lasso_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
    scores = []
    for i, alpha in enumerate(alphas):
        regr = linear_model.Lasso(alpha=alpha)
        regr.fit(X_train, y_train)
        scores.append(regr.score(X_test, y_test))
    line = pe.Line("alpha与score:Lasso")
    line.add("", alphas, scores)
    line.render("../output/test_Lasso_alpha.html")


def test_ElasticNet(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.ElasticNet()
    regr.fit(X_train, y_train)
    print("Coefficients:{coefficients},intercept:{intercept:.2f}".format(coefficients=regr.coef_,
                                                                         intercept=regr.intercept_))
    print("Residual sum of squares: {RSS:.2f}".format(RSS=np.mean((regr.predict(X_test) - y_test) ** 2)))
    print("Score: {score:.2f}".format(score=regr.score(X_test, y_test)))


X_train,X_test,y_train,y_test=load_data()
test_LinearRegression(X_train,X_test,y_train,y_test)
test_Ridge(X_train,X_test,y_train,y_test)
test_Ridge_alpha(X_train,X_test,y_train,y_test)
test_Lasso(X_train,X_test,y_train,y_test)
test_Lasso_alpha(X_train,X_test,y_train,y_test)
test_ElasticNet(X_train,X_test,y_train,y_test)
# test_ElasticNet_alpha(X_train,X_test,y_train,y_test)



