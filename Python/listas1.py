preguntas = ['nombre','objetivo', 'software']
respuestas = ['Giuliano', 'Estudiante', 'Python']
datos = ['Venturo', 'CodiGO', 'Lenguaje de programacion']

for preguntas,respuestas,datos in zip(preguntas,respuestas,datos):
    print('Cual es tu {0}?, la respuesta es {1}. Datos extra "{2}"'. format(preguntas,respuestas,datos))  


    