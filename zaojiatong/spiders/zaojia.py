# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import sys

sys.path.append('..')
from ..items import ZaojiatongItem


class ZaojiaSpider(scrapy.Spider):
    name = 'zaojia'
    allowed_domains = ['https://hubei.zjtcn.com/facx']
    base_url = 'https://hubei.zjtcn.com/facx/c0000_'

    def start_requests(self):
        for cha in range(0, self.settings.get('MAX_CHA') + 1):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                chas = str(cha).zfill(2)
                url = self.base_url + 't{chas}_d201811_p{page}_k_qa_qi.html'.format(chas=chas, page=page)
                yield Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        tbodies = response.xpath("//tbody[@class='more-infor']")
        for tbody in tbodies:
            item = ZaojiatongItem()
            # print(tbody.xpath(".//a[@class='material-link']/text()").extract_first())
            try:
                item['name'] = ''.join(tbody.xpath(".//a[@class='material-link']/text()").extract_first()).strip()
            except Exception:
                item['name'] = ''
            try:
                item['model'] = ''.join(tbody.xpath(".//span[@class='model-tit']/text()").extract_first()).strip()
            except Exception:
                item['model'] = ''
            try:
                item['market_price'] = ''.join(tbody.xpath(".//td[@tip='priceImage']/text()").extract_first()).strip()
            except Exception:
                item['market_price'] = ''
            try:
                item['suggested_price'] = ''.join(
                    tbody.xpath(".//td[@tip='jyjPriceImage']/text()").extract_first()).strip()
            except Exception:
                item['suggested_price'] = ''
            try:
                item['brand'] = ''.join(tbody.xpath(".//span[@class='brand']/text()").extract_first()).strip()
            except Exception:
                item['brand'] = ''
            try:
                item['unit'] = ''.join(tbody.xpath(".//td[@tip='unit']/text()").extract_first()).strip()
            except Exception:
                item['unit'] = ''
            try:
                item['rate'] = ''.join(tbody.xpath(".//td[last()-3]/text()").extract_first()).strip()
            except Exception:
                item['rate'] = ''
            try:
                supplier = ''.join(tbody.xpath(".//a[@class='xianzhi_01']/span/text()").extract_first()).strip()
                item['supplier'] = supplier
            except Exception:
                item['supplier'] = ''
            print('---------------------------' + supplier + '--------------------------------------')
            yield item
