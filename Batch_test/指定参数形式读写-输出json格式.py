# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 17:58:31 2018

@author: Bairong
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 14:24:31 2018

@author: Quant
"""

import json
import codecs
import requests
import numpy as np
import pandas as pd
import time
import sys
import re
import requests
import urllib
from urllib import request
from urllib import parse
from urllib.request import urlopen
" Read excel."
f=open(r"D:\Heinrich\scoreLog\S23\lijun_zhang\Train_Test_Cash_Off.txt",'r',encoding='utf8')
data=f.readlines()
def request_recursion(df, start, url, featureName, Version, path):
	" Add reties and close redundant links."
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	s.keep_alive = True
	try:
		for i in range(start,len(df)):
			data1 = data[i]
			init_dict = {
				"model": {
					"name": featureName,
					"version": Version,

				},
				"extraData": {
					"name_source": -99,
					"id_source": -99,
					"cell_source": -99,
					"user_date": -99,
					# "com_code": "AH14780"
				},
				"apiCode": 4000826,
				"outlevel": 2,
			}

			v= data1.split('"')
			name = v[v.index("name_source")+2]
			id = v[v.index("id_source")+2]
			cell =v[v.index("cell_source")+2]
			date = v[v.index("user_date")+2]

			# init_dict["model"]["name"] = featureName
			# init_dict["model"]["version"] = Version
			init_dict["extraData"]["name_source"] = name
			init_dict["extraData"]["id_source"] = id
			init_dict["extraData"]["cell_source"] = cell
			init_dict["extraData"]["user_date"] = date


			req = parse.urlencode(init_dict).encode('utf-8')
			r = request.Request(url, req)
			result = json.loads(urlopen(r).read())
			# print(result)
			# print(type(result))
			prob = result["resultData"]["scoreLog_S3_V_1_0"]["probability"]

			final_result = {
				"appName" :"FEATURE_API",
				"featureName" : featureName,
				"version" : Version,
				"result_prob":-99,
				"traceID":{
					"cus_num" :-99,
					"cus_num_raw":-99,
					"cus_group": -99,
					"date_use":-99,
					"flagy":-99},
			}

			final_result["result_prob"] = prob
			final_result["traceID"]["cus_num"]=	v[v.index("cus_num")+2]
			final_result["traceID"]["cus_num_raw"] =	v[v.index("cus_num_raw")+2]
			final_result["traceID"]["cus_group"] =	v[v.index("cus_group")+2]
			final_result["traceID"]["date_use"] =	v[v.index("date_use")+2]
			final_result["traceID"]["flagy"]=	v[v.index("flagy")+2]

			j_result = json.dumps(final_result)
			with codecs.open(path, "a", "utf-16") as j:
				j.write(j_result + "\n")
				print("编号：%d 数据写入完成...." % i)

	except Exception as e:
		print("Exception: {}".format(e))

	finally:
		if i < len(df)-1:
			request_recursion(df, i, url, featureName, Version, path)


url = "http://192.168.23.65:18503/v1/get_score_data"
path=r'D:\Heinrich\scoreLog\S3\Train_Test_Cash_Off_train_S3'

request_recursion(data,0,url,'scoreLog_S3','V_1_0',path)

