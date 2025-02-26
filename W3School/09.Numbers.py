#int
x= 1
y=2.8
z=1j
print(type(x),x)
print(type(y),y)
print(type(z),z)

x=1
y=314159265359
z=-314159265359
print(type(x),x)
print(type(y),y)
print(type(z),z)



#float

x=1.0
y=3.14159265359
z=-3.14159265359
print(type(x),x)
print(type(y),y)
print(type(z),z)

x=35e3
y=12E4
z=-87.7e100
print(type(x),x)
print(type(y),y)
print(type(z),z)



#Complex

x = 3 +5j
y=5j
z=-5j


#type Conversion

x=1
y=2.8
z=1j
print(type(x),x)
print(type(y),y)
print(type(z),z)
a=float(x)
b=int(y)
c=complex(x)
print(type(a),a)
print(type(b),b)
print(type(c),c)

#Complex cannot be convreted into another type

#Random
import random
print(random.randrange(1,10))
