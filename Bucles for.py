#imprime tanto como lugares en la lista
for i in [1,2,3]:
    #end para ejecutar en la misma linea
    print("hola", end="\n")

#imprime tantas veces como letras haya en el string
for i in "asdasd":
    print(i)

#i se convierte en un valor del string
mail = False
for i in "lucho@truchomeil:V.com":
    if (i == "@"):
        mail=True
        
if mail == True:
    print("mail correcto")
else:
    print("mail incorrecto")

#del 0 al 9
for i in range(10):
    print("hola",i)

#del 5 al 9
for i in range(5,10):
    print("a",i)

#del 5 al 9 pero de 2 en 2
for i in range(5,10,2):
    print("o",i)


validar = False
email = input("Ingrese el email: ")
for i in range(len(email)):
    if(email[i] == "@"):#se toma el string como un arreglo
        validar = True
    
if validar:
    print("Email correcto")
else:
    print("Email incorrecto")


