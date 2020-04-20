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
        print("En marcha ",self.enMarcha)
        print("acelerando ",self.acelerar)
        print("frenar ",self.frena)
        

class chata(vehiculos):
    

    def carga(self,carga):
        if(self.carga):
            print("cargada")
        else:
            print("no cargada")    

class moto(vehiculos):#se puede utilizar el constructor de la superclase
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "WILIIEEEEEEEEEEEEEE"

    def estado(self):#sobre escribiendo el metodo, al llamar,toma el que esta dentro de la clase del objeto
        print("Marca " + self.marca + "\nmodelo " + self.modelo)
        print("Estado:\n")
        print("En marcha ",self.enMarcha)
        print("acelerando ",self.acelerar)
        print("frenar ",self.frena)    
        print("wili",self.hcaballito)

miMoto = moto("ducati","z200")
miMoto.arrancar()
miMoto.acelera()
miMoto.caballito()
miMoto.estado()

miChata = chata("trafic","2012")
miChata.estado()
miChata.carga(True)

#crear clase con doble herencia


class bicicleta(vehiculos,chata):
    pass
#todos los que tengan el mismo nombre
#a la hora de usar un contructor,metodos, la forma de diferenciarlo de las 2 clases
#es poniendo por referencia primero la clase del contructor
#que queremos usar
miBici = bicicleta()



