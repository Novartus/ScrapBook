# -*- coding: utf-8 -*-
import scrapy


class YahooFinanceSpider(scrapy.Spider):
    name = 'yahoo_finance'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/sector/ms_technology']

    def parse(self, response):
        company_name_list = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[2]/text()').extract()
        company_price_list= response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/span/text()').extract()
        print("")
        print("")
        print("")
        print("")
        count = len(company_name_list)
        print("Total Number :",count)
        for i in range(0,count):
            print(company_name_list[i],company_price_list[i])
        print("")
        print("")
        print("")
        print("")
