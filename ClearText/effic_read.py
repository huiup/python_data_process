import os,time

""" 
高效读取30万条新闻文本
"""
# os.sep：根据你所处的环境，自动采用相应的分隔符号('\','/')
class Load_folders(object):
    def __init__(self,path):
        self.path = path
    def __iter__(self):
        for file in os.listdir(self.path):
            file_abspath = os.path.join(self.path,file)
            if os.path.isdir(file_abspath):
                yield file_abspath # return 
        

class Load_files(object):
    def __init__(self,path):
        self.path = path
    def __iter__(self):
        folders = Load_folders(self.path)
        for folder in folders:
            # os.sep：根据你所处的环境，自动采用相应的分隔符号('\','/')
            file_name = folder.split(os.sep)[-1]
            for file in os.listdir(folder):
                yield file_name,file

if __name__ == "__main__":
    start_time = time.time()
    file_path = os.path.abspath(r'D:\BaiduNetdiskDownload\CSCMNews')
    files = Load_files(file_path)
    for i,msg in enumerate(files):# msg是一个元组
        if i%10000 == 0:
                print('{t} *** {i} \t docs has been read'.format(i=i,
                    t=time.strftime('%Y-%M-%D %H:%M:%S',time.localtime())))
    end_time = time.time()
    print('Total Cost Time : %.2f' %(end_time-start_time)+'s')
