# Scrapy settings for scrapy_osl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ScrapyOslSpider'

SPIDER_MODULES = ['scrapy_osl.spiders']
NEWSPIDER_MODULE = 'scrapy_osl.spiders'

ITEM_PIPELINES = ['scrapy_osl.pipelines.ScrapyOslPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_osl (+http://www.yourdomain.com)'
