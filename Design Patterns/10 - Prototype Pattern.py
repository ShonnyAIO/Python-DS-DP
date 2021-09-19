from copy import deepcopy
import time


class Prototype(object):
    def clone(self):
        return deepcopy(self)


class NetworkConnector(Prototype):
    def __init__(self):
        self.name = 'expensive method here'
        time.sleep(5)
        print("Object created")


obj1 = NetworkConnector()
print(obj1.name)
obj2 = NetworkConnector()
#obj2 = obj1.clone()
# print(obj2.name)
