# -*- coding: utf-8 -*-
#python的变量也是面向对象的
a='qwer'
b=a
a='asdf'
print(b)

#字符编码
'''ASCII编码是1个字节，而Unicode编码通常是2个字节
	Unicode编码转化为“可变长编码”的UTF-8编码
'''
#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A')
chr(25991)
#如果知道字符的整数编码，还可以用十六进制这么写str
'\u4e2d\u6587'
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
x1 = b'ABC'
x2 = 'ABC'
x1==x2   #因为x1表示bytes类型,每个字符只占一个字节，而字符串中每个字符占若干个字节
#Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')
#把bytes变为str，就需要用decode()方法
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

#格式化字符串
print('%2d-%02d' % (3, 1))  #整数占位，可考虑是否补0
print('%.2f' % 3.1415926)   #浮点数占位，考虑小数位
print('Hello, %s' % 'world')#字符型占位
print( 'growth rate: %d %%' % 7)	#用%来转义%。


#list
classmates = ['Michael', 'Bob', 'Tracy']
classmates[0],classmates[-1]	#选取列表的第0个元素和最后一个元素，当写一行会直接拼成元组
classmates.append('Adam')		#列表的添加
classmates.insert(1, 'Jack')		##列表的指定位置插入
classmates.pop()		#列表删除最后一个元素
classmates.pop(1)		#列表删除第一个元素
classmates[1] = 'Sarah'	#列表第一个元素修改

#tuple
classmates = ('Michael', 'Bob', 'Tracy')
#注意，定义只有一个元素的元组需要加逗号来消除歧义
t1=(1)
type(t1)
t2=(1,)
type(t2)
#’可变的‘tuple
t = ('a', 'b', ['A', 'B'])  #实际上tuple的指向并没有改变，只是指向的list发生了改变。
t[2][0]='X'
t[2][1]='Y'
print(t)

#if elif与else
ages = [3,9,20]
for age in ages:
	if age >= 18:
		print('adult')
	elif age >= 6:
		print('teenager')
	else:
		print('kid')

#python的三元表达式
ages = [3,9,20]
for age in ages:
	print('adult' if age>=18 else 'teenager')
	print('adult' if age>=18 else ('teenager' if age>= 6 else 'kid'))

#python的input,input返回的数据类型为str，无法与整型比较
birth=input('birth_year : ')
birth=int(birth)
if birth < 2000:
	print('00前')
else:
	print('00后')

#循环
#for循环
sum = 0
for x in list(range(10)):
	sum = sum + x
print(sum)

#where循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#break提前结束循环
n = 1
while n <= 100:
	if n > 10: # 当n = 11时，条件满足，执行break语句
		break # break语句会结束当前循环
	print(n)
	n = n + 1
print('END')

#continue跳出当前循环执行下一次循环
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0: # 如果n是偶数，执行continue语句
		continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)

