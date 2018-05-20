# -*- coding: utf-8 -*-
import numpy as np
from numpy.random import randn
data={i:randn() for i in range(7)}
data

?data    #在变量的前面或后面加入？，显示有关该对象的一些通用信息

help(data)
help(data.pop)    #寻求帮助

def add_number(a,b):
	'''
	两个数字相加
	返回和
	--------
	:param a:
	:param b:
	:return:
	'''
	return a+b

add_number?     #在函数或类的前或后添加？，则其docstring（如果有）也会被显示出来
add_number??    #？？可以显示函数源代码
help(add_number)   #通过help可以返回函数或类、包等的docstring

#%run 加python脚本文件名（包括路径），可以运行该文件


a=np.random.randn(100,100)
%timeit np.dot(a,a)    #带%的命令是ipython的魔术命令，%timeit指执行这段代码的时间

%reset?      #魔术命令大多带有选项，在其后添加？可以查看选项说明
%quickref    #显示ipython的快速参考
%magic       #显示所有魔术命令的详细文档

%pwd         #返回系统当前的工作路径

#利用%time 和 %timeit测试代码运行时间
strings=['foo','foobar','baz','qux','python','i am a student']*100000
%time method1=[x for x in strings if x.startswith('foo')]    #执行一次的时间
%time method2=[x for x in strings if x[:3]=='foo']

%timeit method1=[x for x in strings if x.startswith('foo')]  #执行多次的平均时间
%timeit method2=[x for x in strings if x[:3]=='foo']



#函数性能分析
import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
	K=100
	results=[]
	for _ in xrange(niter):
		mat= np.random.randn(K,K)
		max_eigenvalue=np.abs(eigvals(mat)).max()
		results.append(max_eigenvalue)
	return results
some_results=run_experiment()
print 'Largest one we saw: %s' % np.max(some_results)

%prun run_experiment()     #函数的性能测试

%prun -l 7 -s cumulative run_experiment()  #打印限制7行，按累积时间排序

%prun?   #查看%prun的选项说明


%run -p -s cumulative E:/xhy_python/pyforda/ch3/cprof_example.py   #通过py文件测试也可以，注意命令为%run -p
