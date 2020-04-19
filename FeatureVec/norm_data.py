# coding:utf8
"""
不均衡的数据归一化处理方法
"""

from numpy import *
from loss_val_numpy import *

    
'''
数值归一化：特征值转化为0-1之间：
new_Value = (old_Value-min)/(max-min)
'''
def norm_dataset(dataset):
    # min/max:参数0是取得列中的最小值，而不是行中最小值
    min_Val = dataset.min(0)# [[0.       0.       0.007509]] 因为数据中有0
    max_Val = dataset.max(0)# [[7.7826000e+04 1.4305636e+01 1.6946410e+00]]
    ranges = max_Val - min_Val

    norm_dataset = zeros(shape(dataset)) # 生成原矩阵一样大小的0矩阵
    m = dataset.shape[0]# 得到多少行

    molecular = dataset - tile(min_Val,(m,1))  # 分子： (oldValue-min)
    Denominator = tile(ranges,(m,1))           # 分母：(max-min)
    norm_data_set = molecular / Denominator     # 归一化结果。

    print('归一化的数据结果：\n'+str(norm_data_set))
    return norm_data_set,ranges,min_Val

if __name__ == "__main__":

    res = load_DataSet(r'DataSet\files\dataset.data','    ')
    data_mat = replace_Nan_With_Mean(res)
    norm_dataset(data_mat[:,:-1])# :-1 表示取除了最后一列的所有列