import types


class StrategyExample:
    def __init__(self, func=None):
        if func is not None:
            self.execute = types.MethodType(func, self)
        pass

    def execute(self):
        print(self.name)


def execute_1(self):
    print('execute #1')


def execute_2(self):
    print('execute #2')


obj1 = StrategyExample(execute_2)
obj2 = StrategyExample(execute_1)
obj1.execute()
obj2.execute()
