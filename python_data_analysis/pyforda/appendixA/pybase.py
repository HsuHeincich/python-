# -*- coding: utf-8 -*-

# 断点调试举例
def foo(bar=[]):
	bar.append('bar')
	return bar


print(foo())
print(foo())
# 设置断点，F7 step into，查看变量变化。

# isinstance函数判断对象是否为某个特定实例
a = 5
isinstance(a, int)  # 返回True

a = 5;
b = 4.5
isinstance(a, (int, float))  # 返回True
isinstance(b, (int, float))  # 返回True

# 查看属性方法
a = 'foo,fob'
type(a)
dir(a)
help(a.split)
a.split(',')
print(a)

# 调用模块中的变量和函数
# 同及目录下调用模块需要将该文件夹设置为Source Root,并且在python console中添加该Source Root.
# 方法一
import some_module

result = some_module.f(5)
pi = some_module.PI

# 方法二
from some_module import f, g, PI

result1 = g(5, PI) + f(2)

# 方法三  别名的使用
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(5)
r2 = gf(6, pi)

# 用is关键字判断两个引用是否指向同一个对象
a = [1, 2, 3]
b = a
c = list(a)  # list函数始终会创建新列表,即c是新生成的列表
a is b  # 返回True
a is not c  # 返回True
a == c  # 返回True

# 向下取整
a = 11;
b = 3
c = a // b  # 值为3，截除小数部分0.6667

# 可变对象-包括列表、字典、NumPy数组和大部分用户自定义类
a_list = ['abc', 2, [3, 4]]
a_list[2] = ('x', 7)
print(a_list)

# 不变对象-包括字符串和元组等
a_tuple = (3, 4, (5, 6))
print a_tuple[2]
a_tuple[1] = 7  # 报错，不支持分配

# 复数的虚部使用j表示的
cval = 1 + 2j
cval2 = cval * (1 - 2j)
print cval2

# 三重引号（单双皆可）处理带有换行符的长字符串
c = '''
this is a longer string that
spans multiple lines
'''
print c

# 字符串不能改变其组成元素，除非利用函数替换生成新的
a = 'this is a string'
a[10] = 'f'  # 报错，不支持分配
a = a.replace('string', 'longer string')
print a

# 字符串转换函数str（）
a = 6.6
s = str(a)
print(s)

# 由于字符串是一串序列，因此可以看做是某种序列类型（列表，元组等）进行处理
s = 'python'
list(s)
s[:2]

# 转义字符\和fan转义字符r和换行符\n
s = '12\\34'
print s

s = 'this\has\no\special\characters'
print s

s = r'this\has\no\special\characters'
print s

# 字符串格式化
template = '%.2f %s are worth $%d'  # 利用实参代替上面的格式化形参(以%开头后面跟着格式字符)
template % (4.5560, 'Argentime Pesos', 1)

# bool()函数查看对象返回的布尔值，确定对象真假
bool([]), bool([1, 2])
bool(''), bool('abc')
bool(0), bool(2)
bool(()), bool((1, 2, 3))
bool(None)

# python的标量类型-None,str,unicode,float,bool,int-long
s = '3.51159'
a = float(s)
b = int(a)  # 取整函数不能转化字符型，先通过float（）函数。向下取整
c = bool(s)
print a, b, c

# None空值
a = None
a is None


def add_or_multiply(a, b, c=None):
	if c is not None:
		result = (a + b) * c
	else:
		result = a + b
	return result


a = add_or_multiply(1, 2, 3)
b = add_or_multiply(1, 2)
print a, b

# 时间日期函数
from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)
days = dt.day
minutes = dt.minute
print days, minutes

a = dt.date()
b = dt.time()
print a, b

c = dt.strftime('%m%d%Y %H:%M')  # 将日期时间转换成字符串
d = datetime.strptime('20091031', '%Y%m%d')  # 将字符串转换成日期时间,这里必须含有两个参数，因为字符串的方法中不包含strptime（）
print c, d

dt1 = dt.replace(minute=0, second=0)
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt1  # 相减产生timedetla类型
print delta

dt3 = delta + dt1  # timedelta与datetime相加产生datetime型
print dt3


