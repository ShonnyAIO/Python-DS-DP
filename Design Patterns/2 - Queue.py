import queue


class Car:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


obj1 = Car("RX-7")
obj2 = Car("Supra GT")
obj3 = Car("BWM M5")
obj4 = Car("Skyline GTR")

q = queue.LifoQueue()
q.put(obj1)
q.put(obj2)
q.put(obj3)
q.put(obj4)
# q.put(Car("Nissan Skyline"))


while not q.empty():
    obj = q.get()
    obj.showName()
