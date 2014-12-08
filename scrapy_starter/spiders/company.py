import scrapy
import cPickle

from scrapy_starter.items import CompanyItem
from scrapy_starter.models import db_connect

class CompanySpider(scrapy.Spider):
  name = "company"
  allowed_domains = ["itjuzi.com"]
  engine = db_connect()
  connection = engine.connect()
  result = connection.execute("select url from company_urls")
  urls = []
  for row in result:
    urls.append(row['url'])
  start_urls = list(set(urls))
  connection.close()

  def parse(self, response):
    for sel in response.xpath("//ul[@class='detail-info']"):
      item = CompanyItem()
      item['company_url'] = response.url
      item['url'] = ''.join(sel.xpath('li[1]/a/text()').extract())
      item['company'] = ''.join(sel.xpath('li[2]/em/text()').extract())
      item['date'] = ''.join(sel.xpath('li[3]/em/text()').extract())
      item['location'] = ''.join(sel.xpath('li[4]/a/text()').extract())
      item['state'] = ''.join(sel.xpath('li[5]/a/text()').extract())
      item['stage'] = ''.join(sel.xpath('li[6]/a/text()').extract())
      item['area'] = ''.join(sel.xpath('li[7]/a/text()').extract())
      item['tags'] = cPickle.dumps(sel.xpath('li[8]/a/text()').extract())
      item['desc'] = ''.join(sel.xpath('li[9]/em/text()').extract())
      yield item
