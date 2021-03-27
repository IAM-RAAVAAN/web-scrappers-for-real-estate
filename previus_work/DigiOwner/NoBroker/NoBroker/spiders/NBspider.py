import scrapy
import pandas as pd
from ..items import NobrokerItem

class NBSpider(scrapy.Spider):
    name = 'nb_spider'
    start_urls = [
        'https://www.nobroker.in/property/rent/mumbai/Navi%20Mumbai/?searchParam=W3sibGF0IjoxOS4wMzMwNDg4LCJsb24iOjczLjAyOTY2MjUsInBsYWNlSWQiOiJDaElKclJNZnVQQzU1enNSYWZpRkVXajNFanciLCJwbGFjZU5hbWUiOiJOYXZpIE11bWJhaSJ9XQ==&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&pageNo=10'
    ]

    # def __init__(self):
    #         self.items = {
    #             'title':[],
    #             'price':[],
    #             'area':[],
    #             # 'owner_name':[],
    #             'address':[]
    #         }

    def parse(self, response):     

        items = NobrokerItem()

        title = response.css('h2::text').extract()
        price = response.css('.solid-border-right .inr_resale+ span::text').extract()
        area = response.css('.solid-border-right meta+ span::text').extract()
        # owner_name = response.css('.seller-name span::text').extract()
        address = response.css('.card-header-title h5::text').extract()
        negotiable_rent = response.css('.rentMaintDiv .inr_resale+ span::text').extract()
        furnishing = response.css('.property-furnishing .semi-bold::text').extract()

        # TO REMOVE UNWANTED SYMBOLS AND DATA
        for i, elem in enumerate(title):
             title[i] = elem.replace('\n', '') 

        for i, elem in enumerate(address):
             address[i] = elem.replace('\n', '') 


        items['title'] = title[1::2]
        items['price'] = price
        items['area'] = area
        items['address'] = address
        items['negotiable_rent'] = negotiable_rent[::3]
        items['furnishing'] = furnishing

        yield items

        df = pd.DataFrame() 
        df = pd.DataFrame.from_dict(items, orient='index')
        df = df.transpose()	
        df.to_excel('test03.xlsx')

        # df = pd.DataFrame() 
        # df = pd.DataFrame.from_dict(items, orient='index')
		# # df.transpose()	
		# # df.head()
		# df.to_excel('r.xlsx', index = False)

		
        pass