from typing import Counter
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import base

engine = create_engine('mmysql+mysqlconnector://root:L%40ng99%40mysql@localhost/articledb', echo=True)
Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'
    id = Column('id', String)
    url = Column('url', Integer, primary_key=True)
    publisher = ('publisher', String)
    datetime = ('datetime', DateTime)
    title = ('title', String)
    body = ('body', String)
    category = ('category', String)

class Writer(Base):
    __tablename__ = 'writer'
    Article_id = Column('article_id', String)
    writer = Column('writer', String)

class Tag(Base):
    __tablename__ = 'tag'
    Article_id = Column('article_id', String)
    tag = Column('tag', String)

Base.metadata.create_all(bind=engine)
