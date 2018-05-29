# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/29 15:22
# @Author  :  wanghuodong  
# @note    : 

from sklearn.preprocessing import Normalizer

X = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,3,5,2,4],
    [2,4,1,3,5]
]

norms = ["l1",'l2','max']
print("before transform: \n", X)
for norm in norms:
    normalizer  = Normalizer(norm=norm)
    print("after {norm:-^10} transform \n ".format(norm=norm) , normalizer.transform(X))