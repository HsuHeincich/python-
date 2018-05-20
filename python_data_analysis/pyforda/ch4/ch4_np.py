# -*- coding: utf-8 -*-
from __future__ import division
#导入python未来支持的语言特征division(精确除法)，当我们没有在程序中导入该特征时，"/"操作符执行的是截断除法(Truncating Division)
# 当我们导入精确除法之后，"/"执行的是精确除法.若导入后想执行截断除法，使用‘//’
from numpy.random import randn
import numpy as np
np.set_printoptions(precision=4, suppress=True)   #精度为4，正值根据默认不打印前面的‘+’

data = randn(2, 3)              #通过randn函数随机生成数组，（两个维度，第0个维度大小为2，第1个维度为3）
data
data * 10
data + data
data.shape                       #显示data的各维度大小
data.dtype                       #data数组里的数据类型

#创建ndarray
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)           #通过np的array函数构建数组
arr1

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]   #二维数组
arr2 = np.array(data2)
arr2
arr2.ndim                              #显示arr2的维度
arr2.shape

arr1.dtype
arr2.dtype

np.zeros(10)                           #元素全为0的一维
np.empty((3, 6))                       #元素全为空（未初始化的值，有可能是0）的二维
arr3=np.ones((2, 3, 4))                #元素全为1的三维（第0个维度2个轴，即维度大小）
arr3

np.arange(15)                          #内置函数range的数组版

np.eye(3)                              #生成N*N的单位矩阵

#数据类型设定
arr1 = np.array([1, 2, 3], dtype=np.float64)  #设定数据类型
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr1.dtype
arr2.dtype

#数据类型转换
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)      #astype将整数转换为浮点型
float_arr.dtype

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
arr.astype(np.int32)                    #astype将浮点型转换为整数，小数部分会被截断
arr.dtype                               #不改变原始数据类型，除非赋值给新变量

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.dtype
float_arr1=numeric_strings.astype(float)     #astype将全是数值的字符串转换为浮点型,NumPy会自动将float映射到等价的dtype上
float_arr1.dtype

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)            #将int_array的类型转换为和calibers的类型一致

empty_uint32 = np.empty(8, dtype='u4')      #数据类型的简写
empty_uint32

#大小相等的数组间的算数运算运算
#数组与标量的算数运算
#以上两种情况均会将运算应用到元素级
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
arr * arr
arr - arr

1 / arr
arr ** 0.5


#数组的索引与切片，返回的是源数组的视图，不会进行任何复制操作
#一位数组的索引与切片与列表类似
arr = np.arange(10)
arr
arr[5]
arr[5:8]             #一维数组的切片，与列表类似
arr[5:8] = 12        #多个一维数组元素更改
arr

#列表不能将切片区域更改为一个数
list_t=range(10)
list_t
list_t[8]=12          #单个列表元素更改
list_t
list_t[5:7]=(13,14)   #多个列表元素更改
list_t

#数组切片是原始数组的视图，视图上的任何修改都会直接反映到源数组上
arr_slice = arr[5:8]  #新建一个数组切片的视图
arr_slice
arr_slice[1] = 12345  #修改视图的第一个元素
arr                   #源数组也相应反生改变
arr_slice[:] = 64     #修改整个视图
arr

#注意，若只想生成切片的副本而非视图，需要显式进行复制操作
arr_copy=arr[5:8].copy()
arr_copy
arr_copy[:]=128
arr                   #修改副本的部分值，不会改变源数组

#高维数组的索引
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]              #二维数组的一级索引是个一维数组

arr2d[0][2]           #二维数组的二级索引查询元素
arr2d[0, 2]           #与上述方式等价，结果一致

arr3d = np.array([[[1, 2, 3,4], [5, 6, 7,8],[9,10,11,12]],
				  [[13,14,15,16], [17, 18, 19,20],[21,22,23,24]]])   #2*3*4维数组
arr3d
arr3d[0]             #第0个维度的第0个轴是一个3*4的数组

old_values = arr3d[0].copy()    #复制第0个维度的第0个轴是一个3*4的数组
arr3d[0] = 42                   #将标量赋值给第0个维度的第0个轴（更改）
arr3d
arr3d[0] = old_values           #将数组赋给第0个维度的第0个轴（更改）
arr3d

arr3d[1, 0]       #第0个维度的第1个轴，第1个维度的第0个轴的所有元素
arr3d[1,0,3]      #第0个维度的第1个轴，第1个维度的第0个轴，第2个维度的第3个轴
#注意，在上述所有这些选取数组子集的例子中，返回的数组都是视图，对视图的更改都会对源数组进行更改

