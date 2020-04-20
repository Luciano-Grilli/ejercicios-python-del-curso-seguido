class persona():
    def __init__(self,nombre,edad,residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

        
    def descripcion(self):
        print("Nombre: ",self.nombre,"\nedad: ",self.edad,"\nResidencia: ",self.residencia,"\n")   



class empleado(persona):
    def __init__(self,salario,antiguedad,nombre,edad,residencia):#le paso los parametros para el metodo super
        super().__init__(nombre,edad,residencia)#este metodo envia los parametros para la clase persona
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: $",self.salario,"\nantiguedad: ",self.antiguedad)    

antonio = persona("antonio",50,"argentina")
antonio.descripcion()


empleado1 = empleado(20000,3,"pepe",30,"peru")

empleado1.descripcion()


#ver si un objeto pertenece a una clase,devuelve T o F
print(isinstance(empleado1,persona))
