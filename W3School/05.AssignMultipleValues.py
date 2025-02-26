#x, y, z = "x"
#print(x)
#print(y)
#print(z)

#    x, y, z = "x"
#    ^^^^^^^
#ValueError: not enough values to unpack (expected 3, got 1)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to multiple variables

x = y = z = "Hello there!"

print(x)
print(y)
print(z)

#Unpacking a Collection
fruits = ["apple","banana","cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

