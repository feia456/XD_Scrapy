# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class XdscrapySpider(XMLFeedSpider):
    name = 'xdscrapy'
    allowed_domains = ['http://iqianyue.com/']
    start_urls = ['http://http://iqianyue.com//feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
