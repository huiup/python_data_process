import os
import fnmatch
import win32com
from win32com.client import Dispatch
'''
功能描述：word文件转存txt，默认保存在根目录下，支持自定义
'''


def word2txt(file_path, save_path=''):
    # 1 切分文件路径为文件目录和文件名
    # os.path.split（）返回文件的路径和文件名
    path, file_name = os.path.split(file_path)
    # print(path,'\n', file_name)
    print(path)
    print(file_name)
    # 2 修改切分后的文件后缀
    new_name = ""
    if fnmatch.fnmatch(file_name, '*.doc'):
        # 保存文件名
        new_name = file_name[:-4]+'.txt'
    elif fnmatch.fnmatch(file_name, "*.docx"):
        new_name = file_name[:-5] + '.txt'
    else:
        print("骚瑞，只支持doc或docx格式文件！")
        # return
    # 3 设置新的文件保存路径
    if save_path == '':
        save_path = path
    else:
        save_path = save_path
    word2txt_path = os.path.join(save_path, new_name)
    print(word2txt_path)
    # 4 加载文本提取的处理程序，word-->txt
    word_app = win32com.client.Dispatch('Word.Application')
    print('----------------')
    print(file_path)
    mytxt = word_app.Documents.Open(file_path)
    # 5 保存文本信息

    mytxt.SaveAs(word2txt_path, 4)# 参数4代表抽取文本
    mytxt.Close()


if __name__ == '__main__':
    # os.path.abspath()返回文件的绝对路径
    fpath = os.path.abspath(r'/wordfile/张晖晖开题报告-修改稿.doc')
    word2txt(fpath)


