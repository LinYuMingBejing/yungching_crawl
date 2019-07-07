# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YungchingRentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_name = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    housetype = scrapy.Field()
    pass