# 控制流--if,elif,else
def f(x):
	if x < 0:
		return '负数'
	elif x == 0:
		return '零'
	elif 0 < x < 5:
		return '五以内正数'
	else:
		return '大于或等于五'


a = f(3)
b = f(-3)
print a, b

# if条件里的or,and
a = 5;
b = 7
c = 8;
d = 4
if a < b or c < d:
	print 'do it'  # if语句里当True则执行，因为a<b，则or的语句短路不执行，因此直接执行print

# for循环
sequence = [1, 2, None, 3, 4, None, 5, None, 6, 7, 8]
total_until_6 = 0
for value in sequence:
	if value is None:
		continue
	elif value == 6:
		break
	total_until_6 += value
print total_until_6

# while循环
x = 256
total = 0
while x > 0:
	if total > 500:
		break
	total += x
	x = x // 2
print total

# pass可当做占位符使用
x = 0
if x < 0:
	print '负数'
elif x == 0:
	# TODO:在这里放点代码
	pass
else:
	print '正数'  # 可以看出在x==0时，if执行结束后不返回任何值，若删除注释添加代码，则会返回代码结果


# 异常处理
def attempt_float(x):  # 改进版float函数
	try:
		return float(x)
	except:  # 异常时执行
		return x


attempt_float('3.154689')  # 返回3.154689
attempt_float('strings')  # 返回strings，不报错


def attempt_float(x):
	try:
		return float(x)
	except ValueError:  # 值异常时执行
		return x


attempt_float((1, 2))


def attempt_float(x):
	try:
		return float(x)
	except (ValueError, TypeError):  # 值异常和类型异常时执行
		return x


f = open('E:/xhy_python/data-wrangling-master/data/chp5/en-final-table9.txt', 'w')
try:
	write_to_file(f)
finally:
	f.close()  # 无论try代码块是否成功，都执行该段代码，本例中执行write_to_file(f)

f = open('E:/xhy_python/data-wrangling-master/data/chp5/en-final-table9.txt', 'w')
try:
	write_to_file(f)
except:
	print 'failed'
else:
	print 'succeeded'
finally:
	f.close()  # 只在try代码块成功时，执行该段代码，本例中不执行write_to_file(f)

# range和range函数
range(10)  # 默认0开始，步长为1
range(0, 20, 2)  # 从0开始，终于20（不包括20），步长为2

seq = [1, 2, 3, 4]
for i in range(len(seq)):  # range常用于按索引对序列进行迭代
	val = seq[i]
	print val

