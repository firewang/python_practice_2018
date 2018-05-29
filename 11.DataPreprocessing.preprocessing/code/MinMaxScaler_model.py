# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/29 14:31
# @Author  :  wanghuodong  
# @note    : 

from sklearn.preprocessing import MinMaxScaler

X = [
    [1,5,1,2,10],
    [2,6,3,2,7],
    [3,7,5,6,4],
    [4,8,7,8,1]
]
print("before transform: " ,X)
scaler = MinMaxScaler(feature_range=(0,2))
scaler.fit(X)
print("min_is: ",scaler.min_)
print("scale_is: ",scaler.scale_)
print("data_min_is: ",scaler.data_min_)
print("data_max_is: ",scaler.data_max_)
print("data_range_is: ",scaler.data_range_)

print("after transform : ",scaler.transform(X))
