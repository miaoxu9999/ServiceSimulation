# @Time    : 2018/1/25 0025 16:55
# @Author  : miaoxu
# @Site    : 
# @File    : ServiceAppend.py
# @Software: PyCharm Community Edition
from Stragety.ServiceAddStragety import ServiceAddStragety
from Respository.ServiceRespository import ServiceRespository
from Entity.Service import Service
class ServiceAppend():
    def __init__(self, ServiceAddStragety):
        self.ServiceAddStragety = ServiceAddStragety

    # 根据ServiceAddStragety得到需要生成的service列表
    def getService(self):
        serviceMap = self.ServiceAddStragety.getServiceMap()
        for tag in serviceMap.keys():
            self.generate(tag, serviceMap[tag])

    # 生成所需的服务标签和要求的数量生成服务列表
    def generate(self, tag, servicenum):
        loops = range(servicenum)
        temp_list = []
        try:
            for i in loops:
                service = Service(tag, self.ServiceAddStragety.reputationStragety.getReputation())
                temp_list.append(service)

            ServiceRespository.save(temp_list)
        except:
            pass