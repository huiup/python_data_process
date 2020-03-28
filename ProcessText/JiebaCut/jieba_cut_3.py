import jieba
import jieba.posseg
import jieba.analyse
'''
extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
sentence 为待提取的文本
topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
withWeight 为是否一并返回关键词权重值，默认值为 False
allowPOS 仅包括指定词性的词，默认值为空，即不筛选
jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件
'''
print('='*60)
print('1. 关键词提取')
print('-'*60)
print(' TF-IDF')
print('-'*60)


s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.extract_tags(s,10, withWeight=True):
    print('%s %s' % (x, w))

print('-'*60)
print('2.TextRank(文本排名)')
print('-'*60)


# textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 直接使用，接口相同，注意默认过滤词性。
# 文本排名，按权重排名
for x, w in jieba.analyse.textrank(s, 10,withWeight=True):
    print('%s %s' % (x, w))

print('='*60)
print('3. 词性标注')
print('-'*60)

words = jieba.posseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))
# 我 r
# 爱 v
# 北京 ns
# 天安门 ns
print('='*60)
print('4. Tokenize: 返回词语在原文的起止位置')
print('-'*60)
print(' 默认模式')
print('-'*60)

result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
# word 永和                start: 0                end:2
# word 服装                start: 2                end:4
# word 饰品                start: 4                end:6
# word 有限公司            start: 6                end:10
print('-'*60)
print(' 搜索模式(使分词粒度更细)')
print('-'*60)

result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
# word 永和                start: 0                end:2
# word 服装                start: 2                end:4
# word 饰品                start: 4                end:6
# word 有限                start: 6                end:8
# word 公司                start: 8                end:10
# word 有限公司            start: 6                end:10