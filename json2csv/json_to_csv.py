#-*-coding:utf-8-*-
import csv
import json
import codecs
import os

os.chdir(r'D:\Heinrich\转换测试')
def json_to_csv(name):
	jsonData = codecs.open(name+'.json', 'rb', 'utf-16')
	# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
	# csvfile = open(path+'.csv', 'wb') # python2下
	csvfile = open(name+'.csv', 'w', newline='')  # python3下
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)   #对所有写入的字段加‘’
	#初始化想要的字段，转为字典
	init_dict={
		'featureName':None,
		'prob':None,
		'flagy':None
	}

	flag = True
	for line in jsonData:
		#判断是否带BOM字符
		if line.startswith(u'\ufeff'):
			line = line.encode('utf8')[3:].decode('utf8')
		dic = json.loads((line[0:-1]))

		init_dict['featureName'] = dic['featureName']
		prob=dic['result_prob']
		init_dict['prob'] = prob
		init_dict['flagy'] = dic['traceID']['flagy']

		if flag:
			# 获取属性列表
			keys = list(init_dict.keys())
			# print(keys)
			writer.writerow(keys)  # 将属性列表写入csv中
			flag = False
		# 读取json数据的每一行，将values数据一次一行的写入csv中
		writer.writerow(list(init_dict.values()))
	jsonData.close()
	csvfile.close()

json_to_csv('Train_Test_Cash_Off_train')