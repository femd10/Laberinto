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
        for fila in self.estructuraNivel:
            for columna in fila:
                x= columna_index * self.tamanoRecuadro
                y = fila_index * self.tamanoRecuadro
                if columna =="1":
                    tile=Pared((x,y),self.tamanoRecuadro)
                    self.paredes.add(tile)
                elif columna.upper() =="W":
                    tile=Meta(  (x,y),self.tamanoRecuadro)
                    self.meta.add(tile)
                elif columna.upper() =="X":
                    tile=Jugador((x,y),self.tamanoRecuadro)
                    tile2=Suelo((x,y),self.tamanoRecuadro)
                    self.jugador.add(tile)
                    self.suelos.add(tile2)
                else:
                    tile=Suelo((x,y),self.tamanoRecuadro)
                    self.suelos.add(tile)
                columna_index+=1
            columna_index=0
            fila_index+=1
                
    def run(self):
        self.paredes.draw(self.ventana)
        self.suelos.draw(self.ventana)
        self.meta.draw(self.ventana)
        self.jugador.draw(self.ventana)
    
