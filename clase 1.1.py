class ClasePerros:

    raza=""

    color=""

    tamaño=""

    edad=0

    nombre=""

    vacunas=""

    peso=0.0

   



    def metodoladrar(self):

        print("Guau Guau")

   

    def metodocorrer(self,distancia):

        print("El perro corrio " + str(distancia) + " Metros")





#inicializando objeto llamado perrodedavid con la clase ClasePerros

perrodedavid=ClasePerros()

perrodedavid.raza="schnauzer"

perrodedavid.nombre="Bit"

perrodedavid.tamaño="Toy"



#inicializando objeto llamado perrolaura con la clase ClasePerros

perrodelaura=ClasePerros()

perrodelaura.nombre = "zarca"

perrodelaura.raza = "a la tortrix"

perrodelaura.tamaño="Mediano"



perrodewilson=ClasePerros()

perrodewilson.nombre="Toby"

perrodewilson.raza="Pastor Aleman"

perrodewilson.tamaño="Grande"



print(ClasePerros.nombre)

print(perrodedavid.nombre)

print(perrodelaura.nombre)

print(perrodewilson.nombre)