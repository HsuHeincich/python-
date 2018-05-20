# -*- coding: utf-8 -*-
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)

%pwd

#读取文本文件、读取其他格式文件、架子啊数据库中的文件、利用Web API操作网络资源

#读取文本格式的数据
!type E:\xhy_python\pydata-book-1st-edition\ch06\ex1.csv

path='E:/xhy_python/pydata-book-1st-edition/ch06/ex1.csv'

#通过read_csv和read_table读取ex1
df = pd.read_csv(path)         #read_csv默认逗号分隔符
df

pd.read_table(path, sep=',')   #read_table需要指定分隔符

#读取的文本文件没有标题行
!type E:\xhy_python\pydata-book-1st-edition\ch06\ex2.csv
#pandas自动分配标题行
path='E:/xhy_python/pydata-book-1st-edition/ch06/ex2.csv'
pd.read_csv(path,header=None)   #第一行不作为标题行，则pandas自动分配标题行
pd.read_csv(path, names=['a', 'b', 'c', 'd', 'message']) #指定标题行

#读取过程，将指定列作为索引（行），index_col
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv(path, names=names, index_col=4)         #指定列位置作为行索引
pd.read_csv(path, names=names, index_col='message') #指定列名作为行索引

#index_col传入指定列编号或列名组成的列表生成层次化索引
!type E:\xhy_python\pydata-book-1st-edition\ch06\csv_mindex.csv

path='E:/xhy_python/pydata-book-1st-edition/ch06/csv_mindex.csv'

parsed = pd.read_csv(path, index_col=['key1', 'key2']) #index_col指定多个列的列表生成层次化索引
parsed

#利用正则表达式作为分隔符
path='E:/xhy_python/pydata-book-1st-edition/ch06/ex3.txt'
list(open(path))           #由数量不定的空格作为分隔符

result = pd.read_table(path, sep='\s+')  #'\s+'表示匹配一个或多个空格符
result                                   #pandas推断第一列为索引（行），因为有列名的数量比列的数量少1

#参数skiprows跳过指定行
!type ..\pydata-book-1st-edition\ch06\ex4.csv

pd.read_csv('../pydata-book-1st-edition/ch06/ex4.csv', skiprows=[0, 2, 3])

#读取文件的缺失值处理
!type ..\pydata-book-1st-edition\ch06\ex5.csv

#默认对NA、-1.#IND、NULL标记识别为缺失
result = pd.read_csv('../pydata-book-1st-edition/ch06/ex5.csv')
result
pd.isnull(result)

#na_values用于接受一组用于表示缺失值的字符串
result = pd.read_csv('../pydata-book-1st-edition/ch06/ex5.csv', na_values=['NULL'])
result

#可以借用字典为各列设置不同的缺失值标记
sentinels = {'message''message': ['foo', 'NA'], 'something': ['two']}
#将'message'列的'foo', 'NA'标记为缺失值，'something'列的‘two’标记为缺失值
pd.read_csv('../pydata-book-1st-edition/ch06/ex5.csv', na_values=sentinels)

#逐块读取文本文件
result = pd.read_csv('../pydata-book-1st-edition/ch06/ex6.csv')
result
pd.read_csv('../pydata-book-1st-edition/ch06/ex6.csv',nrows=5)   #读取前5行

#设置文件块的大小，逐块读取
chunker = pd.read_csv('../pydata-book-1st-edition/ch06/ex6.csv', chunksize=1000)
chunker    #对象类型为TextParser，该对象有10000/1000个元素（10），每个元素是一个dataframe，大小为1000行

tot = Series([])
for piece in chunker:       #遍历chunker的每个元素
	print piece['key'].value_counts()   #打印每个元素‘key’列的值计数结果，返回的是series
	tot = tot.add(piece['key'].value_counts(), fill_value=0)
#巧妙利用series的值相加的自动对齐功能，重叠的索引名相加，不重叠的为缺失，这里由于空的series与第一个元素的series
#相加会全部为空，则利用fill_value填充缺失值（注意是先填充后相加），可参见下面的例子
tot = tot.sort_values(ascending=False)  #series无order属性，可用sort_values
tot

#空series与非空series相加，两种情况对比分析
Series([]).add(Series([1,2,3],index=['a','b','c']))                #全为空
Series([]).add(Series([1,2,3],index=['a','b','c']),fill_value=0)   #正常，说明先填充缺失再相加

#写入文本
data = pd.read_csv('../pydata-book-1st-edition/ch06/ex5.csv')
data

#to_csv写入csv文件
data.to_csv('../pydata-book-1st-edition/ch06/out.csv')
!type ..\pydata-book-1st-edition\ch06\out.csv

#写到sys.stdout仅仅是打印结果而已，分隔符为‘|’
data.to_csv(sys.stdout, sep='|')

#将输出结果的缺失值指定表示为‘NULL’
data.to_csv(sys.stdout, na_rep='NULL')

#禁用行标签和标题行
data.to_csv(sys.stdout, index=False, header=False)

#指定写入部分列，并指定写入顺序
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

#series的to_csv方法
dates = pd.date_range('1/1/2000', periods=7)   #range的日期范围
ts = Series(np.arange(7), index=dates)
ts.to_csv('../pydata-book-1st-edition/ch06/tseries.csv')
!type ..\pydata-book-1st-edition\ch06\tseries.csv