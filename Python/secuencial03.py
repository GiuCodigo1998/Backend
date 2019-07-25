dni = input("ingresar el dni: ")
sueldo = float(input("ingresa el el sueldo"))
dept = input("Ingresa tu departamento")
if dept == "log":
    total=sueldo*1.02
elif dept == "sis":
    total=sueldo*1.03
elif dept == "rh":
    total= sueldo*1.05
else:
    total=sueldo*1.01
print("El sueldo ha percibir es: ", (total), " soles.")