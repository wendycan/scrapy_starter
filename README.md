scrapy_starter
===========================
A spider to scrawl [http://itjuzi.com](http://itjuzi.com)

Requirements
---------
* pip
* scrapy
* sqlalchemy
* sqlite

Install
---------

~~~ sh
$ pip install scrapy
$ pip install sqlalchemy
~~~

Crawling
---------

List all spider:

~~~ sh
$ scrapy list
-> company company_url investevents
~~~

You should run CompanySpider after running CompanyUrlSpider,because CompanyUrlSpider generate data(table) for CompanySpider.

Crawl websites:

~~~  sh
$ scrapy crawl investevents
$ scrapy crawl company_url
$ scrapy crawl company
~~~

Ref
---------

* [xPath](http://www.w3schools.com/xpath/xpath_syntax.asp)
* [WEB SCRAPER](http://newcoder.io/scrape/)
* [Scrapy Doc-zh](http://scrapy-chs.readthedocs.org/zh_CN/latest/topics/stats.html)
* [Scrapy Doc-en](http://doc.scrapy.org/en/latest/intro/tutorial.html)
