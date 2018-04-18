# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/17 16:56
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn.cluster import KMeans

# 生成一个随机数据，样本大小为1000, 特征数为2
data = np.random.rand(1000,2)

scores = []
for i in range(1,10):
    estimator = KMeans(n_clusters=i,)
    estimator.fit(data)
    scores.append(estimator.inertia_)
# print(scores)
# from pyecharts import Scatter
# sc = Scatter("肘方法判断K值")
# sc.add('',list(range(1,10)),scores)
# sc.render("../output/肘方法判断K值.html")
from pyecharts import Line
line = Line("肘方法判断K值")
line.add('SSE',list(range(1,10)),scores)
line.render("../output/肘方法判断K值.html")
