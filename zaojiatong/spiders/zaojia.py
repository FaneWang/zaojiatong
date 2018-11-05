# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ZaojiaSpider(scrapy.Spider):
    name = 'zaojia'
    allowed_domains = ['https://hubei.zjtcn.com/facx']
    base_url = 'http://https://hubei.zjtcn.com/facx/c0000_'

    def start_requests(self):
        for cha in range(1,self.settings.get('MAX_CHA') + 1,2):
            for page in range(1,self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + '_t{cha}_d201811_p{page}_k_qa_qi.html'.format(cha=cha,page=page)
                yield Request(url=url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        pass
