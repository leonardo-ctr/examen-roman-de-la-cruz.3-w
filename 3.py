print("Roman De la Cruz Leonardo Antonio,1211-3-w")
(" ")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # Inicializa los lados del triángulo
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        # Imprime el valor del lado con el tamaño mayor
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor del triángulo es: {mayor}")
    
    def tipo_triangulo(self):
        # Determina el tipo de triángulo según los lados
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Ejemplo de uso:
# Crear un objeto de la clase Triangulo
triangulo1 = Triangulo(3, 4, 5)

# Imprimir el lado mayor
triangulo1.imprimir_lado_mayor()

# Mostrar el tipo de triángulo
triangulo1.tipo_triangulo()

# Otro ejemplo
triangulo2 = Triangulo(5, 5, 5)
triangulo2.imprimir_lado_mayor()
triangulo2.tipo_triangulo()
