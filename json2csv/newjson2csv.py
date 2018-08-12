# -*- coding: utf-8 -*-
import csv
import json
import codecs
import os
import pandas as pd


#修改1：文件路径。
os.chdir(r"D:\Heinrich\jsontest")


def json_flat(dic):
	lis = []
	init_dic = {}
	keys = list(dic.keys())
	for i in keys:
		init_dic_value = dic[i]
		if type(init_dic_value) == dict:
			init_dic_value = json_flat(init_dic_value)
			init_dic_keys = list(init_dic_value.keys())
			name = i + '_dicflag'
			init_dic[name] = 1
			if len(init_dic_keys) == 0:
				init_dic[name] = 0
			for j in init_dic_keys:
				name = str(i) + '_' + str(j)
				init_dic[name] = init_dic_value[j]
		elif type(init_dic_value) == list:
			length = len(init_dic_value)
			for j in range(length):
				name = str(i) + '_' + str(j)
				init_dic[name] = init_dic_value[j]
		else:
			init_dic[i] = init_dic_value
			lis.append(i)
		flag = False
		for i in list(init_dic.values()):
			if type(i) == dict:
				flag = True
		if flag:
			init_dic = json_flat(init_dic)
	return init_dic
'''
传入一个字典，将字典打平
由于json格式不一致，现统一格式：字段后缀带有'_dicflag'表示判断该字典是否含有该键，有为1，没有为0
命名方式为‘外键_內键1_內键2...’。
'''

def json_total(name):
	jsonData = codecs.open(name + '.txt', 'rb', 'gbk')
	# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
	# csvfile = open(path+'.csv', 'wb') # python2下
	# csvfile = open(name+'.csv', 'w', newline='')  # python3下

	total_key_list = []
	temp_dic_list = []
	for line in jsonData:
		n=line.index('{')
		line=line[n:]
		# 判断是否带BOM字符
		if line.startswith(u'\ufeff'):
			line.encode('utf8')[3:].decode('utf8')

		dic = json.loads(line)
		temp = json_flat(dic)
		key_list = list(temp.keys())
		total_key_list = list(set(total_key_list).union(set(key_list)))
		temp_dic_list.append(temp)

	jsonData.close()
	return total_key_list, temp_dic_list
'''
读取文件名，确认是.txt文本文件。返回列表，total_key_list包含所有键。temp_dic_list将所有行写成字典存储
'''


def get_total_dict(temp_dict):
	dic_ = dic.copy()
	dic_.update(temp_dict)
	# dat = pd.DataFrame.from_dict(dic_, orient='index')
	return dic_
'''
用每个字典（打平后的每行）来更新初始字典，获得规范式的字典（每行规范化）
'''


def json_to_csv(name):
	total, temp = json_total(name)
	global dic
	dic = {}					#初始字典，键为所有行键的集合，键值为-100001
	for i in total:
		dic[i] = -100001

	csvfile = open(name+'.csv', 'w', newline='')  # python3下
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)   #对所有写入的字段加‘’
	flag = True
	for index,tempdic in enumerate(temp):
		# if tempdic.startswith(u'\ufeff'):
		# 	tempdic = tempdic.encode('utf8')[3:].decode('utf8')
		newdic = get_total_dict(tempdic)
		if flag:
			keys = list(newdic.keys())
			writer.writerow(keys)
			flag = False
		writer.writerow(list(newdic.values()))
		print("编号：%d 数据写入完成...." % index)
	csvfile.close()
'''
传入写入文件名，批量写入
'''
# dat = pd.DataFrame(index=total)
#
# for temp_dic in temp:
# 	dat = pd.concat([dat, get_total_dict(temp_dic)], axis=1)
# 	dat.T.to_csv('json_test' + '.csv', index=None, encoding='gbk')


#修改2：修改写入和读取文件名
json_to_csv('json_test - 副本')