# coding:utf8
from numpy import *
import numpy as np

'''
词集模型（Set of Words，简称SoW）：单词构成的集合，每个单词只出现一次。和词袋模型唯一的不同是它仅仅考虑词是否在文本中出现，而不考虑词频。也就是一个词在文本在文本中出现1次和多次特征处理是一样的。
'''

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

'''
特征词转特征向量：词集模型
词集模型构建数据矩阵
遍历文档中的所有单词，如果出现了词汇表中的单词，则将输出的文档向量中的对应值设为1
vocab_List:词汇的集合
data_list:数据文档
'''
def setOfWords2Vec(vocab_List, data_list):
    # 1 所有文档的词向量
    vec_list = []
    for decument in data_list:
        # print('-->',decument) # 每个文档
        # 2 创建一个和词汇表等长的向量，并将其元素都设置为0
        return_vec = [0] * len(vocab_List)
        # 如果单词在词汇表则修正1
        for word in decument:
            if word in vocab_List:
                return_vec[vocab_List.index(word)] = 1
        # 追加所有文档词向量列表
        vec_list.append(return_vec)
    return vec_list

if __name__ == "__main__":
    # 1 打印数据集和标签
    data_list,classlab = load_DataSet()
    # print('数据列表:\n',mat(data_list),'\n标签集:\n',classlab)

    # 2 获取所有单词的集合
    vocab_List=create_vocab_List(data_list)
    # print('\n词汇列表：\n',vocab_List)

    #***********特征词转向量*********************
    # 3 词集模型:文本向量转化
    set_vec = setOfWords2Vec(vocab_List, data_list)
    print('词集模型:\n',mat(set_vec))

