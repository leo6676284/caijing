# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaijingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #股票代码
    sid = scrapy.Field()
    #股票名称
    name = scrapy.Field()
    #今日开盘价 1
    tp = scrapy.Field()
    #昨日收盘价 2
    yp = scrapy.Field()
    #当前价格 3
    np = scrapy.Field()
    #今日最高价 4
    hp = scrapy.Field()
    #今日最低价 5
    lp = scrapy.Field()
    #竞买价，即“买一”报价 6
    fp = scrapy.Field()
    #竞卖价，即“卖一”报价 7 
    sp = scrapy.Field()
    #成交的股票数（单位为“个”） 8
    num = scrapy.Field()
    #成交金额（单位为“元”） 9
    money = scrapy.Field()
    #“买一”申请  股 10
    fn = scrapy.Field()
    #日期时间 11
    date = scrapy.Field()
