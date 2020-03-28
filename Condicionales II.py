print("Verificar edad")
#lower(),upper() minusculas o mayusculas
edad=int(input("Ingrese su edad:"))


if edad > 100 or edad <= 0:
    print("edad incorrecta")
elif edad < 18:
    print("No puede pasar")
else:
    print("puedes pasar")     

print("finalizado")       
