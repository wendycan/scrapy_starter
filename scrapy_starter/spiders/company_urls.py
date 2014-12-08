import scrapy

from scrapy_starter.items import CompanyUrlItem

class CompanyUrlSpider(scrapy.Spider):
  name = "company_url"
  allowed_domains = ["itjuzi.com"]
  start_urls = ['http://itjuzi.com/company?page=%s' % page for page in xrange(1, 423)]

  def parse(self, response):
    for sel in response.xpath("//div[contains(@class, 'company-list')]/div[@class='company-list-item ']"):
      item = CompanyUrlItem()
      item['url'] = ''.join(sel.xpath("div/h4/a/@href").extract())
      item['name'] = ''.join(sel.xpath("div/h4/a/text()").extract())
      yield item