#dict，dict的key必须是不可变对象
'''
通过key计算位置的算法称为哈希算法（Hash）
要保证hash的正确性，作为key的对象就不能变
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d)
#判断key是否在dict中
#通过in判断
if 'Bob' in d:
	pass
else:
	d['Bob']=89
#通过get（）方法判断
d.get('Thomas', False)	#默认当索引的key不存在返回None，这里制定任意返回
#删除指定key
d.pop('Bob')

try:
	key = [1, 2, 3]
	d[key] = 'a list'
except Exception as e:
	print('Exception: {}'.format(e))

for keys,values in d.items():
	print('name is %s, grade is %s' % (keys,values))

#set
s = set([1, 2, 3])
s.add((4,5))   #只能添加可哈希的一个元素
s.remove(1)

#不变对象-字符串,None
a = 'abc'
a.replace('a','AAA')   #变量a依然指向不变，即a未发生改变


#函数的定义，递归迭代的简单应用--类似循环
def f(i):
	num=list(range(10))
	try:
		for i in num:
			x=i*i
			print(x)
	except 	Exception as e:
		print('Exception: {}'.format(e))
	finally:
		if i<9:
			f(i)
f(0)

#函数中的参数类型检查，完善的函数写法
def my_abs(x):
	if not isinstance(x, (int, float)):      #类型检查用isinstance函数
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

#函数的参数,必选参数在前，默认参数在后.默认参数必须指向不变对象！
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

#函数的可变参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
	sum = 0
	for n in numbers:   #自动转为tuple
		sum = sum + n * n
	return sum

nums = [2, 1, 4]
calc(*nums)		#在list或tuple前加*可自动转为可变参数

#函数的关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer') #除了必要参数name和age，还传入关键字参数gender和job；类似必填与选填

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',24,**extra)   #在dict前加**可自动转为关键字参数

#命名关键字参数--限制关键字参数的名字,例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):	#特殊分隔符*后面为命名关键字参数
	print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')		#命名关键字必须传入参数名，且指定

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
	print(name, age, args, city, job)


#命名关键字也可以初始默认值，简化调用
def person(name, age, *args, city='beijing', job):
	print(name, age, args, city, job)


'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

#组合参数的调用
def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#示例理解1
f1(1, 2)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#示例理解2
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#递归函数
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)

#切片
L = list(range(100))
L[:10]
L[-10:]
L[10:20]
L[:10:2]		#前10个数每两个取一个
L[::5]			#所有的数，每5个取一个

#迭代--Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
#示例字典
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)

#for value in d.values()
#for k, v in d.items()

#判断是否是可迭代的对象
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)
isinstance(123, Iterable)

#同时迭代索引和元素--python内置函数enumerate
for i, value in enumerate(['A', 'B', 'C']):
	print(i,value)

#迭代多个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x,y)

#列表生成式
#生成[1*1,2*2,3*3...9*9]
#方法一：循环
L=[]
for x in range(1,10):
	L.append(x*x)
print(L)

#方法二：列表生成式
L=[x*x for x in range(1,10)]
print(L)

[x * x for x in range(1, 11) if x % 2 == 0]		#加if的列表生成式

[m + n for m in 'ABC' for n in 'XYZ']			#两层循环的列表生成式

#列表生成式的简单应用
import os
[d for d in os.listdir('.')]		#'.'表示将.开头的文件也列出来

#列表元素转为小写
L=['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

#生成器--在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))		#方法一：将列表生成式的[]改为（）即可
next(g)								#利用next()函数打印生成器的一个元素，但计算完最后一个元素，再执行next（）会报错
#实际应用中使用for循环打印生成器的元素
g = (x * x for x in range(10))
for i in g:
	print(i)

#生成器是一种推算逻辑，可以完成列表生成式无法完成的任务
#斐波那契数列示例：
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n=n+1
	return 'Done'

#上面函数定义了斐波那契的推算规则，与生成器思想类似。因此可以转化为生成器
#生成器的方法二：将print(b)换算为yield b
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		# print(b)
		yield b
		a,b = b,a+b
		n=n+1
	return 'Done'

generator=fib(8)		#通过含有yield的函数生成所需的生成器
for i in generator:
	print(i)

#generator函数的调用逻辑--每当执行yield返回，下次接着从该yield语句后执行。
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

f=odd()
next(f)		#执行三次，查看结果加深理解

#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

#杨辉三角
def yh(max):
	L = [1]
	m=0
	flag=True
	while flag:
		yield L
		L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]		#arange(0)的loop为空
		if m>max:
			flag=False
		m=m+1

g=yh(9)
for i in g:
	print(i)


#可迭代对象--使用isinstance()判断一个对象是否是Iterable对象
#集合数据类型，如list、tuple、dict、set、str等
#generator，包括生成器和带yield的generator function
isinstance((x for x in range(10)), Iterable)

#迭代器--可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator，如generator
#判断一个对象是否迭代器
from collections import Iterator
isinstance((x for x in range(10)), Iterator)

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
#Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
isinstance(iter([]), Iterator)

#小结
'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''

#变量可以指向函数
f=abs
f(-10)

#一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
	return f(x) + f(y)

add(-5, 6, abs)

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x*x

r = map(f, [1, 2, -3, 4, 5, 6, 7, 8, 9])		#map函数将可迭代对象的每个元素运用f（）函数。

list(map(str,[1,2,3,4,5]))						#也可以使用内置函数

#reduce--reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#其效果如下：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce		#reduce需要导入
#序列求和
def add(x,y):
	return x+y

reduce(add,[1,2,3,4,5,6,])

#序列转化为整数
def fn(x,y):
	return x*10+y

reduce(fn,[1,2,3,4,5,6])

#配合map和reduce写函数str2int
def str2int(s):
	global digits
	digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	def fn(x,y):
		return x*10+y
	def chr2num(s):
		return digits[s]
	return reduce(fn,map(chr2num,s))

#利用lambda函数简化
def strtoint(s):
	def chr2num(s):
		global digits
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[s]
	return reduce(lambda x,y:x*10+y,map(chr2num,s))

#姓名规整化
L1 = ['adam', 'LISA', 'barT']
from string import capwords
def normalize(name):
	return map(capwords,name)

#求序列的积
def prod(L):
	return reduce(lambda x,y:x*y,L)

#编写str2flota函数
def str2float(s):
	if '.'  not in s:
		s=s+'.0'
	def char2(s):   # 返回字符串值对应的数字
		global digits
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[s]
	def f(x, y):    # 像老师的例子一样定义一个函数
		return x * 10 + y
	n = s.index('.')  # 定位小数点的位置
	return reduce(f, map(char2, s[:n])) + reduce(f, map(char2, s[n+1:])) * 10**(-1*(len(s)-n-1))

#filter--和map()类似，filter()也接收一个函数和一个序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#示例1：筛选奇数
def is_odd(n):
	return n % 2 == 1

list(filter(is_odd,[1,2,3,4,5,6,7]))

#示例2：删除空字符串
def not_empty(s):
	return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

#用filter求素数--埃氏筛法
'''
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, -, 5, -, 7, -, 9, -, 11, -, 13, -, 15, -, 17, -, 19, -, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, -, 7, -, -, -, 11, -, 13, -, -, -, 17, -, 19, -, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, -, -, -, 11, -, 13, -, -, -, 17, -, 19, -, ...
不断筛下去，就可以得到所有的素数。
'''
#step1:构造3开始的奇数
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
#step2:定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0
#step3:定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列
#打印primes（注意primes（）也是无限长度的）
for n in primes():
	if n < 1000:
		print(n)
	else:
		break

#回文数
def is_palindrome(n):
	return str(n)==str(n)[::-1]			#[::-1]表示全部序列从后往前步长为1进行选取

for i in filter(is_palindrome, range(1, 1000)):
	print (i)

#sorted也是高阶函数，参数key