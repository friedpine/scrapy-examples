import re
import json
import sys
import os
from os.path import dirname


path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)
print path

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector

#from CSDNBlog.items import *
from items import *

class CSDNBlogSpider(Spider):

    name = "CSDNBlog"

    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/u012150179/article/details/11749017"]

    def parse(self, response):
        sel = Selector(response)
        item = CsdnblogItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')
        yield item

        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            print url
            url = "http://blog.csdn.net" + url
            print url
            yield Request(url, callback=self.parse)
