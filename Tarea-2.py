# -*- coding: utf-8 -*-
"""2. Listas Circulares.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BJMZqC-UoTpBL7rcEYGaGgRasFOH139x

##**Listas Circulares**
**Definición de Listas Circulares**
"""

class Estudiante:
  def __init__(self, Carnet, Nombre, Edad, Address, Phone, Email, Carrera, Puesto):
    self.Carnet = Carnet
    self.Nombre = Nombre
    self.Edad = Edad
    self.Address = Address
    self.Phone = Phone
    self.Email = Email
    self.Carrera = Carrera
    self.Puesto = Puesto

"""**Definición de la clase Nodo**"""

class Nodo:
  def __init__(self, Estudiante = None, Siguiente = None):
    self.Estudiante = Estudiante
    self.Siguiente = Siguiente

"""**Definición de la clase Lista Circular**"""

class lista_circular:
  def __init__(self):
    self.Primero = None
  def insertar(self, Estudiante):
    if self.Primero is None:
      self.Primero = Nodo(Estudiante)
      self.Primero.Siguiente = self.Primero
    else:
      actual = Nodo(Estudiante, Siguiente = self.Primero.Siguiente)
      self.Primero.Siguiente = actual

  def recorrer(self):
    if self.Primero is None:
      return
    actual = self.Primero
    print(f"Carnet: {actual.Estudiante.Carnet}; Nombre: {actual.Estudiante.Nombre}; Email: {actual.Estudiante.Email} ->")
    while actual.Siguiente != self.Primero:
      actual = actual.Siguiente
      print(f"Carnet: {actual.Estudiante.Carnet}; Nombre: {actual.Estudiante.Nombre}; Email: {actual.Estudiante.Email} ->")

  def eliminar(self, Carnet):
    actual = self.Primero
    anterior = None
    no_encontrado = False
    while actual and actual.Estudiante.Carnet != Carnet:
      anterior = actual
      actual = actual.Siguiente
      if actual == self.Primero:
        no_encontrado = True
        break

      if not no_encontrado:
        if anterior is not None:
          anterior.Siguiente = actual.Siguiente
      else:
        while actual.Siguiente != self.Primero:
          actual = actual.Siguiente
        actual.Siguiente = self.Primero.Siguiente
        self.Primero = self.Primero.Siguiente

  def buscar(self, Carnet):
    actual = self.Primero
    pos = 0
    while actual and actual.Estudiante.Carnet != Carnet:
      actual = actual.Siguiente
      pos += 1
    if actual is None:
      print("No se encontró al estudiante.\n")
    else:
      print(f'El estudiante se encuentra en la posición: {pos}\nDatos del Estudiante Encontrado:\nCarnet: {actual.Estudiante.Carnet};\nNombre: {actual.Estudiante.Nombre};\nEdad: {actual.Estudiante.Edad};\nDirección: {actual.Estudiante.Address};\nTeléfono: {actual.Estudiante.Phone};\nEmail: {actual.Estudiante.Email};\nCarrera: {actual.Estudiante.Carrera};\nPuesto: {actual.Estudiante.Puesto}\n')

"""**Creación de Objetos Estudiante**"""

e1 = Estudiante(201015050, "Gerson Ortiz", 20, "0 calle 18-82 zona 1", 24400101,"gerson.ortiz@gmail.com", "Ing. Sistemas", "Programador Jr.")
e2 = Estudiante(201015060, "Karen Hurtarte", 21, "7 calle 18-82 zona 1", 24400102,"karen.hurtarte@gmail.com", "Ing. Sistemas", "Programador Jr.")
e3 = Estudiante(201015061, "Luis Mendez", 22, "8 calle 18-82 zona 1", 24400101,"luis.mendez@gmail.com", "Ing. Sistemas", "Programador Jr.")

"""**Inserción**"""

lista_c = lista_circular()
lista_c.insertar(e1)
lista_c.insertar(e2)
lista_c.insertar(e3)

"""**Recorrer Lista**"""

lista_c.recorrer()

"""**Eliminar un nodo de la lista**"""

lista_c.eliminar(201015060)
lista_c.recorrer()

"""**Buscar un Estudiante de la lista**"""

lista_c.buscar(201015050)