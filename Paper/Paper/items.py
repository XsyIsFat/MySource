# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VIPItem(scrapy.Item):
    # define the fields for your item here like:
    gender = scrapy.Field()
    education = scrapy.Field()
    age = scrapy.Field()
    house = scrapy.Field()
    amount = scrapy.Field()
    marriage = scrapy.Field()
    description = scrapy.Field()
    period = scrapy.Field()
    rate = scrapy.Field()
    count = scrapy.Field()
    count_1 = scrapy.Field()
class Item(scrapy.Item):
   url = scrapy.Field()
   no = scrapy.Field()


