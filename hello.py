#coding:utf-8
def add(a=3,b=4):
    # a=1
    # b=2
    c = a+b
    # return "打印出c的值：%s" %c
    return c

print add(7,8)

d = add()
print d
if d == 3:
    print "pass"
else:
    print "fail"
