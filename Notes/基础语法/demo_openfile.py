# -*- codeing = utf-8 -*-
# @Time : 2020/8/22 5:33 下午
import time
'''
# -----打开一个文件
f = open('/Users/dev/Downloads/aaaa.log', 'w')
#将字符串写入文件
f.write('hello world, i am here!')
f.close()


f.readlines()  一次性读取全部文件列表，显示一个列表
f.readline()   一次性读取一行
'''

# -----异常处理
'''
try:
    print('---------test1----------')
    #打开了一个不存在的文件，用只读模式，报错
    f = open("test.txt", "r")
    #异常之后代码不会执行
    print('----------test2-----------')
#文件没找到属于IO异常（输入输出异常）
except IOError:
    #捕获异常后,执行的代码
    pass
'''

# -----获取错误描述
'''
try:
    print('---------test1----------')
    #打开了一个不存在的文件，用只读模式，报错
    f = open("test.txt", "r")
    #异常之后代码不会执行
    print('----------test2-----------')
    print(num)
#as一个result变量名 在将result错误描述打印出来
except Exception as result:
    #捕获异常后,执行的代码
    print(result)
'''

# ---try。。。。finally 嵌套
'''
try:
    f = open("text.txt", "r")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print("hellow --word")
    #发生异常后 finally至少被执行一次
    finally:
        f.close()
except Exception as reslut:
    print("发生异常")
'''

# -----作业

def ReadFile(fn):
    try:
       fn.open(fn,"r")
       content = f.readlines()
       print(content)
    except Exception as result:
        print(result)
    finally:
        f.close()



def WriteFile(f):
    try:
        Chins = ["上善若水", "水善利万物而不争", "处众人之所恶", "故几于道"]
        f.writelines(Chins)
    except Exception as result:
        print(result)
    finally:
        f.close

f = open("pyhton.txt", 'w+')
WriteFile(f)
#f2 = open("python.txt", 'r')
ReadFile(f)