import os,time

""" 
普通方法递归批量读取30万条新闻文本
"""
# 功能描述：遍历目录，对子文件单独处理
def Traversal_Dir(root_Dir):
    # 返回指定目录包含的文件或文件夹的列表，i为序号
    for i,lists in enumerate(os.listdir(root_Dir)):
        path = os.path.join(root_Dir,lists)
        if os.path.isfile(path):
            if i%10000 == 0:
                print('{t} *** {i} \t docs has been read'.format(i=i,
                    t=time.strftime('%Y-%M-%D %H:%M:%S',time.localtime())))
        if os.path.isdir(path):
            Traversal_Dir(path)

if __name__ == "__main__":
    start_time = time.time()

    root_dir = r'D:\BaiduNetdiskDownload\CSCMNews'

    Traversal_Dir(root_dir)

    end_time = time.time()
    print('Total Cost Time : %.2f' %(end_time-start_time)+'s')