sum = 0
for i in xrange(10000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i
print sum

# 三元表达式--常用于简单的if条件语句，使代码简化
x = 5
y = '负数' if x < 0 else '非负'
print y

x = 5
print '负数' if x < 0 else '非负'

# 元组
tup = 4, 5, 6
print tup  # 返回（4,5,6）元组的表示形式

# 由元组构成的元组
tup = (4, 5, 6), (6, 7)
print tup

# tuple()函数可将任何序列或迭代器转换为元组
tup1 = tuple([4, 5, 6])
tup2 = tuple('string')
print tup1, tup2

# 元组也可以索引，且从0开始
tup2[2]

# 元组内的元素是固定不可修改的，但元组内的元素若是列表，则可以对列表进行增删操作
tup = tuple(['foo', [1, 2], True])
tup[2] = False  # 不可修改
tup[1].append('x')
print tup
tup[1].remove(1)
print tup

# 元组的+与*
a = (4, None, 'foo') + (6, 0) + ('bar',)
print a
b = (1, 'x') * 4
print b

# 元组或列表（包括嵌套元组、列表）拆包
tup = 4, 5, (6, 7)
print tup
a, b, (c, d) = tup
print a, c

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
	print a, b, c

# 元组方法--常用的count,计算元素出现的次数
a = (1, 2, 2, 4, 2, 5, 6, 2, 8, 3)
a.count(2)

# 列表--内容可更改
a_list = [2, 4, 6, None]
b_list = list(('foo', 2, 3))
print a_list, b_list
b_list[1] = 'xhy'  # 修改第1个元素
print b_list

# 列表方法
a_list = [2, 4, 6, None]
a_list.append([2, 3, 4])  # 添加一个元素,该元素可以是一个列表
print a_list

a_list = [2, 4, 6, None]
a_list.extend([2, 3, 4])  # 添加一个列表，其添加的元素个数是添加列表中元素的个数
print a_list

a_list = [2, 4, 6, None]
b_list = a_list + [2, 3, 4]  # 与上述extend相同，但必须创建新列表才能将两个列表元素复制，因此操作费资源

a_list = [2, 4, 6, None]
a_list.remove(None)
print a_list  # 删除列表中一个元素

a_list = [2, 4, 6, None]
a_list.insert(1, 'xhy')  # 向指定位置插入指定元素
print a_list
ret = a_list.pop(2)  # 移除指定位置的元素（insert的逆操作），并返回移除的元素
print a_list, ret

a_list = [2, 4, 6, None]
6 in a_list  # 判断元素是否位于列表中

# 列表的排序
a = [5, 6, 2, 3, 7, 9, 1, 8, 4]
a.sort()
print a
a.reverse()
print a

b = ['saw', 'small', 'six', 'he', 'foxes']
b.sort(key=len)  # 以关键字排序，后面跟函数，该函数应返回一个确切的值。
print b

# 内置的bisect模块
import bisect

c = [1, 2, 2, 2, 3, 4, 6, 8]
bisect.bisect(c, 5)  # 新元素应该查到第几个位置上保持原有序列顺序不变
bisect.insort(c, 5)  # 直接将新元素查到应该的位置上保持原有序列顺序不变
print c

# 切片，从0开始
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq[1:3]  # 第1个到第2个元素（包括左不包括右）

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq[3:5] = ['x', 'h', 'y']  # 将第3位、4位元素重新赋值'x','h','y'（即理解成删去3、4位元素，重新加入元素'x','h','y'）
print seq

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq[:5]  # 省略开始，即0-5
seq[5:]  # 省略结尾，即5-end，注意这里包括最后一个元素

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
seq[-4:]  # 倒数第四开始到最后（注意，不存在倒数第0个元素）
seq[-6:-2]  # 同样包括start不包括stop

seq[::2]  # 冒号后加步长，这句表明从开始到最后，每两个取一个
seq[:]  # 从开始到最后
seq[:5:2]  # 从开始到第4位，每两个取一个
seq[::-1]  # 表示倒数，（end-start,包括了start）每一个取一个，实现序列的反序
# 负步长表示从右向左，若start<stop，则为空；正步长从左到右，若start>stop则为空
seq[8:5:2]
seq[0:5:-2]
# 理解下面
seq[:5:-1]  # 从右往左，相当于seq[end:5:-1],不包括第5个
seq[5::-1]  # 从右往左，相当于seq[5:start:-1]，包括第start个（省略不写就包括-个人理解）
seq[5:0:-1]  # 和上述结果不一样，不包括第0个

# 内置的序列函数
seq = [9, 2, 5, 8, 6, 7, 3, 4, 1]
seq2=[x**3 for x in seq]            #如何计算幂次方的例子
for i, value in enumerate(seq):
	value = value * i
	print value  # 可同时返回序列的索引即对应索引的值，同时迭代两个序列

seq = [9, 2, 5, 8, 6, 7, 3, 4, 1]
for i in range(len(seq)):
	value = i * seq[i]
	print value  # 可得到与上述相同结果，但明显复杂

# enumerate可用带将序列映射到字典
some_list = ['x', 'h', 'y']
some_name = dict((value, i) for i, value in enumerate(some_list))
print some_name

# sorted函数
sorted([9, 8, 7, 6, 5])
sorted('horse race', reverse=True)  # 空格为最小字符，返回单个字符的排序
set('this is a apple')  # 返回序列中不重复字符的排序后集合,升序，
sorted(set('this is a apple'), reverse=True)  # 将set（）后的集合转换成列表

# zip函数，两两配对
seq1 = ['x', 'h', 'y']
seq2 = [1, 'one', 'cool']
a = dict(zip(seq1, seq2))
print a

# zip多个配对，以最短序列决定配对后的元素个数
seq1 = ['a', 'b', 'c''d']
seq2 = [1, 2, 3]
seq3 = [True, False]
zip(seq1, seq2, seq3)

for i, (a, b, c) in enumerate(zip(seq1, seq2, seq3)):
	print('%d: %s,%s,%s' % (i, a, b, c))  # 综合性的小例子，迭代多个序列

# zip用于拆分，类似于元组
seq = [('x', 1), ('h', 'one'), ('y', 'cool')]
a, b = zip(*seq)  # 等价于zip(seq[0],seq[1],seq[2])
print a, b

# reversed用于降序
list(reversed(range(10)))

# 字典
empty_dict = {}
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
print d1
d1[7] = 'an integer'  # 字典的插入，键7对应键值’an integer‘
print d1
d1['a']  # 字典的访问，通过键访问键值
'b' in d1  # 判断字典是否存在某个键
del d1[7]  # 删除字典元素，根据指定键
print d1
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
ret = d1.pop('a')  # pop()方法移除指定元素（指定键），并返回指定元素的值（键值3）
print ret, d1

# 获取字典的键与键值
d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
d1.keys()
d1.values()  # 以列表的形式返回

d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
d1.update({'c': 'xhy'})  # 将另一个字典整合到字典d1中（相当于添加一个字典元素）
print d1
d2 = {'d': "cool", 'e': 'good'}
d1.update(d2)  # 将另一个字典整合到字典d1中（相当于添加多个字典元素）
print d1

key_list = ['x', 'h', 'y']
value_list = [1, 2, 3, 4]
mapping = {}
for key, value in zip(key_list, value_list):
	mapping[key] = value
print mapping  # 常见的字典创建

key_list = ['x', 'h', 'y']
value_list = [1, 2, 3, 4]
mapping = dict(zip(key_list, value_list))
print mapping  # 简单的字典创建方式

# 默认值
# 引例--根据首字母对一组单词分类并创建字典
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
	letter = word[0]
	if letter not in by_letter:
		by_letter[letter] = [word]  # 键值以列表的形式易于添加列表元素
	else:
		by_letter[letter].append(word)
print by_letter

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
	letter = word[0]
	by_letter.setdefault(letter, []).append(word)  # 字典的setdefault（）方法解决上述例子
print by_letter
# setdefault(key,default=None),若键不存在于字典中，则会添加键，并将设置的值设为默认值；
# 若键存在于字典中，则不添加键。
dict = {'x': 'cool', 'h': 'good'}
print "Value : %s" % (dict.setdefault('x', None))  # 返回’cool‘,键’x‘在字典中，故返回该键对应的键值
print "Value : %s" % dict.setdefault('y', 'nice')  # 返回’nice‘，键’y‘不再字典中，故返回改建设置的值

# 内置模块的defaultdict
from collections import defaultdict

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = defaultdict(list)  # 定义一个字典by_letter,若新增字典元素的键不在该字典中，添加该键，并将键值默认设置为[]列表类型
for word in words:
	by_letter[word[0]].append(word)
print by_letter

counts = defaultdict(lambda: 4)  # 将默认值设为四，lambda返回固定值得函数。
counts['xhy']
print counts
counts['a'] = 'hahaha'
print counts

# 字典键的有效性--字典的键必须是不可变的额对象（如整数、浮点数、字符串）或元组（元组的所有对象也必须是不可变的）
# hash（）可以判断某个对象是否是可hash的（即可以作为字典的键）
hash('string')  # 可以
hash((1, 2, (3, 4)))  # 可以
hash((1, 2, [3, 4]))  # 不可以，因为元组里的列表是可变的
# 将列表当做键的最简单方法是转化为元组
d = {}
d[(1, 2, tuple([3, 4]))] = 'list'
print d

# 集合--set是由唯一元素组成的无序集，可以看做只有键而无值的字典
# 创建
set([2, 2, 2, 3, 1, 5])  # set（）创建
{2, 2, 2, 1, 3, 3}  # 花括号创建

# 集合运算--交、并、差、对称差
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a | b  # 并（或）
a & b  # 交（与）
a - b  # 差
a ^ b  # 对称差（异或）-并集去除相交的部分

# 子集与超集的判断
a_set = {1, 2, 3, 4, 5}
{1, 2, 3}.issubset(a_set)  # 是否子集
a_set.issuperset({1, 2, 3})  # 是否超集

# 集合函数
'''
函数                         其他表示方式                说明
a.add(x)                     无                        将元素x添加到集合a中
a.remove(x)                  无                        删除
a.union(b)                   a|b                       a和b的全部唯一元素
a.intersection(b)            a&b                       a和b共同的元素
a.difference(b)              a-b                       a中不属于b的元素
a.symmetric_difference(b)    a^b                       a或b中不同时属于a和b的元素
a.issubset(b)                无                        a是否是b的子集
a.issuperset(b)              无                        a是否是b的超集
a.isdisjoint(b)              无                        a和b是否没有公共元素                             
'''

# 列表推导式
strings = ['a', 'as', 'bat', 'car', 'dogs', 'hy']
a_list = [x.upper() for x in strings if len(x) > 2]  # 列表推导式用的是方括号
print a_list

# 等价于下面的for循环
result = []
for x in strings:
	if len(x) > 2:
		result.append(x.upper())  # 注意列表没有upper()方法
print result

# 集合推导式--用花括号
strings = ['a', 'as', 'bat', 'car', 'dogs', 'hy']
unique_lens = {len(x) for x in strings}
print unique_lens

# 字典推导式
strings = ['a', 'as', 'bat', 'car', 'dogs', 'hy']
mapping = {key: n for n, key in enumerate(strings)}  # 指定键的变量，利用enumerate()迭代两个变量，一个作为键，一个只作为键值
print mapping  # enumerate()返回序列索引号和对应的元素（值）

# 上述结果的另一种构造
strings = ['a', 'as', 'bat', 'car', 'dogs', 'hy']
mapping = dict((key, n) for n, key in enumerate(strings))
print mapping

# 嵌套列表推导式
# 引例
all_data = [['tom', 'billy', 'jefferson', 'andrew', 'wesley', 'steven', 'joe'],
			['susie', 'casey', 'jill', 'ana', 'eva', 'jennifer', 'stephanie']]
# 找出带有两个及以上字母e的名字，将其放入新列表
names_of_interest = []
for names in all_data:
	enough_es = [name for name in names if name.count('e') >= 2]
	names_of_interest.extend(enough_es)
print names_of_interest

# 利用嵌套列表推导式完成上面引例
all_data = [['tom', 'billy', 'jefferson', 'andrew', 'wesley', 'steven', 'joe'],
			['susie', 'casey', 'jill', 'ana', 'eva', 'jennifer', 'stephanie']]
result = [name for names in all_data for name in names
		  if name.count('e') >= 2]  # 按for前后顺序递进，即相当于先读取all_data的每一个names，然后读取每一个names的name
print result  # 将满足条件的name放进result列表中。


# 函数基础
def my_founction(x, y, z=1.5):
	if z > 1:
		return z * (x + y)
	else:
		return z / (x + y)


my_founction(1, 2, z=3)
my_founction(3, 2, 1.0)  # 函数的两种调用，注意z取1.0和1的区别


# 局部函数--当只有外层函数被调用时才会被动态创建出来，当外层函数结束执行，局部函数将会立即被销毁
def outer_function(x, y, z):
	def inner_function(a, b, c):
		pass

	pass


# python函数可以返回多个值，以元组，或字典的形式等
def f():
	a = 5
	b = 6
	c = 7
	return a, b, c


a, b, c = f()  # f()实际上返回的是一个元组（5,6,7），通过元组拆包将元素赋值给各变量
print a, b, c


def f():
	a = 5
	b = 6
	c = 7
	return a, b, c


return_value = f()  # 可以看出该函数返回了三个值，我们将三个值放进retur_value变量中，以元组的形式
print return_value


# 以字典形式返回多个值
def f():
	a = 5
	b = 6
	c = 7
	return {'a': a, 'b': b, 'c': c}


return_value = f()
print return_value

# 明确一个知识点
strings = 'abjkd'
str.title
strings = str.title(strings)  # str.title(strings)和strings.title()其返回的结果是一样的，且都不改变原字符串
print strings

strings = 'abjkd'
strings = strings.title()
print strings

# 将函数作为对象调用的例子
# 引例
states = ['  Alabama ', 'Georgia!', 'Georgia', 'georgia',
		  'FlOrTda', 'south carolina##', 'West virginia?']
# 格式统一
import re  # 正则表达式模块


def clean_strings(strings):
	result = []
	for value in strings:
		value = value.strip()  # 去除前后空格
		value = re.sub('[!#?]', '', value)  # 移除指定标点符号，用''代替方括号中任一匹配的字符
		value = value.title()
		result.append(value)  # 首字母大写，其余小写
	return result


clean_strings(states)


# 调用函数作为列表元素
def remove_punctuation(value):
	return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
	result = []
	for value in strings:
		for clean_function in ops:
			value = clean_function(value)
		result.append(value)
	return result


clean_strings(states, clean_ops)  # 这种调用方式便于修改，且更易复用

# 将函数作为其他函数的参数
map(remove_punctuation, states)  # map(),在一组数据上应用一个函数

# 匿名（lambda）函数--由一条语句组成，其结果就是返回值，根据关键字lambda定义
equiv_anon = lambda x: x * 2  # 定义lambda函数equiv_anon(参数为x),返回值为x*2
equiv_anon(4)  # 调用lambda函数equiv_anon（x）


# 小例子
def apply_to_list(some_list, f):  # 调用参数-列表，函数
	return [f(x) for x in some_list]  # 对于列表中的每一个元素，进行函数f（），返回列表结果


int_list = [4, 0, 1, 5, 6]
apply_to_list(int_list, lambda x: x * 2)  # 列表参数为int_list，函数参数为lambda函数--参数为x，返回结果为x*2
# 虽然可以直接编写[x*2 for x in int_list]

# 根据字符串中各元素不同字母的数量进行排序
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))  # 可以直接set(x).因为key后面跟的是个函数，而函数的参数就是一组字符串的元素
print strings  # 这里的lambda充当key后面的函数，且函数的参数设为x，即x表示一组字符串的元素


