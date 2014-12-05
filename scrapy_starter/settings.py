# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_starter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_starter'

SPIDER_MODULES = ['scrapy_starter.spiders']
NEWSPIDER_MODULE = 'scrapy_starter.spiders'

ITEM_PIPELINES = { 'scrapy_starter.pipelines.ScrapyStarterPipeline': 1 }

DATABASE = {'drivername': 'sqlite',
            'database': 'juzi'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_starter (+http://www.yourdomain.com)'
