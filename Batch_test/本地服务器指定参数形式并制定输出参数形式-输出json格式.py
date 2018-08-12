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


" Read excel."
df = pd.read_csv(r"D:\Heinrich\deriveFeatureData\deriveFeatureData.csv")

" Select train and test data."
train_test_bool = (df["data_use"] == "train and test")
df_train_test = df.loc[train_test_bool, :]

" Select validation data."
validation_bool = (df["data_use"] == "validation")
df_validation = df.loc[validation_bool, :]

#train
" Select Cash Off data."
cash_off_bool = (df_train_test["cus_group"] == "cashoff")
df_cash_off = df_train_test.loc[cash_off_bool, :]

" Select Cons On data."
cons_on_bool = (df_train_test["cus_group"] == "conson")
df_cons_on = df_train_test.loc[cons_on_bool, :]

" Select Revoloan off data."
revoloan_bool = (df_train_test["cus_group"] == "revoloan")
df_revoloan = df_train_test.loc[revoloan_bool, :]

#validation
" Select Cash Off  data."
cash_off_val_bool = (df_validation["cus_group"] == "cashoff")
df_cash_off_val = df_validation.loc[cash_off_val_bool, :]

" Select Cons On data."
cons_on_val_bool = (df_validation["cus_group"] == "conson")
df_cons_on_val = df_validation.loc[cons_on_val_bool, :]

" Select Revoloan off data."
revoloan_val_bool = (df_validation["cus_group"] == "revoloan")
df_revoloan_val = df_validation.loc[revoloan_val_bool, :]

" Define Re-post function for requests."


def request_recursion(df, start, url, featureName, Version, path):
	""" Convert dataFrame to json by row and request url by post.

	Parameters
	-----------
	df: pandas.DataFrame
		DataFrame need to be converted to json.

	index: int
		the row number of df.

	url: str
		URL need to be requested by post.

	featureName: str
		the value of json.

	Version: str
		the value of json.

	path: str
		the path need to be opened.

	Return
	-------
	response: responese need to be writen to local txt.
	"""

	" Check the type of parameters."
	if type(df) != type(pd.DataFrame()):
		raise TypeError("df must be pandas.DataFrame.")
	if type(start) != int:
		raise TypeError("index must be int.")
	if type(url) != str:
		raise TypeError("url must be str.")
	if type(featureName) != str:
		raise TypeError("featureName must be str.")
	if type(Version) != str:
		raise TypeError("Version must be str.")
	if type(path) != str:
		raise TypeError("path must be str.")

	" Add reties and close redundant links."
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	s.keep_alive = True

	try:
		" Generate dict and dumps json."
		for i in range(start, df.shape[0]):
			" Initilize dict."
			init_dict = {"appName": "FEATURE_API",
						 "featureName": 'featureDerive_S30',
						 "version": 'V_10_0',
						 "traceId": {
							 "cus_num": -99,
							 "cus_num_raw": -99,
							 "cus_group": -99,
							 "date_use": -99,
							 "flagy": -99
						 },
						 "bizParam": {
							 "inparam":
								 {
									 "name": -99,
									 "id": -99,
									 "cell": -99,
									 "user_date": -99}
						 }
						 }

			init_dict["traceId"]["cus_num"] = df.iloc[i, 0]
			init_dict["traceId"]["cus_num_raw"] = str(df.iloc[i, 1])
			init_dict["traceId"]["cus_group"] = df.iloc[i, 3]
			init_dict["traceId"]["date_use"] = df.iloc[i, 4]
			init_dict["traceId"]["flagy"] = str(int(df.iloc[i, -2]))
			init_dict["bizParam"]["inparam"]["name"] = df.iloc[i, 5]
			init_dict["bizParam"]["inparam"]["id"] = df.iloc[i, 6]
			init_dict["bizParam"]["inparam"]["cell"] = df.iloc[i, 7]
			init_dict["bizParam"]["inparam"]["user_date"] = str(df.iloc[i, 2])

			r = requests.post(url, json.dumps(init_dict))

			# str(r.text)
			result=json.loads(str(r.text))
			result=result['resultData']['featureDerive_S30_V_10_0']
			result = json.loads(str(result))
			prob=result['probability']

			final_result = {
				"appName": "FEATURE_API",
				"featureName": featureName,
				"version": Version,
				"result_prob": -99,
				"traceID": {
					"cus_num": -99,
					"cus_num_raw": -99,
					"cus_group": -99,
					"date_use": -99,
					"flagy": -99},
			}

			final_result["result_prob"] = prob
			final_result["traceID"]["cus_num"] = init_dict["traceId"]["cus_num"]
			final_result["traceID"]["cus_num_raw"] = init_dict["traceId"]["cus_num_raw"]
			final_result["traceID"]["cus_group"] = init_dict["traceId"]["cus_group"]
			final_result["traceID"]["date_use"] = init_dict["traceId"]["date_use"]
			final_result["traceID"]["flagy"] = init_dict["traceId"]["flagy"]

			j_result = json.dumps(final_result)
			with codecs.open(path, "a", "utf-16") as j:
				j.write(j_result + "\n")
				print("编号：%d 数据写入完成...." % i)




	except Exception as e:
		print("Exception: {}".format(e))

	finally:
		if i < df.shape[0]-1:
			request_recursion(df, i, url, featureName, Version, path)


url = "http://127.0.0.1:8088/feature/v1/get_data"
path=r'D:\Heinrich\S30\Train_Test_Cash_Off_train_S30'

request_recursion(df_cash_off,0,url,'featureDerive_S30','V_10_0',path)

















