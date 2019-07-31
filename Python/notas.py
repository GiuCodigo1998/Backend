giuliano={"nombre":"giuliano",
"tareas":[12,15,20],
"practicas":[11,17,10],
"examenes":[20,20,20],
}
junior={"nombre":"junior",
"tareas":[13,16,14],
"practicas":[13,18,11],
"examenes":[17,18,19],
}
sebas={"nombre":"sebas",
"tareas":[11,10,20],
"practicas":[12,17,16],
"examenes":[11,13,12],
}
#Indice para mostrar los elementos del diccionario
indice=0
#Crear una lista a partir de nuestro Diccionario
estudiantes=[giuliano,junior,sebas]
#Realizamos el recorrido de nuestra lista mostrando cada
#elemnto de forma individual
for alumno in estudiantes: 
#"""
   print(alumno["nombre"])
   print("Tareas:",alumno["tareas"])
   print("Practicas:",alumno["practicas"])
   print("Examenes:",alumno["examenes"])
#"""