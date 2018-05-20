# -*- coding: utf-8 -*-
#数组创建函数
'''
函数                    说明
array                  将输入数据（列表、元组、数组或其他序列类型）转换为ndarray。数据类型要么python推断，要么显示指定
asarray                将输入转化为ndarray，如果输入本身就是ndarray就不进行复制
arange                 类似内置的range，但返回的是数组而不是列表
ones或ones_like        根据指定的形状和dtype创建一个全为1的数组，like表示是参考另一个数组的形状和dtype
zeros或zeros_like      全为0
empty或empty_like      初始化数组的元素
eye、identity          创建一个N*N的单位矩阵
'''

#多维数组的数据类型
'''
类型                         类型代码（或简写）     说明
int8、uint8                  i1、u1             有符号和无符号的8位（1个字节）整型
int16、uint16                i2、u2             
int32、uint32                i4、u4          
int64、uint64                i8、u8
float16                      f2                半精度浮点数
float32                      f4（f）            标准的单精度浮点数
float64                      f8（d）            标准的双精度浮点数，与c的double型兼容
float128                     f16（g）           扩展精度浮点数
complex64                    c8                 用32位的浮点数表示的复数
complex128                   c16                  64位
complex256                   c32                  128位
bool                                            存储True和False的布尔类型
object                       O                  python对象类型
string_                      S                  S10表示创建长度为10的字符串
unicode_                     U                  固定长度的unicode类型，跟字符串定义方式一样，如U10
'''

#数组的通用函数ufunc
#一元函数
'''
函数                  说明
abs、fabs             绝对值计算，对于非复数，可以使用更快的fabs
sqrt                  计算各元素的平方根，相当于arr**0.5
square                平方
exp                   各元素（x）的指数e^x
log                   自然对数
log10、log2           10为底，2为底
log1p                 log（1+x）
sign                  符号
ceil                  向上取整
floor                 向下取整
rint                  将各元素值四舍五入整数，但保留dtyp
modf                  将小数和整数以两个独立的数组形式返回
isnan                 返回一个表示“哪些值是NaN（这不是一个数字）”的布尔型数组
isfinite、isinf       分别返回“是否有穷的”、“是否无穷的”的布尔型数组
cos、cosh             普通型和双曲型三角函数
sin、sinh
tan、tanh
arccos、arcsosh
arcsin、arcsinh
arctan、arctanh       反三角
logical_not           计算各元素的not x的真值，即~arr
'''
#二元函数
'''
函数                  说明
add                   对应的元素相加
subtract              第一个数组的元素减去第二个数组的元素
multiply              数组元素相乘
divide                除
floor_divide          向下圆整除（丢弃余数）
power                 第一个数组元素的对应第二个数组元素的次方
maximum、fmax         比较大小，fmax将忽略NaN
minimum、fmin
mod                   求模计算（求余数）
copysign              将第二个数组元素的符号赋给第一个数组元素
greater               比较运算，相当于>最终产生布尔型数组
greater_equal         >=
less、less_equal      <、<=
equal、not_equal      ==、!=
logical_and           执行元素间的真值逻辑运算，相当于&
logical_or            |
logical_xor           ^（异或）
'''

#基本数组统计方法
'''
函数（方法）            说明
sum                   计算数组全部或某一轴向的和，零长度的数组sum为0
mean                  算数平均，零长度的mean为NaN
std、var              标准差、方差，自由度可调（默认为n）
min、max              
argmax、argmin        最大、最小元素的索引
cumsum                累积和
cumprod               累计积   
'''

#常见的数组集合运算
'''
函数（方法）            说明
unique（x）            计算x数组中的唯一元素，并返回有序结果
intersect1d（x,y）     交集（公共元素），返回有序结果
union1d（x，y）        并集，返回有序结果
in1d(x,y)             x是否是y的子集，返回布尔型数组
setdiff1d（x，y）      差集
setxor1d（x，y）       对称差（异或），存在于一个数组但不同是存在于两个数组中的元素
'''
#常见的numpy.linalg函数
'''
函数（方法）            说明
diag                  以一维数组的形式返回方阵的对角线（或非对角线）元素；或者将一维数组转化为方阵（非对角线元素为0）
dot                   矩阵乘法
trace                 计算对角线元素的和
det                   计算矩阵行列式
eig                   计算方阵特征值与特征向量
inv                   计算方阵的逆
pinv                  计算矩阵的Moore_Penrose伪逆
qr                    计算QR分解
svd                   计算奇异值分解
solve                 计算线性方程组Ax=b的解，其中A为方阵
lstsq                 计算Ax=b的最小二乘解
'''

#常见的numpy.random的函数
'''
函数                  说明
seed                 确定随机数生成器的种子
permutation          返回一个序列的随机排列或返回一个随机排列的范围
shuffle              对一个序列就地随机排列
rand                 产生均匀分布的样本值
randint              从给定的上下限范围随机产生整数
randn                产生标准正态分布（0,1）
binomial             二项分布
normal               正态分布
beta                 beta分布
chisquare            卡方分布
gamma                gamma分布
uniform              [0,1)均匀分布 
'''
