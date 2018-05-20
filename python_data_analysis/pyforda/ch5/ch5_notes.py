# -*- coding: utf-8 -*-
#可以输入给dataframe的数据类型
'''
类型                           说明
二维ndarray                    数据矩阵，同时传入行标和列标
由数组、列表或元组组成的字典       每个序列会变成dataframe的一列。所有序列的长度必须相同
由series组成的字典              各series成一列，若未显式指定索引，键为列索引，series索引的并集作为结果的行标
由字典组成的字典                 和上类似（内层的键值对类似于series的索引-值的映射）
字典或series的列表              各项成为dataframe的一行，字典键或series的索引的并集成为dataframe的列
由列表或元组组成的列表           类似于二维ndarray
另一个dataframe                沿用上一个dataframe的索引，除非显式地指定
numpy的MaskedArray            类似于二维ndarray，只是掩码值在dataframe的结果会变成缺失值
'''

#pandas中主要的index对象
'''
类                    说明
Index                 最泛化的Index对象，将轴标签表示为一个由python对象组成的numpy数组
Int64Index            针对整数的特殊Index
MultiIndex            “层次化”索引对象，表示单个轴上的多层索引，可以看成由元组组成的数组
DatetimeIndex          储存纳秒级的时间戳（用numpy的datetime64类型表示）
PeriodIndex            针对Period数据（时间间隔）的特殊Index
'''

#常见的Index对象的方法和属性（部分类似于集合）
'''
方法                  说明
append               连接另一个append对象，产生一个新的Index
diff                 计算差集，并得到一个Index
intersection         交集
union                并集
isin                 计算一个指示各值是否都包含在参数集合中的布尔型数组
delete               删除索引i除的元素，产生新的Index
drop                 删除传入的值，产生新的Index
insert               将元素插入到索引i处，产生新的Index
is_monotonic         各元素是否均大于前一个元素（单调）
is_unique            Index对象是否唯一
unique               计算Index的唯一值的索引
'''

#reindex的插值method
'''
参数                 说明
ffill或pad           前向填充或搬运
bfill或backfill      后项填充或搬运
'''

#reindex函数的参数
'''
参数                说明
index              行关键字
columns            列关键字
method             插值（填充）方式，注意它的问题比较多（可能是python版本的问题）
fill_value         引入指定值替代缺失
limit              填充时允许的最大填充量
level              在MultiIndex的指定级别上匹配简单索引，否则选取子集
copy               默认为True，则无论如何都复制，若为False，则新旧相等时不复制
'''

#dataframe的索引选项
'''
类型                        说明
obj[val]                   选取dataframe的单个列或一组列
obj.ix[val]                选取dataframe的单个行或一组行
obj.ix[:,val]              选取dataframe的单个列或一组列
obj.ix[val1,val2]          同时选取行和列
方法                      
reindex                    重新索引
xs                         根据标签选取单行或单列，并返回一个series
icol、irow                 根据整数位置选取单列或单行，并返回一个series
get_value、set_value       根据行标签和列标签选取单个值，前一个是选取，后一个是设置
'''

#常见的dataframe的算数方法
'''
方法                       说明
add                       用于加法+
sub                       减法-
div                       除法/
mul                       乘法*
'''

#排名平级的选项
'''
method=                   说明
'average'                 默认：在平级的分组中，为各值分配平均排名
'min'                     使用整个分组的最小排名
'max'                     使用整个分组的最大排名
'first'                   同级的分组按出现的先后顺序排名
'''

#常见统计方法的选项
'''
选项                    说明
axis                    指定轴，dataframe的行用0，列用1，（则轴向分别对应列，行）
skipna                  忽略缺失值，默认skipna=True
level                   如果轴是层次化索引（即MultiIndex），则根据level分组统计
'''

#描述统计方法汇总
'''
方法                     说明
count                   非NA值的数量
describe                常见的汇总统计
min、max
values.argmin           获得最小值的索引的位置
values.argmax
idxmin、idxmax          获得最小值、最大值索引值（索引名称，或者称行标）
quantile                分位数（0-1）
sum        
mean
median                  中位数（0.5分位数）
mad                     众数
var 
std
skew                    偏度
kurt                    峰度
cumsum                  累和
cummin、cummax          最小累和、最大累和
cumprod                 累积
diff                    一阶差分
pct_change              百分数变化
'''

#唯一值、值计数和成员资格方法（series的方法）
'''
方法                    说明
isin                   判断成员资格
unique                 计算series的唯一值
value_counts           计算色series值的频率，返回series
'''

#NA的处理方法
'''
方法                    说明
dropna                 过滤NA，可以通过阈值调节对缺失值的容忍度
fillna                 指定值填充（也可以ffill和bfill）
isnull                 返回布尔型对象
notnull
'''

#fillna()函数的参数
'''
参数                    说明
value                  指定替换值
method                 指定填充方式替换缺失
axis                   指定待填充的轴，默认axis=0
inplace                不产生副本直接修改源数据
limit                  连续填充的最大数量
'''