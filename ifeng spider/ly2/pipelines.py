# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

class Ly2Pipeline(object):
     def process_item(self, item, spider):
         os.chdir('D:\My Documents\Desktop\ly2\ly2\spiders')
         with open('文化之旅.csv', 'a+', encoding='GBK', newline='')as f:
             writer = csv.writer(f)
             try:
                writer.writerow((item['title'], item['content']))
             except:
                pass
             finally:
                    return item
