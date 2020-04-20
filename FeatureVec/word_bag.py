# coding:utf8
from numpy import *
import numpy as np

""" 
词袋模型(Bag of Words，简称BoW)，即将所有词语装进一个袋子里，不考虑其词法和语序的问题，即每个词语都是独立的，把每一个单词都进行统计，同时计算每个单词出现的次数。
"""
# 加载数据
# 加载数据
def load_DataSet():
    # corpus参数样例数据如下：
    corpus =[]
    tiyu = ['姚明', '我来', '承担', '连败', '巨人', '宣言', '酷似', '当年', '麦蒂', '新浪', '体育讯', '北京', '时间', '消息', '休斯敦', '纪事报', '专栏', '记者', '乔纳森', '费根', '报道', '姚明', '渴望', '一场', '胜利', '当年', '队友', '麦蒂', '惯用', '句式']
    yule = ['谢婷婷', '模特', '酬劳', '仅够', '生活', '风光', '背后', '惨遭', '拖薪', '新浪', '娱乐', '金融', '海啸', 'blog', '席卷', '全球', '模特儿', '酬劳', '被迫', '打折', '全职', 'Model', '谢婷婷', '业界', '工作量', '有增无减', '收入', '仅够', '糊口', '拖薪']
    jiaoyu = ['名师', '解读', '四六级', '阅读', '真题', '技巧', '考前', '复习', '重点', '历年', '真题', '阅读', '听力', '完形', '提升', '空间', '天中', '题为', '主导', '考过', '六级', '四级', '题为', '主导', '真题', '告诉', '方向', '会考', '题材', '包括']
    shizheng = ['美国', '军舰', '抵达', '越南', '联合', '军演', '中新社', '北京', '日电', '杨刚', '美国', '海军', '第七', '舰队', '三艘', '军舰', '抵达', '越南', '岘港', '为期', '七天', '美越', '南海', '联合', '军事训练', '拉开序幕', '美国', '海军', '官方网站', '消息']

    corpus.append(tiyu)
    corpus.append(yule)
    corpus.append(jiaoyu)
    corpus.append(shizheng)

    classVec = ['体育','娱乐','教育','时政']
    return  corpus,classVec

# 获取所有单词的集合:
# 返回不含重复元素的单词列表
def create_vocab_List(data_list):
    vocab_set = set([])
    # 操作符 | 用于求两个集合的并集
    for document in data_list:
        vocab_set = vocab_set | set(document)  
    # print(vocabSet)
    return list(vocab_set)

'''词袋模型构建数据矩阵'''
def bagOfWords2VecMN(vocab_List, data_list):
    # 1 所有文档的词向量
    vec_list = []
    for decument in data_list:
        # print('-->',decument)
        return_vec = [0] * len(vocab_List)
        for word in decument:
            if word in vocab_List:
                return_vec[vocab_List.index(word)] += 1
        vec_list.append(return_vec)
    return vec_list

'''
词袋模型转化为tf-idf计算
https://www.cnblogs.com/cppb/p/5976266.html
'''
def TF_IDF(bag_vec):
    # 词频(TF) = 某个词在文章中出现的总次数/文章中出现次数最多的词的个数
    tf = [word/sum(bag_vec) for word in bag_vec]
    # print(mat(tf))
    # 逆文档频率(IDF) = log（词料库的文档总数/包含该词的文档数+1）
    m = len(bag_vec) # 词料库的文档总数 4
    # sum(mat(bag_vec).T!=0,axis=1):计算转置后的每一行的和
    ndw =sum(mat(bag_vec).T!=0,axis=1).T  # 包含该词的文档数
    idf =  [ log(m/(t+1)) for t in ndw]

    tfidf = tf * np.array(idf)
    # 设置保留小数位
    # np.set_printoptions(precision=4)
    # print('tf:\n',mat(tf),'\nndw:\n',ndw,'\nidf:\n',idf,'\ntfidf:\n',tfidf)
    return tfidf

if __name__ == "__main__":
    # 1 打印数据集和标签
    data_list,classlab = load_DataSet()
    # print('数据列表:\n',mat(data_list),'\n标签集:\n',classlab)

    # 2 获取所有单词的集合
    vocab_List=create_vocab_List(data_list)
    # print('\n词汇列表：\n',vocab_List)

    #***********特征词转向量*********************
    # 3 词袋模型:文本向量转化
    bag_vec = bagOfWords2VecMN(vocab_List, data_list)
    # print('词袋模型:\n',mat(bag_vec))

    # 4 tf-idf计算
    tfidf = TF_IDF(bag_vec)
    print('tf-idf:\n ',tfidf)