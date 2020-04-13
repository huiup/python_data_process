# coding:utf8
from nltk import *
# 从Stop_word.py中导入要用到的方法
from Stop_word import read_file,seg_doc
import matplotlib
"""
NLTK词频统计
"""

# 解决中文显示
# (1)查看当前使用字体格式
# from matplotlib.font_manager import findfont, FontProperties
# print(findfont(FontProperties(family=FontProperties().get_family())))
# (2)在C:\Windows\Fonts查找中文字体SimHei.ttf，并将其复制到包管理工具matplotlib\mpl-data\fonts\ttf\文件夹下面
# (3)设置使用字体 
# 因其默认使用的字体不支持中文，得自己添加支持中文的字体
matplotlib.rcParams['font.sans-serif'] = 'SimHei'
#用来正常显示图片负号
matplotlib.rcParams['axes.unicode_minus'] = False



# 利用nltk进行词频特征统计
def nltk_wf_feature(word_list=None):
    # ********统计词频方法1**************
    fdist=FreqDist(word_list)
    # print(fdist.items())
    # # print(fdist.keys(),fdist.values())
    # # for key in fdist:
    # #     print('{',key, fdist[key],'}')
    # print('='*3,'指定词语词频统计','='*3)
    # w='留学人员'
    # print(w,'出现频率：',fdist.freq(w)) # 给定样本的频率
    # print(w,'出现次数：',fdist[w]) # 出现次数

    # print('='*3,'频率分布表','='*3)
    # # 该方法接受一个数字n作为参数，会以表格的方式打印出现次数最多的前n项
    # fdist.tabulate(10) # 频率分布表

    print('='*3,'可视化词频','='*3)
    fdist.plot(30) # 频率分布图
    fdist.plot(30,cumulative=True) # 频率累计图

    # print('='*3,'根据词语长度查找词语','='*3)
    # wlist =[w for w in fdist if len(w)>2]
    # print(wlist)

    # ********统计词频方法2**************
    # from collections import Counter
    # Words = Counter(word_list)
    # print(Words.keys(),Words.values())
    # wlist =[w for w in Words if len(w)>2]
    # print(wlist)

    return fdist

if __name__ == "__main__":
    # 读取文本
    path = r"D:\BaiduNetdiskDownload\CSCMNews\教育\284461.txt"
    str_doc = read_file(path)
    # 词频特征统计
    word_list = seg_doc(str_doc)
    nltk_wf_feature(word_list)
    # print(word_list)
    