# -*- coding: utf-8 -*-
from pandas import Series, DataFrame   #由于Series和DataFrame使用较频繁，因此将其引入本地命名空间
import pandas as pd

from __future__ import division
from numpy.random import randn
import numpy as np
import os                             #os模块包含普遍的操作系统功能
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))          #设置图片大小
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签,有中文出现的情况，需要u'内容'
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)

#介绍series
obj = Series([4, 7, -5, 3])   #Series由2由子一组数据和一组与之相关的标签（即索引）组成
obj                           #索引在左，值在右。若未指定索引，则自动生成0，N-1的整数索引

#获取Series的索引和值
obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  #指定索引名
obj2

obj2.index

#与普通numpy数组相比，可以通过索引选取Series的值
obj2['a']

#通过索引赋值
obj2['d'] = 6

#根据多个索引选取
obj2[['c', 'a', 'd']]

#布尔型索引
obj2[obj2 > 0]

#一般运算（依然依赖于numpy的数组运算）
obj2 * 2
np.exp(obj2)

#series是索引值到数据值的一个映射，因此可以看成一个定长的字典
'b' in obj2       #用于需要字典参数的函数中，例如字典键的判断
'e' in obj2

#通过字典创建series，只传入字典，则键即为索引
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)      #返回的series有序排列
obj3

#同时传入字典和指定索引，字典的键与索引是否匹配-读取匹配的数据，不匹配,其索引的值为NaN
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4

#pandas的isnull和notnull可以检测缺失数据
pd.isnull(obj4)   #返回布尔型
pd.notnull(obj4)

#series的isnull
obj4.isnull()

#series会自动对齐不同索引的数据
obj3
obj4
obj3 + obj4

#series对象本身和索引都有一个“name”属性，类似于标签
obj4.name = 'population'      #设置series对象本身的“name”属性
obj4.index.name = 'state'
obj4

#通过赋值的方式就地修改series的索引
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

#dataframe的常见创建方式
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],   #等长列的字典
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)             #未指定索引则自动生成编号（0开始），列索引对应字典的键
frame

DataFrame(data, columns=['year', 'state', 'pop'])    #指定列索引


#同时传入字典和指定索引（包括行索引和列索引），
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2       #传入的列无匹配的数据为NaN

#获取索引序列
frame2.columns
frame2.index

#通过类似字典标记的方式或属性获取一个series
frame2['state']
frame2.year                 #两种方式获取series

#可以通过索引字段ix获取行
frame2.ix['three']     #获取行索引为‘three’的行数据，目前已不支持
frame2.loc['three']    #loc通过行索引名称获取
frame2.iloc[2]         #iloc通过行索引的位置获取

#赋值修改列
frame2['debt'] = 16.5  #赋值标量
frame2

frame2['debt'] = np.arange(5.)    #赋值等长序列
frame2

frame2['debt'] =[1,2,3,4,5]       #等长列表
frame2

#赋值series时，会自动匹配索引，未匹配的为缺失
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2

#创建列与删除列
frame2['eastern'] = frame2.state == 'Ohio'
frame2

del frame2['eastern']
frame2.columns

#注意，通过索引返回的子列同样是视图，若想显式的复制副本，可以通过series的copy方法
frame2['debt'].copy()

#嵌套字典的数据形式
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)
frame3         #外层键作为列索引，内层键作为行索引

#转置，交替行列索引
frame3.T

#显式指定行索引，自动匹配内键
DataFrame(pop, index=[2001, 2002, 2003])
#显式指定列索引，自动匹配外键
DataFrame(pop,columns=['Nevada','Oh'])

#由series构成的字典传入dataframe
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata)

#字典或series构成对的列表传入dataframe，各项成一行，字典键或series的索引并集成列标
alist=[{'a':1,'b':5},{'b':2},{'a':3}]
DataFrame(alist)

aseries=Series([1,2,3],index=['a','b','c'])
bseries=Series([4,5,6],index=['b','c','d'])
DataFrame([aseries,bseries])