#高维数组的切片
arr[1:6]          #一维数组的切片

arr2d
arr2d[:2]         #第0个维度，从第0个轴切到第1个轴

arr2d[:2, 1:]     #第0个维度，从第0个轴切到第1个轴；第1个维度，从第1个轴切到最后一个轴

arr2d[1, :2]      #整数索引和切片混合。索引第0个维度的第1个轴，在该范围内切片从开始到第1个轴。
arr2d[2, :1]      #与上类似
arr2d[:,:1]       #只有冒号表示全部，即第0个维度全部，第1个维度从0切到0

arr2d[:2, 1:] = 0 #对切片的赋值也会扩展到源数组的整个区域

#布尔型索引
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)        #np.random中的randn函数随机生成正态分布的7*4的数组元素
names
data

names == 'Bob'     #数组的比较运算也是矢量的，会返回各元素的布尔型

#将布尔型数组用于数组索引
data[names == 'Bob']     #相当于将names分配给第0维度，索引第0维度所有names==Bob的轴
#这就要求布尔型数组的长度与被分配的维度的大小一致（例子中names的长度为7，第0维度的大小也为7个轴）

#布尔型索引与整数索引或切片的混用
data[names == 'Bob', 2:]  #第0个维度所有names==Bob的轴，第1维度切片从2到最后
data[names == 'Bob', 3]

#索引出‘Bob’以外的所有元素，!= 和 ~
names != 'Bob'
data[~(names == 'Bob')]

#多个布尔条件的组合，“&”，“|”.注意，在布尔型数组中，python关键字“and”和“or”无效
mask = (names == 'Bob') | (names == 'Will')
mask
data[mask]

#通过布尔型赋值，简化操作。
data<0               #生成data的布尔型
data[data < 0]       #索引data<0的所有元素
data[data < 0] = 0   #本例将所有负数转化为0
data

#通过一维布尔数组设置整行或整列的值
data[names != 'Joe'] = 7       #修改第0维度names不是‘Joe’的值为7
data

data[:,(True,False,False,False)]=12  #修改第1维度（第0维度全部）第0轴的值为12
data

#花式索引
#生成一个8*4的数组
arr = np.empty((8, 4),dtype=np.int32)
for i in range(8):
    arr[i] = i
arr

#以特定顺序选取子集，只需传入一个用于指定顺序的整数列表或ndarray
arr[[4, 3, 0, 6]]
arr[[-3, -5, -7]]   #负数表示从末尾开始选取（注意没有倒数第0）

#生成8*4的数组
arr = np.arange(32).reshape((8, 4))
arr
#按顺序选取两个维度的子集
arr[[1, 5, 7, 2], [0, 3, 1, 2]]  #选出结果为一位数组，元素分别对应（1,0）（5,3）（7,1）（2，2）

arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] #选出结果为方形区域，按两个维度指定顺序排列

arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]  #通过np.ix_函数，将两个一维整数数组转换为一个用于选取方形区域的索引器
#注意，花式索引与切片不一样，它总是将数据复制到新数组中，而不是返回视图，因此对他的更改不会改变源数组
fancy_arr=arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
fancy_arr=0       #fancy_arr并非源数组的一个视图，对其赋值不会直接作用于源数组
arr

arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]=0   #注意与上面的区别，这里的赋值操作还是直接作用于源数组的
arr

#数组转置和轴对换
arr = np.arange(15).reshape((3, 5))
arr
arr.T    #简单的转置用T属性，转置返回的是源数据的视图

#通过转置求矩阵内积
arr = np.random.randn(6, 3)
np.dot(arr.T, arr)          #等同于矩阵乘法

arr = np.arange(24).reshape((2, 3, 4))   #元素长度必须等于维度大小之积
arr
arr.transpose((1, 0, 2))  #对于高位数组的转置用transpose方法，且需根据由编号组成的元组指定转置类型
#本例中根据编号（1,0,2）分别对应（第1个，第0个，第2个维度大小）对其进行转置，即将其转置为3*2*4

#ndarray的其他方法转置高维数组
#swapaxes,需要接收一对轴编号，返回的也是源数组的视图
arr = np.arange(24).reshape((2, 3, 4))   #元素长度必须等于维度大小之积
arr
arr.swapaxes(1, 2)          #根据给定一对轴（维度）编号，将其转置，即将第1个和第2个维度转置，最后转置成2*4*3

