import os
import time


class TraversalFun:
    '''
    遍历目录文件，打印出所有文件的完整路径
    '''
    # 1 初始化，root_dir目标文件路径
    def __init__(self, root_dir):
        self.root_dir = root_dir
    # 2 遍历目录文件

    def traversal_dir(self):
        TraversalFun.all_files(self, self.root_dir)

    # 3 递归算法遍历所有文件，并打印文件名（非目录文件）
    def all_files(self, root_dir):
        for lists in os.listdir(root_dir):
            path = os.path.join(root_dir, lists)
            if os.path.isfile(path):
                print(os.path.abspath(path))
            elif os.path.isdir(path):
                TraversalFun.all_files(self, path)


if __name__ == '__main__':
    time_start = time.time()
    root_dirs = r"C:/Users/huihuiyo/Documents/Tencent Files/1127473030/FileRecv"
    tra = TraversalFun(root_dirs)
    tra.traversal_dir()
    time_end = time.time()
    print('耗时', (time_start-time_end), 's')

