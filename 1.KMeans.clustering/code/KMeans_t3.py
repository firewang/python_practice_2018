# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/18 11:35
# @Author  :  wanghuodong  
# @note    : 不太明白图怎么做的，待解决

import numpy as np
from sklearn.cluster import KMeans

#生成一个随机数据，样本大小为1000, 特征数为2
data = np.random.rand(1000,2)

#构造一个聚类数为4的聚类器
estimator = KMeans(n_clusters=4,)
#聚类,训练模型
estimator.fit(data)
#聚类器的3个属性，聚类标签、聚类中心、聚类准则总和
label_pred = estimator.labels_
centroids = estimator.cluster_centers_
inertia = estimator.inertia_

from sklearn.metrics import silhouette_samples
from sklearn.metrics import silhouette_score
silhouette_vals = silhouette_samples(data,label_pred,metric='euclidean')
# print(silhouette_vals)
print(np.mean(silhouette_vals))
print(silhouette_score(data,label_pred,metric='euclidean'))
# print(silhouette_vals[label_pred==0],len(silhouette_vals[label_pred==0]))
print(np.unique(label_pred).shape[0])
from matplotlib import cm
import matplotlib.pyplot as plt
y_ax_lower,y_ax_upper = 0,0
yticks=[]
for i,c in enumerate(np.unique(label_pred)):
    c_silhouette_vals = silhouette_vals[label_pred==c]
    c_silhouette_vals.sort()
    y_ax_upper +=len(c_silhouette_vals)
    color = cm.jet(i/np.unique(label_pred))
    plt.barh(range(y_ax_lower,y_ax_upper)
             ,c_silhouette_vals,
             height=1.0,
             edgecolor='none',
             color=color)
    yticks.append((y_ax_lower+y_ax_upper)/2)
    y_ax_lower +=len(c_silhouette_vals)
silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg,color='red',linestyle='--')
plt.yticks(yticks,np.unique(label_pred)+1)
plt.ylabel("Cluseter")
plt.xlabel('Silhouette coefficient')
# plt.show()
plt.savefig("../output/轮廓分析图.jpg")