#数组通用函数（ufunc），快速的元素级数组函数
#亿元函数
arr = np.arange(10)
np.sqrt(arr)     #元素开方
np.exp(arr)      #计算各元素（x）的指数e^x

#二元函数，接收两个数组
x = randn(8)
y = randn(8)
x
y
np.maximum(x, y) # 选取两个数组中的较大的一个，两个数组大小必须一致

#可以返回多个数组的快速数组函数
arr = randn(7) * 5
arr
np.modf(arr)     #将元素的小数和整数分开返回（即一分为二）


#利用数组进行数据处理
points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
points
xs, ys = np.meshgrid(points, points)  #np.meshgrid接受两个一维数组，并产生两个二维数组
xs                                    #第一个二维数组,对传入的第一个一维数组横向排列，产生等于一维数组长度的方阵
ys                                    #第二个二维数组，对传入的第二个一维数组纵向排列，产生等于一维数组长度的方阵


from matplotlib.pyplot import imshow, title
import matplotlib.pyplot as plt

z = np.sqrt(xs ** 2 + ys ** 2)      #在网格型数组计算sqrt（x^2+y^2）
z
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.draw()
plt.show()                         #通过plt.show（）解决在charm中不能直接出图的结果

#数组的三元表达式
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

#用列表三元表达式，根据cond选择xarr或yarr。缺点是速度慢且不适用于多维数组
result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
result

#用np.where（数组的三元表达）完成上例
result=np.where(cond,xarr,yarr)    #where的第二个和第三个参数可以是数组也可以是标量
result

#where常用于根据一个数组产生另一个新数组
arr = randn(4, 4)
arr

np.where(arr > 0, 2, -2)     #数组中>0设置为2，否则为-2
np.where(arr > 0, 2, arr)    #数组中>0设置为2，否则不变

#where的嵌套
#引例
cond1 = np.array([True, False, True, True, False])
cond2 = np.array([True, True, False, True, False])

result = []
for i in range(5):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)
print result

#利用数组的where嵌套完成引例（np.where(条件，表达式1，表达式2)）
np.where(cond1 & cond2, 0,
         np.where(cond1, 1,
                  np.where(cond2, 2, 3)))

#布尔型数组可以当做0或1进行运算，通过运算完成引例
result = 0*(cond1&cond2)+1 * (cond1&~cond2) + 2 * (cond2&~cond1) + 3 * ~(cond1 | cond2)
print result


#数组的统计量（描述性统计量）
arr = np.random.randn(5, 4) # 正态分布数据
arr.mean()
np.mean(arr)   #两种用法
arr.sum()

#求某一轴的描述统计量
arr=np.arange(15).reshape((5,3))
arr.mean(axis=1) #计算第1轴（即第1个维度，各行）的均值，不好理解（可以理解为第1个维度是列，求各行均值生成的数组是列）
arr.sum(0)       #计算第0轴（即第0个维度，各列）的和

#数组的某一轴向的累计和、积，返回源数组大小的的数组
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr.cumsum(0)
arr.cumprod(1)

#高维统计量的理解
#如果将三维数组的每一个二维看做一个平面（plane，X[0, :, :], X[1, :, :], X[2, :, :]）
# 三维数组即是这些二维平面层叠（stacked）出来的结果。
# 则（axis=0）表示全部平面上的对应位置，
# （axis=1），每一个平面的每一列，（即每一列的和组成一行）
# （axis=2），每一个平面的每一行。
arr=np.arange(24).reshape((2,3,4))
arr
arr.sum(axis=0)
arr.sum(1)
arr.sum(2)

#用于布尔型数组的方法
arr = randn(100)
(arr > 0).sum() # Number of positive values

bools = np.array([False, False, True, False])
bools.any()     #是否存在1个或多个True
bools.all()     #是否全部为True

np.any(bools)   #两种用法
np.all(arr>0)


#排序
arr = randn(8)
arr
arr.sort()
arr

#多维数组排序，只需给出轴编号
arr = randn(5, 3)
arr
arr.sort(1)   #按行排序（即每一行取最小作为第一列）
arr           #就地排序会修改数组本身

arr = randn(5, 3)
arr
np.sort(arr,1)  #np.sort()方法则会创建排序副本，不会修改数组本身
arr

#计算数组分位数
large_arr = randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))] # 5%分位数

