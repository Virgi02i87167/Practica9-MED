class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizarnombre(self, nuevonombre):
        self.nombre = nuevonombre

    def actualizarapellido(self, nuevoapellido):
        self.apellido = nuevoapellido

    def actualizarcarnet(self, nuevocarnet):
        self.carnet = nuevocarnet

    def actualizarcarrera(self, nuevacarrera):
        self.carrera = nuevacarrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Carnet: {self.carnet}, Carrera: {self.carrera}"

if __name__ == "__main__":
    estudiante1 = Estudiante("Jonathan", "Alfaro", "u20220076", "Ingeniería en Desarrollo de Software")
    print(estudiante1)

    estudiante1.actualizarnombre("Virgilio")
    estudiante1.actualizarapellido("Hernandez")
    estudiante1.actualizarcarnet("U20220076")
    estudiante1.actualizarcarrera("Tecnico en Desarrollo de Software")

    print(estudiante1)