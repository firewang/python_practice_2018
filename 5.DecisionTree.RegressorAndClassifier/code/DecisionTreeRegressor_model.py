# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/24 10:00
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import model_selection
import pyecharts as pe

def create_data(n):
    np.random.seed(0)
    X = 5 * np.random.rand(n,1)
    y = np.sin(X).ravel()   #ravel() / flatten() 将多维数组降为1维
    noise_num =(int)(n/5)
    y[::5] += 3*(0.5-np.random.rand(noise_num))       #每隔5个点添加随机噪声
    return model_selection.train_test_split(X,y,test_size=0.25,random_state=1)

def test_DecisionTreeRegressor(*data):
    X_train, X_test,y_train, y_test = data
    regr = DecisionTreeRegressor()
    regr.fit(X_train,y_train)
    print("Training score: {score:.2f}".format(score=regr.score(X_train,y_train)))
    print("Testing score: {score:.2f}".format(score=regr.score(X_test,y_test)))
    scatter = pe.Scatter()
    scatter.add("Training",X_train,y_train,symbol_size=5)
    scatter.add("Testing",X_test,y_test,symbol_size=5)
    predict_x = np.linspace(0.0,5.0,num=500)[:,np.newaxis]
    scatter.add("Predicting",predict_x,regr.predict(predict_x),symbol='*',symbol_size=3,symbol_color='blue')
    scatter.render("../output/test_DecisionTreeRegressor.html")
    # scatter+line 尚存在问题,似乎是所有叠加图需要相同的x轴刻度
    # line = pe.Line()
    # line.add("predict",predict_x,regr.predict(predict_x),xaxis_interval=1,xaxis3d_max=5,xaxis3d_min=0)
    # lap = pe.Overlap()
    # lap.add(scatter)
    # lap.add(line)
    # lap.render("../output/test_DecisionTreeRegressor_scatterAndline.html")

#随机划分与最优划分的影响
def test_DecisitionTreeRegressor_splitter(*data):
    X_train, X_test, y_train, y_test=data
    splitters=['best','random']
    for splitter in splitters:
        regr=DecisionTreeRegressor(splitter=splitter)
        regr.fit(X_train,y_train)
        print("Splitter:{}".format(splitter))
        print("Training score: {score:f}".format(score=regr.score(X_train, y_train)))
        print("Testing score: {score:f}".format(score=regr.score(X_test, y_test)))

def test_DecisitionTreeRegressor_depth(*data,maxdepth):
    X_train, X_test, y_train, y_test=data
    depths=np.arange(1,maxdepth)
    train_scores=[]
    test_scores=[]
    for depth in depths:
        regr=DecisionTreeRegressor(max_depth=depth)
        regr.fit(X_train,y_train)
        train_scores.append(regr.score(X_train, y_train))
        test_scores.append(regr.score(X_test, y_test))
    line = pe.Line("max_depth:scores")
    line.add("training scores",depths,train_scores)
    line.add("testing scores",depths,test_scores,xaxis_name="max_depth",yaxis_name='scores',yaxis_min=0.5)
    line.render("../output/max_depth_scores.html")


X_train,X_test,y_train,y_test = create_data(100)
test_DecisionTreeRegressor(X_train,X_test,y_train,y_test)
test_DecisitionTreeRegressor_splitter(X_train,X_test,y_train,y_test)
test_DecisitionTreeRegressor_depth(X_train,X_test,y_train,y_test,maxdepth=20)
