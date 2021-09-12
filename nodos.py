class bases:
    def __init__(self, valor):
        self.valor=valor
        self.Next=None

class Lineas:
    def __init__(self,Id,NumCompo,TiempoE):
        self.Id=Id
        self.NumCompo=NumCompo
        self.TiempoE=TiempoE
        self.Nodo1=None
        self.Next=None
        self.Tiempo=0

class producto:
    def __init__(self,nombre,TiempoE):
        self.nombre=nombre
        self.TiempoE=TiempoE
        self.Nodo1=None