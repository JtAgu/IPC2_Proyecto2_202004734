from nodos import bases
class ListaDatos:
    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,dato):
        if self.size==0:
            self.First=bases(dato)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=bases(dato)
            self.size+=1

class ListaLineas:
    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,Id,NumCompo,TiempoE):
        if self.size==0:
            self.First=bases(Id,NumCompo,TiempoE)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=bases(Id,NumCompo,TiempoE)
            self.size+=1

class ListaProductos:
    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,nombre,Texto):
        if self.size==0:
            self.First=bases(Id,NumCompo,TiempoE)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=bases(Id,NumCompo,TiempoE)
            self.size+=1


    
