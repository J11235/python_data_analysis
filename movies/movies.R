users<- read.table('users.txt',sep =":",encoding = 'utf-8',colClasses = c(NA,"NULL")) #The text file importing functions only support single characters as column separators. However, you can tell read.table to ignore columns for import with its colClasses parameter (see the help file):
colnames(users)<-c('user_id','gender','age','occupation','zip')
head(users)

ratings <- read.csv('ratings.txt',sep=":",encoding = 'utf-8',colClasses = c(NA,"NULL"),fill = T)
colnames(ratings) <- c('user_id','movie_id','rating','timestap')
head(ratings)

movies <- read.csv('movies.txt',sep = ":",encoding = 'utf-8',colClasses = c(NA,"NULL"),fill = T)
colnames(movies) <- c('movie_id','title','genres')

movie_data<-merge(users,ratings,by.x = 'user_id',by.y = 'user_id')
movie_data<-merge(movie_data,movies,by.x = 'movie_id',by.y = 'movie_id')
head(movie_data)
movie_data<-data.frame(movie_data)

library(dplyr)
active_movie<-movie_data %>% group_by(movie_id) %>% dplyr::summarise(count=n()) %>% filter(count>250)
mean_rating<- movie_data %>% group_by(movie_id,gender)%>%dplyr::summarise(mean_rating=mean(rating),count=n()) %>% filter(movie_id  %in% active_movie$movie_id)
head(mean_rating)

#---------------------------------------reshape-------------------------------------------------------
library(reshape2)
#wide to long
head(mtcars)
mt<-mtcars
mt['car_type']<-row.names(mtcars)
rownames(mt)<-NULL
head(mt)
melt(mt,id.vars = 'car_type',variable.name = 'item_type',value.name = 'value')
melt(mt,id.vars = c('car_type','mpg'),variable.name = 'item_type',value.name = 'value') #id.vars = c('car_type','mpg')
m_mt<-melt(mt,id.vars = c('car_type','mpg')) #id.vars = c('car_type','mpg')
acast(m_mt,carb~cyl~variable,mean)

head(airquality)
names(airquality) <- tolower(names(airquality))
aqm <- melt(airquality, id=c("month", "day"), na.rm=TRUE)
head(aqm)

acast(aqm, day ~ month ~ variable)
acast(aqm, month ~ variable, mean)
acast(aqm, month ~ variable, mean, margins = TRUE) # margins = TRUE 计算边际
dcast(aqm, month ~ variable, mean, margins = c("month", "variable"))

library(plyr) # needed to access . function
acast(aqm, variable ~ month, mean, subset = .(variable == "ozone")) #.(variable==) 筛选变量
acast(aqm, variable ~ month, mean, subset = .(month == 5))

#Chick weight example
head(ChickWeight)
names(ChickWeight) <- tolower(names(ChickWeight))
chick_m <- melt(ChickWeight, id=2:4, na.rm=TRUE)
head(chick_m)

dcast(chick_m, time ~ variable, mean) # average effect of time
dcast(chick_m, diet ~ variable, mean) # average effect of diet
acast(chick_m, diet ~ time, mean) # average effect of diet & time

# How many chicks at each time? - checking for balance
acast(chick_m, time ~ diet, length)
acast(chick_m, chick ~ time, mean)
acast(chick_m, chick ~ time, mean, subset = .(time < 10 & chick < 20))

acast(chick_m, time ~ diet, length)

head(chick_m)
dcast(chick_m, diet + chick ~ time)
acast(chick_m, diet + chick ~ time)
acast(chick_m, chick ~ time ~ diet)
acast(chick_m, diet + chick ~ time, length, margins="diet")
acast(chick_m, diet + chick ~ time, length, drop = FALSE)

#Tips example
dcast(melt(tips), sex ~ smoker, mean, subset = .(variable == "total_bill"))

ff_d <- melt(french_fries, id=1:4, na.rm=TRUE)
acast(ff_d, subject ~ time, length)
acast(ff_d, subject ~ time, length, fill=0)
dcast(ff_d, treatment ~ variable, mean, margins = TRUE)
dcast(ff_d, treatment + subject ~ variable, mean, margins="treatment")
if (require("lattice")) {
  lattice::xyplot(`1` ~ `2` | variable, dcast(ff_d, ... ~ rep), aspect="iso")
}


#---------------------------计算男女评分分歧------------------------------------
mean_rating1<-mean_rating[,1:3]
head(mean_rating1)
#先melt
re_mean_rating1<-melt(mean_rating1,id=c('movie_id','gender'))
head(re_mean_rating1)
#再cast
(a<-acast(re_mean_rating1,movie_id~gender))
a
a<-data.frame(a)
a$movie_id<-row.names(a)
head(a)


a<-a%>%mutate(diff=abs(F-M)) # 等价 a['diff']<-abs(a['F']-a['M'])
head(a)
a<-arrange(a,desc(diff))
head(a)
a<-a[,c(3,1,2,4)] # 更改列的顺序
head(a)


#-------------------------计算评分波动性-----------------------------
rating_var<-movie_data %>% filter(movie_id %in% active_movie$movie_id) %>% group_by(movie_id) %>% dplyr::summarise(std=var(rating)) %>% arrange(desc(std))
head(rating_var)








