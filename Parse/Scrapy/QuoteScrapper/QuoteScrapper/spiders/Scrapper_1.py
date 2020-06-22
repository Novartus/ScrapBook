# -*- coding: utf-8 -*-
import scrapy


class Scrapper1Spider(scrapy.Spider):
    name = 'Scrapper_1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        quote_list = response.xpath('/html/body/div[1]/div[2]/div[1]/div/span/text()').extract()
        #author_list= response.xpath('/html/body/div/div[2]/div[1]/div/span/text()').extract()
        print("")
        print("")
        print("")
        print("")
        for i in range(0,len(quote_list)):
            print(quote_list[i])
        print("")
        print("")
        print("")
        print("")
