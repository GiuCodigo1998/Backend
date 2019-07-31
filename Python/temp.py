from time import sleep
password = "codigo"
intentos = 3
while intentos:
    con = input("Password: ")
    if con == password:
        print("CORRECT password")
        break
    else:
        print("INCORRECT password")
        intentos -= 1
        if intentos>0:
            sleep(10 - int(2*intentos))