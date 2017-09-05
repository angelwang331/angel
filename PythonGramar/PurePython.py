# 编码格式3种都可以：
#  coding=utf-8
#  coding:utf-8
#  -*- coding:utf-8 -*-


name = "angel"
age = 20

print ("%s is %d years old" %(name,age))

print ("HelloWorld" + "    " + "angel")

# python27只能用raw_input，不能用Input
name = raw_input("Input you name:")
print ("MyName is: " + name)


# coding:utf-8
a = 60
if a%2:
    print ("a是奇数")
else:
    print ("a是偶数")

a = raw_input("Input an intefer:")
# a = 60
if int(a)%2:
    print ("a是奇数")
else:
    print ("a是偶数")


# 交换a和b的值：
a = 1
b = 2
a,b = b,a

print (a,b)

# 给定一个1-99之间的数，让用户猜数字，当用户猜错时会提示用户猜的数字是过大还是过小，知道用户猜对数字为止，猜对数字用的次数越少成绩越好。
# coding:utf-8
import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
  print
  if guess < n:
    print "guess is low"
    guess = int(raw_input("Enter an integer from 1 to 99: "))
  elif guess > n:
    print "guess is high"
    guess = int(raw_input("Enter an integer from 1 to 99: "))
  else:
    print "you guessed it!"
    break
  print


# coding:utf-8

import random
n = random.randint(1,99)
guess = int(raw_input("Enter an integer from 1 to 99:"))

if guess < n:
    print ("请输入1到 %d" %(guess))
elif guess > n:
    print ("请输入1到 %d" %(n))
else:
    print ("You guess it")


# 1.常见的数据类型：整数、浮点数、字符串、列表、元组、字典
a = 12
b = 12.0
c = "angel"
d = [1,2,"a"]
e = (4,5,"hello","world")
f = {"username": "yoyo", "psw": "123"}
print a
print b
print c
print d
print e
print f

# 求和
i = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for j in i:
    sum = sum + j
print sum

# 多个变量赋值
a = b = c =1
print a,b,c
e,f,g = 1,2,"hello"
print e,f,g

# 字符串只有+和*操作，没有-、/
a = "hello"
b = "world"
print a+b
print a*3

s1 ="hello world"
print s1[1:4]
print s1[4:]
print s1[4]
print len(s1)
print s1.count("l")

L = [1,2,3,4,'a','b','c']
# 在列表中添加元素
L.append(5)
print L
# 删除元素
del L[0]
print L
# 删除指定的包含内容元素
L.remove(2)
print L
# 修改指定元素值
L[0]=100
# 弹出最后一个元素
d =L.pop(-1)
print d
print L
# 列表长度
print len(L)
# 列表排序
print sorted(L)
# 打印元素出现次数
print L.count(100)
# list的切片参考上一页字符串切片
print L[1:4:2]
print L[-1]
print L[0]
# 反着取元素
print L[::-1]
print L[4:1:-1]
# 元组和List区别：
# 区别一：元组定义是（）/list定义是[]
# 区别二：元组里面的元素只能读，无法增删改
# 字典
dict ={}
dict["one"] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print dict['one']
print tinydict
print tinydict.keys()
print tinydict.values()

# if
age = 12
if age > 25:
    print("you are too old!")
elif age < 10:
    print("you are so young!")
else:
    print("it's a boy")

# 依次打印字符串字母
n = 'HelloWorld'
for i in n :
    print i

l = ['he', '12', 12, "hello", "22"]
for i in l:
    print(i)

s = 0
for i in list(range(10)):
    s += i
    print(s)

s = 0
for i in range(10):
    s += i
    print s

# range(1,100,2)  起点，终点，步长


#   if语句：求100以内的奇数和
s = 0
for i in range(100):
    if i % 2:
        s+=iif
    else: continue
print s

# 当s>1000时结束计算
s = 0
for i in range(100):
    if i%2:
        s+=i
        if s >1000:
            break
        continue
print s

# While 语句：pass只是占位，break才是退出
s = 0
i = 1
while i <100:
    if i % 2 :
        s +=i
        if s >1000:
            break
    i = i +1
print s

s = 0
i = 1
while i <100:
    if i % 2 :
        s +=i
        if s >1000:
            pass
    i = i +1
print s

# 和输入比大小：
key = 7
guess = raw_input("请输入：")
if key > guess:
    print ("你输入的大了")
elif key < guess:
    print ("你输入的小了")
else:
    print ("猜对了")

# 猜数字：
import random
a = 1
b =99
key =random.randint(1,100)
while 1:
    guess = int(raw_input("请输入："))
    if guess <key and guess >a:
        a =guess
        print ("请输入%d" %a+ "到"+"%d"  %b)
    elif guess> key and guess < b:
        b = guess
        print ("请输入%d" %a+ "到"+"%d"  %b)
    elif guess<=1 or guess >=100:
        print ("你太调皮了")
    elif guess == key:
        print ("你猜对了")
        break





