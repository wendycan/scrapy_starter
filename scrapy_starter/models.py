from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_investevents_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Investevents(DeclarativeBase):
    __tablename__ = "investevents"

    id = Column(Integer, primary_key=True)
    date = Column('date', String)
    company_url = Column('company_url', String)
    turn = Column('turn', String)
    money = Column('money', String)
    area = Column('area', String)
    investor = Column('investor', String)
    investor_url = Column('investor_url', String)
    company = Column('company', String)

class Companies(DeclarativeBase):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    url = Column('url', String)
    company_url = Column('company_url', String)
    company = Column('company', String)
    date = Column('date', String)
    location = Column('location', String)
    state = Column('state', String)
    area = Column('area', String)
    stage = Column('stage', String)
    tags = Column('tags', String)
    desc = Column('desc', String)

class CompanyUrl(DeclarativeBase):
    __tablename__ = "company_urls"

    id = Column(Integer, primary_key=True)
    url = Column('url', String)
    name = Column('name', String)
