# -*- codeing = utf-8 -*-
# @Time : 2020/9/8 4:07 下午
'''
1.定义需要依赖装饰器@classmethod
2.类方法中只可以使用类属性
3.类中兄弟方法互相调用需要引用self
4.类方法中不能使用普通方法

'''


class Dog:
    nickname = '小黄' # 类属性

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self 对象方法，对象来调用
        print('{}在院子里跑来跑去！'.format(self.nickname))

    @classmethod
    def test(cls):  # class 类方法，类来调用
        print(cls)
        print(cls.nickname)


d = Dog('小白')
d.run()
d.test()
