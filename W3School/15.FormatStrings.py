age = 36
#txt = "My name is Jhonn, I am " + age
#print(txt)
#  File "c:\Users\Estudiante\Desktop\Python\W3School\15.FormatStrings.py", line 2, in <module>
#    txt = "My name is Jhonn, I am " + age
#          ~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
#TypeError: can only concatenate str (not "int") to str


#F-Strings
txt = f"My name is John, I am {age}"
print(txt)

price = 69
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20*69} dollars"
print(txt)