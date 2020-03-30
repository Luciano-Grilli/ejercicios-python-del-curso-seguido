class Cochee():

    #constructor, con self.variable indicas que tendran un punto inicial
    def __init__(self):
        #los __ indican que no se puede,modificar desde afuera de la clase
        #es como un private
        self.__color = "azul"
        self.__motor = "v4"
        self.__velocidadMax = 200
        self.movimiento = False

    def avanzar(self):
        self.movimiento = True


miCoche = Cochee()

#miCoche.__color = "verde" aca imprimiria verde porque seria como otra variable diferente


print(miCoche.color)