#设置dataframe的index、columns的name属性，columns的name属性等同于它的series对象本身属性
frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3

#dataframe的value属性以二维ndarray形式显示
frame3.values

frame2.values  #若dataframe的各列数据类型不同，则值数组就会选用能兼容所有列的数据类型

#pandas的索引对象，包括行索引和列索引序列
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index       #返回index对象，类似元组
index

index[1:]              #index对象的索引与切片

index[1] = 'd'         #index对象元素不可更改

#index对象的不可修改性可以是index对象在多个数据结构之间安全共享
index = pd.Index(np.arange(3))
index
obj2 = Series([1.5, -2.5, 0], index=index)
obj2
obj2.index is index

#索引对象类似于固定大小的集合，因此也存在可用的集合方法
frame3
'Ohio' in frame3.columns
2003 in frame3.index

#series重新索引
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])  #对obj重新索引（重新排序，若某个索引值不存在，则缺失）
obj2

obj.reindex(['a', 'b', 'c', 'd', 'e','f'], fill_value=0)  #插值处理,对缺失值的处理

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3
obj3.reindex(range(6), method='ffill')                    #向前填充

#dataframe重新索引
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
frame

frame2 = frame.reindex(['a', 'b', 'c', 'd'],method='ffill')    #只传入一个序列，则重新索引行,并填充
frame2

states = ['Texas',  'Utah','California']
frame.reindex(columns=states)                #根据关键字columns重新索引列

#同时重新索引行与列，但不能填充，可能是method不能与columns关键字连用(我猜的)
frame.reindex(index=['a', 'b', 'c', 'd'], columns=states)

#若想填充缺失，需先按行重新索引并填充，再重新索引列
frame.reindex(index = ['a','b','c','d'],method='ffill').reindex(columns=states)
#注意不能先同时索引行列然后填充，这样填充不起作用（至于为什么我也不清楚）

#通过"_ix"的标签索引功能重新索引
frame._ix[['a', 'b', 'c', 'd'], states]


#丢弃series上的项，（类似于删除观测）
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
new_obj

obj.drop(['d', 'c'])

#丢弃dataframe上任意轴上的索引值（理解为删除列或行（即变量与观测））
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])

data.drop(['Colorado', 'Ohio'])     #删除行，默认axis=0

data.drop('two', axis=1)            #删除列
data.drop(['two', 'four'], axis=1)

data.drop('Ohio').drop('two', axis=1)  #同时删除行和列

#索引、选取、过滤
#series的索引、选取、过滤
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj['b']  #通过名称索引
obj[1]    #通过位置索引

obj[2:4]
obj[['b', 'a', 'd']]
obj[[3, 1]]
obj[obj < 2]         #各种索引（或切片）、筛选方式

#利用标签的切片，包括末端
obj['a':'c']
#切片（返回的视图）赋值，直接作用源数据
obj['a':'c'] = 5
obj

#dataframe的索引、选取、过滤
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
data

data['two']   #选取列
data[['three', 'one']]

data[:2]     #行的切片，类似与二维数组
data[data['three'] > 5]   #筛选第三列中大于5的数据
data < 5     #将源数据各元素与5比较，返回布尔型
data[data < 5] = 0  #通过布尔型数组赋值
data

data.ix['Colorado', ['two', 'three']]    #ix标签索引功能（ix，但ix在未来不受支持）,行在前，列在后
data._ix[['Colorado', 'Utah'], [3, 0, 1]] #通过位置选取
data.ix[2]                    #只传入一个位置参数，选取该行,默认列为全部，基于位置
data.ix['Utah']               #基于标签的索引
data.ix[2,1]                  #第一个位置参数指定行，第二个指定列
data.ix[:2,1:]                #类似于二维ndarray的切片

data.ix[:'Utah', 'two']      #扩展的标签切片功能，包括末端

