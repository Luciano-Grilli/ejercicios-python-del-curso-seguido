class coche():
    def desplazamiento(self):
        print("Me estoy moviendo en 4 ruedas")

    
class moto():
    def desplazamiento(self):
        print("Me estoy moviendo en 2 ruedas")


class camion():
    def desplazamiento(self):
        print("Me estoy moviendo en 8 ruedas")




def desplazamientoVehiculo(vehiculo):#metodo para el polimorf
    vehiculo.desplazamiento()#recibe un objeto y ejecuta el siguiente metodo




miMoto = moto()
desplazamientoVehiculo(miMoto)#se ejecuta los metodos
#depende del objeto que se envia por parametro






