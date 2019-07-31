seguir = 1
monto_total = 0
while seguir == 1:
    m = int(input("Ingrese el monto del producto a pagar: "))
    IGV = m*0.18
    total = m + IGV
    print("El IGV fue de ", IGV, " soles. El total a pagar es de ", total, " soles")
    pagar = int(input("Ingrese la cantidad de dinero con la que va a pagar: "))
    while pagar - total < 0:
        pagar = int(input("Su pago es menor al costo total del producto. Por favor, ingrese un nuevo pago: "))
    if pagar <= total:
        print("El pago fue exacto. No resive vuelto")
    else:
        vuelto = pagar - total
        print("Su vuelto es de ", vuelto," soles.")
    monto_total += total
    seguir = int(input("Desea seguir con otra operacion? 'Si=1' 'No=0' "))

print("El cajero tiene un total de ", monto_total, " soles.")