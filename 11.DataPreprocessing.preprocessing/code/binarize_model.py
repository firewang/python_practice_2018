# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/29 11:48
# @Author  :  wanghuodong  
# @note    : 

from sklearn.preprocessing import Binarizer
import pprint
X = [ [1,2,3,4,5] ,
      [5,4,3,2,1],
      [3,3,3,3,3],
      [1,1,1,1,1]
      ]
print("{:#^50}".format("Before transform"),X)
binarizer = Binarizer(threshold=2.5)
# print("{:#^50}".format("After transform"),binarizer.transform(X))
print("{:#^50}".format("After transform"))
print(binarizer.transform(X))


