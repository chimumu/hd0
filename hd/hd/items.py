# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pm = scrapy.Field()
    qd = scrapy.Field()
    sum = scrapy.Field()
    ying = scrapy.Field()
    fu = scrapy.Field()
    feng = scrapy.Field()
    shenglv = scrapy.Field()
