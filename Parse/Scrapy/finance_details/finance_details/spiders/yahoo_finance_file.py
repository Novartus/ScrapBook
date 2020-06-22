# -*- coding: utf-8 -*-
import scrapy


class YahooFinanceSpider(scrapy.Spider):
    filename="yahoo_finance_text"
    name = 'yahoo_finance'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/sector/ms_technology']

    def parse(self, response):
        company_name_list = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[2]/text()').extract()
        company_price_list= response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/span/text()').extract()
        count = len(company_name_list)
        with open (filename, "+a") as file:
            for i in range(0,count):
                file.write(company_name_list[i]+","+company_price_list[i])

