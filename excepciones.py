import math

try:                                    #acortar decimales
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))


    print("resultado de la division es:","{0:.2f}".format(num1/num2))
except ZeroDivisionError:#al lado se puede poner el tipo de error o no y que responda a ese error
    print("no se puedo realizar la division con esos numeros")
except ValueError:
    print("Valores ingresados incorrectos")    

#se pueden hacer varias excepciones y se puede poner el tipo de error
#para que responda a este

finally:#el finali se ejecuta siempre si o si
    print("Programa finalizado")

edad = -1
if edad < 0:
    raise TypeError("Error de tontos,no existe edad negativa")
    #con tyerror podes ingresar el mensaje del error
    #tambien se puede ingresar el tipo de error

#ya que estamos asi se realizan la raiz,importando la clase math
math.sqrt(5)    



