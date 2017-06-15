# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:24:46 2017

@author: ranjing
"""

r=np.random.randn(10)
indexer=np.argsort(r)
r.take(indexer)


import os
import urllib
## 下载数据
os.makedirs('./usa.gov')
cd ./usa.gov
filename='data.txt'
local=os.getcwd()
local=os.path.join(local,filename)
url='https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
urllib.request.urlretrieve(url,local)

##读取数据
import json
records=[json.loads(line) for line in open('data.txt')] # 将json 数据格式 转化为 字典

## 纯Python对时区计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts
counts = get_counts(time_zones) # counts 是一个字典

def top_counts(count_dict,n=10): 
    value_key_pairs=[(key,count) for count,key in count_dict.items()] # (key,count)调一下顺序
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[:n]
top10_counts=top_counts(counts)


## 用pandas处理时区计数
from pandas import Series,DataFrame
import pandas as pd
frame = DataFrame(records)
tz_value_count=frame.tz.value_counts()
tz_value_count # 默认从大到小排序
##处理缺失值
clean_tz=frame['tz'].fillna("Missing") #填补缺失值
clean_tz.value_counts()
##操作系统
results=Series([x.split()[0] for x in frame.a.dropna()]) #去掉缺失值
results.value_counts()[:10]

cframe=frame[frame.a.notnull()]
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')

group=cframe.groupby(['tz',operating_system]).size().unstack().fillna(0)

indexer=group.sum(1).argsort()
type(indexer) # Seires
group.ix[indexer.values]
group.take(indexer) # 和上面一行的作用一样

frame
































