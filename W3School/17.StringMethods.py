#All string methods return new values, they do not change the original
txt = "Hello, Cruel World!"

#Fist Caractacter Upper, all the others lower
print(txt.capitalize())

#to lower case alternative
print(txt.casefold())
print(txt.center(5))
x=txt.center(10,"$")
print(x)

txt2 = "banana"
x = txt2.center(20)

print(x)

x=txt2.center(10,"$")
print(x)

#How many times a string is in another
print(txt.count("l"))
print(txt.count("l",0,len(txt)-1))