data.ix[data.three > 5, :3]  #本例，布尔索引（筛选行）与切片（筛选列）结合（注意第一个条件是用来筛选行，第二个筛选列）

data.ix[data.three > 5,data.ix['Colorado']>5]  #同过data的行列表达式筛选

#算数运算的数据对其功能
s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1
s2
s1 + s2   #按series的索引自动对齐，最终索引结果为并集（存在一方缺失索引，其值为NaN，则和也为NaN）

#对于dataframe，对齐操作会同时发生在行和列上
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df1
df2
df1 + df2

#dataframe运算的插值填充
df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1
df2
df1 + df2

df1.add(df2, fill_value=0)  #注意这里的参数fill_value=0表示先进行填充0，然后再相加

df1.reindex(columns=df2.columns, fill_value=0)  #通过重新索引填充

#填充是指在生成缺失值的时机进行填充，若对已经存在的缺失值，应该使用替换函数fillna（）
df3=df2+df1
df3
df3.reindex(columns=df3.columns).fillna(0)

(df1+df2).fillna(0)  #等价

#dataframe与series之间的运算
#引例，ndarray的二维数组与一维数组的运算，即广播
arr = np.arange(12.).reshape((3, 4))
arr
arr[0]               #取第一行的值
arr - arr[0]

#dataframe-series
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.ix[0]
frame
series              #取第一行的值（为什么不可以取第一列的值）
frame - series      #沿着行一直向下广播（类似于excel下拉填充，即每行减去相应值
frame.sub(series,axis=1)  #同上

#若某个索引值在dataframe的列或series的索引找不到，则合并索引，未重叠的为NaN
series2 = Series(range(3), index=['b', 'e', 'f'])
frame + series2

#如何在列上向右广播，必须使用算数方法
series3 = frame['d']
series3
frame
frame.sub(series3, axis=0)  #沿着列一直向右广播，即每列减去相应值

#numpy的ufunc（元素级数组方法）也可用于操作pandas对象
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame

np.abs(frame)

#通过dataframe的apply方法，将函数应用到各列或各行所形成的一维数组上（序列级）
f = lambda x: x.max() - x.min()  #定义匿名函数f，返回极差

frame.apply(f)  #默认axis=0，应用到列上求每列的极差
frame.apply(f, axis=1)   #应用到行上，求每行的极差
#许多常见的数组统计功能都被实现成了dataframe的方法（如sum，mean），则无需使用apply方法

#除标量外，apply还可根据传递的函数性质返回多个值组成的series
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)    #返回每列中最小值和最大值组成的series

#python的元素级函数也可应用于dataframe，此时需使用applymap函数
format = lambda x: '%.2f' % x   #定义元素的格式匿名函数f
frame.applymap(format)

#series也有同样的应用于元素级的函数map
frame['e'].map(format)

#数据集的排序
#按索引排序
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()    #按索引排序

#对dataframe，可指定任意一个轴向排序
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])
frame.sort_index()    #默认按行索引排序

frame.sort_index(axis=1)  #按列索引排序

#默认为升序，降序用关键字ascending=False
frame.sort_index(axis=1, ascending=False)

#按值进行排序
obj = Series([4, 7, -3, 2])
obj.sort_values()   #py2.7版本无order属性，可以sort_values属性

#排序时，任何缺失值都会放在末尾
obj = Series([4, np.nan, 7, np.nan, -3, 2])  #缺失值的写法
obj.sort_values()

#dataframe根据某一列或某几列的值排序，配合关键字“by”
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame

frame.sort_index(by='b')  #sort_index将不受支持，可使用sort_values,根据单列值排序
frame.sort_values(by=['a', 'b'])  #根据多列值排序

#排名，类似于统计中的秩
#默认情况，在平级状况下，取平均排名（假设第5-第7值一样，则秩都为6），注意排名是从第1（没有第0）开始的
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()

#或者在平级下，根据在数据中出现的先后顺序排名，类似于稳定排名
obj.rank(method='first')

