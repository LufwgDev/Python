class People:

    # field that can be called from the classs
    className = "People"

    #Constructor
    def __init__(self, name: str): #: str is a type hint that means string
        #field that can only be called from the objects
        self.name = name

    #Method
    def hi(self):
        print("Hi " +  self.name)

    @staticmethod
    # can NOT access to class fields
    def helloWorld(): #def helloWorld(cls): 
        print("Hello World")
        # print("Hi" + cls.className) # error

    @classmethod
    #to access to class fields
    def holaMundo(cls):
        print("Hola Mundo")
        print("Hi" + cls.className)

#creating an instance of the method
hector = People("Hector")

#calling a method form the object
hector.hi()

#testing access to class fields from object and class
print(hector.className)
print(People.className)

#testing access to class' static methods from object and class
hector.helloWorld()
People.helloWorld()
#testing access to class' classmethods from object and class
hector.holaMundo()
People.holaMundo()

