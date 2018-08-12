# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pandas as pd
import os


os.chdir(r'D:\Heinrich\scoreLog\S3')
def json_to_csv(name):
	f = open(name+'.txt', 'r', encoding='utf16')
	data = f.readlines()
	init = []
	for i in range(0, len(data)):
		v = data[i].split('"')
		cusnum = v[v.index("cus_num") + 2]
		prob= (v[v.index("result_prob") + 1].split())[1]
		prob=(prob.split(','))[0]
		# prob = (v[v.index("result_prob") + 1])
		# prob = (v[v.index("result_prob") + 1]).strip(':').strip(',')
		# prob = (temp.split(","))[0]
		# prob=v[v.index("result_prob") + 2]
		prob=float(prob)
		flag = v[v.index("flagy") + 2]
		temp2 = [prob, flag, cusnum]
		init.append(temp2)

	df = pd.DataFrame(init)
	df.to_csv(name+'.csv')

json_to_csv('Train_Test_Cash_Off_train_S3')
json_to_csv('Train_Test_Cons_On_S3')
# json_to_csv('Train_Test_Revoloan_S1')
json_to_csv('Validation_Cash_Off_S3')
json_to_csv('Validation_Cons_On_S3')
# json_to_csv('Validation_Revoloan_S1')





