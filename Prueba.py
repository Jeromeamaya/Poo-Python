# Crear objeto desde otro archivo ( Se debe importar la clase)
from Animal import Animal

panda=Animal()



# Objeto panda es un animal y tiene los atributos de cualquier animal
# pero tambien puede tener sus propias propiedades
# El metodo registrarAnimal se encarga de llamar al método del padre
# con el nombre que le pasamos como parametro, en este caso "registrarAnimal"



panda.registrarAnimal()
panda.mostrarAnimal()
#print(panda.duplicidad(panda.edad),"del",panda.nombre)
panda.CambiarNombre()

