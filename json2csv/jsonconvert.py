import csv
import json
import codecs
import os

os.chdir(r'D:\Heinrich\jsontest')

def json_flat(dic):
	init_dic = {}
	keys = list(dic.keys())
	for i in keys:
		init_dic_value = dic[i]
		if type(init_dic_value) == dict:
			init_dic_value = json_flat(init_dic_value)
			init_dic_keys = list(init_dic_value.keys())
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
	return init_dic


def json_to_csv(name):
	jsonData = codecs.open(name+'.txt', 'rb', 'gbk')
	# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
	# csvfile = open(path+'.csv', 'wb') # python2下
	csvfile = open(name+'.csv', 'w', newline='')  # python3下
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)   #对所有写入的字段加‘’


	flag = True
	for line in jsonData:
		#判断是否带BOM字符
		if line.startswith(u'\ufeff'):
			line = line.encode('utf8')[3:].decode('utf8')
		dic = json.loads(line)

		temp=json_flat(json_flat(dic))

		if flag:
			# 获取属性列表
			keys = list(temp.keys())
			# print(keys)
			writer.writerow(keys)  # 将属性列表写入csv中
			flag = False
		# 读取json数据的每一行，将values数据一次一行的写入csv中
		writer.writerow(list(temp.values()))
	jsonData.close()
	csvfile.close()



json_to_csv('json_test')