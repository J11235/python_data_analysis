# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:12:55 2017

@author: ranjing
"""

import os
os.mkdir( './names/')
cd ./names/

import urllib
import requests

#下载一个文件
url = 'https://raw.githubusercontent.com/wesm/pydata-book/master/ch02/names/yob1880.txt'
filename = url.split('/')[-1]

os.mkdir('./names_data')
cd ./names_data
local=os.getcwd()
local=os.path.join(local,filename)
urllib.request.urlretrieve(url,local) #储存路径需要事先存在

''' 和上面的作用一样
r=requests.get(url)
with open(filename,'w',encoding='utf-8') as f: #储存路径可以事先不存在。
    f.write(r.text)
'''

##下载多个文件
for i in np.arange(131):
        url_1=url.replace('1880',str(1880+i))
        filename = url_1.split('/')[-1]
        r=requests.get(url_1)
        with open(filename,'w',encoding='utf-8') as f: #储存路径可以事先不存在。
            f.write(r.text)

##读取多个文件        
import sys
syslen=len(sys.argv)
syslen

file_list=os.listdir()
len(file_list)
'''
s='names'+str(1880)
eval(s,pd.read_csv('./names_data/yob2010.txt'))
'''
###数据储存在一个列表中
pieces=[]
years=range(1880,2011)
columns=['name','sex','births']
for year in years:
    path='./names_data/yob%d.txt' % year  #这个表达应该多熟悉一下
    frame=pd.read_csv(path,names=columns)
    frame['year']=year
    pieces.append(frame)
#拼接成一个列表
names=pd.concat(pieces,ignore_index=True)
names.head(5)

# 在‘year’ 和 ‘sex’ 上对 ‘birth’ 做聚合
total_births=names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
total_births.tail(5)

grouped=names[['sex','births','year']].groupby(['year', 'sex'])
total_births_1=grouped.sum()
total_births_1.ix[2010] # 读取某一行
total_births_1.ix[(2010,'F')] #multindex

# 
def add_prop(group):
    group['prop']=group['births']/group['births'].sum()
    return group
names_years_sex=names.groupby(['year','sex']).apply(add_prop) # 分组应用某个函数 apply

names_years_sex.head()

(names_years_sex.groupby(['year','sex']).prop.sum()==1).all()
np.allclose(names_years_sex.groupby(['year','sex']).prop.sum(),1)

#
def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]

##active names
top1000=names.groupby(['year','sex']).apply(get_top1000)
top1000.head()

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']


###------------------------------names variation
def get_var(group):
    return np.cov(group['prop'])
boys=boys.groupby('year').apply(add_prop)
boys_var=boys.groupby('year').apply(get_var)
boys_var=boys_var*10**5
boys_var=pd.DataFrame(boys_var)

girls=girls.groupby('year').apply(add_prop)
girls_var=girls.groupby('year').apply(get_var)*10**5
girls_var=pd.DataFrame(girls_var)

names_var=pd.merge(boys_var,girls_var,left_index=True,right_index=True)

#保存数据
names_var.to_csv('names_var.csv')


names.head()
births_by_year=names.groupby(['year','sex']).sum()
births_by_year.unstack() # births_by_year具有多重index ，unstack之后，变成了dataframe
births_by_year.unstack().stack() # births_by_year具有多重index ，unstack之后，变成了dataframe,再stack之后，变成了multi index
births_by_year.to_csv('births_by_year.csv')


##-----------------------------前1000最受欢迎的名字的占有的比例
top1000_prop=names_years_sex.groupby(['year','sex']).apply(get_top1000)
top1000_prop_year=top1000_prop[['sex','year','prop']].groupby(['year','sex']).sum()
top1000_prop_year.to_csv('top1000_prop_year.csv')

##----------------------------last letter---------------------
names.head()
get_last_letter=lambda x:x[-1]
last_letters=names.name.map(get_last_letter)
last_letters.name='last_letter'

names['last_letter']

table=names.pivot_table('births',index=last_letters,columns=['sex','year'],aggfunc=sum)
table['F'] # 
###选取有代表性的三年
subtable=table.reindex(columns=[1910,1960,2010],level='year')
subtable.head()
letter_prop=subtable/subtable.sum()
letter_prop[np.isnan(letter_prop)]=0
letter_prop.head()

letter_prop['F'].to_csv('f_letter_prop.csv')
letter_prop['M'].to_csv('m_letter_prop.csv')


#-----------------------stack unstack pivot_table-----------------------------
da=names[[0,1,3]]
da.stack()
diff_name=da.pivot_table(index='year', columns='sex',aggfunc=len) # len 查看 每一年每一种性别 有多少种 不同的名字
diff_name=diff_name.unstack()
diff_name.to_csv('./names/diff_name.txt') 
