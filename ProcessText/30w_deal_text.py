# coding:utf8
import os,re,time,jieba
# 这里是对前面知识点的应用，为了方便就不进行导方法包
"""
30万条新闻文本数据清洗
"""
class loadFolders(object):   # 迭代器
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path, file)
            if os.path.isdir(file_abspath): # if file is a folder
                yield file_abspath

class loadFiles(object):
    def __init__(self, par_path):
        self.par_path = par_path
    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:              # level directory
            catg = folder.split(os.sep)[-1]
            for file in os.listdir(folder):     # secondary directory
                file_path = os.path.join(folder, file)
                # 文件具体操作
                if os.path.isfile(file_path):
                    # this_file = open(file_path, 'rb') #rb读取方式更快
                    # content = this_file.read().decode('utf8')
                    # yield catg, content
                    # this_file.close()

                    with open(file_path,'r',encoding='utf-8') as f:
                        content = f.read()
                        yield catg, content

# 利用jieba对文本进行分词，返回切词后的list
def seg_doc(str_doc):
    # 1 正则处理原文本
    sent_list = str_doc.split('\n')
    # map内置高阶函数:一个函数f和list，函数f依次作用在list.
    sent_list = map(test_parse, sent_list)  # 正则处理，去掉一些字符，例如\u3000
    # 2 获取停用词
    stwlist = get_stop_words()
    # 3 分词并去除停用词
    word_2dlist = [rm_tokens(jieba.cut(part, cut_all=False),stwlist) for part in sent_list]
    # 4 合并列表
    word_list = sum(word_2dlist, [])
    return word_list

# 正则对字符串进行清洗
def test_parse(str_doc):
    # 正则过滤掉特殊符号、标点、英文、数字等。
    # r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    # str_doc=re.sub(r1, ' ', str_doc)
    # 去掉字符(\u3000:中文空格)
    str_doc = re.sub('\u3000', '', str_doc)
    # 去除空格等
    str_doc=re.sub('\s+', ' ', str_doc)
    # 去除换行符
    str_doc = str_doc.replace('\n',' ')
    return str_doc

# 创建停用词列表
def get_stop_words(path=r'../DATAPROCESS/dataSet/StopWord/NLPIR_stopwords.txt'):
    file = open(path, 'r',encoding='utf-8').read().split('\n')
    return set(file)# set去重

# 去掉一些停用词和数字
def rm_tokens(words,stwlist):
    words_list = list(words)
    stop_words = stwlist
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words: # 去除停用词
            words_list.pop(i)
        elif words_list[i].isdigit(): # 去除数字
            words_list.pop(i)
        elif len(words_list[i]) == 1:  # 去除单个字符
            words_list.pop(i)
        elif words_list[i] == " ":  # 去除空字符
            words_list.pop(i)
    return words_list



if __name__ == "__main__":
    start_time = time.time()
    file_path = os.path.abspath(r'D:\BaiduNetdiskDownload\CSCMNews')
    files = loadFiles(file_path)
    n = 3  # n 表示抽样率， n抽1
    for i, msg in enumerate(files):
        if i % n == 0:
            catg = msg[0]
            file = msg[1]
            file = seg_doc(file)
            if int(i/n) % 1000 == 0:
                print('{t} *** {i} \t docs has been dealed'
                      .format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())),'\n',catg,':\t',file[:30])
    end_time = time.time()
    print('total spent times:%.2f' % (end_time-start_time)+ ' s')
