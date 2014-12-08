# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Investevents, Companies, CompanyUrl, db_connect, create_investevents_table

class ScrapyStarterPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_investevents_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        print 'spider:', spider.name
        session = self.Session()
        if spider.name == 'investevents':
            investevents = Investevents(**item)
            session.add(investevents)
            session.commit()
        if spider.name == 'company':
            companies = Companies(**item)
            session.add(companies)
            session.commit()
        if spider.name == 'company_url':
            company_url = CompanyUrl(**item)
            session.add(company_url)
            session.commit()
        return item
