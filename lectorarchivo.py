
class LectorArchivo:
    def __init__(self):
        self.texto="nivel.txt"

    def leernivel(self):
        self.abrir= open(self.texto) 
        self.leer= self.abrir.readlines()
        self.lista= [list(y.rstrip("\n")) for y in self.leer]
        self.abrir.close
        return self.lista



        