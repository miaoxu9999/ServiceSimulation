# 模拟标签

# 修改2018年1月29日21:33:45
# 将本类映射到数据库中
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from Entity.Service_Tag import service_tag
from constant.database import Base
# Base = declarative_base()
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key = True)
    # 第一级分类，大类
    firstlevel = Column(Integer, nullable = False)
    # 第二级分类 小类
    secondlevel = Column(Integer, nullable = False)
    # 每一个标签的名字
    name = Column(String(64), nullable = True)
    # def __init__(self, firstlevel, secondlevel, name):
    #     # 第一级分类，大类
    #     self.firstlevel = firstlevel
    #     # 第二级分类 小类
    #     self.secondlevel = secondlevel
    #     # 每一个标签的名字
    #     self.name = name