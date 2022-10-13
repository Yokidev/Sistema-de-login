import json
import hashlib
import random

# Genera el hash de la contraseña
contrasena = '1234'
hash = hashlib.md5(contrasena.encode('utf-8')).hexdigest()
print(hash)

# se añade el hash a la contrasela (Sal)
contrasena_hash = contrasena + hash

#se hace el hash a la contraseña + hash (Sal)
contrasena_Sal= hashlib.md5(contrasena_hash.encode('utf-8')).hexdigest()

print(contrasena_hash)
print(contrasena_Sal)


'''
# Leer el diccionario del fichero txt
fichero = open("Usuarios.txt")
diccionario = json.load(fichero)
fichero.close()


# Funcion guardar los cambios
def guardar_cambios():
  fichero = open("Usuarios.txt", 'w')
  json.dump(diccionario, fichero)
  fichero.close()


# Menu Opciones
banderaOpciones = True
while banderaOpciones:
  opcion = int(
    input(
      "Seleccione una opción: \n 1. Login \n 2. Crear cuenta \n 3. Cambiar contraseña \n 4. Borrar usuario \n 5. Salir \n \n Eleccion: "
    ))
  print()

  # Opción Login
  contador = 0
  if opcion == 1:
    while True:
      contador += 1
      user = input("Usuario: ")
      password = input("Password: ")

      # Validación
      if user.lower() in diccionario and password == diccionario.get(
          user.lower()):
        print("Bienvenido")
        print()
        banderaOpciones = False
        break

      #Límite de intentos
      elif contador > 3:
        print("limite de intentos")
        print()
        break
      else:
        print("Login incorrecto")
        print()

  # Opción Crear cuenta
  elif opcion == 2:
    while True:
      user = input("Introduce un nombre de usuario: ")
      password = input("Introduce un Password: ")

      # ¿Existe el usuario en la BBDD?
      if user.lower() in diccionario:
        print("usuario no valido")
        print()
        continue

      else:
        diccionario[user.lower()] = password
        print()

        #Guardamos los cambios
        guardar_cambios()

        break

  # Opción Cambiar contraseña
  elif opcion == 3:
    while True:
      user = input("Nombre de usuario: ")
      password = input("Nueva Password: ")

      # ¿Existe el usuario en la BBDD?
      if user.lower() in diccionario:

        diccionario[user.lower()] = password
        print()

        #Guardamos los cambios
        guardar_cambios()

        break

      else:
        print("Error")

  elif opcion == 4:
    while True:
      user = input("Nombre de usuario: ")
      password = input("Nueva Password: ")

      # ¿Existe el usuario en la BBDD?
      if user.lower() in diccionario:

        confirmacion = input("¿Estas seguro? (Si/No) \n")

        if confirmacion.lower() == "si":

          password = input("Introduce la contraseña: ")
          if password == diccionario.get(user.lower()):
            del diccionario[user]

            print()
            print("Usuario eliminado")
            print()

            #Guardamos los cambios
            guardar_cambios()

            break

        elif confirmacion.lower() == "no":
          break

        else:
          print("Opcion no válida")

      else:
        print("Error \n")
        intento = input("¿Intentar de nuevo? (Si/No) \n")
        if intento.lower() == "no":
          print()
          break
        

  # Salir
  elif opcion == 5:
    break
'''