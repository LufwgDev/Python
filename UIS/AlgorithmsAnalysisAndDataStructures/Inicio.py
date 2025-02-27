a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a//b) #divivion entera
print(a**b) #potencia
print(a%b) #Módulo

texto = "1025"
numero = 5
#print(numero + texto)
entero = int(texto)
print(numero + entero)
print(type(texto))

img = 25 + 5j


#Caracteres - Strings

curso = "Estructuras de Datos"
print(curso.upper()) #Mayúsculas
print(curso.lower()) #Minusculas
print(curso.capitalize())# Primera Mayúscula

print(len(curso))
print(curso.replace("Datos","Información")) #reemplazar
print(curso.find("de"))#12
print(curso.find("s"))#1

#Condicionales
edad = int(input("Ingresa tu edad \n"))

if edad <12:
    print("Es niño")
elif edad <18:
    print("es adolescente")
elif edad <60:
    print("es Adulto")
else:
    print("es Adulto mayor")

#Ciclos
for i  in range(1,11):
    print(i)#hasta 10

valor = 25

while valor >0:
    valor = valor-15
    print(valor)
    
valor = 25
while valor>0:
    valor-=1
    print(valor)

