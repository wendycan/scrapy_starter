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
    date = Column('date', String)
    company_url = Column('company_url', String)
    turn = Column('turn', String)
    money = Column('money', String)
    area = Column('area', String)
    investor = Column('investor', String)
    investor_url = Column('investor_url', String)
    company = Column('company', String)
