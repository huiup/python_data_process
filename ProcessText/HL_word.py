# coding:utf8

from Stop_word import *
from Word_freq import *

"""
自定义去高低词频
"""
# 选择高低词
def freq_word(fdist):
    wordlist =[]
    print('='*3,'打印统计的词频','='*3)
    for key in fdist.keys():
        # 选取词频大于2小于15的词
        if fdist.get(key)>2 and fdist.get(key)<15:
            wordlist.append(key+':'+str(fdist.get(key)))
    return wordlist

if __name__ == "__main__":
    # 读取文本
    path = r"D:\BaiduNetdiskDownload\CSCMNews\教育\284461.txt"
    str_doc = read_file(path)
    word_list = seg_doc(str_doc)
    # print(word_list)
    # 2 选择高低词
    fdist = nltk_wf_feature(word_list)
    wordlist=freq_word(fdist)
    print(wordlist)