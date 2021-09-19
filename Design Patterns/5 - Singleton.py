class Car:
    _instance = None

    def getInstance():
        if Car._instance == None:
            Car()
        return Car._instance

    def __init__(self):
        if Car._instance != None:
            raise Exception("Singleton: There can only be one project")
        else:
            Car._instance = self


obj = Car()
print(obj)

obj2 = Car.getInstance()
print(obj2)
