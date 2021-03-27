# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NobrokerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    # owner_name = scrapy.Field()
    address = scrapy.Field()
    negotiable_rent = scrapy.Field()
    furnishing = scrapy.Field()
    pass
