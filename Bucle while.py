i = 1

while i <= 10:
    print("hola",i)
    i=i+1

print("finalizado")


#metodo str() para raiz cuadrada, se importa math

#-------------------metodos de los bucles----------------------------
#Continue continua con la siguiente linea
#pass hace que no se ejecute el bucle/se puede utilizar en una clase
#else 

for i in "hola":
    if i == "l":
        continue
    print(i)



#break
for i in "pemen":
    if i == "m":
    
        break
    print(i)

#else funciona cuando el bucle esta vacio
for i in "pemen":    
    print(i)
else:
    print("finalizado")

#rompe el break el bucle
for i in "catunga":
    print(i) 
    if i == "g":

        break 
else:
    print("finalizacion2")





