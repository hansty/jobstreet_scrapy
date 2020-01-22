# -*- coding: utf-8 -*-
import scrapy
from ..items import JobstreetScrapyItem

class JobstreetSpider(scrapy.Spider):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    name = 'Jobstreet'
    allowed_domains = ['jobstreet.com.ph']
    start_urls = ['http://www.jobstreet.com.ph/en/companies/491661-accenture/reviews/']

    def parse(self, response):
        item = JobstreetScrapyItem()
        print("hey")
        item['title'] = response.css('h3._3MyALCcnLdxQbK6kunFzgk a::text').extract()
        item['good'] = response.css('div#good-review div div::text').extract()
        yield item
