import random  # Importamos la librería random
import time

# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = random.randint(5, 5)


print (MAGENTA+"Bienvenido a mi trivia sobre 'La naturaleza'"+RESET)
time.sleep(1)
print ("\nPondremos a prueba tus conocimientos")
print (YELLOW+"\nComenzarás con", puntaje, "puntos"+RESET)
time.sleep(1)
print(MAGENTA+"\nIMPORTANTE"+RESET)
print(GREEN+"Cada respuesta CORRECTA sumará +10 puntos"+RESET)
print(RED+"Cada respuesta INCORRECTA restará -1 punto"+RESET)
time.sleep(2)

nombre = input ("\nIngresa tu nombre: ")
print("\nCargando preguntas...")
time.sleep(1)
print("\n...")
time.sleep(1)

# Es importante dar instrucciones sobre cómo jugar:

print ("\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# Pregunta 1
print (CYAN+"1) ¿Cual es la planta mas venenosa del planeta?"+RESET)
print ("a) La Posidonia")
print ("b) La adelfa") #
print ("c) Planta carnivora")
print ("d) Violeta africana")

time.sleep(1)
respuesta_1 = input("\nTu respuesta: ")
time.sleep(1)
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")


if respuesta_1 == "b":
  puntaje += 10
  print (GREEN+"\nMuy bien, ganaste 10 puntos"+RESET)
else:
  print (RED+"\nIncorrecto, -1 punto"+RESET)
  puntaje -= 1
  print(BLUE+"La respuesta correcta es: 'b'"+RESET)

print("")
print(YELLOW+nombre, "llevas", puntaje, "puntos"+RESET)
time.sleep(1)

# Pregunta 2
print (CYAN+"\n2) ¿Cual es el río más caudaloso del mundo?"+RESET)
print ("a) Rio Tajo")
print ("b) Rio Nilo")
print ("c) Rio Duero")
print ("d) Rio Amazonas") #

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")


if respuesta_2 == "a":
  time.sleep(1)
  print (RED+"\nIncorrecto!" +RESET)
  puntaje -= 1
  print(BLUE+"La respuesta correcta es: 'd'"+RESET)
elif respuesta_2 == "b":
  time.sleep(1)
  print (RED+"\nIncorrecto!" +RESET)
  puntaje -= 1
  print(BLUE+"La respuesta correcta es: 'd'"+RESET)
elif respuesta_2 == "c":
  time.sleep(1)
  print (RED+"\nIncorrecto!" +RESET)
  puntaje -= 1
  print(BLUE+"La respuesta correcta es: 'd'"+RESET)
else:
  puntaje += 10
  time.sleep(1)
  print (GREEN+"Muy bien, ganaste 10 puntos", nombre+RESET)
  
time.sleep(1)
print(YELLOW+"\nLlevas", puntaje, "puntos"+RESET)
time.sleep(1)

# Pregunta 3
print (CYAN+"\n3) ¿Que es la humedad?"+RESET)
print ("a) Vaporización a la presión absoluta donde se mide la temperatura.")
print ("b) Es la cantidad de vapor de agua que hay en el aire ") #
print ("c) Gas sin color ni olor.")
print ("d) Ninguna de las anteriores")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "b":
  puntaje += 10
  print (GREEN+"\nMuy bien, ganaste 10 puntos"+RESET)
else:
  print (RED+"\nIncorrecto", nombre, ""+RESET)
  puntaje -= 1
  print(BLUE+"La respuesta correcta es: 'd'"+RESET)
  
#fin  

print("")
print (MAGENTA+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)