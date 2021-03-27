import scrapy
import re
from ..items import ScraperbricksItem
import pandas as pd

class MagicSpiderSpider(scrapy.Spider):
    name = 'magic_spider'
    start_urls = ['https://www.homeonline.com/property-for-rent-new_palasiya-indore/']

    def parse(self, response):
        items = ScraperbricksItem()

        area = response.css('.cursorPointer .row+ div .row:nth-child(1) .col-sm-9::text').extract()
        price = response.css('.pricesty::text').extract()
        address = response.css('.cursorPointer > .row .col-sm-9::text').extract()
        titles = response.css('.col-md-7 h2::text').extract()

        items['area'] = area
        items['price'] = price
        items['address'] = address
        items['titles'] = titles

        df = pd.DataFrame.from_dict(items)
        df.to_excel("final.xlsx")

        yield items
        pass