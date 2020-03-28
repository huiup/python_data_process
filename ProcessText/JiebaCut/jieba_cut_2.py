import jieba

print('='*60)
print('2. 添加自定义词典/调整词典')
print('-'*60)
# 简单方法调整：suggest_freq(segment, tune=True) 可调节单个词语的词频，使其（或不能）被分出来
print('把合并的拆分：')
print('原文档：\t'+'/'.join(jieba.cut('如果放到数据库中将出错。', HMM=False)))
#如果/放到/数据库/中将/出错/。
jieba.suggest_freq(('中', '将'), True)
print('改进文档：\t'+'/'.join(jieba.cut('如果放到数据库中将出错。', HMM=False)))
#如果/放到/数据库/中/将/出错/。

print('把会拆分的合并：')
print('原文档：\t'+'/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
#「/台/中/」/正确/应该/不会/被/切开
jieba.suggest_freq('台中', True)
print('改进文档：\t'+'/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
#「/台中/」/正确/应该/不会/被/切开

# 使用自定义分词词典
seg_list1 = jieba.cut("今天很高兴在慕课网和大家交流学习")
print('不加载自定义分词词典：\n'+"/ ".join(seg_list1))
# 今天/ 很/ 高兴/ 在/ 慕课/ 网/ 和/ 大家/ 交流学习
# 加载自定义分词词典
seg_list2 = jieba.cut("今天很高兴在慕课网和大家交流学习")
jieba.load_userdict("../DATAPROCESS/DataSet/StopWord/user_dict.txt") 
print('加载自定义分词词典：\n'+"/ ".join(seg_list2))
# 今天/ 很高兴/ 在/ 慕课网/ 和/ 大家/ 交流学习
""" 
词典内容为：
慕课网 3 n
很高兴 vd
 """