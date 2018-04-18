# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/18 15:03
# @Author  :  wanghuodong  
# @note    :  轮廓系数判断聚类质量 或者 初始时判断K值

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# 生成一个随机数据，样本大小为1000, 特征数为2
data = np.random.rand(1000,2)

scores = []
silhouette_scores = []
#轮廓系数要求聚类数大于等于2，小于样本数-1
for i in range(2,10):
    estimator = KMeans(n_clusters=i,)
    estimator.fit(data)
    scores.append(estimator.inertia_)
    silhouette_scores.append(silhouette_score(data,estimator.labels_,metric='euclidean'))

from pyecharts import Line
line = Line("轮廓系数判断聚类质量")
#将SSE标准化
line.add('SSE',list(range(2,10)), (np.array(scores).max() - np.array(scores)) / (np.array(scores).max()-np.array(scores).min()))
line.add('silhouette coefficient',list(range(2,10)),silhouette_scores)
line.render("../output/轮廓系数.html")

#得到最佳聚类数K 为4 ，