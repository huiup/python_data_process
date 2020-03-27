import time
import file2txt
import os


class TraversalFun:
    '''
    功能描述：遍历目录文件，完成文件的转换->text
    参数描述：1 root_dir 根目录 2 func 方法参数 3 sava_dir 保存路径
    '''
    # 1 初始化，root_dir目标文件路径
    def __init__(self, root_dir, func=None, save_dir=''):
        self.root_dir = root_dir
        self.func = func
        self.save_dir = save_dir
    # 2 遍历目录文件

    def traversal_dir(self):
        # 切分文件目录和文件名
        dirs, file_name = os.path.split(self.root_dir)
        #  保存目录
        save_dir = ''
        if self.save_dir == '':
            save_dir = os.path.abspath(os.path.join(dirs, '_new'+file_name))
        else:
            save_dir = self.save_dir
        # 创建保存路径
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # print('保存目录：\n', save_dir)
        # 遍历文件，抽取txt文本内容
        self.all_files(self.root_dir, save_dir)

    # 3 递归算法遍历所有文件
    def all_files(self, root_dir, save_dir=''):
        # 获取目录下的所有文件
        for lists in os.listdir(root_dir):
            path = os.path.join(root_dir, lists)
            if os.path.isfile(path):
                self.func(os.path.abspath(path), os.path.abspath(save_dir))
                # print(os.path.abspath(path))
            if os.path.isdir(path):
                new_save_dir = os.path.join(save_dir, lists)
                if not os.path.exists(new_save_dir):
                    os.mkdir(new_save_dir)
                # 递归调用
                TraversalFun.all_files(self, path, new_save_dir)


if __name__ == '__main__':
    time_start = time.time()
    # 添加保存目录会将文件保存在这个目录下，不会创建_new新的文件夹保存
    # save_dir = r'D:/'
    root_dirs = r"C:\Users\huihuiyo\Documents\Tencent Files\1127473030\FileRecv"
    # 不传递保存目录，则会在同级创建一个_new目录
    tra = TraversalFun(root_dirs, file2txt.file2txt)
    tra.traversal_dir()
    time_end = time.time()
    print('耗时', (time_start-time_end))