#数组的集合运算
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)    #返回唯一并排序
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)
#等价于下面的纯python代码
sorted(set(names))

#in1d判断第一个数组元素在另一个数组的成员资格（即是否是另一个数组的子集），返回布尔型数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])

#数组文件的读存操作
arr = np.arange(10)
np.save('some_array', arr)    #np.save以.npy格式保存于项目路径下

np.load('some_array.npy')     #np.load读取.npy文件

#np.savez储存多个数组文件，并生成压缩文件，通过传入关键字参数储存数组
xarr=np.arange(11)
yarr=np.arange(12)
np.savez('array_archive.npz', x=xarr, y=yarr)

#读取压缩文件的数组文件
arch = np.load('array_archive.npz')   #加载压缩文件会得到一个类似于字典的对象
arch['x']

#文本文件的存取
#pandas的read_csv和read_table
#numpy的np.loadtxt和np.genfromtxt
!type E:\xhy_python\pydata-book-1st-edition\ch04\array_ex.txt
#注意这里的文件路径分隔符与Python的不一样，前面加!表示以交互环境（即cmd）下操作

#数组格式加载文本文件
path='E:/xhy_python/pydata-book-1st-edition/ch04/array_ex.txt'
arr = np.loadtxt(path, delimiter=',')
arr

#np.savetxt执行的是相反的操作，即将数组写到以某种分隔符的文本文件
np.savetxt('array_ex1.txt',arr,delimiter=',')
arr = np.loadtxt('array_ex1.txt', delimiter=',')
arr

#numpy的线性代数
#dot函数，用于矩阵乘法
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
x
y
x.dot(y)  # equivalently np.dot(x, y)
np.dot(x,y)

np.ones(3)
np.ones(3).shape       #与我们认知的矩阵些许区别，一维数组无论是否转置，它都是N行的数组，因此将有一位数组看成列向量
np.ones(3).T.shape
x.shape
np.dot(x,np.ones(3))


t=np.array([1,2,3])
t
t.T
np.dot(t.T,t)          #一维数组的內积依然是一个数

#numpy.linalg中的标准矩阵运算
from numpy.linalg import inv, qr,eig

np.random.seed(12345)
X = randn(5, 5)

mat = X.T.dot(X)
inv(mat)               #mat的逆
mat.dot(inv(mat))      #mat与mat^-1的积为单位阵

q, r = qr(mat)         #矩阵的QR分解法（用来求特征值）
r
q

eig(mat)               #矩阵的特征值与特征向量


#生成随机数
samples = np.random.normal(size=(4, 4))   #生成4*4的标准正态分布样本
samples

#对比np.random和内置random的运行速度，可以看出np.random下的函数生成样本数的速度比内置的快几个数量级
from random import normalvariate
N = 1000000
%timeit samples = [normalvariate(0, 1) for _ in xrange(N)]
#“_”；Python中对于无需关注其实际含义的变量可以用_代替，用_代替仅获取值而已
%timeit np.random.normal(size=N)

#模拟随机漫步来解释如何运用数组运算
#纯python代码的引例
import random
position=0
walk=[position]
steps=1000
for i in xrange(steps):
	step=1 if random.randint(0,1) else -1    #随机生成[0,1]的整数，即随机生成布尔型
	position+=step
	walk.append(position)
print walk

#np.random随机生成
np.random.seed(12345)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)   #这里的randint包括左边，但不包括右边，即[0,2)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()                #累积和

#求最值
walk.min()
walk.max()

#求首次穿越时间，即随机漫步过程中第一次达到某个特定值的时间
#本例求首次达到步长10的索引（即第几次）
(np.abs(walk) >= 10).argmax()


#一次模拟多个随机漫步
np.random.seed(12345)

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) #0或1，并生成5000*1000的数组，相当于5000个随机漫步
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)         #求行的累计和
walks

walks.max()
walks.min()

hits30 = (np.abs(walks) >= 30).any(1)   #返回布尔型一维数组
# 记录每一行中只要存在有距离达到30的随机过程即为True（一共5000个，达到的有3411个）
hits30
hits30.sum() # 达到30的随机过程的数量（即True的次数）

#利用布尔型数组hits30选取距离达到30的随机漫步（行）
#记录这些行首次达到30的时间
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()       #计算平均到达时间

#其他分布方式的随机漫步模拟
steps = np.random.normal(loc=0, scale=0.25,
                         size=(nwalks, nsteps))   #正态分布