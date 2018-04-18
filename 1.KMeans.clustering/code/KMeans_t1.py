# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/17 16:56
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn.cluster import KMeans

#生成一个随机数据，样本大小为1000, 特征数为2
data = np.random.rand(1000,2)

#构造一个聚类数为4的聚类器
estimator = KMeans(n_clusters=4,)
#聚类,训练模型
estimator.fit(data)
#聚类器的3个属性，聚类标签、聚类中心、聚类准则总和
#
label_pred = estimator.labels_
centroids = estimator.cluster_centers_
inertia = estimator.inertia_

print(label_pred)
print(centroids)
print(inertia)

from pyecharts import Scatter
sca = Scatter("测试聚类分群")
sca.add("A",data[label_pred==0][:,0],data[label_pred==0][:,1],)
sca.add("B",data[label_pred==1][:,0],data[label_pred==1][:,1],)
sca.add("C",data[label_pred==2][:,0],data[label_pred==2][:,1],)
sca.add("D",data[label_pred==3][:,0],data[label_pred==3][:,1],)
sca.render("../output/测试聚类分群.html")

from sklearn.externals import joblib
#将KMeans实例打包保存为doc_cluster.pkl
joblib.dump(estimator,  'KMeans_t1.pkl')
#重新装载KMeans实例并 命名为km
km = joblib.load('KMeans_t1.pkl')
#获得模型的标签
clusters = km.labels_.tolist()
print(clusters,type(clusters))
print(type(km.labels_))

#查看KMeans实例(参数)是否一致
print(estimator)
print(km)