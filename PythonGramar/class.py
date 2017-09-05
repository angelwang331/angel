# coding:utf-8
class Allfc():
#  类是一个抽象的概念，好比人类，没具体的事物
    def add(self):
        # 无return
        print "返回一个值"
    def acc(self):
        # 有return
        return "返回一个值"
    def aee(self, a, b):
        # 有参数，无默认值
        return a+b
    def aff(self, a=1, b=2):
        # 有参数默认值
        return a+b
a = Allfc()     # 调用类的时候先返回实例
print a.add()
print a.acc()
print a.aee(1,2)
print a.aff()

