#coding:utf-8
def add(a=1,b=2):
    # print a+b
    return (a+b)

print add()
print add(3,4)
print add(a=3, b=4)
print add(b=7)
print abs(-6)

l = [1,2,3,4,5,6]
print sum(l)
print sum(range(1,1000))
print sum(xrange(1,1000))

r = help(len)
print r