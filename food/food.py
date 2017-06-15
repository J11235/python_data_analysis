# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:03:28 2017

@author: ranjing
"""

import requests
import os
import json
# 下载 和 读取数据
url="https://raw.githubusercontent.com/wesm/pydata-book/master/ch07/foods-2011-10-03.json"
food=requests.get(url)
os.mkdir('./food/')
cd ./food
with open('./food.json','w',encoding='utf-8') as f:
    f.write(food.text)

# db=[json.loads(line) for line in open('food.json')]
db=json.load(open('food.json'))
len(db)
db[1].keys()
frame=DataFrame(db)
frame.head()

db[0]['nutrients']
len(db[0]['nutrients']) # 162
nutrients=DataFrame(db[0]['nutrients'])
nutrients.head()

info_keys=['description','group','id','manufacturer']
info=DataFrame(db,columns=info_keys)
info.head()

##group
info['group']
pd.value_counts(info.group)[:10]

#分析营养成分
nutrients=[]

for food in db:
    f=DataFrame(food['nutrients'])
    f['id']=food['id']
    nutrients.append(f)

nutrients=pd.concat(nutrients,ignore_index=True)    
nutrients.duplicated().sum()
nutrients=nutrients.drop_duplicates()
nutrients.shape
nutrients.head()

# change name
f={'description':'food','group':'fgroup'}
info=info.rename(columns=f,copy=False)

## merge
info.head()
nutrients.head()

ndata=pd.merge(nutrients,info,on='id',how='outer')
ndata.head()
ndata['fgroup'].drop_duplicates()

#根据实物类别和成分 分组，然后取中位数
results=ndata.groupby(['fgroup','description'])['value'].quantile(0.5)

results['Nut and Seed Products']











































