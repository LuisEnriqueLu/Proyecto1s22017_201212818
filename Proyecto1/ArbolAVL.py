from NodoAVL import NodoAVL
from Logical import Logical
from ListaDobleC import ListaDobleC
from NodoB import NodoB

listaDoble = ListaDobleC()

class ArbolAVL:
        def __init__ (self):
                self.inicio = None
                self.digraf = "digraph G{\n"
                self.archivoAVL=None
                self.ArchivosRetornar=None
                
        
        def CrearNodo(self, nombre, archivo, raiz):
                nuevoNodo = NodoAVL(nombre, archivo)
                h = Logical(False)
                return self.agregarAVL(raiz, nuevoNodo, h)
                
        
        def agregarAVL(self, raiz, nuevoNodo, h):
                if raiz == None:
                        raiz = nuevoNodo
                        h.setLogical(True)
                elif nuevoNodo.nombre < raiz.nombre:
                        nodoIz = self.agregarAVL(raiz.izquierda, nuevoNodo, h)
                        raiz.izquierda = nodoIz
                        if h.getLogical() == True:
                                op = raiz.FE
                                if op == 1:
                                        raiz.FE = 0
                                        h.setLogical(False)
                                elif op == 0:
                                        raiz.FE = -1
                                elif op == -1:
                                        nodo1 = raiz.izquierda
                                        if nodo1.FE == -1:
                                                raiz = self.rotacionII(raiz, nodo1)
                                        else:
                                                raiz = self.rotacionID(raiz, nodo1)
                                        h.setLogical(False)
                elif nuevoNodo.nombre > raiz.nombre:
                        nodoDr = self.agregarAVL(raiz.derecha, nuevoNodo, h)
                        raiz.derecha = nodoDr
                        if h.getLogical() == True:
                                op = raiz.FE
                                if op == 1:
                                        nodo1 = raiz.derecha
                                        if nodo1.FE == 1:
                                                raiz = self.rotacionDD(raiz, nodo1)
                                        else:
                                                raiz = self.rotacionDI(raiz, nodo1)
                                        h.setLogical(False)
                                elif op == 0:
                                        raiz.FE = 1
                                elif op == -1:
                                        raiz.FE = 0
                                        h.setLogical(False)
                
                self.inicio = raiz
                return raiz
        
        def rotacionID(self, nodo, nodo1):
                nodo2 = nodo1.derecha
                nodo1.derecha = nodo2.izquierda
                nodo2.izquierda = nodo1
                nodo.izquierda = nodo2.derecha
                nodo2.derecha = nodo
                #nodo = nodo2
                if nodo2.FE == 1:
                        nodo1.FE = -1
                else:
                        nodo1.FE = 0
                if nodo2.FE == -1:
                        nodo.FE = 1
                else:
                        nodo.FE = 0
                nodo2.FE = 0
                return nodo2
            
        def rotacionII(self, nodo, nodo1):
                nodo.izquierda = nodo1.derecha
                nodo1.derecha = nodo
                if nodo1.FE == -1:
                        nodo.FE = 0
                        nodo1.FE = 0
                else:
                        nodo.FE = -1
                        nodo1.FE = 1
                return nodo1
            
        def rotacionDD(self, nodo, nodo1):
                nodo.derecha = nodo1.izquierda
                nodo1.izquierda = nodo
                if nodo1.FE == 1:
                        nodo.FE = 0
                        nodo1.FE = 0
                else:
                        nodo.FE = 1
                        nodo1.FE = -1
                return nodo1
            
        def rotacionDI(self, nodo, nodo1):
                nodo2 = nodo1.izquierda
                nodo1.izquierda = nodo2.derecha
                nodo2.derecha = nodo1
                nodo.derecha = nodo2.izquierda
                nodo2.izquierda = nodo
            
                if nodo2.FE == 1:
                        nodo.FE = -1
                else:
                        nodo.FE = 0
                if nodo2.FE == -1:
                        nodo1.FE = 1
                else:
                        nodo1.FE = 0
                nodo2.FE = 0
                return nodo2        
        
        
        def grabarArchivoUsuario(self, raiz):
                self.inicio = raiz
                archivo = open("ArbolAVLUsuario.txt", 'w')
                self.graficarPreOrden(self.inicio)
                self.digraf += "\n}"
                archivo.write(self.digraf)
                archivo.close()        
        
        def grabarArchivo(self):
                archivo = open("ArbolAVL.txt", 'w')
                self.graficarPreOrden(self.inicio)
                self.digraf += "\n}"
                archivo.write(self.digraf)
                archivo.close()
        
        def graficarPreOrden(self, nuevoNodo):
                if nuevoNodo != None:
                        self.digraf += "nodo_" + str(nuevoNodo.nombre) + ' [label="' +str(nuevoNodo.nombre) + '"]\n'
                        if nuevoNodo.izquierda != None:
                                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.izquierda.nombre) + "\n"
                                self.graficarPreOrden(nuevoNodo.izquierda)
                        else:
                                pass
                        if nuevoNodo.derecha != None:
                                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.derecha.nombre) + "\n"
                                self.graficarPreOrden(nuevoNodo.derecha)                   
                        else:
                                pass
                else:
                        pass      
                
                
        def obtenerAVL(self, nombreArchivo, raiz):
                nodo = NodoAVL(nombreArchivo, nombreArchivo)
                self.buscarAVL(nodo, raiz)
                return self.archivoAVL
        
        def buscarAVL(self, nuevoNodo, raiz):
                if raiz != None:
                        if nuevoNodo.nombre == raiz.nombre:
                                self.archivoAVL = raiz
                                #return nuevoNodo.nombre                        
                        else:
                                self.buscarAVL(nuevoNodo, raiz.izquierda)
                                self.buscarAVL(nuevoNodo, raiz.derecha)        
                                
        
        def retornarArchivos(self, raiz):
                self.ArchivosRetornar = ""
                self.retornarArchivosDeUnaCarpeta(raiz)                
                return self.ArchivosRetornar                
        
        #Retornar Archivos
        def retornarArchivosDeUnaCarpeta(self, nuevoNodo):                
                if nuevoNodo != None:
                        self.ArchivosRetornar += str(nuevoNodo.nombre) + "@"
                        if nuevoNodo.izquierda != None:
                                self.retornarArchivosDeUnaCarpeta(nuevoNodo.izquierda)
                        else:
                                pass
                        if nuevoNodo.derecha != None:
                                self.retornarArchivosDeUnaCarpeta(nuevoNodo.derecha)                   
                        