# -*- coding: utf-8 -*-
import re
import json
import scrapy
from caijing.items import CaijingItem


class SinaSpider(scrapy.Spider):
    name = 'sz002334'
    allowed_domains = ['hq.sinajs.cn/']
    start_urls = ['http://hq.sinajs.cn/?format=text&list=sz002334']
    #start_urls = ['http://hq.sinajs.cn/list=sh601688,sh601003,sh601001']
    def parse(self, response):
        item = CaijingItem()
        #print(json.loads(response.body.encoding))
        #item['gupiao'] = json.loads(response.body)
        #item['gupiao'] = scrapy.Request(self,['http://hq.sinajs.cn/?format=text&list=sh601688']).text
        #item['gupiao'] = response.body
        #rs = response.body.split(',')
        #print(rs)
        #item['name'] = rs[1]
        rs = response.xpath('//p/text()').extract()[0].split(',')
        #print(rs)
        #股票代码
        item['sid'] = rs[0].split('=')[0]
        #股票名称
        item['name'] = rs[0].split('=')[1]
        #今日开盘价
        item['tp'] = rs[1]
        #昨日收盘价
        item['yp'] = rs[2]
        #当前价格
        item['np'] = rs[3]
        #今日最高价
        item['hp'] = rs[4]
        #今日最低价
        item['lp'] = rs[5]
        #竞买价，即“买一”报价
        item['fp'] = rs[6]
        #竞卖价，即“卖一”报价
        item['sp'] = rs[7]
        #成交的股票数（单位为“个”）
        item['num'] = rs[8]
        #成交金额（单位为“元”）
        item['money'] = rs[9]
        #“买一”申请  股
        item['fn'] = rs[10]
        #日期时间
        item['date'] = rs[30]+' '+rs[31]
        #print(item)
        yield item
        # 如果datas存在数据则对下一页进行采集

        
# =============================================================================
# page_num = re.search(r'start=(\d+)', response.url).group(1)
# page_num = 'start=' + str(int(page_num)+20)
# next_url = re.sub(r'start=\d+', page_num, response.url)
# yield Request(next_url, headers=self.headers)
# =============================================================================
