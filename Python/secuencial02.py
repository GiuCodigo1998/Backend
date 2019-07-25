igv=0.18
pre = int(input("Ingresa el precio: "))
can = int(input("Ingrese la cantidad: "))
#El proceso
total = pre*can
imp=total*0.18
neto=total+imp

print("El costo a pagar es de: ", (neto), " soles.")