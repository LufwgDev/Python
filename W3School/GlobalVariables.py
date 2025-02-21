#created outside a function
x = "Good Morning!"
def myfunc():
    x = "awesome"
    print ("Python is " + x)

myfunc()
print ("Python is " + x)

t = "time"

def otherfunction():
    z = "cool"
    global y 
    y = "Fantastic"

#    global w = "fast"

#    global w = "fast"
#             ^
#SyntaxError: invalid syntax

#global x
#x= 13
#    global x
#    ^^^^^^^^
#SyntaxError: name 'x' is used prior to global declaration

    global x
    x=134




otherfunction()

#print ("Pyrhon is " + z)
#    print ("Pyrhon is " + z)
#                          ^
#NameError: name 'z' is not defined
print ("Python is " + y)
print ("Python is " , x)

