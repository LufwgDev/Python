class People:

    # field that can be called from the classs
    className = "People"

    #Constructor
    def __init__(self, name: str, age: int): #: str is a type hint that means string
        #field that can only be called from the objects
        self.name = name
        self.__age = age

        
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
    
    #can acces to private fields and return it
    def get_age(self):
        return self.__age

    def __some(self):
        print("something")

#class with inherited cosntructor
class Bartender(People):
    pass
    def welcome(self):
        print("Welcome")

#class that modifies the inherited cosntructor
class Student(People):
    def __init__(self,name,age,career):
        #sending the parameters to the Super o Father class' cosntructor
        super().__init__(name,age)

        self.career=career

    #overriding the inherited method
    def hi(self):
        print("Hi, I am "+self.name+"and I'm an "+self.career)


#creating an instance of the method
hector = People("Hector",21)

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

#
print(hector.name) #print "Hector"

#print(hector.age) 
#Traceback (most recent call last):
#  File "C:\Users\Estudiante\Desktop\Python\OOP\object.py", line 47, in <module>
#    print(hector.age)
#          ^^^^^^^^^^
#AttributeError: 'People' object has no attribute 'age'

print(hector.get_age())

#hector.__some()
#Traceback (most recent call last):
#  File "C:\Users\Estudiante\Desktop\Python\OOP\object.py", line 67, in <module>     
#    hector.__some()
#    ^^^^^^^^^^^^^
#AttributeError: 'People' object has no attribute '__some'


bart = Bartender("bart",12)
bart.hi()
#invoking new method that parents class do not have.
bart.welcome()


lu = Student("Lu",21,"Engineer")
#method inherited from People class, modified in cild class
lu.hi()
#getting a field that the People class do not have.
print(lu.career)


