# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from SH.items import ShItem
import re
class ShSpider(scrapy.Spider):
    name = 'sh'
    allowed_domains = ['sohu.com']
    def start_requests(self):
        #CHANNEL,TAG，GATEGORY
        # u_list=['1460','1461','1462','1463']
        # u_list = ['1460']
        #http://v2.sohu.com/public-api/feed?scene=CATEGORY&sceneId=1460&page=4&size=20&callback=jQuery112407720197729765084_1521076197992&_=1521076198082
        #参数scene在js包feed。。。。里，sceneID在url末尾数字
        base_url='http://v2.sohu.com/public-api/feed?scene=TAG&sceneId=67230&page={}&size=20'
        # for k in u_list:
        for i in range(100):
            url=base_url.format(str(i))
            yield Request(url=url)
    def parse(self, response):
        rsps=json.loads(response.text)
        for i in rsps:
            u_url='http://www.sohu.com/a/'+str(i['id'])+'_'+str(i['authorId'])
            yield Request(url=u_url,callback=self.content)
    def content(self,response):
        # print(response.text)
        item=ShItem()
        conents=response.xpath('//*[@id="mp-editor"]//text()')
        titles=response.xpath('//div[@id="article-container"]/div[2]/div[1]/div[1]/h1/text()')
        a=''.join(conents.extract()[2:-5]).strip().replace('\n','')
        item['text']=re.sub('(\d+丶)','//',a)
        item['title']=titles.extract_first()
        yield item
