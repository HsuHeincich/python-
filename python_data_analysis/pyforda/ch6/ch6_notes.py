# -*- coding: utf-8 -*-

#pandas的解析函数
'''
函数                 说明
read_csv            读取csv文件，默认逗号为分隔符
read_table          默认分隔符为‘\t’
read_fwf            读取定宽列格式数据（无分隔符）
read_cliboard       读取剪贴板中的数据，可以看做read_table的剪贴板版，在将网页转化为表格时很有用
'''

#read_csv或read_table函数的参数
'''
参数                说明
path               文件位置
sep或delimiter     分隔符形式（或正则表达式表示的形式）
header             用作列名的行号，默认为0，若没有标题行，则为None
index_col          用作行索引的列编号或列标签名，可以是单个也可以是多个组成的列表
names              指定比标题名，结合header=None
skiprows           需要忽略的行数（从文件开始处算起），或指定的行号列表
na_values          一组用于替换NA的值
comment            用于将注释信息从行尾拆分出去的字符（一个或多个）
parse_dates        尝试将数据解析为日期，默认为False。如果为True，则尝试解析所有列。
                   此外也可以指定需要解析的一组列号或列名的列表。如果列表的元素为列表或元组，则会将该内层列表或元组的
                   元素结合到一个列在进行解析工作（主要合并分在多个列的日期）。如果由列表组成的字典，则键作为合并后的列名
keep_date_col      若连接多列解析时间，则保留原始列。默认为False
converters         由列号/列名跟函数之间的映射组成的字典，例如{'foo':f}会对‘foo’列的所有值应用函数f
dayfirst           当解析有歧义的日期时，将其看做国际格式（例如7/6/2012→→→June 7,2012）。默认为False
date_parser        用于解析日期的函数
nrows              需要读取的行数（从文件开始处算起）
iterator           返回一个TextParser以便逐块读取文件
chunksize          文件块的大小
skip_footer        需要忽略的行数（从文件末尾处算起）
verbose            打印各种解析器输出信息，比如“非数值列中缺失值的数量”等
encoding           用于unicode的文本编码格式。例如“utf-8”表示用“UTF-8”编码的文本
squeeze            如果数据经解析只剩下一列，则返回series
thousands          千分位分隔符，默认为False
'''
