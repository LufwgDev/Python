print("Hello")
print('Hello')

#Quotes inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a= "Hello"
print(a)

#Multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

a= '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are arrays. char type does not existe 
a="Hello, World!"
print(a[1])

#Looping througt a String
for x in "banana":
    print(x)

#String Length
print(len(a))

#Check String
txt = "the best things in life are NOT free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

#check if not
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")