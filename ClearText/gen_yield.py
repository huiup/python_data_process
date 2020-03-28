""" 
yield生成器案例
1：数组、链表、字符串、文件等缺点就是所有数据都在内存里，海量的数据很耗内存。
2：生成器是可以迭代的，工作原理就是重复调用next()方法，直到捕获一个异常。
3：有yield的函数不再是一个普通的函数，而是一个生成器generator，可用于迭代。
4：yield是一个类似return 的关键字
 """
import time
# 普通斐波那契数列的实现
def fib(max):
     n,a,b = 0,0,1
     while n<max:
        # if n<100:
        #     print('->',b)
        a,b = b,a+b
        n+=1
        
#  带yield的生成器实现
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
def GeneratorDome():
    max_num = 1000000
    time_start1 = time.time()
    fib(max_num)
    time_end1 = time.time()
    print("running time: %.2f" % ((time_end1-time_start1))+'  s')

    time_start2 = time.time()
    fib2(max_num)
    time_end2 = time.time()
    print("running time: %.2f" % ((time_end2-time_start2))+'  s')


if __name__ == "__main__":
    GeneratorDome()