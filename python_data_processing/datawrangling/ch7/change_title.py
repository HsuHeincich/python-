# -*- coding: utf-8 -*-
from csv import DictReader

data_rdr = DictReader(open('E:/xhy_python/data-wrangling-master/data/unicef/mn.csv', 'rb'))
header_rdr = DictReader(open('E:/xhy_python/data-wrangling-master/data/unicef/mn_headers.csv', 'rb'))

data_rows = [d for d in data_rdr]
# '''列表生成式,代码简单易读，比循环简洁
# 类似于：
# data_rows=[]
# for d in data_rdr:
# 	data_rows.append(d)
# '''
header_rows = [h for h in header_rdr]

print data_rows[:5]
print header_rdr[:5]