# Service类的模拟

# 修改2018年1月29日21:33:45
# 将本类映射到
from time import ctime
class Service:
    count = 0
    def __init__(self, tag, reputation, time = ctime(), resource = [], descripition = ''):
        # global count
        self.id = Service.count
        Service.count = Service.count + 1
        self.tag = tag
        self.reputation = reputation
        self.resource = resource
        self.description = descripition
        self.time = time

    def getCount(self):
        print(Service.count)