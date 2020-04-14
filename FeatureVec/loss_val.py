# coding:utf8

import numpy
from numpy import *
"""
处理数据缺失值
"""

"""
处理数据缺失值
使用可用特征的均值来填补缺失值
使用特殊值来填补缺失值如-1，0
忽略有缺失值的样本
使用相似样本的均值填补缺失值
使用机器学习算法预测缺失值 
"""


'''加载数据集'''
def load_DataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    # print(stringArr) # 二维数组
    datArr = [list(map(float, line)) for line in stringArr]
    # print(datArr)
    # mat()转换为矩阵,才可以进行一些线性代数的操作
    # [52603.0, 3.574737, 0.075163, 1.0]将会转换为如下形式：科学记数法
    # [5.2603000e+04 3.5747370e+00 7.5163000e-02 1.0000000e+00]
    return mat(datArr)


'''将NaN替换成平均值函数'''
def replace_Nan_With_Mean(data_mat):
    num_feat = shape(data_mat)# (143,4)读取矩阵的维度
    # print(numFeat[1]-1)  # 特征数3
    for i in range(num_feat[1]-1):
        # 对value不为NaN的求均值，.A 将矩阵转化为数组
        # print(nonzero(~isnan(data_mat[:, i].A))[0])# numpy.nonzero是用来返回一个多维数组中不为0的元素的下标
        # print(data_mat[nonzero(~isnan(data_mat[:, i].A))[0],i]) # 列特征非nan数据
        mean_val = mean(data_mat[nonzero(~isnan(data_mat[:, i].A))[0], i])
        # 将value为NaN的值赋值为均值
        data_mat[nonzero(isnan(data_mat[:, i].A))[0],i] = mean_val
    return data_mat


if __name__=='__main__':
    # 加载数据集
    res = load_DataSet(r'DataSet\files\dataset.data','    ')
    # print(res)
    res2 = replace_Nan_With_Mean(res)
    print(res2)
    # 均值填补缺失值
    # datMat = replace_Nan_With_Mean()
    # print(datMat)




#************3 Pandas 处理丢失值*******************
# 机器学习和数据挖掘等领域由于数据缺失导致的数据质量差，
# 在模型预测的准确性上面临着严重的问题。

# import pandas as pd
# import numpy as np

# datMat = load_DataSet(r'DataSet\files\dataset.data','    ')
# df = pd.DataFrame(datMat)
# # df = pd.DataFrame(datMat, index=range(datMat.shape[0]),columns=['one', 'two', 'three', 'four'] )
# # 使用重构索引(reindexing)，创建了一个缺少值的DataFrame。 输出中，NaN表示不是数字的值
# df = df.reindex(range(datMat.shape[0]+5))

# # 1 重构矩阵
# # print (df)    # 打印矩阵

# # 2 检查是否为空
# # print (df.isnull())
# # print (df['one'].notnull()) # 检查第一列是否为空

# # 3 均值填充法：NAN视为0.若数据是 NAN和是 NAN

# # lossVs = [df[col].mean() for col in range(datMat.shape[1])] # 计算特征列均值
# # print(lossVs)
# # lists= [ list(df[i].fillna(lossVs[i])) for i in range(len(lossVs)) ]
# # print(mat(lists).T)

# # lists.append(list(df[0].fillna(lossVs[0])))
# # lists.append(list(df[1].fillna(lossVs[1])))
# # lists.append(list(df[2].fillna(lossVs[2])))
# # lists.append(list(df[3].fillna(lossVs[3])))


# # 4 其他缺失值处理方法
# # 4.1 用标量值替换NaN
# # print ("NaN replaced with '0':")
# # print (df.fillna(0))

# # 4.2 前进和后退:pad/fill 和 bfill/backfill
# # print (df.fillna(method='pad'))
# # print (df.fillna(method='backfill'))

# # 4.3 丢失缺少的值：axis=0在行上应用，axis=1在列上应用
# # print (df.dropna(axis=0))

# # 4.4 忽略无效值
# # print("df.dropna():\n{}\n".format(df.dropna()))