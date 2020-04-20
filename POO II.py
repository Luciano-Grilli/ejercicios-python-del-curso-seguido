class Cochee():

    

    #constructor, con self.variable indicas que tendran un punto inicial
    def __init__(self):
        #los __ indican que no se puede,modificar desde afuera de la clase
        #es como un private,se encapsula
        self.__color = "azul"
        self.__motor = "v4"
        self.__velocidadMax = 200
        self.movimiento = False
        self.gasolina = 30
        self.puertasCerradas = True
        self.aceite = True
        self.arranque = False
        

    def avanzar(self):
        if(self.arranque):#si no se pone nada pregunta si es true
            print("El coche procedera a avanzar \navanzando....")
            self.movimiento = True#self indica la variable por referencia de la clase

    def estado(self):#self,usara los parametros por refernecia
        
        print("Estado del coche:")
        if(self.movimiento == False):
            print("El coche esta parado")

        else:
            print("El coche esta en marcha")    

    def chequeoInterno(self):
        print("realizando checkeo")

        if(self.gasolina <= 5):
            print("queda poca gasolina")
        if(self.aceite <= 1):
            print("queda poco aceite")
        if(self.puertasCerradas == False):
            print("puertas cerradas, no puede arrancar")
        else:
            self.arranque = True
            print("inicio de arranque.....")
            self.avanzar()    



#crea el objeto
miCoche = Cochee()

#miCoche.__color = "verde" aca imprimiria verde porque seria como otra variable diferente

miCoche.estado()
miCoche.chequeoInterno()
miCoche.estado()













