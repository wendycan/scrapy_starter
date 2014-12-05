import scrapy
import cPickle

from scrapy_starter.items import ScrapyStarterItem

class InvesteventsSpider(scrapy.Spider):
  name = "investevents"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/investevents?page=%s' % page for page in xrange(1,3)]

  def parse(self, response):
    for sel in response.xpath("//table[@class='children-norml-link']//tbody//tr"):
      item = ScrapyStarterItem()
      item['date'] = ''.join(sel.xpath('td[1]/text()').extract())
      item['company'] = ''.join(sel.xpath('td[2]/a/text()').extract())
      item['company_url'] = ''.join(sel.xpath('td[2]/a/@href').extract())
      item['turn'] = ''.join(sel.xpath('td[3]/a/text()').extract())
      item['money'] = ''.join(sel.xpath('td[4]/text()').extract())
      item['area'] = ''.join(sel.xpath('td[5]/a/text()').extract())
      item['investor'] = cPickle.dumps(sel.xpath('td[6]/a/text()').extract())
      item['investor_url'] = cPickle.dumps(sel.xpath('td[6]/a/@href').extract())
      yield item
