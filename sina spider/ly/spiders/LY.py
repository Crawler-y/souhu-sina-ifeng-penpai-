# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from ly.items import LyItem

class LySpider(scrapy.Spider):
    name = 'LY'
    allowed_domains = ['sina.com.cn']
    def start_requests(self):
        #需要改的参数
        #type=domestic国内游，type:exit境外游
        basr_url='http://interface.sina.cn/travel/2017/index_newslist.d.json?&type=exit&cardpage={}&page={}'
        for i in range(3):
            for j in range(1000):
                yield Request(url=basr_url.format(str(i+1),str(j+1)))
    def parse(self, response):
        datas=json.loads(response.text)
        if datas['data'] == False:
            return
        else:
            dat_list = datas['data']['docs']
            for dat in dat_list:
                trg_url = dat['url']
                title = dat["title"]
                yield Request(url=trg_url, callback=self.parse_content, meta={'meta': title})
    def parse_content(self,response):
        item=LyItem()
        item['title']=response.meta['meta']
        item['content']=''.join(response.xpath('//div[@id="artibody"]//p/text()').extract()).strip().replace('\u3000','').replace('\xa0','')
        yield item
