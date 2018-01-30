# @Time    : 2018/1/29 0029 22:10
# @Author  : miaoxu
# @Site    : 
# @File    : testService_tag.py
# @Software: PyCharm Community Edition
import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from Entity.Tag import Tag as Tag
from Entity.Service import Service as Service

from Entity.Service_Tag import service_tag
from constant.database import Base




engine = create_engine('mysql+pymysql://root:root@localhost:3306/ServiceSimulation?charset=utf8')
# Base = declarative_base()
# class Tag(Base):
#     __tablename__ = 'tags'
#
#     id = Column(Integer, primary_key = True)
#     # 第一级分类，大类
#     firstlevel = Column(Integer, nullable = False)
#     # 第二级分类 小类
#     secondlevel = Column(Integer, nullable = False)
#     # 每一个标签的名字
#     name = Column(String(64), nullable = True)
# class Service(Base):
#     __tablename__ = 'services'
#
#     id = Column(Integer, primary_key = True)
#     # 信任值（评分）
#     reputation = Column(Integer, nullable = False)
#     # service的功能描述
#     description = Column(String(2000), nullable = True)
#     time = Column(Integer, nullable=True)
#     tags = relationship('Tag', secondary = 'service_tag', backref = 'services')


# service_tag = Table(
#         'service_tag', Base.metadata,
#         Column('service_id', Integer, ForeignKey('services.id')),
#         Column('tag_id', Integer, ForeignKey('tags.id'))
#
#     )


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    facker = Factory.create()
    Session = sessionmaker(bind = engine)
    session = Session()
    # faker_tags = [Tag(firstlevel = facker.random_int(), secondlevel = facker.random_int(), name = facker.word()) for i in range(10)]
    # session.add_all(faker_tags)
    #
    # for i in range(100):
    #     service = Service(
    #         reputation = facker.random_int(),
    #         description = facker.word(),
    #         time = facker.random_int(),
    #
    #     )
    #     for tag in random.sample(faker_tags, random.randint(2, 5)):
    #         service.tags.append(tag)
    #     session.add(service)

    sql = session.query(Service).all()
    for item in sql:
        print(item.description)
    # print(sql)
    session.commit()
