#equivalentes a arrays
#estos pueden tener diferentes tipos de valores juntos,mesclados

miLista=["maria","jose","pepe","mario"]
#indices   0    ,   1  ,  2   ,  3

#si ponemos -1 cuenta desde atras hacia adelante mostraria "mario"
print(miLista[-1])# print(miLista[1])


#imprime desde el 1 hasta el 3(sin incluir el 3)
print(miLista[1:3])


#imprime desde el 0 hasta el 3(sin incluir el 3)
print(miLista[:3])

#imprime desde el 2 hasta el final
print(miLista[2:])

# append agrega un elemento al final de la lista
miLista.append("tito")
print(miLista[-1])

# insert agrega un elemento a la lista en el indice indicado
miLista.insert(1,"tete")
print(miLista[:])

# implementar varios valores a la lista
miLista.extend(["sandra","lucia"])
print(miLista[:])

# buscar el indice de un valor
miLista.extend(["sandra","lucia"])
print(miLista.index("sandra"))

#se pueden repetir los valores y si preguntamos por el
#  indice este mustra el primero que aparece en la lista

#mostrar si el valor esta en la lista,devuelve true o false
print("pepe" in miLista)

#eliminar elementos
miLista.remove("tete")
print(miLista[:])

#elimina el ultimo elemento de la lista
miLista.pop()
print(miLista[:])

#sumar listas(no sumar valores,sino juntar todos los valores en otra lista)
miLista2=["hola"]

miLista3 = miLista+miLista2
print(miLista3[:])


#repetir listas con el *
miLista2=["holaa"]*3
print(miLista2[:])
