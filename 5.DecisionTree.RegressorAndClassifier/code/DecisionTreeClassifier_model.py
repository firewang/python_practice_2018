# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/24 13:42
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
import time
from sklearn import datasets
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
import pyecharts as pe
import pydotplus
from dtreeviz.trees import dtreeviz

def load_data():
    iris = datasets.load_iris()
    return model_selection.train_test_split(iris.data,iris.target,test_size=0.25,random_state=0,stratify=iris.target)


def writeTree(clf, feature_names=None, class_names=None, filename='tree'):
    """绘制决策图"""
    dot_data = tree.export_graphviz(clf,
                                    feature_names=feature_names,
                                    class_names=class_names,
                                    out_file=None,
                                    filled=True,
                                    rounded=True)  # rounded 用于支持中文
    # graph = pydotplus.graph_from_dot_data(dot_data)
    graph = pydotplus.graph_from_dot_data(dot_data.replace('helvetica', '"Microsoft YaHei"'))
    # Image(graph.create_png())
    # 将决策树模型输出为图片
    currenttime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    graph.write_png(f'../output/{filename}-{currenttime}.png')
    # 将决策树模型输出为PDF
    graph.write_pdf(f'../output/{filename}-{currenttime}.pdf')


def myDecisionTreeClassifier(*data):
    X_train,X_test,y_train,y_test = data
    clf = DecisionTreeClassifier()
    clf.fit(X_train,y_train)
    print("Training Score:{score:f}".format(score=clf.score(X_train,y_train)))
    print("Testing Score:{score:f}".format(score=clf.score(X_test,y_test)))
    print(clf.classes_)
    print(clf.feature_importances_)
    print(clf.max_features_)
    print(clf.n_classes_)
    print(clf.n_features_)
    print(clf.n_outputs_)

    # 绘制决策图
    iris = datasets.load_iris()
    writeTree(clf,
              feature_names=iris.feature_names,
              class_names=iris.target_names,
              )

    # 另一种方式的决策图
    treeviz = dtreeviz(
        clf,
        X_train,
        y_train,
        target_name="hua",
        feature_names=iris.feature_names,
        class_names=["setosa", "versicolor", "virginica"]
    )
    treeviz.view()
    treeviz.save(treeviz.save_svg())


def test_DecisionTreeClassifier_criterion(*data):
    X_train,X_test,y_train,y_test = data
    criterions = ["gini","entropy"]
    for criterion in criterions:
        clf = DecisionTreeClassifier(criterion=criterion)
        clf.fit(X_train,y_train)
        print("Criterion: {}".format(criterion))
        print("Training Score:{score:f}".format(score=clf.score(X_train,y_train)))
        print("Testing Score:{score:f}".format(score=clf.score(X_test,y_test)))

def test_DecisionTreeClassifier_splitter(*data):
    X_train,X_test,y_train,y_test = data
    splitters = ["best","random"]
    for splitter in splitters:
        clf = DecisionTreeClassifier(splitter=splitter)
        clf.fit(X_train,y_train)
        print("Splitter: {}".format(splitter))
        print("Training Score:{score:f}".format(score=clf.score(X_train,y_train)))
        print("Testing Score:{score:f}".format(score=clf.score(X_test,y_test)))

def test_DecisionTreeClassifier_depth(*data,maxdepth):
    X_train, X_test, y_train, y_test=data
    depths=np.arange(1,maxdepth)
    train_scores=[]
    test_scores=[]
    for depth in depths:
        regr=DecisionTreeClassifier(max_depth=depth)
        regr.fit(X_train,y_train)
        train_scores.append(regr.score(X_train, y_train))
        test_scores.append(regr.score(X_test, y_test))
    line = pe.Line("max_depth:scores",page_title='Classifier.max_depth_scores')
    line.add("training scores",depths,train_scores)
    line.add("testing scores",depths,test_scores,xaxis_name="max_depth",yaxis_name='scores',yaxis_min=0.65,yaxis_name_gap=50)
    line.render("../output/Classifier.max_depth_scores.html")


X_train,X_test,y_train,y_test = load_data()
myDecisionTreeClassifier(X_train,X_test,y_train,y_test)
# test_DecisionTreeClassifier_criterion(X_train,X_test,y_train,y_test)
# test_DecisionTreeClassifier_splitter(X_train,X_test,y_train,y_test)
# test_DecisionTreeClassifier_depth(X_train,X_test,y_train,y_test,maxdepth=20)

