# @Time    : 2018/1/29 0029 22:06
# @Author  : miaoxu
# @Site    : 
# @File    : Service_Tag.py
# @Software: PyCharm Community Edition
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from time import ctime
from constant.database import Base
# Base = declarative_base()
service_tag = Table(
    'service_tag', Base.metadata,
    Column('service_id', Integer, ForeignKey('services.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))

)