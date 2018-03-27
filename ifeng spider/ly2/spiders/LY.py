# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ly2.items import Ly2Item
import time
class LySpider(scrapy.Spider):
    name = 'LY'
    allowed_domains = ['ifeng.com']
    def start_requests(self):
        ob_id=['66-1508-','66-1632-','66-1768-','66-1877-']
        base_url='http://travel.ifeng.com/o/dynpage/{}/1/pPlist.shtml'
        for id in ob_id:
            yield Request(url=base_url.format(id))
    #http://travel.ifeng.com/o/dynpage/66-1632-/1/pPlist.shtml
    def parse(self, response):
        print(response.url)
        node_list=response.xpath('//div[@class="lvre clearfix"]//div[1]/div')
        for node in node_list:
            title=node.xpath('.//p//text()|.//a//text()').extract()[0]
            tmp=set(node.xpath('.//a/@href').extract())
            try:
                trg_url=list(tmp)[0]
                yield Request(url=trg_url,meta={'title':title},callback=self.content)
            except:
                print('============')
                print('============')
                print('============')
                print('============')
        next_page=response.xpath('//div[@class="fy clearfix"]//a[contains(text(),"下一页")]/@href').extract_first()
        if next_page:
            yield Request(url=next_page)
    def content(self,response):
        time.sleep(1)
        item=Ly2Item()
        contents=''.join(response.xpath('//div[contains(@class,"tConT")]//p/text()').extract()).strip().replace('\uf934','').replace('\xa0','').replace('\n','')
        item['title']=response.meta['title']
        item['content']=contents
        yield item
