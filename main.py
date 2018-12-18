# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:39:14 2018

@author: chris
"""

import time
import os
while True:
  os.system("scrapy crawl sina")
  time.sleep(300) #每隔一天运行一次 24*60*60=86400s或者，使用标准库的sched模块
import sched
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