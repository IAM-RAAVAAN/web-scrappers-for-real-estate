# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scraper99Item(scrapy.Item):
    title = scrapy.Field()
    prices = scrapy.Field()
    area = scrapy.Field()
    bhk = scrapy.Field()
    date_of_posting = scrapy.Field()
    link = scrapy.Field()

    pass
