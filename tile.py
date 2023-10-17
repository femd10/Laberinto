import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,posicion,tamano):
        super().__init__()
        self.direccionImagen : type[str]
        self.image= pygame.transform.scale(pygame.image.load(self.direccionImagen).convert_alpha(),(tamano,tamano))
        self.rect=self.image.get_rect(topleft=posicion)

class Suelo(Tile):
    def __init__(self,posicion,tamano):
        self.direccionImagen="esprites/suelo.jpg"
        super().__init__(posicion,tamano)

class Pared(Tile):
    def __init__(self,posicion,tamano):
        self.direccionImagen="esprites/pared.png"
        super().__init__(posicion,tamano)

class Meta(Tile):
    def __init__(self,posicion,tamano):
        self.direccionImagen="esprites/meta.jpg"
        super().__init__(posicion,tamano)

class Jugador(Tile):
    def __init__(self,posicion,tamano):
        self.direccionImagen="esprites/pj.png"
        super().__init__(posicion,tamano)