#降序排名，即值越大排名越靠前（越小）
obj.rank(ascending=False, method='max')    #平级状况下，以排名最大值（即排名靠后）为主

#dataframe可以在行或列上进行排名
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})
frame

frame.rank(axis=1)  #按行进行排名
frame.rank()        #默认按列进行排名

#带有重复值的轴索引
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj

#判断索引是否唯一
obj.index.is_unique
#选取具有重复索引的索引标签
obj['a']   #返回一个series

#dataframe的重复行进行索引
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
df._ix['b']       #“_ix”非常不靠谱，一会儿能用，一会儿不能用，不能用去掉前面_运行后再加上就能用，WTF

#汇总和描述统计
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
df

#按列统计
df.sum()   #返回统计各列和结果的series
#按行统计
df.sum(axis=1)     #默认自动忽略缺失值，若行或列全是缺失，则返回0（以前是返回NA）

#禁止忽略NA
df.mean(axis=1, skipna=False) #此情况下含有NA的行或列统计量为NA

#常用统计方法实例
df.idxmax()           #返回各列达到最小值的行索引（标签名）
df.values.argmin()    #返回各列达到最小值的行索引位置（整数位置）
ser=Series([1,5,2,8,6],index=list('abcde'))
ser.values.argmax()
df.quantile(0.1)

df.cumsum()          #累计和（忽略NA，除非累加到NA处，则该处累计和为NA）

#数值型描述统计量
df.describe()        #常见汇总统计，注意统计数目count（类似样本数）忽略NA

#字符型描述统计量
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()

#相关系数与协方差
#import pandas.io.data as web       #不受支持

from pandas_datareader import data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker)          #yahoo无法连接了，本例无法实现

price = DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.iteritems()})
volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.iteritems()})

returns = price.pct_change()                          #计算百分数变化
returns.tail()                                        #显示最后5项


#网上小例子
#计算百分数变化
a = np.arange(1,17).reshape(4,4)
data = DataFrame(a)
data
#计算列的百分比变化，如果想计算行设置axis=1
data.pct_change()      #新值相对旧值增加的百分比

print(data.head())    #输出前五行,默认是5，可以通过设置n参数来设置输出的行数
print(data.tail())    #输出最后五行

#计算dataframe中列与列的相关系数
#重新修改索引名
row=['a','b','c','d']
col=['one','two','three','four']
data.index
data.columns
data.rename(index={2:'mm'})           #利用rename修改单个索引名
data.rename(columns={1:'xxx'})
data.index=row                        #利用index对象修改整个索引名
data.columns=col
data

data_pc=data.pct_change()

#计算dataframe的列与列的相关系数
data_pc.one.corr(data_pc.three)

#计算dataframe的列与列的协方差
data_pc.two.cov(data_pc.four)

#返回打dataframe的各列间的相关系数与协方差，返回矩阵结果
data_pc.corr()
data_pc.cov()

#dataframe的corrwith方法可以计算其列（或行）与另一个series或另一个dataframe之间的相关系数
data_pc.corrwith(data_pc.three)       #各列与第三列的相关系数

a=randn(16).reshape(4,4)
data=DataFrame(a,index=row,columns=['one','two','four','five'])

data_pc.corrwith(data)     #按标签对其计算两个dataframe中对应列的相关系数（注意，行标也必须对应）
#传入axis=1按行计算相关系数
data_pc.corrwith(data,axis=1)  #这里计算行相关系数每行只有'one','two','four'三个有效数值

#唯一值、值计数与成员资格
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

uniques = obj.unique()
uniques
#返回的值是唯一的，但未排序
uniques.sort()   #排序

#计算series中各值出现的频率
obj.value_counts()   #按频率高低返回

#value_counts是一个顶级pd方法，可用于任何数组或序列
obj.values  #返回series值的数组
data.one    #返回series

