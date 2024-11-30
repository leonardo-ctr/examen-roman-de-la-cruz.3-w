print("Roman De la Cruz Leonardo Antonio,1211-3-w")
(" ")
class persona:
    def __init__(self, nombre, edad):
        # Inicializa los atributos de la clase
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        # Imprime el nombre y la nota del alumno
        print(f"Nombre: {self.nombre}")
        print(f"edad: {self.edad}")
    
    def resultado(self):
        # Muestra el resultado basado en la nota del alumno
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad {self.edad}.")
        else:
            print(f"{self.nombre} es menor de edad {self.edad}.")

# Ejemplo de uso:
# Crear un objeto de la clase Alumno
alumno1 = persona("Natanael cano",23)

# Imprimir los datos del alumno
alumno1.imprimir()

# Mostrar el resultado de la nota
alumno1.resultado()

