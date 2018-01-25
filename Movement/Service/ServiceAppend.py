# @Time    : 2018/1/25 0025 16:55
# @Author  : miaoxu
# @Site    : 
# @File    : ServiceAppend.py
# @Software: PyCharm Community Edition
from Stragety.MoveInStragety import MoveInStragety
from Respository.ServiceRespository import ServiceRespository
from Entity.Service import Service
class ServiceAppend():
    def __init__(self, MoveInStragety):
        self.moveInStragety = MoveInStragety

    # 根据MoveInStragety得到需要生成的service列表
    def getService(self):
        serviceMap = self.MoveInStragety.getServiceMap()
        for tag in serviceMap.keys():
            self.generate(tag, serviceMap[tag])

    # 生成所需的服务标签和要求的数量生成服务列表
    def generate(self, tag, servicenum):
        loops = range(servicenum)
        temp_list = []
        for i in loops:
            service = Service(tag, self.moveInStragety.reputationStragety.getReputation())
            temp_list.append(service)

        ServiceRespository.save(temp_list)