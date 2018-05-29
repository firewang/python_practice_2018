# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2018/5/29 13:41
# @Author  :  wanghuodong  
# @note    : 

from sklearn.preprocessing import OneHotEncoder

X = [ [1,2,3,4,5] ,
      [5,4,3,2,1],
      [3,3,3,3,3],
      [1,1,1,1,1]
      ]
print("{:#^50}".format("Before transform"),'\n', X)
print()
encoder = OneHotEncoder(sparse=False)
encoder.fit(X)
print("{name:>18}:{value:}".format(name="active_features_" , value = str(encoder.active_features_)))
print("{name:>18}:{value:}".format(name="feature_indices_" , value = str(encoder.feature_indices_)))
print("{name:>18}:{value:}".format(name="n_values_" , value = str(encoder.n_values_)))
print("{name:>11}:{value:}".format(name="热编码实际总长" , value = sum(encoder.n_values_)))
print("{name:>11}:{value:}".format(name="激活热编码总长" , value = len(encoder.active_features_)))

print("{:#^50}".format("After transform"),'\n', encoder.transform([[1,2,3,4,5]]))