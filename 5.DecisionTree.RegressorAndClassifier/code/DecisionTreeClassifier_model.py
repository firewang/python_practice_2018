# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/24 13:42
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
import pyecharts as pe

def load_data():
    iris = datasets.load_iris()
    return model_selection.train_test_split(iris.data,iris.target,test_size=0.25,random_state=0,stratify=iris.target)

def test_DecisionTreeClassifier(*data):
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
############# 绘制决策图
    import pydotplus
    from sklearn import tree
    from sklearn.externals.six import StringIO
    import os
    tree.export_graphviz(clf,out_file='../output/tree.dot')
    #delete tree.dot file  === os.remove()
    # os.unlink("../output/tree.dot")
    # os.remove("../output/tree.dot")
    dot_data = StringIO()  #把文件暂时写在内存的对象中?
    iris = datasets.load_iris()
    tree.export_graphviz(clf,out_file=dot_data,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("../output/iris1.pdf")
    # graph.write_png("../output/iris1.png")




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
test_DecisionTreeClassifier(X_train,X_test,y_train,y_test)
test_DecisionTreeClassifier_criterion(X_train,X_test,y_train,y_test)
test_DecisionTreeClassifier_splitter(X_train,X_test,y_train,y_test)
test_DecisionTreeClassifier_depth(X_train,X_test,y_train,y_test,maxdepth=20)

