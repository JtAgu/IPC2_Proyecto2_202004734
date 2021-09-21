from os import name
from nodos import Acciones, bases
from nodos import Lineas
from nodos import producto, Pieza,Simulacion
import xml.etree.cElementTree as ET


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
        self.Last=None

    def Añadir(self,Id,NumCompo,TiempoE):
        if self.size==0:
            self.First=Lineas(Id,NumCompo,TiempoE)
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            nodo=Lineas(Id,NumCompo,TiempoE)
            aux.Next=nodo
            self.Last=nodo
            nodo.Anterior=aux
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
                print("No.: "+str(a.Id),"Linea: "+str(a.Linea),"Nombre: "+a.nombre)
                a=a.Next
            print("=========================================")
            aux=aux.Next
    
    def obtener(self, nombre):
        a=self.First
        while a.nombre!=nombre:
            a=a.Next
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

    def AñadirPiezas(self,nombre,Linea,Id,nombrePieza,numPieza):
        aux=self.BuscarNodo(nombre)
        nodoNuevo=Pieza(Linea,Id,nombrePieza,numPieza)
        if aux.NodoPieza==None:
            aux.NodoPieza=nodoNuevo
        else:
            pieza=aux.NodoPieza
            while pieza.Next!=None:
                pieza=pieza.Next
            pieza.Next=nodoNuevo
            nodoNuevo.Anterior=pieza
    
    def BuscarNodo(self,nombre):
        a=self.First
        while a.nombre!=nombre:
            a=a.Next
        return a


