a = int(input("Ingrese el año que desee: "))
if a % 4 or not(a % 100 and a % 400):
    print("Su año es BISIESTO")
else:
    print("Su año NO es BISIESTO")