# coding:utf8
import jieba.posseg as ps
"""
自定义提取特征词
人名、地名、机构名等命名实体识别，统称为实体特征提取
"""

# 不同业务场景:评论情感判断，可以自定义特征抽取规则.
def extract_feature_words(str_doc):
    featWord =""
    stwlist = get_stop_words()
    user_pos_list = [ 'nr', 'ns','nt','nz']  # 用户自定义特征词性列表
    for word, pos in ps.cut(str_doc):
        # 过滤掉停用词
        if word not in stwlist and pos in user_pos_list:
            if word+' '+pos+'\n' not in featWord:
                featWord += word+' '+pos+'\n'
    print(featWord)


# 创建停用词列表
def get_stop_words(path=r'../DATAPROCESS/dataSet/StopWord/NLPIR_stopwords.txt'):
    file = open(path, 'r',encoding='utf-8').read().split('\n')
    return set(file)# set去重


# 读取文本信息
def read_file(path):
    str_doc = ''
    with open(path,'r',encoding='utf-8') as f:
        str_doc = f.read()
    return str_doc


if __name__=='__main__':
    # 1 读取文本
    path= r'D:\BaiduNetdiskDownload\CSCMNews\教育\284461.txt'
    str_doc = read_file(path)
    # 2 分词去停用词
    extract_feature_words(str_doc)