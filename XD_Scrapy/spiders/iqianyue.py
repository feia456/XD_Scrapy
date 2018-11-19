# -*- coding: utf-8 -*-
import scrapy


class IqianyueSpider(scrapy.Spider):
    name = 'iqianyue'
    allowed_domains = ['http://iqianyue.com/']
    start_urls = ['http://http://iqianyue.com//']

    def parse(self, response):
        pass
