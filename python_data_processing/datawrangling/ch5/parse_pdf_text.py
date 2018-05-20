# -*- coding: utf-8 -*-
pdf_txt = 'E:/xhy_python/data-wrangling-master/data/chp5/en-final-table9.txt'
openfile = open(pdf_txt, 'r')

# '''双行国家名的参考列表'''
double_line_countries = [
	'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Lao People\xe2\x80\x99s Democratic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]


# for line in openfile:
# 	print line

# country_line=False
# for line in openfile:
# 	if line.startswith('and areas'):
# 		country_line=True
# 	print line

# country_line=False
# for line in openfile:
# 	if country_line:
# 		print '%r' % line
# 	if line.startswith('and areas'):
# 		country_line=True

# country_line=False
# for line in openfile:
# 	if country_line:
# 		print line
# 	if  line.startswith('and areas'):
# 		country_line=True
# 	elif country_line:
# 		if line=='\n':
# 			country_line=False

# country_line=total_line=False
# for line in openfile:
# 	if country_line or total_line:
# 		print line
#
# 	if line.startswith('and areas'):
# 		country_line=True
# 	elif country_line:
# 		if line=='\n':
# 			country_line=False
#
# 	if line.startswith('total'):
# 		total_line=True
# 	elif total_line:
# 		if line=='\n':
# 			total_line=False

def turn_on_off(line, status, start, prev_line, end='\n'):
	'''
	:param line: 循环中每一行的值
	:param status: (布尔)开关变量，值为False或者	True
	:param start: 标志开始的字符串
	:param prev_line:上一行的字符串值
	:param end: 标志结束的字符串
	:return: 返回status
	'''
	if line.startswith(start):
		status = True
	elif status:
		if line == end and prev_line != 'and areas':
			status = False
	return status


def clean(line):
	'''
	清洗代码中的换行符、空格或其他特殊符号
	:param line: 需要清洗的字符串
	:return: 返回清洗后的字符串
	'''
	line = line.strip('\n').strip()
	# '''
	# 去除字符串首尾’\n‘和首尾空格
	# '''
	line = line.replace('\xe2\x80\x93', '-')
	line = line.replace('\xe2\x80\x99', '\'')
	return line


# country_line=total_line=False
# for line in openfile:
# 	if country_line or total_line:
# 		print line
#
# 	country_line=turn_on_off(line,country_line,'and areas')
# 	total_line=turn_on_off(line,total_line,'total')

countries = []
totals = []
country_line = total_line = False
previous_line = ''
# '''补充变量previous_line,并赋值为空'''

for line in openfile:

	# if country_line:
	# 	countries.append(clean(line))

	if country_line:
		# print '%r' % line
		# '''打印国名的python格式'''
		if previous_line in double_line_countries:
			line = ' '.join([clean(previous_line), clean(line)])
			countries.append(line)
		elif previous_line not in double_line_countries:
			countries.append(clean(line))
	elif total_line:
		if len(line.replace('\n','').strip())>0:
			# '''添加一行代码，防止采集空白值给totals'''
			totals.append(clean(line))
	country_line = turn_on_off(line, country_line, 'and areas', previous_line)
	total_line = turn_on_off(line, total_line, 'total',  previous_line)
	previous_line = line
	# '''将line的值赋给previous_line，进入下一个循环'''
import pprint

# pprint.pprint(countries)

test_data = dict(zip(countries, totals))
pprint.pprint(test_data)
