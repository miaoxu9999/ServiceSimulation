# Service类的模拟

# 修改2018年1月29日21:33:45
# 将本类映射到数据库中
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from time import ctime
from Entity.Service_Tag import service_tag
from Entity.Tag import Tag
from constant.database import Base
engine = create_engine('mysql+pymysql://root:root@localhost:3306/blog?charset=utf8')
# Base = declarative_base()

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key = True)
    # 信任值（评分）
    reputation = Column(Integer, nullable = False)
    # service的功能描述
    description = Column(String(64), nullable = True)
    time = Column(Integer, nullable=True)
    tags = relationship('Tag', secondary = 'service_tag', backref = 'services')

#
# service_tag = Table(
#         'service_tag', Base.metadata,
#         Column('service_id', Integer, ForeignKey('services.id')),
#         Column('tag_id', Integer, ForeignKey('tags.id'))
#
#     )
    # count = 0
    # def __init__(self, tag, reputation, time = ctime(), resource = [], descripition = ''):
    #     # global count
    #     self.id = Service.count
    #     Service.count = Service.count + 1
    #     self.tag = tag
    #     self.reputation = reputation
    #     self.resource = resource
    #     self.description = descripition
    #     self.time = time
    #
    # def getCount(self):
    #     print(Service.count)