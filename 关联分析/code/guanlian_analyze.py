# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/4/19 16:00
# @Author  :  wanghuodong  
# @note    : 

from numpy import *
import itertools

support_dic = {}


# 生成原始数据，用于测试
def loadDataSet():
    # return [['1', '3', '4'], ['2', '3', '5'], ['1', '2', '3', '5'], ['2', '5']]
    import pandas as pd
    raw_data = pd.read_csv('../data/raw_data_all.txt', header=None, sep='\t')
    # print(raw_data.head)
    order_list = []
    matList = []
    for i in range(len(raw_data.values)):
        if raw_data.values[i, 0] not in order_list:
            order_list.append(raw_data.values[i, 0])
            matList.append([])
        else:
            index_num = order_list.index(raw_data.values[i, 0])
            matList[index_num].append(str(raw_data.values[i, 1]))

    matList1 = [list(set(i)) for i in matList]
    matList1 = [i for i in matList1 if len(i)>1]
    return matList1


# 获取整个数据库中的一阶元素
# C1 = {1, 2, 3, 4, 5}
def createC1(dataSet):
    C1 = set([])
    for item in dataSet:
        C1 = C1.union(set(item))
    return [frozenset([i]) for i in C1]


# 输入数据库（dataset） 和 由第K-1层数据融合后得到的第K层数据集（Ck），
# 用最小支持度（minSupport)对 Ck 过滤，得到第k层剩下的数据集合（Lk）
def getLk(dataset, Ck, minSupport):
    global support_dic
    Lk = {}
    # 计算Ck中每个元素在数据库中出现次数
    for item in dataset:
        for Ci in Ck:
            if Ci.issubset(item):
                if not Ci in Lk:
                    Lk[Ci] = 1
                else:
                    Lk[Ci] += 1
    # 用最小支持度过滤
    Lk_return = []
    for Li in Lk:
        support_Li = Lk[Li] / float(len(dataSet))
        if support_Li >= minSupport:
            Lk_return.append(Li)
            support_dic[Li] = support_Li
    return Lk_return


# 将经过支持度过滤后的第K层数据集合（Lk）融合
# 得到第k+1层原始数据Ck1
'''连接步'''


def genLk1(Lk):
    Ck1 = []
    for i in range(len(Lk) - 1):
        for j in range(i + 1, len(Lk)):
            if sorted(list(Lk[i]))[0:-1] == sorted(list(Lk[j]))[0:-1]:
                Ck1.append(Lk[i] | Lk[j])
    return Ck1


# 遍历所有二阶及以上的频繁项集合
def genItem(freqSet, support_dic):
    for i in range(1, len(freqSet)):
        for freItem in freqSet[i]:
            genRule(freItem)


# 输入一个频繁项，根据“置信度”生成规则
# 采用了递归，对规则树进行剪枝
def genRule(Item, minConf=0.5):
    if len(Item) >= 2:
        for element in itertools.combinations(list(Item), 1):
            if support_dic[Item] / float(support_dic[Item - frozenset(element)]) >= minConf:
                print(str([Item - frozenset(element)]) + "----->" + str(element))
                print(support_dic[Item] / float(support_dic[Item - frozenset(element)]))
                genRule(Item - frozenset(element))


# 输出结果
if __name__ == '__main__':
    dataSet = loadDataSet()
    result_list = []
    Ck = createC1(dataSet)
    # 循环生成频繁项集合，直至产生空集
    while True:
        Lk = getLk(dataSet, Ck, 0.02)
        if not Lk:
            break
        result_list.append(Lk)
        Ck = genLk1(Lk)
        if not Ck:
            break
    # 输出频繁项及其“支持度”
    print(support_dic)
    # 输出规则
    genItem(result_list, support_dic)