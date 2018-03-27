# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv

class ShPipeline(object):
    def process_item(self, item, spider):
        os.chdir('D:\My Documents\Desktop\SH\SH\spiders')
        with open('sohu区块链.csv', 'a+', encoding='GBK', newline='')as f:
            writer = csv.writer(f)
            writer.writerow((item['title'], item['text']))
            return item
