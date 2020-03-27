import os
import fnmatch
import win32com
from win32com.client import Dispatch


def file2txt(file_path, save_path=''):
    try:
        '''
        功能描述：word、pdf文件转存txt，默认保存在根目录下，支持自定义
        '''
        # 1 切分文件路径为文件目录和文件名
        # os.path.split（）返回文件的路径和文件名
        path, file_name = os.path.split(file_path)
        # print(path,'\n', file_name)
        # 2 修改切分后的文件后缀
        type_name = os.path.splitext(file_name)[-1].lower()#获得文件后缀
        new_name = tran_type(file_name, type_name)
        # 3 设置新的文件保存路径
        file2txt_path = ''
        if save_path == '':
            save_path = path
        else:
            save_path = save_path
        file2txt_path = os.path.join(save_path, new_name)
        print(file2txt_path)
        # 4 加载文本提取的处理程序，word-->txt
        word_app = win32com.client.Dispatch('Word.Application')
        print('----------------')
        print(file_path)
        mytxt = word_app.Documents.Open(file_path)
        # 5 保存文本信息
        mytxt.SaveAs(file2txt_path, 4)# 参数4代表抽取文本
        mytxt.Close()
    except Exception as e:
        print(e)


def tran_type(file_path, ext_type):
    '''
    功能描述：根据文件后缀修改文件名
    参数描述：1 filepath：文件路径  2 ext_type ：文件后缀
    返回参数：new_file_name 返回修改后的新的文件名
    '''
    new_file_name = ''
    if ext_type == '.pdf':
        if fnmatch.fnmatch(file_path, '*.pdf'):
            new_file_name = file_path[:-4]+'.txt'
        else:
            return
    elif ext_type == '.doc' or ext_type == '.docx':
        if fnmatch.fnmatch(file_path, '*.doc'):
            new_file_name = file_path[:-4]+'.txt'
        elif fnmatch.fnmatch(file_path, '*.docx'):
            new_file_name = file_path[:-5] + '.txt'
        else:
            return
    else:
        print('您传入的是【', ext_type, '】文件，本程序只支持doc/docx/pdf格式文件！')
        return
    return new_file_name


# if __name__ == '__main__':
    # os.path.abspath()返回文件的绝对路径
    # word_path = os.path.abspath(r'..\ExtractText\wordfile\张晖晖开题报告-修改稿.doc')
    # pdf_path = os.path.abspath(r'C:\Users\huihuiyo\Downloads\基于文本挖掘技术的高血压临床诊疗规律分析研究.pdf')
    # file2txt(word_path)



