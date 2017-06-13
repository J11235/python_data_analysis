# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:20:27 2017

@author: ranjing
"""
import numpy as np
#生成一个数组
data=np.array(
      [[1,2,3],
       [2,3,4],
       [3,4,5]])

#维一些基本方法
data.shape
data.dtype

#创建ndarray
data1=[1,2,3,4.1] #这是一个列表
###列表的基本操作
data1.append(5)
data1.pop()
data1[2:]
data1.count(1)
data1.reverse()
data1.sort()
data1

###由列表创建array
arr1=np.array(data1)
arr1
arr1.ndim

###全0(/1)
np.zeros(10)
np.zeros((3,4))
np.ones((3,4),dtype=np.float32)
np.ones_like(data) #新建一个和data有相同维度的全1矩阵

###其它方法
np.empty((3,4))
np.eye(5) # 5×5的单位矩阵
np.identity(5) #同上
np.arange(10)

#格式转换
data2=data.astype(np.float64)
data2.astype(np.int32)

#数组与标量之间的运算
data
data*data
1/data
data**3 #每个元素的三次方

#基本索引和切片

###一维
arr=np.arange(10)
arr1=arr[5:]  #包括起点
arr1[2]=0
arr #由于arr和arr1在内存中指向同一个地址，所以对arr1的改变，arr也变化了。
arr2=arr[:5].copy() # 不包括终点
arr2[0]=10
arr #没有变化

###高维
arr=np.array([[1,2,3],
              [2,3,4],
              [3,4,5]])

arr[2] #第三行
arr[2][1]
arr[2,1] #和上一行等价
arr[:2] #前两行
arr[:,:2] #前两列
arr[:2,1:]

#布尔索引
name=np.array(['a','b','a','d','c'])
data=np.random.rand(5,7)
data[name=='a']
data[name=='a',3:]

mask=(name=='a') |(name=='c')
mask

#花式索引
arr=np.arange(32).reshape(4,8)
arr[[3,2]][:,[2,3,1]] # 第3,2行，第2,3,1列
arr[[3,2],[4,5]] #(3,4),(2,5)
arr[np.ix_([1,2],[4,2,3])]
np.ix_([1,2],[3,2,4])

#转置
arr.T

#通用函数
arr=np.random.rand(5,6)*5
np.modf(arr)
np.isnan(arr)

#利用数组进行数据处理
points=np.arange(-5,5,0.1)
points1=np.arange(-4,4,0.1)
xx,yy=np.meshgrid(points,points1)
xx
yy
zz=np.sqrt(xx**2+yy**2)

#条件逻辑表达式
arr=np.random.randn(3,7)
np.where(arr>0,1,-1)
np.where(arr>0,1,arr)
arr[arr>0]=1 #作用同上

#数学统计方法

np.mean(arr,axis=0) #按列求均值
np.mean(arr)
np.sum(arr,axis=1)
np.max(arr,axis=1)

(arr>0).sum()
(arr>0).any()
(arr>0).all()

arr.sort(1)
arr
arr.sort(0)
arr


#唯一化

name=['q','q','a','b']
np.unique(name)
set(name) #集合的元素唯一
sorted(set(name)) # 整理为列表

name1=['a','b','c']
np.in1d(name1,name)

# 线性代数
data
a=np.dot(data,data.T)

from numpy.linalg import inv,qr
inv(a)
q,r=qr(a)

arr=np.random.randn(100,500)
arr1=np.where(arr>0,1,-1)
arr2=np.cumsum(arr1,axis=1)
arr2
arr2.max()
arr2.min()
arr2.max(axis=1)
mask=np.abs(arr2).max(axis=1)>30
np.sum(mask) #28

arr3=np.abs(arr2)[mask]
np.mean(np.argmax(arr3>30,axis=1))

#保存加载数据
np.save('walks',arr3)
np.load('walks.npy')





