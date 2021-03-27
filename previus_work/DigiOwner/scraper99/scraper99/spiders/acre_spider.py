
import scrapy
from ..items import Scraper99Item
import pandas as pd

class AcreSpiderSpider(scrapy.Spider):
	name = 'acre_spider'
	page_number = 2
	start_urls = [
		'https://www.99acres.com/kalpataru-estate-rent-in-pimple-gurav-pune-62904-rnpffid'
		]

	def parse(self, response):

		items = Scraper99Item()
		
		title = response.css('h2').css('::text').extract()
		price = response.css('#srp_tuple_price::text').extract()
		area = response.css('#srp_tuple_primary_area::text').extract()
		bhk = response.css('#srp_tuple_bedroom::text').extract()
		owner_name = response.css('.list_header_semiBold a::text').extract()
		date_of_posting = response.css('.caption_strong_small span::text').extract()
		link = response.xpath('//a[@class="body_med srpTuple__propertyName"]/@href').extract()

		items['title'] = title
		items['price'] = price
		items['area'] = area
		items['bhk'] = bhk
		items['owner__name'] = owner_name
		items['date_of_posting'] = date_of_posting
		items['link'] = link

		yield items

		# next_page = 'https://www.99acres.com/rent-property-in-vijay-nagar-indore-ffid?dealerRelaxation=false&src=CLUSTER&page='+str(AcreSpiderSpider.page_number)

		# if AcreSpiderSpider.page_number <= 4:
		# 	yield response.follow(next_page, callback=self.parse)

		#for item in zip(title, price, area, bhk, owner_name, date_of_posting):

		# scraped_info = {
		# 'title' : title,
		# 'area' : area,
		# 'bhk' : bhk,
		# # 'owner_name' : owner_name,
		# 'date_of_posting' : date_of_posting,
		# }

		df = pd.DataFrame.from_dict(items)
		df.to_excel("mahindra sir.xlsx")
		# yield scraped_info



		



		
		
