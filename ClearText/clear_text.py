import re

'''
正则清洗文本数据
'''

# 读取文本内容
def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        text_str = f.read()
    return text_str

# 正则对字符串清洗
def text_parse(str_doc):
    # 正则过滤掉特殊符号、标点、英文、数字等。
    r1 = '[a-zA-Z0-9’!"#$%&\'()*+,-./:：;；|<=>?@，—。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    # 去除空格
    r2 = '\s+'
    str_doc=re.sub(r1, ' ', str_doc)
    # 多个空格成1个
    str_doc=re.sub(r2, ' ', str_doc)
    # 去除换行符
    # str_doc = str_doc.replace('\n',' ')
    return str_doc


if __name__ == "__main__":
    path = r"D:\BaiduNetdiskDownload\CSCMNews\财经\798979.txt"
    text = read_file(path)
    text = text_parse(text)
    print(text)