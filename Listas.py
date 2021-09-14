from nodos import bases
from nodos import Lineas
from nodos import producto, Pieza,Simulacion

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

    def Reinicio(self):
        self.First=None
        self.size=0


class ListaLineas:
    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,Id,NumCompo,TiempoE):
        if self.size==0:
            self.First=Lineas(Id,NumCompo,TiempoE)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=Lineas(Id,NumCompo,TiempoE)
            self.size+=1

    


    def MostrarDatos(self):
        aux=self.First
        print("Lista de Lineas y su info")
        while aux!=None:
            print("No. :"+aux.Id,"Componentes: "+aux.NumCompo,"Tiempo Ensamblado: "+aux.TiempoEnsablado)
            print("=========================================")
            aux=aux.Next
        


class ListaProductos:

    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,nombre,Texto):
        if self.size==0:
            self.First=producto(nombre,Texto)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=producto(nombre,Texto)
            self.size+=1
    def MostrarDatos(self):
        aux=self.First
        print("Lista de productos y su info")
        while aux!=None:
            print("Nombre: "+aux.nombre, "cadena: "+aux.Cadena)
            print("=========================================")
            a=aux.NodoPieza
            while a!=None:
                print("No.: "+a.Id,"Linea: "+a.Linea,"Nombre: "+a.nombre)
                a=a.Next
            print("=========================================")
            aux=aux.Next
    
    def obtener(self, nombre):
        a=self.First
        a2=self.First
        while a.nombre!=nombre:
            a=a.Next
        print(a.nombre)
        if a.nombre==a2.nombre:
            self.First=a.Next
        elif a.nombre==nombre: 
            while a2.Next.nombre!=nombre:
                a2=a2.Next 
            if a.Next!=None:
                a2.Next=a.Next
            else:
                a2.Next=None
            a.Next=None
            self.size-=1
        return a
    
    def AñadirNodo(self,nodo):
        if self.size==0:
            self.First=nodo
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=nodo
            self.size+=1


    def AñadirPiezas(self,nombre,Linea,Id,nombrePieza):
        aux=self.BuscarNodo(nombre)
        nodoNuevo=Pieza(Linea,Id,nombrePieza)
        if aux.NodoPieza==None:
            aux.NodoPieza=nodoNuevo
        else:
            pieza=aux.NodoPieza
            while pieza.Next!=None:
                pieza=pieza.Next
            pieza.Next=nodoNuevo
    
    def BuscarNodo(self,nombre):
        a=self.First
        while a.nombre!=nombre:
            a=a.Next
        return a

class ListaSimulaciones:
    def __init__(self):
        self.First=None
        self.size=0

    def Añadir(self,nombre,nombreP):
        if self.size==0:
            self.First=Simulacion(nombre,nombreP)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=Simulacion(nombre,nombreP)
            self.size+=1