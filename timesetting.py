# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:46:06 2018

@author: chris
"""
import time#加载时间库
from os import listdir
#nameList=listdir('caijing/caijing/spiders')
#print(nameList)
def timeTransform1(time1):#时间戳转换函数
    #当time1小于1970时
    if time1 <= 197001010000:
        time1 = 197001020000
    #把时间转为字符串
    time1 = '%s' %time1
    #转为时间格式
    st = time.strptime(time1,'%Y%m%d%H%M')
    #转为时间戳
    st = time.mktime(st)
    return st

import os #加载os库
def fuc(direction,n,jg):#需要运行的函数
    nameList=listdir(direction)
    m = len(nameList)
    for i in range(n):
        for j in range(0,m-2):#批量运行爬虫
            name = nameList[j].split('.')[0]
            os.system("scrapy crawl %s"%name)#运行爬虫sh600291
        time.sleep(jg)
#fuc(2,3)
import sys #加载系统库
sys.setrecursionlimit(10000)  #修改最大递归次数
def timesetting(date1,time1,time2,jg,direction,k):#date1程序运行间隔，一般为1天86400秒；time1，time2为两个唤醒时间；k为唤醒后爬虫运行持续时间；jg为爬虫每次运行的时间间隔
    #获取当前时间的格式
    now_time =int(time.time())
    #print(now_time)
    #求出开盘时间段内循环次数
    #n = int(120/jg)
    t1 = int(timeTransform1(time1))#time1时间戳
    t2 = int(timeTransform1(time2))#time2时间戳
    if k>t2-t1:
        print('运行时间必须小于等于唤醒间隔！')
        return

    if now_time<t1:#当时间小于time1，睡眠直到time1程序唤醒
        print('%s启动，请稍候！'%time1)
        slt = t1-time.time()#计算time1和现在时间间隔      
        time.sleep(slt)#睡眠
        timesetting(date1,time1,time2,jg,direction,k)#递归
        return
    #if now_time == time1 or now_time == time2:#当时间等于time1，time2程序唤醒
    if now_time in range(t1,t1+k+1):
        n = int((t1+k-now_time)/jg)#运行次数
        fuc(direction,n,jg)#批量运行爬虫
        timesetting(date1,time1,time2,jg,direction,k)#递归
        return
    if now_time in range(t2,t2+k+1):
        n = int((t2+k-now_time)/jg)#运行次数
        fuc(direction,n,jg)#批量运行爬虫
        timesetting(date1,time1,time2,jg,direction,k)#递归
         
    if now_time>t1+k and now_time<t2:#当时间在time1，time2中间，睡眠直到time2唤醒
        print('%s会再次启动，请稍候！'%time2)
        slt = t2-time.time()  #计算time2和现在时间间隔        
        time.sleep(slt)#睡眠
        timesetting(date1,time1,time2,jg,direction,k)#递归
        return
    else:#当时间大于time2睡眠，直到time1后的date1秒后唤醒
        st1 =  t1+date1 #下一个time1时间戳      
        time1 = int(time.strftime('%Y%m%d%H%M',time.localtime(st1)))#转换成当地时间格式
        
        st2 = t2+date1#下一个time2时间戳
        time2 = int(time.strftime('%Y%m%d%H%M',time.localtime(st2)))#转换成当地时间格式
        
        timesetting(date1,time1,time2,jg,direction,k)#递归
        return     
timesetting(86400,201811010930,201811011300,300,'caijing/spiders',7200)
