BOT_NAME = 'CSDNBlog'

SPIDER_MODULES = ['CSDNBlog.spiders']
NEWSPIDER_MODULE = 'CSDNBlog.spiders'

COOKIES_ENABLED = False

ITEM_PIPELINES = {
    'CSDNBlog.pipelines.CsdnblogPipeline':300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CSDNBlog (+http://www.yourdomain.com)'
T_NAME = 'CSDNBlog'
