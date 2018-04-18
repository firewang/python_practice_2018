# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/18 15:37
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabaz_score
# 生成一个随机数据，样本大小为1000, 特征数为2
data = np.random.rand(1000,2)

calinski_harabaz_scores = []

for i in range(2,10):
    estimator = KMeans(n_clusters=i,)
    estimator.fit(data)
    calinski_harabaz_scores.append(calinski_harabaz_score(data,estimator.labels_))

from pyecharts import Line
line = Line("calinski_harabaz_score")

line.add('calinski_harabaz_score',list(range(2,10)),calinski_harabaz_scores)
line.render("../output/calinski_harabaz_score.html")