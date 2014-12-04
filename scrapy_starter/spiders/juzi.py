import scrapy

class JuziSpider(scrapy.Spider):
    name = "juzi"
    allowed_domains = ["itjuzi.com"]
    start_urls = [
        "http://itjuzi.com/investevents"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
