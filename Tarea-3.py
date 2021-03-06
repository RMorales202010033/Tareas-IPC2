# -*- coding: utf-8 -*-
"""3. Lista doblemente enlazada.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gqGzpU5lv8_zmkjtZbn4n3Dc9zHXlNYb

##**Listas Doblemente Enlazadas**
**Definición Clase Estudiante**
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

"""**Definición Clase Nodo**"""

class Nodo:
  def __init__(self, Estudiante = None, Siguiente = None, Anterior = None):
    self.Estudiante = Estudiante
    self.Siguiente = Siguiente
    self.Anterior = Anterior

"""**Definición de la Clase Lista Doblemente Enlazada**"""

class lista_doble:
  def __init__(self):
    self.Primero = None

  def insertar(self, Estudiante):
    if self.Primero is None:
      self.Primero = Nodo(Estudiante=Estudiante)
    else:
      actual = Nodo(Estudiante=Estudiante,Siguiente=self.Primero)
      self.Primero.Anterior = actual
      self.Primero = actual

  def recorrer(self):
    if self.Primero is None:
      return
    actual = self.Primero
    print(f"Carnet: {actual.Estudiante.Carnet}, Nombre: {actual.Estudiante.Nombre}, Email: {actual.Estudiante.Email}")
    while actual.Siguiente:
      actual = actual.Siguiente
      print(f"Carnet: {actual.Estudiante.Carnet}, Nombre: {actual.Estudiante.Nombre}, Email: {actual.Estudiante.Email}")

  def eliminar(self,Carnet):
    actual = self.Primero
    while actual:
      if actual.Estudiante.Carnet == Carnet:
        if actual.Anterior:
          if actual.Siguiente:
            actual.Anterior.Siguiente = actual.Siguiente
            actual.Siguiente.Anterior = actual.Anterior
          else:
            actual.Anterior.Siguiente = None
            actual.Anterior = None
        else:
          if actual.Siguiente:
            self.Primero = actual.Siguiente
            actual.Siguiente.Anterior = None
          else:
            self.Primero = None
        return True
      else:
        actual = actual.Siguiente
    return False

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

"""**Creación Objetos Estuadiante**"""

e1 = Estudiante(201015050, "Gerson Ortiz", 20, "0 calle 18-82 zona 1", 24400101,"gerson.ortiz@gmail.com", "Ing. Sistemas", "Programador Jr.")
e2 = Estudiante(201015060, "Karen Hurtarte", 21, "7 calle 18-82 zona 1", 24400102,"karen.hurtarte@gmail.com", "Ing. Sistemas", "Programador Jr.")
e3 = Estudiante(201015061, "Luis Mendez", 22, "8 calle 18-82 zona 1", 24400101,"luis.mendez@gmail.com", "Ing. Sistemas", "Programador Jr.")

"""**Inserción**"""

lista_d = lista_doble()
lista_d.insertar(e1)
lista_d.insertar(e2)
lista_d.insertar(e3)

"""**Recorrer Lista**"""

lista_d.recorrer()

"""**Eliminar el nodo del medio de la lista**"""

lista_d.eliminar(201015060)
lista_d.recorrer()

"""**Eliminar el primer nodo de la lista**"""

lista_d.eliminar(201015061)
lista_d.recorrer()

"""**Eliminar el último nodo de la lista**"""

lista_d.eliminar(201015050)
lista_d.recorrer()

"""**Eliminar nodo a nodo de la lista**"""

lista_d.eliminar(201015061)
lista_d.eliminar(201015060)
lista_d.eliminar(201015050)
lista_d.recorrer()

"""**Buscar un Estudiante en la Lista**"""

lista_d.buscar(201015050)