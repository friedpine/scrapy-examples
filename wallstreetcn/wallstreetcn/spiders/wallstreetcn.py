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


from wallstreetcn.items import *
from misc.log import *

class wallstreetcn_Spider(CrawlSpider)
	name = "wallstreetcn"
	allowed_domains = ["wallstreetcn.com"]
	download_delay = 1
	start_urls = [
		"http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=100&page=1"
	]
	rules = [
		Rule(sle(allow=("/node/\d+")),callback='parse')
	]

#XPATH:
#//*[@id="main"]/article/div[2]
#//*[@id="main"]/article/div[2]/p[2]
#//*[@id="main"]/article/div[2]/p[5]
	def parse(self,response):
		sel = Selector(response)
		item = WallstreetcnItem()

		article_url = str(response.url)
		article_name = sel.xpath()


