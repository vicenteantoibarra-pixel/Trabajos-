from mascota import Mascotas

class Veterinaria:
    def __init__(self,nombreVeterinaria):
        self.nombreVeterinaria = nombreVeterinaria
        self.mascota = []

    def mascotas (self,mascota:Mascotas):
        self.mascota = mascota