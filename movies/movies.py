# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:00:29 2017

@author: ranjing
"""

import requests
import pandas as pd
import numpy as np
#下载保存数据
movies=requests.get("https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/movies.dat")
ratings=requests.get("https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/ratings.dat")
users=requests.get("https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/movielens/users.dat")    
with open('./movies.txt','w',encoding='utf-8') as f:
    f.write(movies.text)
with open('./ratings.txt','w',encoding='utf-8') as f:    
    f.write(ratings.text)
with open('./users.txt','w',encoding='utf-8') as f:
    f.write(users.text)

#读取数据
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.txt',sep="::",header=None,names=unames)    

rnames=['user_id','movie_id','rating','timestap']
ratings=pd.read_table('ratings.txt',sep="::",header=None,names=rnames)

mnames=['movie_id','title','genres']
movies=pd.read_table('movies.txt',sep="::",header=None,names=mnames)

users[:5]
ratings[:5]
movies[:5]

#汇集数据
data=pd.merge(pd.merge(ratings,users,on='user_id'),movies,on='movie_id')
##保存数据
with open('movie_data.txt','w',encoding='utf-8') as f:
    f.write(data)
data[0:1] #查看第一行
data.ix[0]# 查看第一行

##分类汇总 picot_table(透视表)
mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc=[np.mean,len],fill_value=0)
mean_ratings[:5]
mean_ratings[('mean','F')] # 层次化索引

''' 和上面作用一样
mean_ratings=pd.pivot_table(data,index='title',columns='gender',values='rating',aggfunc=[np.mean,len])
mean_ratings[:5]

mean_ratings=pd.pivot_table(data,index=['title','genres','gender'],values='rating',aggfunc=[np.mean])
mean_ratings[:50]
'''

##active titles
ratings_by_title =data.groupby('title').size()
active_titles=ratings_by_title[ratings_by_title>250].index
mean_ratings=mean_ratings.ix[active_titles]

''' 和上面的作用一样
ratings_by_title=data.pivot_table(index='title',values='genres',aggfunc=len)
active_titles=ratings_by_title[ratings_by_title>250].index
mean_ratings.ix[active_titles]
'''

##排序
mean_ratings.sort_index(by=('mean','F'),ascending=False) # 层次化索引 by=('mean','F')

##计算男女评分分歧
mean_ratings['diff']=np.abs(mean_ratings[('mean','F')]-mean_ratings[('mean','M')]) # 增加一行
mean_ratings_sort_by_diff=mean_ratings.sort_index(by='diff',ascending=False)

##计算评分波动
rating_std=data.groupby('title')['rating'].std()[active_titles]
#rating_std=pd.DataFrame(rating_std,columns=['std']) # 没有加[]的时候，显示错误Index(...) must be called with a collection of some kind, 'std' was passed
rating_std[:5]
rating_std.order(ascending=False)[:10]




























