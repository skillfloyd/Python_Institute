# pruebas
dic={"1":0,"2":3}
li=[1,2,3]
tup=(1,2,3)

# pruebas 1
#-80 16
j= 50 
x = 2
var = 50
rem = 10
i = 5
j=j-(i + var + rem) 
j-= (i + var + rem)
x**=2
x **=  2
print(j, x)

# pruebas 2
#1 1 
var1 = 1 
var2 = var1 
print(var2, var1)

# pruebas 3
#4
x = 1 
x = x * 2 
x*= 2
print(x)

# pruebas 4
#error
# var 1 = 120
# @var1 = 120
# 1var = 120
# var-1 = 120

# pruebas 5
#8
y = (1+1)** (5-2)
print(y)

# pruebas 6
#256
x = 4**2**2
print(x)

# pruebas 7
def SumarDosnumeros():
    num1 = float(input("Ingrese el numero 1: ")) 
    num2 = float(input("Ingrese el numero 2: ")) 
    print("la suma de", int(num1), "+", int (num2), "es igual a: ", int (num1 + num2))
SumarDosnumeros()

# pruebas 8
#0.8
#0
#-1.0
#1.0
4 / 5 * 1 % 2 ** 1
3 // 2 - 2 + 3 % 2
2 // 3 / 3 - 1 ** 3
5 / 5 + 5 * 5 ** 5 % 5

# pruebas 9
#error
if 5 > 2:
 print("Five is greater than two!")
        #print("Five is greater than two!")
        
        
# pruebas 10
#####("Hello World")


# pruebas 11
#comentario


# pruebas 12
#cre una variable  "hello" y que contenga "mundo"
####=#######


#pruebas 13
#6
igual = 0
for x in range (2):
    for y in range (2):
        if x == y:
            igual += 2
    else:
        igual += 1
print (igual)

#pruebas 14
#¿Cuál es la diferencia entre lista y tuplas en Python?
#Las listas son mutables
#Las tuplas son inmutables


#pruebas 15
#¿Python es sensible a las mayúsculas y minúsculas?
#Sí

#pruebas 16
#¿cual son algunos Type Conversion (conversión de tipos) en Python?
#int()
#float() 
#str()


#pruebas 17
#con que palabra se define una funcion
#def

#pruebas 18
# ¿Cómo funciona break, continue?
# Break	Permite la terminación del bucle cuando se cumple alguna condición y el control se transfiere a la siguiente instrucción.
# Continue 	Permite saltar alguna parte de un bucle cuando se cumple alguna condición específica y el control se transfiere al principio del bucle.

#pruebas 19
# ¿Cómo se escriben los comentarios en Python?
#


#pruebas 20
#Hola Mundo
print(((((("Hola Mundo"))))))


#pruebas 21
#4
stg='ABCD'
len(stg)

#pruebas 22
# que valores reemplazar en 1 2 3 para que el programa me diga si es primo o no el numero a ingresar
a=int(input("ingresa un numero"))
if a>1:
    for x in range(2,a):
        if(a%x)==0:
            print("1")#no es primo
            break
    else:
            print("2")#es primo
else:
        print("3")#no es primo
        
#pruebas 23        
#¿Cuál es el resultado de lo siguiente?

# try:
#     if '1' != 1:
#       raise "algún error"      
#     else:
#         print("no se ha producido algún error")
# except "un error":
#     print ("se ha producido algún error")

# a) se ha producido algún error
# b) no se ha producido algún error
# c) código inválido
# d) ninguno de los anteriores
# Respuesta: c) código no válido


#pruebas 24
#Cuál de las siguientes declaraciones es válida?
# a) xyz = 1000
# b) x y z = 10 20 30
# c) a,b,c = 10, 20, 30 
# d) a_b_c = 102030
# Respuesta: ACD


#pruebas 25
# ¿Cuál de estos es división de piso (floor division)?
# a) /
# b) //
# c) %
# d) Ninguna de las anteriores
# Respuesta: b) //


#pruebas 26
# ¿Cuál de estos es exponecial?
# a) **
# b) *
# c) %
# d) Ninguna de las anteriores
# Respuesta: a) **


#pruebas 27
# ¿Cuál de estos es exponecial?
# a) **
# b) *
# c) %
# d) Ninguna de las anteriores
# Respuesta: a) **


#pruebas 28
#¿Cuál de estos es operador de Módulo (Modulo Operator)?
# a) /
# b) //
# c) %
# d) Ninguna de las anteriores
# Respuesta: c) %


#pruebas 29
#0
#0
#-24 
#4.0
1 % 1 ** 1 / 1 * 1 
2 + 2 % 2 // 2 - 2
3 - 3 ** 3 // 3 * 3
4 * 4 * 4 / 4 // 4 


#pruebas 30
#[1, 2, 3]
a = [1, 2]
a.append(3)
print(a)


