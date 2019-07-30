import os
resp= ""
cursos=["java","python","c++"]
#Funciones principales de mi programa
#Inserto un nuevo valor a mi lista de cursos
def insertar():
   valor=input("Ingrese un Nuevo Curso:")
   cursos.append(valor)

def funcname(parameter_list):
    pass

def listar():
   tam=len(cursos)
   for x in range(0,tam):
       print(cursos[x])



def menu():
   opc="0"
   print("Menu principal")
   print("1.-Ingreso")
   print("2.-Busqueda")
   print("3.-Listar")
   print("4.-Eliminar")
   print("5.-Actualizar")
   print("6.-Ordenar")
   opc=input("Elija la Opcion:")
   if opc=="1":
       insertar()
   elif opc=="2":
       print("Llamar funcion Buscar")
   elif opc=="3":
      listar()
   elif opc=="4":
       print("Llamar funcion Eliminar")
   elif opc=="5":
       print("Llamar funcion Actualizar")
   elif opc=="6":
       print("Llamar funcion Ordenar")
   else:
       print("Opcion No Existe")
while resp!="N":
    menu()
    resp=input("Desea Continuar:")
    os.system('cls')