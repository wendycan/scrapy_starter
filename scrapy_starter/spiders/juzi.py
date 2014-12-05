import scrapy

from scrapy_starter.items import ScrapyStarterItem

class JuziSpider(scrapy.Spider):
  name = "juzi"
  allowed_domains = ["itjuzi.com"]
  start_urls = [
      "http://itjuzi.com/investev ents"
  ]
  start_urls = ['http://itjuzi.com/investevents?page=%s' % page for page in xrange(1,51)]

  def parse(self, response):
    for sel in response.xpath("//table[@class='children-norml-link']//tbody//tr"):
      item = ScrapyStarterItem()
      item['date'] = sel.xpath('td[1]/text()').extract()
      item['company'] = sel.xpath('td[2]/a/text()').extract()
      item['company_url'] = sel.xpath('td[2]/a/@href').extract()
      item['turn'] = sel.xpath('td[3]/a/text()').extract()
      item['money'] = sel.xpath('td[4]/text()').extract()
      item['area'] = sel.xpath('td[5]/a/text()').extract()
      item['investor'] = sel.xpath('td[6]/a/text()').extract()
      item['investor_url'] = sel.xpath('td[6]/a/@href').extract()
      yield item
