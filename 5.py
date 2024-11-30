print("Roman De la Cruz Leonardo Antonio,1211-3-w")
(" ")
class Agenda:
    def __init__(self):
        self.contactos = []
    
    def menu(self):
        print("\n1. Añadir contacto\n2. Listar contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
        return input("Elige una opción: ")

    def añadir(self):
        self.contactos.append({"nombre": input("Nombre: "), "telefono": input("Teléfono: "), "email": input("Email: ")})
        print("Contacto añadido.")

    def listar(self):
        print("\n".join([f"{c['nombre']} - {c['telefono']} - {c['email']}" for c in self.contactos]) or "No hay contactos.")
    
    def buscar(self):
        nombre = input("Buscar nombre: ")
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                print(f"{c['nombre']} - {c['telefono']} - {c['email']}")
                return
        print("No encontrado.")
    
    def editar(self):
        nombre = input("Editar nombre: ")
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                c["nombre"] = input(f"Nuevo nombre ({c['nombre']}): ") or c["nombre"]
                c["telefono"] = input(f"Nuevo teléfono ({c['telefono']}): ") or c["telefono"]
                c["email"] = input(f"Nuevo email ({c['email']}): ") or c["email"]
                print("Contacto editado.")
                return
        print("No encontrado.")
    
    def cerrar(self):
        print("Agenda cerrada.")
        exit()

def main():
    agenda = Agenda()
    while True:
        opcion = agenda.menu()
        if opcion == '1': agenda.añadir()
        elif opcion == '2': agenda.listar()
        elif opcion == '3': agenda.buscar()
        elif opcion == '4': agenda.editar()
        elif opcion == '5': agenda.cerrar()
        else: print("Opción no válida.")

main()