# 闭包：返回函数的函数
def make_closure(a):
	def closure():
		print('I know the secret: %d' % a)

	return closure


demo = make_closure(5)  # 传入参数5，赋给临时变量a,创建内函数，并将内函数的引用返回给demo
demo()  # 调用内部函数，启用了外部函数的临时变量a（因为demo存了外函数的返回值即内函数的引用）


# 网上小例子，便于理解
# 闭包函数的实例
# outer是外部函数 a和b都是外函数的临时变量
def outer(a):
	b = 10

	def inner():      # inner是内函数
		print(a + b)  # 在内函数中，用到了外函数的临时变量a与b

	return inner      # 外函数的返回值是内函数的引用，注意inner后没有括号
	# 在这里我们调用外函数传入参数5
	# 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
	# 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
	demo = outer(5)
	# 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
	# demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
	demo()  # 15
	demo2 = outer(7)
	demo2()  # 17

#闭包的内部状态一般是静态的（如上例中的a；a，b），也可以是可变对象（如字典、集合、列表等）动态的
#返回一个能记录其曾经传入的一切参数
def make_watcher():
	have_seen={}
	def has_been_seen(x):
		if x in have_seen:
			return True
		else:
			have_seen[x]=True
			return False
	return has_been_seen
#对一组整数使用该函数
vals=[5,6,1,5,1,6,3,5,]
watcher=make_watcher()   #将函数make_watcher()的返回值即内函数has_been_seen的引用赋给watcher
[watcher(x) for x in vals]

