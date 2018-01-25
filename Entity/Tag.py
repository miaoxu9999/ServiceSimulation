# 模拟标签
class Tag():
    def __init__(self, firstlevel, secondlevel, name):
        # 第一级分类，大类
        self.firstlevel = firstlevel
        # 第二级分类 小类
        self.secondlevel = secondlevel
        # 每一个标签的名字
        self.name = name