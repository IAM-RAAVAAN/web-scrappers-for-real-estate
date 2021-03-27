# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappersqaureItem
import pandas as pd

class SqaureSpider(scrapy.Spider):
	name = 'sqaure'
	start_urls = ['https://www.squareyards.com/rent/property-for-rent-in-andheri-west-mumbai']

	def parse(self, response):

		items = ScrappersqaureItem()

		title = response.css('.strong span::text').extract()
		price = response.css('small+ small::text').extract()
		details = response.css('.collapse::text').extract()
		area = response.css('.location::text').extract()
		owner_name = response.css('.text::text').extract()

		items['title'] = title
		items['price'] = price
		items['area'] = area
		items['owner_name'] = owner_name
		items['details'] = details

		scraped_info = items

		df = pd.DataFrame.from_dict(scraped_info, orient='index')
		df = df.transpose()
		df.to_excel("final.xlsx")

		yield items

