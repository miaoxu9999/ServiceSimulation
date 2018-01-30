# @Time    : 2018/1/25 0025 17:01
# @Author  : miaoxu
# @Site    : 
# @File    : ServiceAddStragety.py
# @Software: PyCharm Community Edition
from Stragety import MoveInStragety
class ServiceAddStragety(MoveInStragety):
    def __init__(self, numTagMap, interval, time, reputationStragety):
        super(ServiceAddStragety, self).__init__(numTagMap, interval, time, reputationStragety)