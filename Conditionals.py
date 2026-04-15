"""
Estructura de los condicionales

if (condición):
    Bloque de codigo si se cumple la condición

    

Operadores de comparación:
"""

# ==  igual a  (igualdad)
# edad = 18
# if edad == 18:
#     print("Tiene 18")

# !=  diferente de
# edad = 18
# if edad != 18:
#     print("No tiene 18")


# >   mayor que
# edad = 20
# if edad > 20:
#     print("Es mayor a 20")

# <   menor que
# edad = 16
# if edad < 18:
#     print("Es menor a 18")


# >=  mayor o igual que
# edad = 20
# if edad >= 20:
#     print("Es mayor a 20")


# <=  menor o igual que
# edad = 20
# if edad > 20:
#     print("Es mayor a 20")


"""
operadores logicos:
"""

# and → todas las condiciones deben cumplirse
# edad = 20
# tiene_cedula = True

# if edad >= 18 and tiene_cedula:
#     print("Puede entrar")


# or → al menos una condición debe cumplirse
# edad = 16
# tiene_permiso = True

# if edad >= 18 or tiene_permiso:
#     print("Puede entrar")



# not → invierte el valor lógico
# activo = False

# if not activo:
#     print("El usuario está inactivo")


"""
        Comparadores de identidad
para comprar el mismo objeto en memori
Is
Is not

usuario = True

if usuario is None:
    print("El usuario no existe")

if usuario is not None:
    print("Tenemos un usuario válido")

"""




# Python existe una forma más corta de escribir condiciones, conocida como condicional ternario.

# variable = valor_si_true if condicion else valor_si_false

# Ejemplo
# edad = 20
# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"




"""
                    EJERCICIOS

1 
edad = 15
permiso = True

if edad >= 18 or edad >= 16 and permiso:
    print("Entra")
else:
    print("No entra")


2
x = 0

if x:
    print("A")
else:
    print("B")


3
activo = False

if not not activo:
    print("activo o inactivo ? ")



4
x = None

if x == None:
    print("A")

if x is None:
    print("B")



5
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a == c)

6
if True or False and False:
    print("se ejecuta o no?")

7
x = ""
if not x:
    print("Vacío?")

    
8  ternario
edad = 17
resultado = "Mayor" if edad >= 18 else "Menor"
print(resultado)


9
a = 1000
b = 1000

print(a is b)
print(a == b)
"""
