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
def load_DataSet(file_name, delim='\t'):
    fr = open(file_name)
    string_arr = [line.strip().split(delim) for line in fr.readlines()]
    # print(stringArr) # 二维数组
    data_arr = [list(map(float, line)) for line in string_arr]
    # print(data_arr)
    # mat():将数组转换为矩阵,才可以进行一些线性代数的操作
    # [52603.0, 3.574737, 0.075163, 1.0]将会转换为如下形式：科学记数法
    # [5.2603000e+04 3.5747370e+00 7.5163000e-02 1.0000000e+00]
    return mat(data_arr)

""" 
mean()函数功能：求取均值
经常操作的参数为axis，以m * n矩阵举例：
axis 不设置值，对 m*n 个数求均值，返回一个实数
axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵 
"""
'''将NaN替换成平均值函数'''
def replace_Nan_With_Mean(data_mat):
    num_feat = shape(data_mat)# (143,4)读取矩阵的维度
    # print(numFeat[1]-1)  # 特征数3
    for i in range(num_feat[1]-1):
        # 对value不为NaN的求均值，.A 将矩阵转化为数组
        # numpy.nonzero是用来返回一个多维数组中不为0的元素的下标
        # print(nonzero(~isnan(data_mat[:, i].A))[0])# 其中[:, i]意思为第i列所有行的元素
        # print(data_mat[nonzero(~isnan(data_mat[:, i].A))[0],i]) # 列特征非nan数据
        mean_val = mean(data_mat[nonzero(~isnan(data_mat[:, i].A))[0], i])# 取列特征非nan数据平均值
        # 将value为NaN的值赋值为均值
        # print(mean_val)
        # 33302.211267605635
        # 6.564913424460432
        # 0.8228272553191489
        data_mat[nonzero(isnan(data_mat[:, i].A))[0],i] = mean_val
    return data_mat


if __name__=='__main__':
    # 加载数据集
    res = load_DataSet(r'DataSet\files\dataset.data','    ')
    # print(res)
    # 均值填补缺失值
    data_mat = replace_Nan_With_Mean(res)
    print(data_mat)

