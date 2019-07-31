def mayor(valor, valor2):
    if valor2 < valor:
        valor2 = valor
    return valor2

print("Ingrese el numero de candidatos en las secciones del: \n")
n = int(input("Norte: "))
total = mayor(n,0)
s = int(input("Sur: "))
total = mayor(s,total)
c = int(input("Centro: "))
total = mayor(c,total)

print("La mayor cantidad de votantes fue de", total)