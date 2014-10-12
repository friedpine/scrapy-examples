import re
import json
import sys


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from doubanbook.items import *
from misc.log import *


class DoubanBookSpider(CrawlSpider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    download_delay = 1  
    start_urls = [
        #"http://book.douban.com/tag/"
    	"http://book.douban.com/doulist/1556952/?start=0&amp;filter="
	]
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_2'),
        #Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        #Rule(sle(allow=("/tag/$", )), follow=True),
    ]

    def parse_2(self, response):
        items = []
        sel = Selector(response)
        sites = sel.css('#wrapper')
        print "#################"
        print response.url
        for site in sites:
            item = DoubanSubjectItem()
            item['title'] = site.css('h1 span::text').extract()
            item['link'] = response.url
            item['content_intro'] = site.css('#link-report .intro p::text').extract()
            items.append(item)
            a=repr(item)
            print a.decode('utf-8').decode('unicode-escape')
        # info('parsed ' + str(response))
        return items

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request
