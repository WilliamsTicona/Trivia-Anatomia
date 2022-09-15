import random # Importamos la libreria random y time
import time

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

iniciar_trivia = True # Iniciamos la variable True
intentos = 0 #Variable que almacenará el número de intentos del usuario 

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia

print ("\033[34mBienvenido a mi trivia sobre Anatomía \033[39m")
print ("\033[34mPondremos a prueba tus conocimientos\033[39m")
# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 11)

print ("\033[33mComenzaras con", puntaje, "puntos\033[39m")

while iniciar_trivia == True: #Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print ("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
  nombre = input("\033[34mIngresa tu nombre: \033[39m")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
  print ("\n \033[34m Hola", nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presiona 'Enter' para     enviar tu respuesta:\033[39m\n")
# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1 b
  print ("\033[34m1) Con respecto a las siguientes afirmaciones indica cual es verdadera:\n ")
  print ("a)Flexión: acción de enderezar o aumentar el ángulo entre partes del cuerpo.")
  print ("b)Aducción: movimiento de acercamiento al plano medio.")
  print ("c)Supinación: rotación medial del antebrazo y mano.")
  print ("d)Eversión: movimiento de la planta del pie hacia el plano medial.\033[39m")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("\033[31mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Tienes", puntaje, "puntos\n")
  if respuesta_1 == "c":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Tienes", puntaje, "puntos\n")
  if respuesta_1 == "d":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Tienes", puntaje, "puntos\n\033[39m")
  
  if respuesta_1 == "b":
    puntaje += random.randint(10, 21)
    print ("\033[32mMuy bien!", nombre,"Tienes", puntaje, "puntos\033[39m\n")

  time.sleep(3)

  # Pregunta 2 c
  print ("\033[34m2) Señala la alternativa incorrecta:\n")
  print ("a)Lordosis curvado hacia delante.")
  print ("b)Lordosis curvado lateral con rotación del cuerpo vertebral.")
  print ("c)La cifosis es la curvatura normal de la columna cervical.")
  print ("d)La escoliosis es una curvatura patológica.\033[39m\n")
  
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a","b","c","d","x"):
    respuesta_2 = input("\033[31mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "a":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es correcta, tienes", puntaje, "puntos\n")
  elif respuesta_2 == "b":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es correcta, tienes", puntaje, "puntos\n")
  elif respuesta_2 == "d":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es correcta, tienes", puntaje, "puntos\033[39m\n")
  elif respuesta_2 == "x":
    puntaje += 10000
    print ("\033[35mEntontraste el mensaje secreto y recibiras tu recompenza :3\033[39m\n")
  else:
    puntaje += random.randint(10, 21)
    print ("\033[32mMuy bien!", nombre,"La cifosis es una curvatura exagerada hacia adelante de la parte superior de la espalda. Tienes", puntaje, "puntos\033[39m\n")
  
  time.sleep(3)
  
  #Pregunta 3 c
  print ("\033[34m3) ¿Cuál de estas afirmaciones es falsa?\n")
  print ("a)Las articulaciones fibrosas no poseen movimiento.")
  print ("b)Las sindesmosis son articulaciones con poca movilidad y el tejido de unión es tejido conectivo denso.")
  print ("c)La diartrosis son articulaciones poco móviles.")
  print ("d)Las sincondrosis son articulaciones en las que el tipo de unión es cartilaginosa.\033[39m")
  
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3 = input("\033[31mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_3 == "a":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es verdadera, tienes", puntaje, "puntos\n")
  elif respuesta_3 == "b":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es verdadera, tienes", puntaje, "puntos\n")
  elif respuesta_3 == "d":
    puntaje -= random.randint(0, 11)
    print ("\033[31mIncorrecto!", nombre,"Esta alternativa es verdadera, tienes", puntaje, "puntos\n\033[39m")
  else:
    puntaje += random.randint(10, 21)
    print ("\033[32mMuy bien!", nombre,"La diartrosis es la articulación con mayor movimiento. Tienes", puntaje, "puntos\033[39m\n")
  
  time.sleep(3)
  
  #Pregunta 4 a
  print ("\033[34m4) En un accidente de tráfico sufrido durante una limpieza, un trabajador se rompió el tendón de Aquiles, donde se inserta este tendón que está integrado en el triceps sural?\n")
  print ("a)Calcáneo.")
  print ("b)Cuboides.")
  print ("c)Astrágalo.")
  print ("d)Peroné.\033[39m")
  
  respuesta_4 = input("\nTu respuesta: ")
  while respuesta_4 not in ("a","b","c","d"):
    respuesta_4 = input("\033[31mDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_4 == "b":
    puntaje = puntaje / 2
    print ("\033[31mTotalmente Incorrecto! ...\n")
  elif respuesta_4 == "c":
    puntaje = puntaje + 5
    print ("\033[31mIncorrecto!\n")
  elif respuesta_4 == "d":
    puntaje = puntaje - 5 
    print ("\033[31m...\033[39m\n")
  else:
    puntaje = puntaje * 2
    print ("\033[32mMuy bien!", nombre,"el tendón de Aquiles se inserta en el Calcáneo, tienes", puntaje, "puntos\033[39m\n")
    
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero", nombre,"que hayas disfrutado esta trivia, hasta otra oportunidad!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.