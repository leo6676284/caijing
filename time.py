# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:51:26 2018

@author: chris
"""

import time
st = time.strptime('19700102','%Y%m%d')

st=time.mktime(st)
print(st)


import os
import sched

#for i in range(10):
    #print(i*10)
#print(1538291887/86400)
#print(time.time())
#print(time.time()/60/60/24)

"""
st=time.time()

num = 0   
for i in range(100000):
    t = 86400*i
    a = time.localtime(t)
    b = int(time.strftime('%d%w',a))
    if b == 135:
        print(time.strftime('%Y-%m-%d',a))
        num +=1
print(num,time.time()-st)
"""
k =59
k = int(59/100)*3600
print(k)

import time
def fuct(k):
    if k<=2967:
        k+=1
        print(k)
        time.sleep(0.01)
        fuct(k)
    else:
        return
fuct(0)
    
    


#print(dir(time))
#now = time.strftime('%Y%m%d',time.localtime())
now_time =int(time.strftime('%H%M',time.localtime()))
print(now_time)
if now_time >=930 and now_time <= 1130 or now_time >=1300 and now_time <=1500:
    while True:
      os.system("scrapy crawl sina")
      time.sleep(300) #每隔一天运行一次 24*60*60=86400s或者，使用标准库的sched模块
  
#初始化sched模块的scheduler类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
    schedule = sched.scheduler ( time.time, time.sleep )
#被周期性调度触发的函数
    def func():
        os.system("scrapy crawl sina")
        def perform1(inc):
            schedule.enter(inc,0,perform1,(inc,))
            func()  # 需要周期执行的函数
            def mymain():
                schedule.enter(0,0,perform1,(300,))
    if __name__=="__main__":
        mymain()
        schedule.run() # 开始运行，直到计划时间队列变成空为止关于cmd的实现方法，本人在单次执行爬虫程序时使用的是 
    cmdline.execute("scrapy crawl sina".split())#但可能因为cmdline是scrapy模块中自带的，所以定时执行时只能执行一次就退出了。
else:
    time.sleep()