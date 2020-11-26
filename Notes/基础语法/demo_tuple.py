# -*- codeing = utf-8 -*-
# @Time : 2020/8/22 4:10 下午


# ------使用enumerate函数，同时拿到列表下标和元素内容
'''
mylist = ['a', 'b', 'c', 'd']
for i, x in enumerate(mylist):
    print(i, x)
'''

# -----遍历字典
'''
info = {"name": "吴彦祖", "age": 18}
for key,valuer in info.items():
    print(key,valuer)
'''

# ----返回多个值的函数
'''
def sum(num1,num2):
    shang = num1//num2
    yushu = num1%num2
    return shang, yushu

s,y = sum(10, 14)
print(s, y)
'''

# ----函数作业
'''
def lin(number):
    for l in range(number):
        print("---------")
lin(20)
'''