#闭包的技术限制：虽然可以修改任何内部状态对象（例如向字典添加键值对），但无法修改绑定的外层函数作用域中的变量
#解决方法：将外曾函数定义为可修改的列表、字典等，而不是绑定的不能修改的变量
def make_counter():
	count=[0]        #将count变量定义为列表，其列表元素为0，方便对其进行修改
	def counter():
		# 将count的值改为2
		count[0]+=2
		return count[0]
	return counter
xhy=make_counter()
xhy()


#闭包一般常用来通过定义多个非一般化的函数来组装成专门化的函数
#创建一个字符串格式化函数
def format_and_pad(template,space):
	def formatter(x):
		return (template % x).rjust(space)
	return formatter

#利用上述函数创建一个始终返回15位字符串的浮点数格式化器
fmt=format_and_pad('%.4f',15)   #传入外函数的参数
fmt(1.756)    #内函数引用，传入参数1.756   #‘         1.7560’

#扩展调用语法--*args，**kwargs
#函数的位置参数和关键字参数实际上是分别被打包成元组和字典的，实际上函数接收到的是一个元组args和一个字典kwargs
def say_hello_then_call_f(f,*args,**kwargs):       #位置参数*args，关键字参数**kwargs
	print 'args is',args                           #打印所有的位置参数
	print 'kwargs is',kwargs                       #打印所有的关键字参数
	print("Hello! Now I'm going to call %s" % f)   #打印字符串并调用f（该参数代表一个函数）
	return f(*args,**kwargs)                       #调用函数f，并返回位置参数*args，关键字参数**kwargs的结果

