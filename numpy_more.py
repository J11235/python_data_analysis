# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:02:35 2017

@author: ranjing
"""
import numpy as np
import pandas as pd
arr=np.array(np.random.rand(15))
arr.reshape(5,-1)
arr1=np.ones((3,5))
arr.reshape(arr1.shape)
arr.ravel() ## 散开 #改变了原数据
arr1.flatten() ##散开 返回副本
arr1

# 行优先 和 列优先 分别被称为 C 和 Fortran 顺序
arr=np.arange(15).reshape(3,-1)
arr.ravel()
arr.ravel('F') #按照列优先，扁平化。
arr.reshape((5,3),order='F') # Fortran 顺序


#数据的合并和拆分
arr1=np.ones((3,5))
arr1
arr2=np.random.randn(15).reshape(arr1.shape)
arr2
np.concatenate([arr1,arr2],axis=0)
np.concatenate([arr1,arr2],axis=1)

np.hstack([arr1,arr2]) # 水平 horizon 
np.vstack([arr1,arr2]) # 垂直 vertical


# pandas 中
from pandas import DataFrame
frame1=DataFrame([[1,2,3],[4,5,6]])
frame2=DataFrame([[7,8,9],[10,11,12]])
pd.concat([frame1,frame2],ignore_index=True)

pd.concat([frame1,frame2],axis=1,ignore_index=True)






#元素重复操作
arr=np.arange(3)
arr.repeat(3)
arr.repeat([2,3,4])
arr1.repeat([1,2,3],axis=0) #在垂直方向上，分别重复1,2,3次。

## 花式索引的替代，take & put
arr=np.random.randn(1000,50)
inds=np.random.permutation(1000)[:500]

%timeit arr[inds]
%timeit arr.take(inds,axis=0) # 速度更快

##广播
frame=np.random.randn(20).reshape(4,-1)
m=frame.mean(1).reshape((4,1))
n=frame-m
n.mean(1)

k=frame.mean(0)
l=frame-k
l.mean(0)

frame[:2]=np.array([[1],[2]]) #重新赋值
frame

arr=np.zeros((4,5))
arr[:]=1
arr
arr[:]=np.arange(4).reshape(4,1)
arr
arr[:]=np.arange(5)
arr

##ufunc 高级应用

#reduceat
arr=np.arange(100)
np.add.reduceat(arr,[0,10,30,50]) #分组求和
#outer
arr=np.multiply.outer(np.arange(4),np.arange(5))
arr
#在数组中先分组，再求和。
np.add.reduceat(arr,[0,2,4],axis=1) 


##排序

values=np.random.permutation(10)
values
indexer=np.argsort(values)
indexer
values[indexer]
values[indexer][::-1] # 逆序

arr=np.random.randn(20).reshape(4,5)
arr[:,np.argsort(arr[2])] # 第二行 是从小到大的
arr[np.argsort(arr[:,0]),:] # 第0列是从小到大的

frame=DataFrame(arr)
frame
frame.sort_index(by=0,ascending=False) # 根据第0列的值进行排序，降序。
frame.sort_values(by=0,ascending=False,axis=1) # 作用同上。

frame.sort_index(by=0,ascending=False,axis=1)


a=[3,1,5,4,2]
a.sort()
a
a.sort(reverse=False)
a

sorted(a)



##自定义分组求均值
labels=np.array([3,4,5]).repeat([100,200,300])
data=np.random.randn(600)
Series(data).groupby(labels).mean()


##一些扩展

#cython



























