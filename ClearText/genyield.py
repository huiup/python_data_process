""" 
yield生成器案例
 """
import time
# 普通斐波那契数列的实现
def fib(max):
     n,a,b = 0,0,1
     while n<max:
        if n<100:
            print('->',b)
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