pd.value_counts(obj.values,sort=False)      #默认按频率排序
pd.value_counts(data.one)
pd.value_counts(list('abcksbchdjufhaklxcjashdlxcjsfh'))  #计算序列元素的频率

#利用isin判断成员资格，并选取series或dataframe列中数据的子集
mask = obj.isin(['b', 'c'])  #判断series中各元素是否属于['b','c']中
mask

#利用布尔型索引选取在['b','c']中的元素
obj[mask]

#计算dataframe多个列的频率
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
data

#将pd.value_counts传递给apply（）函数即可
format = lambda x: '%.0f' % x   #定义元素的格式匿名函数f

result = data.apply(pd.value_counts).fillna(0).applymap(format)

result

#处理缺失值
#NaN标记缺失
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data

string_data.isnull()

#python内置的None标记缺失
string_data[0] = None
string_data.isnull()

string_data[string_data.values=='avocado']='ssssss'   #替换值

#滤除缺失值
from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data.dropna()

#可通过布尔型索引删除缺失
data[data.notnull()]

#dataframe默认删除含有NA的行
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
data
cleaned

#参数how='all'删除全为NA的行
data.dropna(how='all')

#删除含有NA的列
data.dropna(axis=1)

#删除全为NA的列
data[4] = NA
data
data.dropna(axis=1, how='all')

#通过thresh参数设置阈值来容忍允许的缺失值
df = DataFrame(np.random.randn(3, 7))
df.ix[1, :5] = NA; df.ix[2, 1:2] = NA
df

df.dropna(thresh=3)    #在每行至少有三个非缺失值则保留该行

#填充缺失值
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA; df.ix[:2, 2] = NA
df

df.fillna(0)    #指定值填充

df.fillna({1: 0.5, 2: -1})  #指定列填充指定值，通过字典实现类型

#填充缺失值后，就地修改源数据
_ = df.fillna(0, inplace=True)  #'_'作为临时性名称使用，在后面并不会再次使用该名称（不care它）
df

#通关参数method指定插值类型
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA; df.ix[4:, 2] = NA
df

df.fillna(method='ffill')  #前向填充

df.fillna(method='ffill', limit=2)   #前向连续填充最大量为2个单位（即前向连续填充两个缺失)

#fillna（）传入函数实现多样填充功能
data = Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())   #利用平均值填充缺失

#层次化索引
#创建索引为二维的series
data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data

data.index   #返回的索引类型为MultiIndex

#选取层次化索引对象的子集
#通过外层索引标签选择
data['b']

data['b':'c']

data.ix[['b', 'd']]

#通过内层索引标签选择
data[:, 2]

#unstack方法将层次化series堆拆成dataframe
data.unstack()
#stack方法将dataframe堆成层次化series
data.unstack().stack()

#dataframe的每条轴都可以有多层索引
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])
frame

#dataframe各层的name属性指定
frame.index.names = ['key1', 'key2']        #行的外层与内存轴标签的name属性
frame.columns.names = ['state', 'color']
frame

#多层索引的dataframe的选取
frame['Ohio']   #列的外层选取
frame.ix['a']   #行的外层选取
frame.xs('Green',axis=1,level='color')    #列的内层选取，需借助列的name属性
frame.xs(1,axis=0,level=1)   #行的内层选取，无需借助name属性，level=0表示第0层（外）,level=1表示第1层（内）

#花式多层索引
frame.loc[pd.IndexSlice[:,1],pd.IndexSlice['Ohio',:]]
#pd.IndexSlice表示行或列的每一级都要选择，：表示全选，.loc（）第一个参数表示行，第二个参数表示列
#上例表明行的外层索引全选，内层索引选标签为1，列的外层索引为'Ohio'，内层索引全选

#单独创建MultiIndex
row=pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]],names=['key1','key2'])
col=pd.MultiIndex.from_arrays([['Ohio','Ohio','Colorado'],['Green','Red','Green']],
                              names=['state','color'])

#复用MultiIndex构造多层索引dataframe
frame = DataFrame(np.arange(12).reshape((4, 3)),index=row,columns=col)
frame

