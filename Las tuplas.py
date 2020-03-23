#las tuplas son listas pero que no se pueden modificar
#pero se puede extraer cosas pero esta no se extrae
#seria como solo lectura y no permite index

mitupla = ("hola","ser","pepe")

print(mitupla)


#se puede pasar todos los valores de la tupla a la lista
miLista = list(mitupla)
print(miLista)


#ase puede convertir una lista en una upla
mi2tupla=tuple(miLista)
print(mi2tupla)

#tambien se piede usar el "pepe" in tupla y
#devuelve true o false

#ver cuantos elementos de un valor existe en la tupla
print(mi2tupla.count("hola"))

#ver cantidad de elementos en total d ela tupla
print(len(mi2tupla))

#asiganr valores de una tupla a variables
tuplanueva=("juan",17,2000)
nombre,edad,agno = tuplanueva

print(nombre,edad,agno)