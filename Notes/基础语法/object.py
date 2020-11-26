# -*- codeing = utf-8 -*-
# @Time : 2020/9/8 2:24 下午

'''
class 类名[(父类)]
    属性： 特征

    方法： 动作

    # 1.魔术方法之一：称作魔术方法__名字__()
    # 2.只要创建对象就会执行init初始化方法
    def __init__(self):    init初始化
        pass

'''


class Student:
    # 类属性
    def __init__(self, name, age, note):
        self.name = name
        self.note = note
        self.age = age
        self.address_book = []

    def call(self):
        print("正在打电话----")
        for person in self.address_book:  # 不能保证每个self中都存在address_book
            print(person.items())
        print(self.note)


# -----使用类创建对象
feifei = Student('菲菲', 20, '菲菲专有属性')
'''
feifei = Student()
1.找有没有一块空间是feifei
2.利用Student类，向内存申请一块feifei的空间 0x78392nabc
3.去Student类中找有没有__init__(self)方法,如果没有则执行将开辟的内存地址给对象名：feifei
4.如果有__init__(self)，则会进入init方法执行里面动作，执行完init在赋值给对象feifei
'''

# -----对象age属性赋值
feifei.age = 20
feifei.name = 'feifei'
# ------当前对象添加一个属性
feifei.note = '菲菲的专有'
feifei.address_book = [{'11231': '菲菲'}, {'5461233': '辉辉'}]
# -----对象调用函数
feifei.call()
print('*' * 30)