#多层索引的重新分级排序
frame.swaplevel('key1', 'key2')    #swaplevel接受两个级别编号或名称，返回交换级别的新对象（不改变源数据）
frame.swaplevel(-2,-1,axis=1)      #通过级别编号和axis关键字交换列级别

#排序（按索引）
frame.sortlevel(1)    #默认axis=0（行），level=0（外层）
#注意sortlevel is deprecated, use sort_index(level= ...)
frame.sort_index(level=1)  #建议使用sort_index()

#交换索引级别并排序
frame.swaplevel(0, 1).sort_index(level=0)

#根据级别汇总统计，类似于pandas的groupby
frame.sum(level='key2')
frame.sum(level='color', axis=1)

#行索引与列（不是列索引）的转换
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
frame

#set_index函数接受dataframe的一个或多个列，并转换为行索引
frame2 = frame.set_index(['c', 'd'])   #默认转换成行索引的列会被删除
frame2
frame.set_index(['c', 'd'], drop=False) #保留转换成行索引的列

#将层次化行索引转换成列，reset_index
frame2.reset_index()  #放置列的最前面


#pandas的整数索引，对于整数型的索引标签，整数索引易产生歧义
ser = Series(np.arange(3.),index=[1,3,5])
ser[2]  #产生歧义，这里用索引标签索引而不是位置索引（列表与元组的整数索引是基于位置的）
#基于位置索引
ser.iloc[-1]  #建议使用标签索引函数，iloc，这里使用的是位置索引
ser.ix[:3]    #切片（基于标签名，包括末端），也可用loc(因为ix的支持正在消失),iloc用于获取切片的第一个值

#非整数型索引标签，不会产生歧义
ser2 = Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]
#建议使用索引标签函数
ser2.iloc[:3]  #只基于位置，一般用于整数的索引名
ser2.ix[:3]
ser2.ix['a':'c']  #即基于位置又基于标签名，但在整数的索引名中产生歧义
ser2.loc['a':'c']

#不考虑索引类型的基于位置的索引
#series的基于位置的索引
ser3 = Series(range(3), index=[-5, 1, 3])
ser3.ix[-5]
ser3.ix[-5:3]   #基于标签名的索引(非整数可以基于位置)
ser3.iloc[0]
ser3.iloc[0:2]  #基于位置索引的切片

#整数索引号的dataframe基于位置的索引
frame = DataFrame(np.arange(6).reshape((3, 2)), index=[2, 0, 1])
frame.iloc[0]      #基于位置的行
frame.iloc[0:2,0]  #基于位置的列，行位切片

#总结，当索引标签是整数时，为了不产生歧义的基于位置的索引与切片，建议使用iloc,但基于标签名的索引与切片用ix
#对于索引标签是非整数时，建议使用ix（或loc）

#面板数据，相当于多个dataframe
#利用三维数组创建
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print p   #Items axis（axis=0），有几个dataframe
#Major_axis（axis=1），dataframe的索引（行）
#Minor_axis（axis=2），dataframe的列

#利用一个由多个dataframe对象组成的字典创建
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p   #结果自动匹配行与列的大小，“长板”原则，本例最终由两个Items，每个Items的大小为4*3（缺少的为缺失值）

#创建空面板
p1 = pd.Panel()
print p1

#选择数据
p['Item1']
p.Item1

p.major_xs(1)  #行,每个Item的第1行
p.minor_xs(0)  #列,每个Item的第0列

#综合选取
p.ix['Item1',:2,0]
p.Item1.iloc[:2,0]

#交换轴索引,未来取消支持，建议转为多层次索引的dataframe
p.swapaxes('items','minor')
p.swapaxes(0,2)

#panel转换为多层的dataframe
p.to_frame()   #默认过滤缺失的列或行
p.to_frame().to_panel()
p.to_frame().to_xarray()    #to_panel在未来将不受支持