class ListaAcciones:
    def __init__(self):
        self.First=None
        self.size=0


    def Añadir(self,nodo):
        if self.size==0:
            self.First=nodo
            self.size+=1
        else:
            aux=self.First
            while aux.Next:
                aux=aux.Next
            aux.Next=nodo
            self.size+=1


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
    

    def Procesar(self, nombre,lineas,ListaLineas):
        aux=self.First
        lineActual=ListaLineas.First
        tiempoAux=0
        #print(str(l1.Id),l1.NumCompo,str(l1.TiempoEnsablado)+"s")
        
        while aux:
            lineActual=ListaLineas.First
            while lineActual:
                lineActual.Posicion=0
                lineActual=lineActual.Next
            lineActual=ListaLineas.First
            t=1
            tiempoAux=0
            if aux.nombre==nombre:
                a=aux.producto.NodoPieza
                NombreProd=aux.producto.nombre
                mov=0
                #if aux.NodoAccion==None:
                #   t=0
                Lista=ListaAcciones()
                instruccion=""
                while a:
                    while lineActual.Id!=a.Linea:
                        if lineActual.Id<a.Linea:
                            lineActual=lineActual.Next
                        else:
                            lineActual=lineActual.Anterior
                    Tarmado=int(lineActual.TiempoEnsablado)

                    if int(lineActual.Posicion)<int(a.Numero):
                        lineActual.Posicion=int(lineActual.Posicion)+1
                        instruccion="Movimiento hacia componente "+str(lineActual.Posicion)
                        nodo=Acciones(a.Linea,t,instruccion,NombreProd)
                        Lista.Añadir(nodo)
                        if t==aux.TiempoRealizado:
                            aux.TiempoRealizado+=1
                        t+=1
                        
                    elif int(lineActual.Posicion)>int(a.Numero):
                        lineActual.Posicion=int(lineActual.Posicion)-1
                        instruccion="Movimiento posicion "+str(lineActual.Posicion)
                        nodo=Acciones(a.Linea,t,instruccion,NombreProd)
                        Lista.Añadir(nodo)
                        if t==aux.TiempoRealizado:
                            aux.TiempoRealizado+=1
                        t+=1
                    else:
                        if a.Anterior!=None:
                            if a.Anterior.Linea!=a.Linea:
                                cambio=aux.NodoAccion
                                tiempoAux=0
                                while cambio.Next:
                                    if cambio.Linea==a.Anterior.Linea:
                                        tiempoAux=cambio.Tiempo
                                    cambio=cambio.Next
                        if t<=tiempoAux:
                            instruccion="No hacer nada"
                            nodo=Acciones(a.Linea,t,instruccion,NombreProd)
                            Lista.Añadir(nodo)
                            t+=1
                        else:
                            while Tarmado>0:
                                instruccion="Armando componente "+str(lineActual.Posicion)
                                nodo=Acciones(a.Linea,t,instruccion,NombreProd)
                                Lista.Añadir(nodo)
                                t+=1
                                Tarmado-=1
                            if t==aux.TiempoRealizado:
                                aux.TiempoRealizado+=1
                            a.Armado=True
                            if a.Next!=None:
                                if a.Next.Linea!=a.Linea:
                                    cambio=aux.NodoAccion
                                    t=1
                                    while cambio.Next:
                                        if cambio.Linea==a.Next.Linea:
                                            t=int(cambio.Tiempo)+1
                                        cambio=cambio.Next
                                
                            a=a.Next
                    if aux.NodoAccion==None:
                        aux.NodoAccion=nodo
            
            print(t) 
            relleno=ListaLineas.First
            
            conteo=0
            while relleno:
                conteo=0
                cambio=aux.NodoAccion
                while cambio:
                    if relleno.Id==cambio.Linea:
                        conteo+=1
                        tiempoAux=cambio.Tiempo
                    cambio=cambio.Next
                print(relleno.Id,conteo)
                while conteo<(int(t)-1):
                    instruccion="No hacer nada"
                    tiempoAux+=1
                    nodo=Acciones(relleno.Id,tiempoAux,instruccion,NombreProd)
                    Lista.Añadir(nodo)
                    conteo+=1
                relleno=relleno.Next
            aux.TiempoRealizado=t-1
            aux.Procesado=True
            aux=aux.Next
        
        aux=self.First
        while aux:
            a=aux.NodoAccion
            componer=0
            while a:
                componer+=1
                a=a.Next
            aux.TiempoRealizado=componer//ListaLineas.size
            aux=aux.Next


    def Obtener(self,nombreProd,nombreSim):
        aux=self.First
        while aux:
            if aux.nombre==nombreSim:
                if aux.producto.nombre==nombreProd:
                    return aux
            aux=aux.Next
        return aux


    def imprimirXML(self, nombre):
        aux=self.First  
        
        if 1==1:
            #ruut=ET.Element("SalidaSimulacion ",name=nombre)
            ruut=ET.Element("SalidaSimulacion")
            Name=ET.SubElement(ruut,"Nombre").text=nombre
            Listado=ET.SubElement(ruut,"ListadoProductos")
            while aux:
                if aux.nombre==nombre:
                    ET.SubElement(Listado,"Nombre").text=aux.producto.nombre
                    Tiempo=ET.SubElement(Listado,"TiempoTotal")
                    Tiempo.text=str(aux.TiempoRealizado)
                    
                    Elaboracion=ET.SubElement(Listado,"ElaboracionOptima")
                    l="1"
                    while int(l)<=aux.TiempoRealizado:
                        a=aux.NodoAccion
                        T=ET.SubElement(Elaboracion,"Tiempo",NoSegundo=""+str(l))
                        while a:
                            print("Esto es  L:"+str(l))
                            if a.Tiempo==int(l):
                                print("Esto es tiempo: "+str(a.Tiempo))
                                ET.SubElement(T,"LineaEnsamblaje",NoLinea=""+str(a.Linea)).text=a.Descripcion
                            a=a.Next
                        l=int(l)+1
                aux=aux.Next

            arbol=ET.ElementTree(ruut)
            try:
                arbol.write(nombre+".xml")
                print("ARCHIVO XML GENERADO")
            except IOError as exc:
                print(exc)

        else:
            print("No ha seleccionado un terreno analizado...")
            
    
    def Mostrar(self):
        aux=self.First
        while aux:
            print(aux.nombre,aux.producto.nombre)
            if aux.NodoAccion!=None:
                a=aux.NodoAccion
                while a:
                    print("Linea: "+str(a.Linea),a.Descripcion, " en: "+str(a.Tiempo)+"s")
                    a=a.Next
                print("=========================================")
            else:
                print("=========================================")
            aux=aux.Next
            

        