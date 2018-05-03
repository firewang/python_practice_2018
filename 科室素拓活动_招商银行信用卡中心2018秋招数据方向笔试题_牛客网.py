# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/3 11:10
# @Author  :  wanghuodong  
# @note    : 
'''
科室素拓进行游戏，游戏规则如下：随机抽取9个人作为游戏参与人员，分别编号1至9，
每轮要求k(k<=9且k>=0)个人自由组合使编号之和为n。输出满足规则的所有可能的组合。
要求组合内部编号升序输出，组合之间无顺序要求。
输入描述:
输入数据为以空格分隔的两个整数k和n
输出描述:
每行输出一个可能的编号组合，组合内部各个编号以空格分隔升序输出。若无满足规则的组合，则输出None
时间限制：1秒
空间限制：65536K
'''
from itertools import combinations
s = [1,2,3,4,5,6,7,8,9]
s_input = input().split()
k = s_input[0]
# print(k)
n = s_input[1]
# print(n)
com_list = list(combinations(s,int(k)))
#print(com_list)
num = 0
for i in com_list:
    total = 0
    for j in i:
        total += j
    if total == int(n):
        num += 1
        for z in i:
            print(z,end=" ")
        print("\t")
if num==0:
    print("None")

# print(len(com_list))