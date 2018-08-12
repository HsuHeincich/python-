# -*- coding: utf-8 -*-
A = {'A':111,'B':{'2':'b','1':{'a':23,'b':34,'c':{'xhy':'good','hhh':[3,2,'q']}},'3':[1,2,3]},'C':['a',34,{'mm':567,'gg':678}]}
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


json_flat(json_flat(A))