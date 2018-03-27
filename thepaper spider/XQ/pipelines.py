# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv

class XqPipeline(object):
    def process_item(self, item, spider):
        os.chdir('D:\My Documents\Desktop\XQ\XQ\spiders')
        #25462 中国政库 ，25488 中南海，25489舆论场，25490打虎记，25423 人事风向，25426 法制中国
        with open('法制中国.csv', 'a+', encoding='GBK', newline='')as f:
            writer = csv.writer(f)
            writer.writerow((item['title'], item['content']))
            return item
