# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/28 14:30
# @Author  :  wanghuodong  
# @note    : 

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture
import pyecharts as pe

def create_data(centers, num =100 ,std=0.7):
    '''
    make_blobs() 产生分隔的 高斯分布的 聚类簇
    :param centers: 聚类中心 构成的数组
    :param num: 样本数
    :param std: 簇中样本的标准差
    :return: 元组， （样本点，类别标记）
    '''
    X,labels_true = make_blobs(n_samples=num , centers = centers, cluster_std=std)
    return X,labels_true

def test_DBSCAN(*data):
    X,labels_true = data
    clst = cluster.DBSCAN()
    predicted_labels = clst.fit_predict(X)
    print("ARI：{}".format(adjusted_rand_score(labels_true,predicted_labels)))
    print("core sample num: {}".format(len(clst.core_sample_indices_)))


def test_DBSCAN_epsilon(*data):
    '''
    epsilon: 邻域内两样本点的最远距离，确定了邻域的大小
    :param data:
    :return:
    '''
    X,labels_true = data
    epsilons = np.logspace(-1,2)
    ARIs = []
    Core_nums = []
    for epsilon in epsilons:
        clst = cluster.DBSCAN(eps=epsilon)
        predicted_labels = clst.fit_predict(X)
        ARIs.append(adjusted_rand_score(labels_true,predicted_labels))
        Core_nums.append(len(clst.core_sample_indices_))
    line = pe.Line("DBSCAN_eps",page_title="DBSCAN_eps")
    line.add("ARIs",epsilons,ARIs,xaxis_name='eps',is_symbol_show=False)
    line.add("Core_nums",epsilons,Core_nums,xaxis_name='eps',is_smooth=True,is_symbol_show=False)
    line.render("../output/DBSCAN_eps.html")

def test_DBSCAN_MinPts(*data):
    '''

    :param data:
    :return:
    '''
    X,labels_true = data
    min_samples = list(range(1,100))
    ARIs = []
    Core_nums = []
    for min_sample in min_samples:
        clst = cluster.DBSCAN(min_samples=min_sample)
        predicted_labels = clst.fit_predict(X)
        ARIs.append(adjusted_rand_score(labels_true,predicted_labels))
        Core_nums.append(len(clst.core_sample_indices_))
    line2 = pe.Line("DBSCAN_MinPts",page_title="DBSCAN_MinPts")
    line2.add("ARIs",min_samples,ARIs)
    line2.add("Core_nums",min_samples,Core_nums,xaxis_name="min_samples(MinPts)")
    line2.render("../output/DBSCAN_MinPts.html")



if __name__ =='__main__':
    X,labels_true = create_data([[1,1],[2,2],[1,2],[10,20]],1000,0.5)
    test_DBSCAN(X,labels_true)     #ARI：0.3314717019583459    core sample num: 991  划分为991个簇
    test_DBSCAN_epsilon(X,labels_true)
    test_DBSCAN_MinPts(X,labels_true)
