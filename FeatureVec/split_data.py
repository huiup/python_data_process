# coding:utf8
import os
from numpy import *
"""
解析数据文件，返回特征集和标签集
"""
'''
特征数据集：
特征1：年均投入时间（min）
特征2：玩游戏占时间百分比
特征3：每天看综艺的时间（h）
标签集：
1：学习专注
2：学习正常
3：比较贪玩
munpy中的zeros(全0)和ones(全1)方法：
B=zeros(n)：生成n个元素的数组(ndarray)。
B=zeros((m,n))：生成m×n数组。
B=zeros([m n])：生成m×n数组。
B=zeros((d1,d2,d3……))：生成d1×d2×d3×……全零数组。
B=zeros([d1 d2 d3……])：生成d1×d2×d3×……全零数组。
B=zeros(size(A))：生成与矩阵A相同大小的全零数组。
ones与上类似
'''

def file_matrix(filename):
    f = open(filename)
    arrayLines = f.readlines()
    # zeros生成0矩阵
    returnMat = zeros((len(arrayLines),3))   # 特征数据集
    classLabelVactor = []                   # 标签集
    index = 0
    for line in arrayLines:
        listFromLine = line.strip().split('\t')    # 分析数据，空格处理
        # 数据格式为：40920	8.326976	0.953952	3
        returnMat[index,:] = listFromLine[0:3]# 取前三列
        classLabelVactor.append(int(listFromLine[-1]))# 取标签
        index +=1
    return returnMat,classLabelVactor

if __name__=='__main__':
    path = os.path.abspath(r'DataSet\files\dataset.txt')
    returnMat,classLabelVactor=file_matrix(path)
    print('数据集:\n',returnMat,'\n标签集:\n',classLabelVactor)