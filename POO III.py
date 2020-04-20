class vehiculos():
    def __init__(self,marca,modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelerar = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelera(self):
        self.acelerar = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca " + self.marca + "\nmodelo " + self.modelo)
        print("Estado:\n")
        if(self.enMarcha == True):
            print("En marcha....")
        else:
            print("No esta en marcha")    
        if(self.acelerar == True):
            print("Acelerando....")
        if(self.frenar == True):
            print("Frenando....")
        



class moto(vehiculos):#se puede utilizar el constructor de la superclase
    pass

miMoto = moto("ducati","z200")
miMoto.arrancar()
miMoto.acelera()
miMoto.estado()



