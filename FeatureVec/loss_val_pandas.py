# coding:utf8
import time
import pandas as pd
import numpy as np
from numpy import *
""" 
************3 Pandas 处理丢失值*******************
机器学习和数据挖掘等领域由于数据缺失导致的数据质量差，
在模型预测的准确性上面临着严重的问题。 
"""
""" 
DataFrame.fillna()函数
method:pad/ffill：用前一个非缺失值去填充该缺失值,用左边的非缺失值去填充该缺失值
backfill/bfill：用下一个非缺失值填充该缺失值,用右边的非缺失值去填充该缺失值
None：指定一个值去替换缺失值（默认这种方式)
limit参数：限制填充个数
axis参数：修改填充方向,默认为纵向填充,axis=1的时候,横向填充 
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


data_mat = load_DataSet(r'DataSet\files\dataset.data','    ')
# DataFrame是一种表格型数据结构,DataFrame的行索引是index，列索引是columns，我们可以在创建DataFrame时指定索引的值
df = pd.DataFrame(data_mat)
# df = pd.DataFrame(data_mat, index=range(data_mat.shape[0]),columns=['one', 'two', 'three', 'four'] )
# 1 重构矩阵
# 使用重构索引(reindex)，创建了一个缺少值的DataFrame。 用NaN填充
df = df.reindex(range(data_mat.shape[0]+5))# 多添加5行
# print (df)

# 2 检查是否为空
# print (df.isnull())
# print (df['one'].notnull()) # 检查第一列是否为空

# 3 均值填充法：NAN视为0.若数据是 NAN和是 NAN
# 计算特征列各列的均值
# mean_val = [df[col].mean() for col in range(data_mat.shape[1])] 
# lists= [ df[i].fillna(mean_val[i]) for i in range(len(mean_val)) ]
# print(mat(lists).T)# .T转置


# 4 其他缺失值处理方法
# 4.1 用标量值替换NaN
# print ("NaN replaced with '0':")
# print (df.fillna(NaN))

# 4.2 前进和后退:pad/fill 和 bfill/backfill
# print (df.fillna(method='pad'))
# print (df.fillna(method='backfill'))

# 4.3 丢失缺少的值：axis=0在行上应用(去掉有nan的行)，axis=1在列上应用(去掉有nan的列)
# print (df.dropna(axis=0))#  默认为axis=0

# 4.4 忽略无效值
# df.dropna(how = 'all')    # 传入这个参数后将只丢弃全为缺失值的那些行
# df.dropna(axis = 1)       # 丢弃有缺失值的列（一般不会这么做，这样会删掉一个特征）
# df.dropna(axis=1,how="all")   # 丢弃全为缺失值的那些列
# df.dropna(axis=0,subset = [0, 1, 2])   # 丢弃0,1和2这三列中有缺失值的行
# print("df.dropna():\n{}\n".format(df.dropna()))
