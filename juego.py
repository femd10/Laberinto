import pygame, sys
from nivel import Nivel
class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla= pygame.display.set_mode((500, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.activo=True
        self.nivel= Nivel(self.pantalla, 100)
        
    def correr(self):
        while self.activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.pantalla.fill('black')
            self.nivel.run()

            pygame.display.update()
            self.clock.tick(60)