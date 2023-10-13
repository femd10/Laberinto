import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,posicion,tamano):
        self.direccionImagen : type[str]
        self.sprite= pygame.transform.scale(pygame.image.load(self.direccionImagen).convert_alpha(),(tamano,tamano))
        self.rect=self.sprite.get_rect(topleft=posicion)

class Suelo(Tile):
    def __init__(self,posicion,tamano):
        super.__init__(posicion,tamano)
        self.direccionImagen="esprites/suelo.jpg"

class Pared(Tile):
    def __init__(self,posicion,tamano):
        super.__init__(posicion,tamano)
        self.direccionImagen="esprites/pared.png"

class Meta(Tile):
    def __init__(self,posicion,tamano):
        super.__init__(posicion,tamano)
        self.direccionImagen="esprites/meta.jpg"

class Personaje(Tile):
    def __init__(self,posicion,tamano):
        super.__init__(posicion,tamano)
        self.direccionImagen="esprites/pj.png"

