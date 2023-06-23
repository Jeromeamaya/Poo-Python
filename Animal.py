# Clase
class Animal: 
# ATributos
    nombre = "" # Atributo Estatico
    edad = 0
    color = ""
    


    # Metodos   
    
    # Metodo constructor
    
    def __init__(self,n,m):
        self.nombre=n
        self.edad=m


    # Metodos Propios
    def registrarAnimal(self):
        self.nombre = input("Ingrese el nombre del animal")
        self.edad = int(input("Ingrese la edad"))    

    def mostrarAnimal(self):
        print(self.nombre,self.edad)
        
    def CambiarNombre(self):
        self.nuevoNombre=input("Ingrese el nuevo nombre")
        print(f"el nuevo nombre es {nuevoNombre}")
        
    def duplicidad(self,edad): 
        duplicar=edad*2
        return duplicar
        print(duplicar) 
  
        
        
        


# Crear o instanciar una clase o objeto