class bases:
    def __init__(self, valor):
        self.valor=valor
        self.Next=None

class Acciones:
    def __init__(self,Linea ,Tiempo,Descripcion,nombreProd):
        self.Linea=Linea
        self.Descripcion=Descripcion
        self.Tiempo=Tiempo
        self.nombreProd=nombreProd
        self.Next=None


class Pieza:
    def __init__(self,Linea,Id,nombre,numero):
        self.nombre=nombre
        self.Linea=Linea
        self.Id=Id
        self.Numero=numero
        self.Next=None
        self.Anterior=None
        self.Armado=False


class Simulacion:
    def __init__(self,nombre,producto):
        self.producto=producto
        self.nombre=nombre
        self.TiempoRealizado=0
        self.Procesado=False
        self.NodoAccion=None         #Nodo que conectara con las instrucciones de armado
        self.Next=None


class Lineas:
    def __init__(self,Id,NumCompo,TiempoE):
        self.Id=Id
        self.NumCompo=NumCompo
        self.TiempoEnsablado=TiempoE
        self.NodoPieza=None
        self.NodoArmado=None
        self.Posicion=0
        self.Next=None
        self.Anterior=None
        self.Tiempo=0


class producto:
    def __init__(self,nombre,Cadena):
        self.nombre=nombre
        self.Cadena=Cadena
        self.TiempoE=0
        self.NodoPieza=None         #Nodo que conectara con las piezas de armado
        self.Next=None


