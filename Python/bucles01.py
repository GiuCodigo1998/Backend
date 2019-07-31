password = "codigo"
flag = 0
while flag < 3:
    con = input("Ingrese contra: ")
    
    if con == password:
        print("Correct password!!!")
        break
    else:
        print("INCORRECT password")
        flag += 1