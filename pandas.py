# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 09:17:17 2017

@author: ranjing
"""
import pandas  as pd
from pandas import Series,DataFrame

#Series 列表是的index是0，1，2……且无法更改；series有可以更改的index
obj=Series([4,2,3,5,1])
obj.index　　#RangeIndex(start=0, stop=5, step=1)
obj.values  #values

obj2=Series([2,1,2,4],index=['d','t','a','c'])
obj2['a'] #根据index索引

obj2[obj2>2]
obj2**2

'd' in obj2 #可以将Series看成一个有序的字典

sdata={'math':90,'physics':94,'chemistry':84}
grade=Series(sdata)
pd.isnull(grade)

grade.index.name='discipline'
grade.name='Grade'
grade

#DataFrame
data={'name':['a','b','c','d'],
      'year':[2011,2008,2013,2016],
      'gpa':[3.2,3.6,3.6,2.9]}
frame=DataFrame(data)
frame
frame=DataFrame(data,columns=['name','year','gpa']) #指定列的顺序
frame2=DataFrame(data,columns=['name','year','gpa'],index=['one','two','three','four'])

frame['name']  #列索引
frame.name# 同上
frame2.ix['one'] #行索引
frame2.ix[['one','three'],['name','gpa']] # 同时索引行和列

frame2['university']='ucas' #增加一列
frame2.ix['five']=['d','2012','3.5','ucas'] #增加一行
del frame2['university'] # 删除一列
frame2.drop('five') #删除一行
frame2.drop('university',axis=1) #删除一列

##索引对象
frame2.index.name='index'
frame2.columns.name='property'
frame2.index[2]='t' # 不能更改索引，为了安全共享。
'gpa' in frame2.columns
'fou' in frame2.index


#基本功能
##重新索引
obj2
obj2.reindex(['a','c','d','t']) # 返回一个新的，obj2并没有改变
obj2.reindex(['a','b','c','d','t'],fill_value=0) # 填补缺失值# 填补缺失值 index must be monotonic increasing or decreasing

frame2
frame2.reindex(columns=['name','gpa','year','university'])

frame2.drop(['one','two'],axis=0) # 丢弃行，但axis是0，因为行的index是按列排列的！！！！！！！！！！

arr3.shape
np.mean(arr3,axis=1)  #按行求均值

frame3=DataFrame(arr3)
frame3.mean(axis=1)  #按行求均值


frame2['one':'four']
frame2['gpa']
frame2[frame2['gpa'].astype(np.float)>3] # 转换数据类型  按条件删选

#算数运算 和数据对齐
df1=DataFrame(np.arange(32).reshape((8,4)),columns=['a','b','c','d'])
df2=DataFrame(np.arange(45).reshape((9,5)),columns=['a','b','c','d','e'])
df1.add(df2,fill_value=0)
df1.reindex(columns=df2.columns,fill_value=0)

##dataframe 和 series 之间的运算
arr1=np.arange(4)
df1-arr1 # 每一行都减去了arr1, 广播
df1*arr1

##函数应用和映射

f=lambda x : x.max()-x.min()
arr3.apply(f,axis=1) #'numpy.ndarray' object has no attribute 'apply'
frame3.apply(f,axis=1)

def f(x):
    return Series([x.max(),x.min()],index=['max','min'])
frame3.apply(f,axis=1)

###排序和排名
frame2
#####sort_index
frame2.sort_index(axis=0)
frame2.sort_index(axis=1,ascending=False)
###sort value
frame2.sort_index(by='gpa')

###汇总
frame.idxmax()
frame.describe()

arr3[0].corr(arr3[1])
frame3[2].corr(frame3[1])
frame3[2].cov(frame3[1])

frame3.T.corr()

frame4=frame2.stack()
frame4.index.name='level'





















