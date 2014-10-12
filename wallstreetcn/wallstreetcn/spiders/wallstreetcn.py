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


#from wallstreetcn.items import *
from items import *
from misc.log import *

class wallstreetcn_Spider(CrawlSpider):
	name = "wallstreetcn"
	allowed_domains = ["wallstreetcn.com"]
	download_delay = 1
	start_urls = [
		"http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=10&page=1"
		#"http://wallstreetcn.com"
	]
	rules = [
		Rule(sle(allow=("m.wallstreetcn")),callback='parse_1'),
		Rule(sle(allow=("/node/\d+")),callback='parse_2'),
	]

	def parse_2(self,response):
		sel = Selector(response)
		item = WallstreetcnItem()
		print "###############################################################################"
		article_url = str(response.url).encode('utf-8')
		print article_url
		article_name = sel.xpath("//*[@id='main']/article/h1/text()").extract()[0].encode('utf-8')
		article_content = ''.join(response.xpath("//*[@id='main']/article/div[2]//p/text()").extract()).encode('utf-8')

		item['title'] = article_name
		item['link'] = article_url
		item['content'] = article_content
		return item

	def parse_1(self,response):
		print str(response.url)
		print "##############mobile"

	def _process_request(self, request):
		info('process ' + str(request))
		return request





