# Operadores y estructuras de control

# Operadores Aritméticos
print (f"La suma de 9 + 15 es: {9 + 15}")
print (f"La resta de 1993 - 2024 es: {1993 - 2024}")
print (f"La Multiplicación de 42 * 5 es: {42 * 5}")
print (f"La división de 12 / 13 es: {12 / 13}")
print (f"El módulo de 5 es: {5 % 2 }")
print (f"La división entera de 4 // 3 es: {4 // 3}")
print (f"La raíz cuadrada de 4 es: {4 ** 0.5}")
print (f"La potencia de 8 es: {8 ** 2}")

# Operadores de Comparación
print (f"Igualdad: manzana == manzana  {'manzana'== 'manzana'}")
print (f"Diferencia: carros != motos {'carros' != 'motos'}")
print (f"Mayor que: 30 > 28 {30 > 28}")
print (f"Menor que: 28 < 30 {28 < 30}")
print (f"Mayor o igual que: 50 >= 50 {50 >= 50}")
print (f"Menor o igual que: 50 <= 30 {50 <= 30}")

# Operadores Lógicos
print (f"AND: 9 + 5 == 14 and 5 * 2 == 10 {9 + 5 == 14 and 5 * 2 == 10}")
print (f"OR: 9 + 5 == 14 or 10 - 2 == 4 {9 + 5 == 14 or 10 - 2 == 4}")
print (f"NOT: not 9 + 5 == 15 {not 9 + 5 == 15}")

# Operadores de Asignación
numero = 3
print (f"Número es: {numero}")
numero += 5
print (f"Suma y Asignación += : {numero}")
numero -= 1
print (f"Resta y Asignación -= : {numero}")
numero *= 5
print (f"Multiplicación y Asignación *= : {numero}")
numero /= 5
print (f"División y Asignación /= : {numero}")
numero %= 2
print (f"Módulo y Asignación %= : {numero}")

# Operadores de Identidad
# Compara el valor de la posición de memoria
number = numero
print (f"Numero is number es: {numero is  number}") # Igualdad
print (f"Numero is not same number: {numero is not number}") # Desigualdad

# Operadores de Pertenencia
# Objeto que pertenece a un conjunto
print (f"'dragons' in 'imagine dragons'{'dragons' in 'imagine dragons'}")
print (f"'oz' not in 'imagine dragons'{'oz' not in 'imagine dragons'}")

# Operadores de Bit
d = 7 # 0111
r = 4 # 0100
print (f"AND: 7 & 4 = {7 & 4}") #0100
print (f"OR: 7 | 4 = {7 | 4}") #0111
print (f"XOR: 7 ^ 4 = {7 ^ 4}") #0011
print (f"NOT: ~7 = {~7}")
print (f"Desplazamiento derecha: 4 >> 2 = {4 >> 2}") #001
print (f"Desplazamiento izquierda: 4 << 2 = {4 << 2}") #010000

# Estructuras de control

# Condicionales

numero = 8
if numero <= 0:
    print (f"El número es negativo")
elif numero % 2 == 0:
    print (f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")    

# Iterativos 
# for
for i in range (21): 
    print(i)

acumulador = 0 
# While
while acumulador <= 5: 
    print(f"Número: {acumulador}")
    acumulador += 1 

# Excepciones

try:
    cantidad = int(input("Ingresa una cantidad: "))
except:        
    print ("Error, La cantidad debe ser un número entero")
    
# Dificultad Extra

for numero in range (10,56):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print (numero)    
