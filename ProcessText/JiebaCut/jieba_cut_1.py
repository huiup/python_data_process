#coding:utf8

"""
jieba分词操作详解
"""

import jieba,os,sys



'''
支持三种分词模式与特点：
    精确模式:试图将句子最精确地切开，适合文本分析；
    全模式:把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
    搜索引擎模式:在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
    支持繁体分词
    支持自定义词典
安装方法：
    自动安装： pip install jieba
    半自动安装：下载 http://pypi.python.org/pypi/jieba/解压后运行 python setup.py install
    手动安装：将 jieba 目录放置于当前目录或者 site-packages 目录,
    通过 import jieba 来引用
核心算法：
    基于前缀词典实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图 (DAG)
    采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合
    对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法
主要功能：
    jieba.cut 三个输入参数: 待分词的字符串；cut_all参数是否全模式；HMM 参数是否 HMM 模型(隐马尔可夫模型)
    jieba.cut_for_search 两个参数：待分词的字符串；是否 HMM 模型。该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
    jieba.cut 以及 jieba.cut_for_search 返回的是一个生产器
    jieba.lcut 以及 jieba.lcut_for_search 返回 一个list
    jieba.Tokenizer(dictionary=DEFAULT_DICT) 新建自定义分词器，可用于同时使用不同词典。jieba.dt 为默认分词器。
'''
#********************1 结巴中文分词基本操作***********************************

print('='*60)
print('1. 分词')
print('-'*60)

# 1 全模式，扫描所有可以成词的词语, 速度非常快，但不能解决歧义.
seg_list = jieba.cut("我来到了北京清华大学", cut_all=True)
print("\nFull Mode(全模式): " + "/ ".join(seg_list))

# 2 默认是精确模式，适合文本分析.
seg_list = jieba.cut("我来到了北京清华大学", cut_all=False)
print("\nDefault Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了北京清华大学")
print('\n默认切词：'+"/ ".join(seg_list))# 默认模式

# 3 搜索引擎模式,对长词再次切分，提高召回率，适合用于搜索引擎分词。
#jieba.cut_for_search 该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造",HMM=False)
print('\n搜索引擎模式：'+", ".join(seg_list))
print(type(seg_list))# <class 'generator'>
