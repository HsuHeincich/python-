# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:10:22 2018

@author: Bairong
"""

import pandas as pd
import numpy as np
from time import strptime
from datetime import datetime
import os

os.chdir(r'D:\Heinrich\模型部署\scorerevoloan—S4.0上线')
# 地址数据清洗成地址明细

data_keys = pd.read_excel('3000DT数据.xlsx', encoding='gb18030', dtype=str)
data_keys.columns
data_keys['sl_user_date'] = data_keys['user_date']

#data_keys['申请日期'] = '2017-09-21'
data_test = pd.DataFrame()
data_test['cus_num'] = ['cus_num={},'.format(x) for x in data_keys['cus_num']]
data_test['name'] = ['name={},'.format(x) for x in data_keys['name']]
data_test['id'] = ['id={},'.format(x) for x in data_keys['id']]
data_test['cell'] = ['cell={},'.format(x) for x in data_keys['cell']]
#data_test['联系人手机号'] = ['linkman_cell={}'.format(x) for x in data_keys['联系人手机号']]
data_test['user_date'] = ['user_date={},'.format(x) for x in data_keys['user_date']]
data_test['sl_user_date'] = ['sl_user_date={},'.format(x) for x in data_keys['sl_user_date']]
data_test['score'] = ['score={};'.format(x) for x in data_keys['score']]
#data_test['bank_id'] = ['bank_id={};'.format(x) for x in data_keys['bank_id']]

data_test.to_excel('scoreconsoff.xlsx', index=False, encoding='utf-8')

 
import pandas as pd
import numpy as np
from time import strptime
from datetime import datetime
import os
os.chdir(r'D:\文件\信用风险识别-线上消费分期-S4.1-20180626')
# 地址数据清洗成地址明细

data_keys = pd.read_excel('test3000.xlsx', encoding='gb18030', dtype=str)
data_keys.columns
#data_keys['sl_user_date'] = data_keys['user_date']

#data_keys['申请日期'] = '2017-09-21'
data_test = pd.DataFrame()
data_test['cus_num'] = ['cus_num={},'.format(x) for x in data_keys['客户数据编号']]
data_test['name'] = ['name={},'.format(x) for x in data_keys['姓名']]
data_test['id'] = ['id={},'.format(x) for x in data_keys['身份证号']]
data_test['cell'] = ['cell={},'.format(x) for x in data_keys['手机号']]
#data_test['联系人手机号'] = ['linkman_cell={}'.format(x) for x in data_keys['联系人手机号']]
data_test['user_date'] = ['user_date={},'.format(x) for x in data_keys['申请日期']]
data_test['sl_user_date'] = ['sl_user_date={},'.format(x) for x in data_keys['特殊名单申请日期']]
#data_test['user_time'] = ['user_time={},'.format(x) for x in data_keys['当日多次申请时间']]
#data_test['custApiCode'] = ['custApiCode={},'.format(x) for x in data_keys['客户apicode']]
#data_test['biz_addr'] = ['biz_addr={};'.format(x) for x in data_keys['公司地址']]
data_test['score'] = ['score={};'.format(x) for x in data_keys['point']]

data_test.to_excel('score.xlsx', index=False, encoding='utf-8')
