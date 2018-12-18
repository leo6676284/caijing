# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from numpy import *
from os import listdir
#from caijing.items import CaijingItem

class CaijingPipeline(object):
    #item = CaijingItem()
    def process_item(self, item, spider):
        #for each in response.xpath(body)
        now = time.strftime('%Y%m%d',time.localtime())
        #print(now)
        #item = CaijingItem()
        print(item['name'])
        filename =item['sid']+'/'+now+'.txt'
        with open(filename,'a') as f:
            f.write(item['date']+'\t')
            f.write(item['sid']+'\t')
            f.write(item['name']+'\t')
            f.write(item['tp']+'\t')
            f.write(item['yp']+'\t')
            f.write(item['np']+'\t')
            f.write(item['hp']+'\t')
            f.write(item['lp']+'\t')
            f.write(item['fp']+'\t')
            f.write(item['sp']+'\t')
            f.write(item['num']+'\t')
            f.write(item['money']+'\t')
            f.write(item['fn']+'\n')
            f.close()
            
            time.sleep(1)
        return item
        
