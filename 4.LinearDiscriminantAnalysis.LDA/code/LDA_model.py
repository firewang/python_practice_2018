# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/23 11:39
# @Author  :  wanghuodong  
# @note    : 

from sklearn import datasets
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np
import pyecharts as pe


def load_data():
    iris = datasets.load_iris()
    return model_selection.train_test_split(iris.data,iris.target,random_state=0,test_size=0.25)

def test_LinearDiscriminantAnalysis(*data):
    X_train,X_test,y_train,y_test = data
    regr = LinearDiscriminantAnalysis()
    regr.fit(X_train,y_train)
    print("Coefficients:{coefficients} , intercept:{intercept}".format(coefficients=regr.coef_,
                                                                             intercept=regr.intercept_))
    print("score:{score:>+6.2f}".format(score=regr.score(X_test, y_test)))
    print("explained_variance_ratio : {}".format(regr.explained_variance_ratio_))
    print("xbar :{} ".format(regr.xbar_))
    print("means :{} ".format(regr.means_))
    print("scalings :{} ".format(regr.scalings_))
    print("classes :{} ".format(regr.classes_))


X_train, X_test, y_train, y_test = load_data()
test_LinearDiscriminantAnalysis(X_train,X_test,y_train,y_test)

######### 测试不同solver
def test_LinearDiscriminantAnalysis_solver(*data):
    X_train, X_test, y_train, y_test = data
    solvers = ['svd', 'lsqr',  'eigen']
    for solver in solvers:
        regr = LinearDiscriminantAnalysis(solver=solver)
        regr.fit(X_train, y_train)
        print("Coefficients:{coefficients} , intercept:{intercept}".format(coefficients=regr.coef_,
                                                                       intercept=regr.intercept_))
        print("score:{score:>+6.2f}".format(score=regr.score(X_test, y_test)))

test_LinearDiscriminantAnalysis_solver(X_train,X_test,y_train,y_test)


############shrinkage的影响,仅在solver = lsqr / eigen时有效
def test_LinearDiscriminantAnalysis_shrinkage(*data):
    X_train, X_test, y_train, y_test = data
    shrinkages = np.linspace(0,1,num=20)
    scores = []
    for shrinkage in shrinkages:
        regr = LinearDiscriminantAnalysis(solver='lsqr',shrinkage=shrinkage)
        regr.fit(X_train, y_train)
        scores.append(regr.score(X_test, y_test))
    line = pe.Line("lsqr.shrinkage与scores")
    line.add("",shrinkages,scores,xaxis_name='shrinkages',yaxis_name='scores',yaxis_name_gap=50,
             yaxis_min=0.89)
    line.render("../output/test_LinearDiscriminantAnalysis_shrinkage.html")

test_LinearDiscriminantAnalysis_shrinkage(X_train,X_test,y_train,y_test)