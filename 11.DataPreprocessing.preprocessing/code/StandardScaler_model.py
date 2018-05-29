# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/29 15:04
# @Author  :  wanghuodong  
# @note    : 

from sklearn.preprocessing import StandardScaler

X = [
    [1,5,1,2,10],
    [2,6,3,2,7],
    [3,7,5,6,4],
    [4,8,7,8,1]
]
print("before transform: " ,X)

scaler = StandardScaler()
scaler.fit(X)
print("scale_is: ",scaler.scale_)
print("mean_is: ",scaler.mean_)
print("var_is: ",scaler.var_)
print("n_samples_seen_is: ",scaler.n_samples_seen_)

print("after transform : ",scaler.transform(X))