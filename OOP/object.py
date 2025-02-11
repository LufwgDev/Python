class People:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print("Hi " +  self.name)

hector = People("Hector")

hector.hi()