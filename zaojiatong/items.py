# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZaojiatongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collections = 'zaojiatong'
    name = Field()
    model = Field()
    market_price = Field()
    suggested_price = Field()
    brand = Field()
    unit = Field()
    rate = Field()
    supplier = Field()
