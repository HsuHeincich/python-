# -*- coding: utf-8 -*-
import os
import codecs
import chardet
def utf2gbk(name):
	with open(name + '.txt', 'rb') as f_start:
		temp = f_start.read()
		print(chardet.detect(temp))
	with codecs.open(name+'.txt', 'r', encoding='utf-8') as f, codecs.open(name+'_new.txt', 'w', encoding='gbk') as wf:
		for line in f:
			lines = line.strip('\n')
			# newline = '{}\t{}\n'.format((lines[2]).encode('gbk'), (lines[3]).encode('gbk'))
			# newline = lines[2] + '\t'.decode('gbk') + lines[3] + '\n'.decode('gbk')
			wf.write(lines + '\n')
	with open(name + '_new.txt', 'rb') as f_end:
		temp = f_end.read()
		print(chardet.detect(temp))

utf2gbk('utf')