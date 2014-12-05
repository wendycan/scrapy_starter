# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Investevents, db_connect, create_investevents_table

class ScrapyStarterPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_investevents_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        investevents = Investevents(**item)
        session.add(investevents)
        session.commit()
        return item
