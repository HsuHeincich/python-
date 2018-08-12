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

" Read excel."
df = pd.read_excel(r"D:\Heinrich\deriveFeatureData.xlsx")

" Select train and test data."
train_test_bool = (df["data_use"] == "train and test")
df_train_test = df.loc[train_test_bool, :]

" Select Cash Off data."
cash_off_bool = (df_train_test["cus_group"] == "cashoff")
df_cash_off = df_train_test.loc[cash_off_bool, :]

" Select Cons On data."
cons_on_bool = (df_train_test["cus_group"] == "conson")
df_cons_on = df_train_test.loc[cons_on_bool, :]

" Select Revoloan off data."
revoloan_bool = (df_train_test["cus_group"] == "revoloan")
df_revoloan = df_train_test.loc[revoloan_bool, :]

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
						 "featureName": featureName,
						 "version": Version,
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

			time.sleep(2)

			with codecs.open(path, "a", "utf-16") as f:
				f.write(r.text + "\n")
				print("编号：%d 数据写入完成...." % i)

	except Exception as e:
		print("Exception: {}".format(e))

	finally:
		if i < df.shape[0]:
			request_recursion(df, i, url, featureName, Version, path)


url = "http://192.168.23.69:16000/feature/v1/get_data"
path=r'D:\Heinrich\S36\Train_Test_Cash_Off_S36'

request_recursion(df_cash_off,0,url,'featureDerive_S36','V_3_0',path)

















