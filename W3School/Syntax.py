#Execute 
#python --version
#Python 3.13.2

#python syntax.py

#python
#Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>>
#>>>print("Hello, World!")
#Hello, World!
#>>> exit()

import sys
print (sys.version)
#3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]





#Identation
if 5 > 2:
    print("Five is greater than two")

#if 5>2:
#print("Five is greater than two")

#File "C:\Users\Estudiante\Desktop\Python\W3School\syntax.py", line 22
#    print("Five is greater than two")
#    ^^^^^
#IndentationError: expected an indented block after 'if' statement on line 21

#
if 5 > 2:
                                    print("Five is greater than two")

if 5>2:
 print("Five is greater than two")

#
if 5 > 2:
    print("five is greater than two!")
        print("the same!")

# File "C:\Users\Estudiante\Desktop\Python\W3School\syntax.py", line 39
#    print("the same!")
#IndentationError: unexpected indent





#Variables
x = 5
y = "Hello, world!"
print(x)
print(y)





#Comments
#in code Documentation
print(x)#prints 5
#print(W) does not print
print(y) #prints Hello, world!