# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/23 9:18
# @Author  :  wanghuodong  
# @note    : 

from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import numpy as np
import pyecharts as pe  # pyecharts==0.5.11
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


# 鸢尾花 setosa, versicolor, virginica
# 萼片sepal 长度、宽度， 花瓣petal 长度、宽度
def load_data():
    iris = datasets.load_iris()  # 分层采样 stratify
    return model_selection.train_test_split(iris.data, iris.target, test_size=0.25, random_state=0,
                                            stratify=iris.target)


def test_LogisticRegression(*data):
    X_train, X_test, y_train, y_test = data
    regr = LogisticRegression()
    regr.fit(X_train, y_train)
    print("Coefficients:{coefficients} , intercept:{intercept}".format(coefficients=regr.coef_,
                                                                       intercept=regr.intercept_))
    coefficients = pd.DataFrame(regr.coef_, columns=[f"coeff_{col}" for col in range(pd.DataFrame(X_train).shape[1])])
    coefficients.loc[:, "intercept"] = pd.Series(regr.intercept_)
    print(coefficients)
    print("score:{score:>+6.2f}".format(score=regr.score(X_test, y_test)))


X_train, X_test, y_train, y_test = load_data()
test_LogisticRegression(X_train, X_test, y_train, y_test)


########分类策略 multi_class 的影响
def test_LogisticRegression_multinomial(*data):
    X_train, X_test, y_train, y_test = data
    regr = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    regr.fit(X_train, y_train)
    print("Coefficients:{coefficients} , intercept:{intercept}".format(coefficients=regr.coef_,
                                                                       intercept=regr.intercept_))
    coefficients = pd.DataFrame(regr.coef_, columns=[f"coeff_{col}" for col in range(pd.DataFrame(X_train).shape[1])])
    coefficients.loc[:, "intercept"] = pd.Series(regr.intercept_)
    print(coefficients)
    print("score:{score:>+6.2f}".format(score=regr.score(X_test, y_test)))


test_LogisticRegression_multinomial(X_train, X_test, y_train, y_test)


def test_LogisticRegression_C(*data):
    X_train, X_test, y_train, y_test = data
    Cs = np.logspace(-2, 4, num=100)  # 等比数列
    scores = []
    for c in Cs:
        regr = LogisticRegression(multi_class='multinomial', solver='lbfgs', C=c)
        regr.fit(X_train, y_train)
        scores.append(regr.score(X_test, y_test))
    line = pe.Line("LogisticRegression_C")
    line.add("LogisticRegression_C", Cs, scores, yaxis_min=0.8, yaxis_max=1,
             xaxis_name="C", yaxis_name='Score', yaxis_name_gap=50)
    line.render("../output/LogisticRegression_C.html")


test_LogisticRegression_C(X_train, X_test, y_train, y_test)
