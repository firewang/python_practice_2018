# -*- encoding: utf-8 -*-
# @Version : 1.0  
# @Time    : 2019/11/25 14:01
# @Author  : whd
# @note    : 最小编辑距离（莱文斯坦（Levenshtein）距离）：两不等长字符串相似度距离

import numpy as np


def distance_str(str1, str2):
    """莱文斯坦（Levenshtein）距离, 实现方式2"""
    dp = np.zeros((len(str1) + 1, len(str2) + 1))
    m = len(str1)
    n = len(str2)
    for k in range(1, m + 1):
        dp[k][0] = k
    for k in range(1, n + 1):
        dp[0][k] = k
    for k in range(1, m + 1):
        for j in range(1, n + 1):
            dp[k][j] = min(dp[k - 1][j], dp[k][j - 1]) + 1  # 这里表示上边和下边的数值最小数值
            if str1[k - 1] == str2[j - 1]:
                dp[k][j] = min(dp[k][j], dp[k - 1][j - 1])
            else:
                dp[k][j] = min(dp[k][j], dp[k - 1][j - 1] + 1)
    print(dp)
    print(dp[-1][-1])


def normal_Levenshtein_distance(str1, str2):
    """莱文斯坦（Levenshtein）距离: 不等长或者等长字符串之间距离
    https://www.jianshu.com/p/9a53f32cf62b
    """
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    # create matrix
    matrix = [0 for n in range(len_str1 * len_str2)]
    # init x axis
    for i in range(len_str1):
        matrix[i] = i
    # init y axis
    for j in range(0, len(matrix), len_str1):
        if j % len_str1 == 0:
            matrix[j] = j // len_str1

    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[j * len_str1 + i] = min(matrix[(j - 1) * len_str1 + i] + 1,
                                           matrix[j * len_str1 + (i - 1)] + 1,
                                           matrix[(j - 1) * len_str1 + (i - 1)] + cost)
    print(matrix)
    print(matrix[-1])
    return matrix[-1]


if __name__ == '__main__':
    distance_str("kitten", "sitting")
    normal_Levenshtein_distance("kitten", "sitting")
