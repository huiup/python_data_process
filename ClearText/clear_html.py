import re

'''
清洗html文本中的htnl标签、特殊符号
re.I   使匹配对大小写不敏感
re.L   做本地化识别（locale-aware）匹配
re.M   多行匹配，影响^(开头)和$(结尾)
re.S   使.匹配包含换行在内的所有字符
re.U   根据Unicode字符集解析字符，这个标志影响 \w, \W, \b, \B
re.X   该标志通过给予你更灵活的格式以便你将正则表达式写得更加容易
'''

# 过滤html标签
def filter_tags(html_str):
    # 过滤DOCTYPE
    html_str = ' '.join(html_str.split())#去掉多余的空格
    re_doctype = re.compile(r'<!DOCTYPE .*?> ', re.S)
    s = re_doctype.sub('',html_str)

    # 过滤CDATA
    re_cdata = re.compile('//<!CDATA\[[ >]∗ //\] > ', re.I)
    s = re_cdata.sub('', s)

    # 过滤Script
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    s = re_script.sub('', s)  # 去掉SCRIPT

    # style
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    s = re_style.sub('', s)  # 去掉style

    # 处理换行
    re_br = re.compile('<br\s*?/?>')
    s = re_br.sub('', s)     # 将br转换为换行

    # HTML标签
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('', s)  # 去掉HTML 标签

    # HTML注释
    re_comment = re.compile('<!--[^>]*-->')
    s = re_comment.sub('', s)

    # 多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('', s)

    blank_line_l = re.compile('\n')
    s = blank_line_l.sub('', s)

    blank_kon = re.compile('\t')
    s = blank_kon.sub('', s)

    blank_one = re.compile('\r\n')
    s = blank_one.sub('', s)

    blank_two = re.compile('\r')
    s = blank_two.sub('', s)

    blank_three = re.compile(' ')
    s = blank_three.sub('', s)

    # 剔除超链接
    http_link = re.compile(r'(http://.+.html)')
    s = http_link.sub('', s)
    return s



def read_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        text_str = f.read()
    return text_str

if __name__ == "__main__":
    path = r'.\ClearText\htmlDemo.txt'
    res = read_file(path)
    res = filter_tags(res)
    print(res)