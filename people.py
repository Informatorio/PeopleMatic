#!/usr/bin/python3

import random
import sqlite3
import string

def ingreso_datos():  
#  LUGARES = ["DEPÓSITO 1","DEPÓSITO 2", "DEPÓSITO 3"]
#  ARCHIVOS = [["1","10"],["2","8"],["3","8"],["4","8"],["5","8"],["6","8"],["7","8"],["8","8"],["9","5"]]###

  APELLIDOS = ["Martínez", "Radovancich", "Íbalo", "López", "Acosta", "Alegre", "Alessio", "Arregín", "Artiga", "Blanco", "Bogado", "Cardozo", "Castillo", "Cernik", "Cornejo", "Correa", "Cuevas", "Duarte", "Fernández", "Flores", "Frías", "García", "Gómez", "Gramajo", "Herrera", "Ibañez", "Miño", "Musura", "Obregón", "Ojeda", "Olivera", "Oliveras", "Oscar", "Osiska", "Paluj", "Paz", "Rodríguez", "Sánchez", "Sandobal", "Santillán", "Segovia", "Talavera", "Vasquez", "Vera", "Villalba", "Zanabria"]
  NOMBRESM = ["Juan", "Alejandro", "Pedro", "Ramón", "Fernando", "Brahim", "Lucas", "Lucio", "Facundo", "Arón", "Samuel", "Bruno", "Héctor", "Cristian", "Luis", "Diego", "Martín", "Thiago", "Lisandro", "Natanael", "Jeremías"]
  NOMBRESF = ["María", "Vanesa", "Cecilia", "Elsa", "Gloria", "Tiara", "Lorena", "Ludmila", "Andrea", "Brenda", "Moria", "Zulma", "Estela", "Josefina", "Natalia", "Brisa", "Juliana", "Jeniffer", "Breda"]
  alumnos = []
  legajoA = []
  legajoB = []
  legajo = []
  anacimientos = []
  mnacimientos = []
  dnacimientos = []
  nacimientos = []
  dni = []
  alumno = []

  for i in range(5):
    AP = random.choice(APELLIDOS)
    for j in range(4):
      NMM = random.choice(NOMBRESM)
      for h in range(3):
        NM = random.choice(NOMBRESM)
        if NMM == NM:
          break
        temp = NM + " " + NMM
        alumnos.append([AP,temp])
    for j in range(4):
      NFF = random.choice(NOMBRESF)
      for h in range(3):
        NF = random.choice(NOMBRESF)
        if NFF == NF:
          break
        temp = NF + " " + NFF
        alumnos.append([AP,temp])

         
  for i in alumnos:  
    legajoA.append(random.randint(1000,9999))
    legajoB.append(random.randint(1000,9999))
    anacimientos.append(random.randint(2002, 2003))
    mnacimientos.append(random.randint(1,12))
    dnacimientos.append(random.randint(1,28))
    dni.append(random.randrange(42000000, 43000000))

  legajoA.sort()
  legajoB.sort()
  anacimientos.sort()
  mnacimientos.sort()
  dnacimientos.sort()
  dni.sort()

  for i in range(len(anacimientos)):
    temp = str(anacimientos[i]) + "-" + str(mnacimientos[i]) + "-" + str(dnacimientos[i])
    nacimientos.append(temp)

  for i in range(len(legajoA)):
    temp = str(legajoA[i]) + "-" + str(legajoB[i])
    legajo.append(temp)

  for i in range(len(alumnos)):
    alumno.append([legajo[i],dni[i],alumnos[i],nacimientos[i]])
#    print(alumno[i])

  return alumno #,LUGARES,ARCHIVOS

def conectar(ruta):
  #  Conectar a la base de datos
  conexion = sqlite3.connect(ruta)
  #  Seleccionar el cursor para realizar la consulta
  consulta = conexion.cursor()
  return (consulta,conexion)

def terminar_consulta(consulta):
  #  Terminar la consulta
  consulta.close()

def commit(conexion):
  #  Guardar los cambios en la base de datos
  conexion.commit()

def cerrar_conexion(conexion):
  #  Cerramos la conexión a la base de datos
  conexion.close()

def insertar_datos(alu):
  #INGRESO DE ALUMNOS
  for i in range(len(alu)):
    argumentos = (alu[i][0],alu[i][1],alu[i][2][0],alu[i][2][1],alu[i][3])
    sql = """
    INSERT INTO Alumnos_alumno(legajo, dni, apellido, nombre, fecha_nacimiento)
    VALUES (?,?,?,?,?)
     """
     #  Ejecutamos la consulta
    if (consulta.execute(sql, argumentos)): print("Alumno guardado con éxito.")
    else: print("Ha ocurrido un error al guardar el registro.")

#  # INGRESO DE LUGARES
#  for i in range(len(lugares)):
#    argumentos = [lugares[i]]
#    sql = """
#    INSERT INTO Alumnos_lugar(descripcion)
#    VALUES (?)
#     """
#     #  Ejecutamos la consulta
#    if (consulta.execute(sql, argumentos)): print("Lugar guardado con éxito.")
#    else: print("Ha ocurrido un error al guardar el registro.")

#  # INGRESO DE ARCHIVOS 
#  sql = "SELECT * FROM Alumnos_lugar"
#  if (consulta.execute(sql)):
#    sqlLugares = consulta.fetchall()
#    x = 0
#    for lugar in sqlLugares:
#      # import ipdb; ipdb.set_trace()
#      j = 0
#      while x <= len(archi) and j < 3:
#        argumentos = [archi[x][0],archi[x][1],lugar[0]]
#        sql = """
#        INSERT INTO Alumnos_archivo(numero,cajones,lugar_id)
#        VALUES (?,?,?)
#         """
#        if (consulta.execute(sql, argumentos)): print("Archivo guardado con éxito.")
#        else: print("Ha ocurrido un error al guardar el registro.")
#        j = j + 1
#        x = x + 1      
#  else:
#    print("Ha ocurrido un error, no hay registro.")

#  # INGRESO DE LOCALIZACIÓN
#  sql = "SELECT * FROM Alumnos_alumno"
#  if (consulta.execute(sql)):
#    sqlAlumnos = consulta.fetchall()

#    for alumno in sqlAlumnos:
#      alumno_id = alumno[0]
#      sql = "SELECT * FROM Alumnos_archivo"
#      if (consulta.execute(sql)):
#        sqlArchivos = consulta.fetchall()
#        archivo     = random.choice(sqlArchivos)
#        archivo_id  = archivo[0]
#        lugar_id    = archivo[3]
#        archivo_cajones = archivo[2]
#        cajon = random.randint(1,archivo_cajones)

#        argumentos = [cajon,alumno_id,archivo_id,lugar_id]
#        sql = """
#        INSERT INTO Alumnos_localizacion(cajon,alumno_id,archivo_id,lugar_id)
#        VALUES (?,?,?,?)
#         """
#        if (consulta.execute(sql, argumentos)): print("Localización guardada con éxito.")
#        else: print("Ha ocurrido un error al guardar el registro.")


ruta = "../Sis_LegajosV2/db.sqlite3" 
consulta,conexion = conectar(ruta)
commit(conexion)

alumno = ingreso_datos()
print(len(alumno))
# ****** INSERTAR DATOS ******
insertar_datos(alumno)

terminar_consulta(consulta)
commit(conexion)
## ****************************
cerrar_conexion(conexion)
