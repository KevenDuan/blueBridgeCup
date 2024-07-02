#模拟日期-星期几
from datetime import *
a=date(1949,10,1)
b=date(2012,10,1)
cnt=0
while a<=b:
    if a.weekday()==6 and a.month==10 and a.day==1:
        cnt+=1
    a += timedelta(1)
print(cnt)
 
'''
函数详解：
date(year,month,day):格式转换函数：数字格式→日期格式
a.weekday()：星期几函数，默认从星期一开始（下标为0）
a.month: 日历月份
a.day:   日历天数
timedelta(1):1天(时间单位)
print(9)
'''
