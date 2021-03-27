# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapermakaanItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    bhk = scrapy.Field()
    address = scrapy.Field()
    furnishing = scrapy.Field()
    links = scrapy.Field()
    pass