def g(x,y,z=1):                                    #定义函数g，位置参数x，y和关键字参数z(默认值1)
	return (x+y)/z

say_hello_then_call_f(g,1,2,z=5.)

#柯里化，部分参数应用
def add_numbers(x,y):
	return x+y
#根据上述函数派生出一个只有一个参数的函数add_five
add_five=lambda y:add_numbers(5,y)    #所以将add_numbers函数的第二个参数称为‘柯里化的’(即定义一个可以调用现有函数的新函数而已)
add_five(7)

#上述例子可以通过内置模块functools的partial函数进行简化
from functools import partial

def add_numbers(x,y):
	return x+y

add_five=partial(add_numbers,5)     #将add_numbers函数的一个参数设置为5，进行部分参数调用派生出新函数
add_five(9)

#生成器
#对字典迭代得到所有的键
some_dict={'x':1,'y':2,'h':3}
for key in some_dict:
	print key,                     #注意print语句结尾的‘,’若没有‘，’则会纵向排列输出所有的键，加上‘，’后会在一行输出所有键

#当编写上面的for语句是，python会首先尝试从some_dict中创建一个迭代器
dict_iterator=iter(some_dict)
print dict_iterator                #迭代器是一种特殊的对象

#迭代器的方法，大部分接受列表对象的方法也能接受任何迭代器对象,例如min，max，sum等内置方法以及list()和tuple（）等类型构造器
min(dict_iterator)     #返回迭代器中最小的元素
list(dict_iterator)    #将迭代器转换成列表对象

