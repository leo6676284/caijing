# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:40:20 2018

@author: chris
"""

import time
#a = time.localtime(0)
#print(time.strftime('%Y-%m-%d %H:%M:%S',a))


#转换时间戳函数
def timeTransform(time1):
    #当time1小于1970时
    if time1 <= 19700101:
        time1 = 19700102
    #把时间转为字符串
    time1 = '%s' %time1
    #转为时间格式
    st = time.strptime(time1,'%Y%m%d')
    #转为时间戳
    st = time.mktime(st)
    return st

#计算黑色星期五函数    
def blackFriday(time1,time2):
    #开始运行函数时间
    st = time.time()
    #转为时间戳
    st1 = timeTransform(time1)
    st2 = timeTransform(time2)
    #计算两个时间到1970年的天数范围 一天为86400s
    m = int(st1/86400)
    n = int(st2/86400)
    print(n-m)
    #计数
    num = 0
    #每天循环
    for i in range(m,n):
        #转为每天的时间戳
        t = 86400*i
        #转为时间格式
        a = time.localtime(t)
        #提取时间的日期 星期进行对比
        b = int(time.strftime('%d%w',a))
        #当日期为13 星期为5的日期提取出来并打印
        if b == 135:
            print(time.strftime('%Y-%m-%d',a))
            #每打印一次计数+1
            num +=1
            time.sleep(0.5)
    #打印总数，花费时间
    print(time.time()-st,num)
blackFriday(19990812,20181009)