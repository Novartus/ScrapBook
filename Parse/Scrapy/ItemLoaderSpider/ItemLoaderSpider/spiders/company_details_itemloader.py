import scrapy

from ItemLoaderSpider.items import finance_details
from scrapy.loader import ItemLoader

class CompanyDetailsItemLoaderSpider(scrapy.Item):
    name= "company_details_itemloader"
    allowed_domains= ["finance.yahoo.com"]
    start_urls= ["https://finance.yahoo.com/sector/ms_technology"]

    def parse(self,response):
        company_results = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/')

        for company in company_results:
            details_loader= ItemLoader(item = CompanyDetailsItem(), selector= company)
            details_loader.add_xpath('company_name','td[2]/text()')
            details_loader.add_xpath('company_symbol_link','td[1]/a/@href')
            details_loader.add_xpath('company_price_intraday', 'td[3]/span/text()')

            yield details_loader.load_item()