#生成器，构造新的可迭代对象的一种方式，只需将函数中的return换成yeild即可,即通过延迟的方式返回一个值序列而不是直接返回单个值
def squares(n=10):
	print 'Generating squares from 1 to %d' % (n ** 2)
	for i in xrange(1,n+1):
		yield i**2    #注意若是return，则在执行第一次平方和时就结束了，返回单个值
gen=squares()         #gen为生成器对象
print gen   #调用该生成器，没有代码会立即被执行

#从该生成器中请求元素时，才会开始执行代码，即请求一个元素，执行一次，执行结束后暂停直到下一个请求。
for x in gen:
	print x,

#生成器表达式（推导式）
gen = (x**2 for x in xrange(11))     #同列表表达式，只是将列表表达式的方括号改为圆括号
print gen
for x in gen:
	print x,                         #同上例一致

#生成器表达式可用于任何接受生成器的函数
sum(x**2 for x in xrange(11))
dict((i,i**2) for i in xrange(5))

#itertools模块，用于许多常见算法的生成器，例如groupby
import itertools
first_letter=lambda x:x[0]
names=['Alan','Adam','Wes','Will','Albert','Steven']
for letter,name in itertools.groupby(names,first_letter):    #groupby函数将接受一个序列和一个函数，根据函数的返回值排序
	print letter,list(name)                                              #排序规则-将连续的返回值放进同一序列
#上述的name是一个生成器，注意groupby返回的是根据首字母排序的姓名，所以其对应关系类似'A-Alan'
#因此for循环的对应关系为letter，name


