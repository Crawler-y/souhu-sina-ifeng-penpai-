# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from XQ.items import XqItem

class XqSpider(scrapy.Spider):
    name = 'xq'
    allowed_domains = ['thepaper.cn']
    def start_requests(self):
        # 25462 中国政库 ，25488 中南海，25489舆论场，25490打虎记，25423 人事风向，25426 法制中国
        content_id=['25426']
        for id in content_id:
            for i in range(1000):
                base_url='http://www.thepaper.cn/load_index.jsp?nodeids={}&topCids=&pageidx={}'.format(id,str(i))
                yield Request(url=base_url)

    def parse(self, response):
        if not response.text:
            return
        else:
            node_list=response.xpath('/html/body/div')
            for node in node_list:
                trg_url='http://www.thepaper.cn/'+node.xpath('.//h2/a/@href').extract_first()
                yield Request(url=trg_url,callback=self.parse_content)
    def parse_content(self,response):
        item=XqItem()
        title=''.join(response.xpath('//div[@class="newscontent"]/div/following-sibling::h1[1]/text()').extract()).replace('\xa0','')
        content=''.join(response.xpath('//div[@class="news_txt"]/text()').extract()).replace('\xa0','')
        who=''.join(response.xpath('//div[@class="news_about"]/p[1]/text()').extract())
        time=''.join(response.xpath('//div[@class="news_about"]/p[2]/text()').extract()).strip()
        item['title']=title
        item['content']=content
        item['who']=who
        item['time']=time
        yield item