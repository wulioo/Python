# -*- codeing = utf-8 -*-
# @Time : 2020/8/22 11:55 上午
import random



# ------for遍历字典
'''
list = ['aa', 'bb', 'cc']
for li in range(len(list)):
    print(li, list[li], end='\t')
'''

# -----while循环
'''
i = 0
while i < 5:
    print("第一次循环：{}".format(i))
    i += 1
'''
# ~~~len()函数可以得到列表的长度 list(长度为3)
''''
length = len(list)
i = 0
while i < length:
    print(list[i])
    i += 1
'''

# ----嵌套循环列表
'''
offices = [[], [], []]
names = ['小王', '小郑', '小李', '小辉', '小杰', '小紫']
#循环names,定义一个0-2的随机数,offices[随机数].append(name)将名字随机添加到offices列表
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)
#定义一个下标，先循环offices列表,得出列表每个内嵌列表长度,在内嵌循环内嵌列表
i = 1
for office in offices:
    print("办公室{} 人数为:{}".format(i, len(office)))
    i += 1
     for name in office:
         print("%s"%name)
'''

# ------作业
'''
products = [["iphone", 6888], ["MacPro", 14800], ["MacBook", 23000], ["Windows", 7999], ["Myipd", 4897], ["iwahch", 2500]]
print("-------商品列表-------")
i = 0
# range(len())函数将Product列表长度循环为0-5,products[prods][0]去长度0的嵌套列表中的坐标0字段。
for prods in range(len(products)):
    print(i, products[prods][0], products[prods][1])
    i += 1

shoping = []
while True:
    user = input("请问需要购买什么商品: 输入编号添加购物车！")
    if user.isdigit():
        user = int(user)
        if user >= 0 and user < len(products):
            shoping.append(products[user])
            print("商品{}已经添加购物车".format(products[user]))
        else:
            print("输入的商品不存在！")
    elif user == 'q':
        if len(shoping) > 0:
            for sp in range(len(shoping)):
                print("你已经购买以下商品：{}".format(shoping[sp][0]))
        break
'''