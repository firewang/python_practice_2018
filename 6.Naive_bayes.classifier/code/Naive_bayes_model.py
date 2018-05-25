# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/24 17:10
# @Author  :  wanghuodong  
# @note    : 

from sklearn import model_selection
from sklearn import datasets
from sklearn import naive_bayes
import numpy as np
import matplotlib.pyplot as plt
import pyecharts as pe

########使用sklearn自带的手写识别数据集 Digit Dataset
def show_digits():
    digits = datasets.load_digits()
    fig = plt.figure()
    print("vertor from images0: ",digits.data[0])
    for i in range(25):
        ax= fig.add_subplot(5,5,i+1)
        ax.imshow(digits.images[i], cmap=plt.cm.gray_r , interpolation='nearest')
    plt.show()

def load_data():
    digits = datasets.load_digits()
    return model_selection.train_test_split(digits.data,digits.target,test_size=0.25,random_state=0,stratify=digits.target)

######### GaussianNB
def test_GaussianNB(*data):
    X_train,X_test,y_train,y_test = data
    clf = naive_bayes.GaussianNB()
    clf.fit(X_train,y_train)
    print("{:#^20}".format("GaussianNB")) #[fill,align,sign,0,width,.precision,type]
    print("Training Score: {:.2f}".format(clf.score(X_train,y_train)))
    print("Testing Score: {:.2f}".format(clf.score(X_test,y_test)))

####### MultinomialNB
def test_MultinomialNB(*data):
    X_train,X_test,y_train,y_test = data
    clf = naive_bayes.MultinomialNB()
    clf.fit(X_train,y_train)
    print("{:#^20}".format("MultinomialNB"))
    print("Training Score: {:.2f}".format(clf.score(X_train,y_train)))
    print("Testing Score: {:.2f}".format(clf.score(X_test,y_test)))

def test_MultinomialNB_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = np.logspace(-2,5,num=200)
    train_scores = []
    test_scores = []
    for alpha in alphas:
        clf = naive_bayes.MultinomialNB(alpha=alpha)
        clf.fit(X_train, y_train)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))
    line = pe.Line("MultinomialNB_alpha",page_title="MultinomialNB_alpha")
    line.add("training",alphas,train_scores)
    line.add("testing",alphas,test_scores,yaxis_min=0.8,xaxis_name="MultinomialNB_alpha",yaxis_name="scores",yaxis_name_gap=50,
             is_smooth=True)
    line.render("../output/MultinomialNB_alpha.html")



####### BernoulliNB
def test_BernoulliNB(*data):
    X_train,X_test,y_train,y_test = data
    clf = naive_bayes.BernoulliNB()
    clf.fit(X_train,y_train)
    print("{:#^20}".format("BernoulliNB"))
    print("Training Score: {:.2f}".format(clf.score(X_train,y_train)))
    print("Testing Score: {:.2f}".format(clf.score(X_test,y_test)))

def test_BernoulliNB_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = np.logspace(-2,5,num=200)
    train_scores = []
    test_scores = []
    for alpha in alphas:
        clf = naive_bayes.BernoulliNB(alpha=alpha)
        clf.fit(X_train, y_train)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))
    line = pe.Line("BernoulliNB_alpha",page_title="BernoulliNB_alpha")
    line.add("training",alphas,train_scores)
    line.add("testing",alphas,test_scores,yaxis_min=0.8,xaxis_name="BernoulliNB_alpha",yaxis_name="scores",yaxis_name_gap=50,
             is_smooth=True)
    line.render("../output/BernoulliNB_alpha.html")

def test_BernoulliNB_binarize(*data):
    X_train, X_test, y_train, y_test = data
    min_x = min(np.min(X_train.ravel()),np.min(X_test.ravel()))-0.1
    max_x = max(np.max(X_train.ravel()),np.max(X_test.ravel()))+0.1
    binarizes = np.linspace(min_x,max_x,endpoint=True,num=100)
    train_scores = []
    test_scores = []
    for binarize in binarizes:
        clf = naive_bayes.BernoulliNB(binarize=binarize)
        clf.fit(X_train, y_train)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))
    line = pe.Line("BernoulliNB_binarize", page_title="BernoulliNB_binarize")
    line.add("training", binarizes, train_scores)
    line.add("testing", binarizes, test_scores, yaxis_min=0.8, xaxis_name="BernoulliNB_binarize", yaxis_name="scores",
             yaxis_name_gap=50,
             is_smooth=True, xaxis_min=min_x-1)
    line.render("../output/BernoulliNB_binarize.html")

if __name__ == '__main__':
    # show_digits()
    X_train,X_test,y_train,y_test = load_data()
    test_GaussianNB(X_train,X_test,y_train,y_test)
    test_MultinomialNB(X_train,X_test,y_train,y_test)
    test_MultinomialNB_alpha(X_train,X_test,y_train,y_test)
    test_BernoulliNB(X_train,X_test,y_train,y_test)
    test_BernoulliNB_alpha(X_train,X_test,y_train,y_test)
    test_BernoulliNB_binarize(X_train,X_test,y_train,y_test)
