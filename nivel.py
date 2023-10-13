import pygame
from lectorarchivo import LectorArchivo
from tile import *
class Nivel:
    def __init__(self, ventana,tamanoRecuadro):
        self.ventana=ventana
        self.tamanoRecuadro= tamanoRecuadro
        self.lector= LectorArchivo()
        self.estructuraNivel= self.lector.leernivel()
        self.ubicar_sprites()

    def ubicar_sprites(self):
        self.paredes= pygame.sprite.Group()
        self.suelos= pygame.sprite.Group()
        self.meta=pygame.sprite.GroupSingle()
        self.jugador= pygame.sprite.GroupSingle()
        fila_index=0
        columna_index=0
        for fila in range(len(self.estructuraNivel)):
            for columna in range(len(fila)):
                x= columna_index * self.tamanoRecuadro
                y = fila_index * self.tamanoRecuadro
                if columna =="1":
                    tile=Pared((x,y),self.tamanoRecuadro,self)
                #pendiente

                
    def run(self):
        self.paredes.draw(self.ventana)
        self.suelos.draw(self.ventana)
        self.meta.draw(self.ventana)
        self.jugador.draw(self.ventana)
    
