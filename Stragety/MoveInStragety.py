# @Time    : 2018/1/25 0025 14:16
# @Author  : miaoxu
# @Site    : Service加入的策略
# @File    : ServiceMoveIn.py
# @Software: PyCharm Community Edition
from Stragety.MoveInStragety import MoveInStragety
class MoveInStragety(object):
    def __init__(self, numTagMap, interval, time, reputationStragety):
        self.numTagMap = numTagMap
        self.interval = interval
        self.time = time
        self.reputationStragety = reputationStragety

    # 获取得到每个Service的标签的数量
    def getServiceMap(self):
        return self.numTagMap
    # 获取多长时间进行一次获取Service的操作
    def getServiceInterval(self):
        return self.interval
    # 得到Service进入的时间
    def getServiceTime(self):
        return self.time

    def getReputationStragety(self):
        return self.reputationStragety
