# -*- coding: utf-8 -*-
path = 'E:/xhy_python/pydata-book-1st-edition/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()     #读取文件中的一行


import json
path = 'E:/xhy_python/pydata-book-1st-edition/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]    #json模块的loads函数逐行加载文件，并将每行转换成字典对象，方括号为列表推导式
records[0]                  #访问第0个元素
records[0]['tz']            #访问第0个元素键为‘tz’的键值
print records[0]['tz']      #打印形式（不是编码格式）

time_zones = [rec['tz'] for rec in records]   #导出records里的所有时区，发现有的记录不包括‘tz’字段

time_zones = [rec['tz'] for rec in records if 'tz' in rec]   #过滤掉没有‘tz’字段的记录
time_zones[:10]

def get_counts(sequence):  #统计序列中各元素出现的次数
	counts={}
	for x in sequence:
		if x in counts:
			counts[x]+=1
		else:
			counts[x]=1
	return counts


from collections import defaultdict   #利用collection的defaultdict统计序列中个元素出现的次数
def get_counts2(sequence):
	counts=defaultdict(int)   #字典所有的键值均会被初始化为0
	for x in sequence:
		counts[x]+=1
	return counts

counts=get_counts(time_zones)	#传入参数，计算时区序列各时区的次数

#查找字典的前10位（按字典键值排序的时区）键与键值
def top_counts(count_dict,n=10):    #定义函数，查找键值前十的键值对
	value_key_pairs=[(count,tz) for tz,count in count_dict.items()]   #将键值对以值-键元组的形式赋给变量value_key_pairs
	value_key_pairs.sort()
	return value_key_pairs[-10:]

top_counts(counts)

#利用标准库中的collections.Counter类来统计序列中出现元素最多的前十位及其出现次数
from collections import Counter
counts=Counter(time_zones)        #标准库的collections.Counter类统计序列元素及其出现次数,Counter类型（非字典类型）
top10_counts=counts.most_common(10)    #出现次数前十
print top10_counts


#利用pandas库对时区进行计数

#导入必要的库，测试
from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)


import json
path = 'E:/xhy_python/pydata-book-1st-edition/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
lines = open(path).readlines()
records = [json.loads(line) for line in lines]

from pandas import DataFrame, Series
import pandas as pd;import numpy as np

frame = DataFrame(records)    #导入数据到dataframe里
frame
frame['tz'][:10]   #显示‘tz’字段的前十行
tz_counts = frame['tz'].value_counts()   #计算‘tz’字段各值的次数，并降序
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')   #用‘Missing’替换缺失值NA
clean_tz[clean_tz == ''] = 'Unknown'       #利用布尔型数组索引将空字符串替换为‘Unknow’
tz_counts = clean_tz.value_counts()        #计算处理后的‘tz’字段的值的次数
tz_counts[:10]

plt.figure(figsize=(10, 5))
tz_counts[:10].plot(kind='barh', rot=0)   ## kind为画图类型,rot为旋转角度
import matplotlib.pyplot as plt     #防止在pycharm中不显示图，导入该类，利用plt.show（）显示图
plt.show()



#处理‘a’字段
frame['a'][1]    #‘a’字段的第1个观测
frame['a'][50]
frame['a'][51]

results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]