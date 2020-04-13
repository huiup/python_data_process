# coding:utf8

from Stop_word import read_file,seg_doc
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
"""
利用sklearn计算tfidf值特征
"""
# 利用sklearn计算tfidf值特征
def sklearn_tfidf_feature(corpus=None):
    # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer() # 构建词汇表
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  
    word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()  
    # print(tfidf)# (0, 139) 0.06350006350009527 0表示列表中读取的第一个文本内容，139表示特征词的所在位置的序号，最后是其频率
    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):  
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])

if __name__ == "__main__":
    corpus = []
    path = r"D:\BaiduNetdiskDownload\CSCMNews\教育\284461.txt"
    str_doc = read_file(path)
    word_list1 = ' '.join(seg_doc(str_doc))

    path = r"D:\BaiduNetdiskDownload\CSCMNews\时政\339764.txt"
    str_doc = read_file(path)
    word_list2 = ' '.join(seg_doc(str_doc))
    # print(word_list)
    corpus.append(word_list1)
    corpus.append(word_list2)
    # print(corpus)
    sklearn_tfidf_feature(corpus)