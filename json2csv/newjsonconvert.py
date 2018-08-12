import csv
import json
import codecs
import os
import pandas as pd

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


def json_total(name):
	jsonData = codecs.open(name + '.txt', 'rb', 'gbk')
	# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
	# csvfile = open(path+'.csv', 'wb') # python2下
	# csvfile = open(name+'.csv', 'w', newline='')  # python3下

	total_key_list = []
	temp_dic_list = []
	for line in jsonData:
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


def get_total_dict(temp_dict):
	dic_ = dic.copy()
	dic_.update(temp_dict)
	# dat = pd.DataFrame.from_dict(dic_, orient='index')
	return dic_


def json_to_csv(name):
	total, temp = json_total(name)
	global dic
	dic = {}
	for i in total:
		dic[i] = -100001

	csvfile = open(name+'.csv', 'w', newline='')  # python3下
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)   #对所有写入的字段加‘’
	flag = True
	for tempdic in temp:
		newdic = get_total_dict(tempdic)
		if flag:
			keys = list(newdic.keys())
			writer.writerow(keys)
			flag = False
		writer.writerow(list(newdic.values()))
	csvfile.close()

# dat = pd.DataFrame(index=total)
#
# for temp_dic in temp:
# 	dat = pd.concat([dat, get_total_dict(temp_dic)], axis=1)
# 	dat.T.to_csv('json_test' + '.csv', index=None, encoding='gbk')

json_to_csv('json_test')