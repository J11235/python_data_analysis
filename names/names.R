columns=c('name','sex','births')
names=data.frame()
t1=Sys.time()
for (year in 1880:2010){
  path=paste('./names_data/yob',year,'.txt',sep='')
  frame=read.csv(path,col.names =columns)
  frame['year']=year
  names=rbind.data.frame(names,frame)
}
t2=Sys.time()
t=t2-t1
table(names$year) 
# 和python相比较，读取速度慢了不少。 Time difference of 43.68585 secs
# year=2010
# path=paste('./names_data/yob',year,'.txt',sep='')
# frame=read.csv(path,col.names =columns)
# pieces$year=frame

#-------------------------------------------names variety------------------------------------
names_var<-read.csv('names_var.csv')
library(ggplot2)
colnames(names_var)<-c('year','M','F')
#宽数据变长,然后再ggplot中画图。
names_var_year<-melt(names_var,id=c('year'))
names_var_year %>% ggplot(aes(x=year,y=value,color=variable))+geom_line()+geom_point() + ggtitle('Names variety of Male and Female') +xlab('Year') + ylab('Variety')

#--------------------------------------------births by year-------------------------------------
births_by_year<-read.csv('births_by_year.csv')
head(births_by_year)
births_by_year %>% ggplot(aes(x=year,y=births,color=sex))+geom_line()+geom_point() + ggtitle('Births by year of Male and Female') +xlab('Year') + ylab('Births')


#------------------------------------------top 1000 names prop-----------
top1000names_prop<-read.csv('top1000_prop_year.csv')
head(top1000names_prop)
top1000names_prop%>% ggplot(aes(x=year,y=prop,color=sex))+geom_point()+geom_line() + labs(title='Top 1000 names problility',x='Year',y='Probility')

#-----------------------------------------last letter prop----------------

m_letter_prop<-read.csv('m_letter_prop.csv')
head(m_letter_prop)
m_letter_prop_l<-melt(m_letter_prop,id='last_letter')
m_letter_prop_l %>%ggplot(aes(x=last_letter,y=value,fill=variable))+geom_bar(position = 'dodge',stat = 'identity')+labs(title="Male last letter",x='Last letter',y='Probility') # stat = 'identity' 柱状图的y轴为 value，不设置stat的话，y轴为count（默认）


f_letter_prop<-read.csv('f_letter_prop.csv')
head(f_letter_prop)
f_letter_prop_l<-melt(f_letter_prop,id='last_letter')
f_letter_prop_l %>%ggplot(aes(x=last_letter,y=value,fill=variable))+geom_bar(position = 'dodge',stat = 'identity')+labs(title="Female last letter",x='Last letter',y='Probility') # stat = 'identity' 柱状图的y轴为 value，不设置stat的话，y轴为count（默认）



diff_name<-read.csv('diff_name.txt')
colnames(diff_name)<-c('name','sex','year','counts')
diff_name %>% ggplot(aes(x=year,y=counts,color=sex)) + geom_bar(stat = 'identity',position = 'dodge')+labs(title="Different kinds of names Male vs Female")











install.packages("car")
library(car)
data(Salaries)
head(Salaries)
