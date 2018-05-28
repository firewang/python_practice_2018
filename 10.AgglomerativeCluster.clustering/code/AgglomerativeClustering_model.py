# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/28 16:06
# @Author  :  wanghuodong  
# @note    : 

from sklearn.datasets.samples_generator import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
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

def test_AgglomerativeClustering(*data):
    X,labels_true = data
    clst = cluster.AgglomerativeClustering()
    predicted_labels = clst.fit_predict(X)
    print("ARIs：{}".format(adjusted_rand_score(labels_true,predicted_labels)))

def test_AgglomerativeClustering_nclusters(*data):
    X,labels_true = data
    nclusters = list(range(1,50))
    ARIs = []
    for ncluster in nclusters:
        clst = cluster.AgglomerativeClustering(n_clusters=ncluster)
        predicted_labels = clst.fit_predict(X)
        ARIs.append(adjusted_rand_score(labels_true,predicted_labels))

    line = pe.Line("AgglomerativeClustering_nclusters",page_title='AgglomerativeClustering_nclusters')
    line.add("ARIs",nclusters,ARIs,is_symbol_show=False,is_smooth=True,xaxis_name='簇数量',yaxis_name='ARI',
             legend_top='bottom')
    line.render('../output/AgglomerativeClustering_nclusters.html')

def test_AgglomerativeClustering_linkage(*data):
    X,labels_true = data
    linkages = ['ward','complete','average']
    nclusters = list(range(1,50))
    line = pe.Line("AgglomerativeClustering_linkage", page_title="AgglomerativeClustering_linkage")
    for linkage in linkages:
        ARIs = []
        for ncluster in nclusters:
            clst = cluster.AgglomerativeClustering(linkage=linkage,n_clusters=ncluster)
            predicted_labels = clst.fit_predict(X)
            ARIs.append(adjusted_rand_score(labels_true,predicted_labels))
        line.add("{linkage:}".format(linkage=linkage),nclusters,ARIs,xaxis_name="簇数量",
                 is_smooth=True,legend_top="bottom",yaxis_name_gap=50,yaxis_name="ARI",
                 )
    line.render("../output/AgglomerativeClustering_linkage.html")

if __name__ == '__main__':
    X,labels_true = create_data([[1,1],[2,2],[1,2],[10,20]],1000,0.5)
    test_AgglomerativeClustering(X,labels_true)
    test_AgglomerativeClustering_nclusters(X,labels_true)
    test_AgglomerativeClustering_linkage(X,labels_true)

