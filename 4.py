print("Roman De la Cruz Leonardo Antonio,1211-3-w")
(" ")
class Calculadora:
    def __init__(self, valor1, valor2):
        # Inicializa los dos valores enteros
        self.valor1 = valor1
        self.valor2 = valor2
    
    def suma(self):
        # Método para calcular la suma
        return self.valor1 + self.valor2
    
    def resta(self):
        # Método para calcular la resta
        return self.valor1 - self.valor2
    
    def multiplicacion(self):
        # Método para calcular la multiplicación
        return self.valor1 * self.valor2
    
    def division(self):
        # Método para calcular la división, con comprobación de división por cero
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir por cero"

# Ejemplo de uso:
# Pedir al usuario que ingrese dos valores enteros
valor1 = int(input("Introduce el primer valor: "))
valor2 = int(input("Introduce el segundo valor: "))

# Crear un objeto de la clase Calculadora
calculadora = Calculadora(valor1, valor2)

# Realizar y mostrar las operaciones
print(f"La suma de {valor1} y {valor2} es: {calculadora.suma()}")
print(f"La resta de {valor1} y {valor2} es: {calculadora.resta()}")
print(f"La multiplicación de {valor1} y {valor2} es: {calculadora.multiplicacion()}")
print(f"La división de {valor1} y {valor2} es: {calculadora.division()}")
