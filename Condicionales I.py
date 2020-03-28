def evaluacion(nota):
    valor="aprobado"
    if nota <= 5:
        valor="desaprobado"
    return valor


notai = input("Ingrese la nota: ")

print(evaluacion(int(notai)))