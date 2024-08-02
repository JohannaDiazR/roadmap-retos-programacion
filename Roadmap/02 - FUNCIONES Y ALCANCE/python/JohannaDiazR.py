# Funciones

# Función básica

def bandas():
    print ("Imagine Dragons,", "Mägo de oz,","OneRepublic")

bandas()

# Función con retorno
def nevados_Colombia():
    return "Cocuy","Santa Isabel","Tolima"
print (nevados_Colombia())

# Función con parámetro
def genero_musical(nombre):
    print(f"Imagine Dragons, {nombre}")
genero_musical("Rock Alternativo")

# Función con parámetros
def generos(bandas, nombre):
    print (f"{bandas},{nombre}")
generos("Ed Sheeran ","pop")    
generos (bandas="Caligaris",nombre="ska")

# Función con argumento predefinido
def default_musica (nombre = "Imagine Dragons"):
    print(f"Banda, {nombre}")
default_musica()    

# Retornar varios valores
def varios_return():
    return "Banda","Moügli"

bandas, nombre = varios_return()
print (bandas)
print (nombre)  

# Número variable de argumentos
# Más de un argumento separados por ,
def variable(*nombres):
    for nombre in nombres:
        print (f"Banda, {nombre}")
variable("Twenty One Pilots","Maroon 5","Morat","Lérica" )        

# Número variable con palabra clave

def clave_variable(**nombres):
    for key, value in nombres.items():
        print (f"{value} ({key})")

clave_variable(
    nombre="Imagine Dragons",
    integrantes=["Dan Reynolds","Ben Mckee","Wayne Sermon"],
    albumes= ["Evolve","Mercury","Origins"]
)

# Funciones dentro de otras

def externa():
    def interna():
        print("Interna: Imagine Dragons,", "Mägo de oz,","OneRepublic")
    interna()
externa()        

# Funciones definidas de python
print(len("Fuerte como Roble"))
print ("Rendirse no esta en nuestros genes".title().split())
print(type("var"))

# Variables Locales y Globales
# Global El ámbito es superior a lo que se quiere ejecutar
# Local Solo se permite el acceso dentro de la función

global_v = "Lavander"
print (global_v)

def plant():
    local_v = "plant"
    print (f"{local_v} : {global_v}🪻")

plant()

# Dificultad Extra

def text_number(a,b)-> int:
    contador = 0
    for number in range (1,101):
        if number % 3 == 0 and number % 5 == 0:
            print (a + b)
        elif number % 3 == 0:
            print (a)
        elif number % 5 == 0:
            print (b)
        else:
            print (number)
            contador += 1
    return contador        

print (text_number("You're ","Great :) "))        
