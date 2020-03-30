class Coche():#crear la clase
    largoCoche = 250
    color = "rojo"
    motor = "v4"
    velocidadMax = 200
    enMarcha = False

    def avanzar(self):
    #una funcion que pertenece a la clase    
        self.enMarcha = True
        #self es como in this,hace referencia a variables de clase

    def estado(self):#self es como si hiciera objeto.estado y hace referencia a las variables de clase
        if self.enMarcha == True:
            print("el auto esta en marcha")
        else:
            print("El auto esta detenido")

#crear el objeto
miCoche = Coche()


print("El color de mi choche es "+miCoche.color)

miCoche.avanzar()
miCoche.estado()

