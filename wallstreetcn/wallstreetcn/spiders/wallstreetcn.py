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
from scrapy.contrib.linkextractors import LinkExtractor


#from wallstreetcn.items import *
from items import *
from misc.log import *

class wallstreetcn_Spider(CrawlSpider):
	name = "wallstreetcn"
	allowed_domains = ["wallstreetcn.com"]
	download_delay = 0.1
	start_urls = [
		"http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=100&page=1"
		#"http://wallstreetcn.com"
	]
	rules = [
		Rule(LinkExtractor(allow=("m\.wallstreetcn\.com/node/",)),callback='parse_1'),
		Rule(LinkExtractor(allow=("/node/\d+",)),callback='parse_2'),
	]

	def parse_2(self,response):
		sel = Selector(response)
		item = WallstreetcnItem()
		article_url = str(response.url)
		print article_url

		article_name = sel.xpath("//*[@id='main']/article/h1/text()").extract()[0]
		article_content = ''.join(response.xpath("//*[@id='main']/article/div[2]//p/text()").extract())

		item['title'] = article_name
		item['link'] = article_url
		item['content'] = article_content
		return item

	def parse_1(self,response):

		#/html/body/div[1]/div[2]/div/h2
		sel = Selector(response)
		item = WallstreetcnItem()
		article_url = str(response.url)
		print article_url
		
		article_name = sel.xpath("/html/body/div[1]/div[2]/div/h2/text()").extract()[0]
		article_content = ''.join(response.xpath("/html/body/div[1]/div[2]/div/div[2]/p/text()").extract())

		item['title'] = article_name
		item['link'] = article_url
		item['content'] = article_content
		return item

	def _process_request(self, request):
		info('process ' + str(request))
		return request





