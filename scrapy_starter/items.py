# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyStarterItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  date = scrapy.Field()
  company = scrapy.Field()
  company_url = scrapy.Field()
  money = scrapy.Field()
  area = scrapy.Field()
  turn = scrapy.Field()
  investor = scrapy.Field()
  investor_url = scrapy.Field()
