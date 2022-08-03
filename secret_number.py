# secret_number = 777

# print(
# """
# +==================================+
# | ¡Bienvenido a mi juego, muggle!  |
# | Introduce un número entero       |
# | y adivina qué número he          |
# | elegido para ti.                 |
# | Entonces,                        |
# | ¿Cuál es el número secreto?      |
# +==================================+
# """)
# a=0
# b=1
# while b==1:
#     if a == secret_number:
#         print("¡Bien hecho, muggle! Eres libre ahora")
#         b=0
#         break 
#     else:
#         print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
#         a = input("ingresa tu numero: ")
#         print(a)

def add(a):
    if a==1:
        return a - add(a-1)
       
    

print(add(a=4))



