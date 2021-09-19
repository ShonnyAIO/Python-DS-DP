class ComputerState:
    name = "state"

    def __str__(self):
        return self.name

    def switch(self, state):
        self.__class__ = state
        print(self.name)


class On(ComputerState):
    name = "on"


class Off(ComputerState):
    name = "off"


class Hibernate(ComputerState):
    name = "hibernate"


class Suspend(ComputerState):
    name = "suspend"


class Computer(ComputerState):
    def __init__(self):
        print('Computer')
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


obj = Computer()
obj.change(On)
obj.change(Off)
obj.change(Hibernate)
obj.change(Suspend)
obj.change(On)
obj.change(On)
