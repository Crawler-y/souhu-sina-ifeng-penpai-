# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

class LyPipeline(object):
    def process_item(self, item, spider):
        os.chdir('D:\My Documents\Desktop\ly\ly\spiders')
        # 需要改的参数
        # type=domestic国内游，type:exit境外游
        with open('境外游.csv', 'a+', encoding='GBK', newline='')as f:
            writer = csv.writer(f)
            writer.writerow((item['title'], item['content']))
            return item
