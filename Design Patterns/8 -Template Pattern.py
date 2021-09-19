class MakeFood:
    def prepare(self):
        pass

    def collect(self):
        pass

    def cook(self):
        pass


class MakePizza(MakeFood):
    def prepare(self):
        print('Prepare dough')
        print('Cut tomatoes...')

    def collect(self):
        print('Get tomatoes, dough etc')

    def cook(self):
        print('Baking pizza')


class MakeSpaghetti(MakeFood):
    def prepare(self):
        print('Preparing...')

    def collect(self):
        print('prepare enough')

    def cook(self):
        print('Wait for spaghetti to cook')


obj1 = MakeSpaghetti()
obj1.prepare()
obj1.collect()
obj1.cook()
