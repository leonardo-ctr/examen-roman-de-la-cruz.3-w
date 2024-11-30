print("Roman De la Cruz Leonardo Antonio,1211-3-w")
(" ")
class alumno:
    def __init__(self, nombre, nota):
        # Inicializa los atributos de la clase
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        # Imprime el nombre y la nota del alumno
        print(f"Nombre: {self.nombre}")
        print(f"nota: {self.nota}")
    
    def resultado(self):
        # Muestra el resultado basado en la nota del alumno
        if self.nota >= 5:
            print(f"{self.nombre} pasaste bro {self.nota}.")
        else:
            print(f"{self.nombre} no pasaste {self.nota}.")

# Ejemplo de uso:
# Crear un objeto de la clase Alumno
alumno1 = alumno("Natanael cano",8.6)

# Imprimir los datos del alumno
alumno1.imprimir()

# Mostrar el resultado de la nota
alumno1.resultado()