#pruebas 31
#que numero eliminiara
#5
a = [1, 2, 3, 4, 5]
a.pop()


#pruebas 32
#[4, 3, 2, 1]
lista = [3, 2, 4, 1]
lista.sort()
lista.sort(reverse=True)


#pruebas 33
#-2
def add(a, b):
    return a + b - a * b

add(a=2, b=4)

#pruebas 34
#[2, 1, 0]
def funcion(x):
    lista = []
    for y in range(0, x):
        lista.insert(0, y)
    return lista
print(funcion(3))



#pruebas 35
#¿Qué hace el símbolo '#' en Python?
# el simbolo '#' se usa para comentar


#pruebas 36
#Cuál es la indexación negativa
#a[-1]


#pruebas 37
#¿Cual seria la salida esperada?

try:
  print(x)
except NameError:
  print("Variable x no definida")
except:
  print("Algo salio mal")
# a) SyntaxError
# b) Imprime x
# c) Variable x no definida
# d) Algo salio mal
# Respuesta: c) Variable x no definida
 
  
#pruebas 38 
#¿Cual seria la salida esperada?
# a) albano
# b) nombre es: albano
# c) SyntaxError
# d) "nombre es: " + Nombre?
# Respuesta: c) SyntaxError

# Nombre? = "albano"
# print("nombre es: " + Nombre?)


#pruebas 39
#¿Que hace este codigo?
nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")
# a) Imprime mi nombre y tambien la cantidad de letras
# b) Imprime mi nombre en mayusculas y tambien la cantidad de letras
# c) Imprime mi nombre en minusculas y tambien la cantidad de letras
# d) Imprime mi nombre 2 veces
# Respuesta: b) Imprime mi nombre en mayusculas y tambien la cantidad de letras

#pruebas 40
#¿Que hace este codigo?
frase = input("Introduce una frase: ")
print(frase[::-1])
# a) Imprime mi frase
# b) Imprime la ultima letra de mi frase
# c) Imprime mi frase invertida
# d) Imprime mi frase excepto la ultima letra de frase
# Respuesta: c) Imprime mi frase invertida


#pruebas 41
#¿Que imprimira este codigo si ingresamos
# Leche
# 5000
# 10
# respectivamente?
#Leche: 10 unidades x 5000.0$ = 50000.0$
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades} unidades x {precio}€ = {total}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
# a) Error en el Codigo
# b) Leche: 10 unidades x 5000 = 5000
# c) Leche: 10 unidades x 5000.0$ = 50000.0$
# d) Leche: 10 unidades x 5000 = 50000
# Respuesta: c) Leche: 10 unidades x 5000.0$ = 50000.0$


#pruebas 42
#¿Que imprimira este codigo si ingresamos $
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")

# a) Error en el Codigo
# b) Dollar
# c) $
# d) La divisa no está.
# Respuesta: b) Dollar



#pruebas 43
#¿Que imprimira este codigo?
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")
    
# a) 1 2 3 4 5 6 7 8 9 10
# b) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# c) 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
# d) 10 9 8 7 6 5 4 3 2 1
# Respuesta: c) 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,


#pruebas 44
#¿Que imprimira este codigo si ingresamos arañara?
palabra = input("Introduce una palabra: ")
palabra_invertida = palabra
palabra = list(palabra)
palabra_invertida = list(palabra_invertida)
palabra_invertida.reverse()
if palabra == palabra_invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
# a) Es un palíndromo
# b) No es un palíndromo
# c) NameError
# d) SyntaxError
# Respuesta: a) Es un palíndromo


#pruebas 45
#¿Que imprimira este codigo?
Valor_1= 2
Valor_2= 1 
print(Valor_1<<Valor_2)
# a) 4
# b) 2
# c) 1
# d) SyntaxError
# Respuesta: a) 4


#pruebas 46
#¿Que imprimira este codigo?
Valor_1= "dos"
Valor_2= "cuatro"
print(len(Valor_2)*len(Valor_1))
# a) 18
# b) 8
# c) NameError
# d) SyntaxError
# Respuesta: a) 18



#pruebas 47
#¿Que deberia ser colocado en cada espacio para que al introcudir 10 el resultado sea "Eres mayor de edad."?

#edad = int(input("¿Cuál es tu edad? "))
# if edad < 18: 
#     print (Codigo_1)
# else:
#     print(Codigo_2)

# a) Codigo_1= "Eres mayor de edad." 
# b) Codigo_2= "Eres mayor de edad." 
# c) Codigo_1= "Eres menor de edad." 
# d) Codigo_2= "Eres menor de edad."
# Respuesta: a) d) 



#pruebas 48
#Una tupla es mutable
#falso

#pruebas 49
#Una variable booleana es una variable que sólo puede tomar dos posibles valores True y False
#verdadero

#pruebas 50
a=0
b=1
c=0
a == b and a == c or a == b or c == b and c != b
#False
