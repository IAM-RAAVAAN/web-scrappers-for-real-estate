# -*- coding: utf-8 -*-
import scrapy


class HomeonlimeSpySpider(scrapy.Spider):
    name = 'homeonlime_spy'
    allowed_domains = ['homeonline.com']
    start_urls = ['http://homeonline.com/']

    def parse(self, response):
        pass
