from NodoB import NodoB
from ArbolB import ArbolB
from Pagina import Pagina
from ListaDobleC import ListaDobleC
from ListaSimple import ListaSimple
from ArbolAVL import ArbolAVL

claseArbolB = ArbolB()
claseLista = ListaDobleC()
claseListaSimple = ListaSimple()
claseListaCircular = ListaDobleC()
claseArbolAVL = ArbolAVL()

if __name__ == "__main__":    
    
    nwhile = 0
    while nwhile!=None:
        print("\n---- MENU ----")
        #print("1. Agregar")
        #print("2. Crear Archivo Arbol")
        #print("3. Insertar Lista Doble")
        #print("4. Imprimir")
        #print("5. Crear Archivo Lista Doble")
        #print("6. Insertar Lista Simple")
        #print("7. Crear Archivo Lista Simple")
        #print("8. Insertar B En Lista Circular")
        print("1. Probar")
        num = input("Ingrese una opcion: ")
        if num == "1":
            claseArbolB.crearNodoInsertar("Carpetas", "C1")
            claseArbolB.crearNodoInsertar("Documentos", "C2")
            claseArbolB.crearNodoInsertar("Videos", "C3")  
            claseArbolB.crearNodoInsertar("APK", "C4")  
            claseArbolB.crearNodoInsertar("Archivos", "C5")
            claseArbolB.crearNodoInsertar("Archivos", "C5")                       
        elif num == "2":
            claseArbol.crearArchivo()                    
        elif num == "3":
            claseLista.InsertarFinal("1", "Luis", "123")
            claseLista.InsertarFinal("2", "Jose", "123")
            claseLista.InsertarFinal("3", "Pedro", "123")
            claseLista.InsertarFinal("4", "Juan", "123")
        elif num == "4":
            claseLista.Imprimir()
        elif num == "5":
            claseLista.grabarArchivo()
        elif num == "6":
            claseListaCircular.InsertarFinal(1,"Pedro", "123", "Home")
            claseListaCircular.InsertarFinal(1,"Luis", "123", "Casa")            
            claseListaCircular.InsertarFinal(1,"Julio", "123", "Inicio")
            claseListaCircular.InsertarFinal(1,"Estre", "123", "Raiz")            
        elif num == "7":
            claseListaSimple.crearArchivo() 
        elif num == "8":
            claseArbolB = ArbolB()
            claseListaCircular.InsertarFinal("Luis", "123")           		            
            
            raizArbolB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada = claseArbolB.crearNodoInsertarUsuario(50, "ABC", "C1", raizArbolB)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada)
            
            raizArbolB1 = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada1 = claseArbolB.crearNodoInsertarUsuario(20, "APK", "C2", raizArbolB1)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada1)
            
            raizArbolB2 = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada2 = claseArbolB.crearNodoInsertarUsuario(30, "DOC", "C3", raizArbolB2)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada2)
            
            raizArbolB3 = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada3 = claseArbolB.crearNodoInsertarUsuario(40, "VAL", "C4", raizArbolB3)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada3)
            
            raizArbolB4 = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada4 = claseArbolB.crearNodoInsertarUsuario(60, "NEW", "C4", raizArbolB4)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada4)
            
        elif num == "9":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB(40, "VAL", "C4", raizB)
            NuevaRaiz = claseArbolAVL.CrearNodo("20", "Hola", RetornarCarpeta.RiazNodoAVL)
            claseArbolB.ActualizarRaizAVL_De_ArbolB(40, "VAL", "C4", RetornarCarpeta, NuevaRaiz)
            
            
        elif num == "10":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB(40, "VAL", "C4", raizB)
            NuevaRaiz = claseArbolAVL.CrearNodo("30", "Mundo", RetornarCarpeta.RiazNodoAVL)
            claseArbolB.ActualizarRaizAVL_De_ArbolB(40, "VAL", "C4", RetornarCarpeta, NuevaRaiz) 
            
        elif num == "11":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB(40, "VAL", "C4", raizB)
            NuevaRaiz = claseArbolAVL.CrearNodo("10", "Como", RetornarCarpeta.RiazNodoAVL)
            claseArbolB.ActualizarRaizAVL_De_ArbolB(40, "VAL", "C4", RetornarCarpeta, NuevaRaiz) 
        
        elif num == "12":  
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB(40, "VAL", "C4", raizB)
            NuevaRaiz = claseArbolAVL.grabarArchivoUsuario(RetornarCarpeta.RiazNodoAVL)
            claseArbolB.ActualizarRaizAVL_De_ArbolB(40, "VAL", "C4", RetornarCarpeta, NuevaRaiz) 
            
        elif num == "13":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB(40, "VAL", "C4", raizB)
            claseArbolAVL.grabarArchivoUsuario(RetornarCarpeta.RiazNodoAVL)
        
        elif num == "14":
            claseArbolB = ArbolB()
            claseListaCircular.InsertarFinal("Julio", "123", claseArbolB.crearNodoInsertar(100, "Casa", "C100"))           		            
            
            raizArbolB = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            RaizRetornada = claseArbolB.crearNodoInsertarUsuario(500, "ABC", "C1", raizArbolB)
            claseListaCircular.ActualizarRaiz("Julio", "123", RaizRetornada)
            
            raizArbolB1 = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            RaizRetornada1 = claseArbolB.crearNodoInsertarUsuario(200, "APK", "C2", raizArbolB1)
            claseListaCircular.ActualizarRaiz("Julio", "123", RaizRetornada1)
            
            raizArbolB2 = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            RaizRetornada2 = claseArbolB.crearNodoInsertarUsuario(300, "DOC", "C3", raizArbolB2)
            claseListaCircular.ActualizarRaiz("Julio", "123", RaizRetornada2)
            
            raizArbolB3 = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            RaizRetornada3 = claseArbolB.crearNodoInsertarUsuario(400, "VAL", "C4", raizArbolB3)
            claseListaCircular.ActualizarRaiz("Julio", "123", RaizRetornada3)
            
            raizArbolB4 = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            RaizRetornada4 = claseArbolB.crearNodoInsertarUsuario(600, "NEW", "C4", raizArbolB4)
            claseListaCircular.ActualizarRaiz("Julio", "123", RaizRetornada4)
        
          
        elif num == "15":  
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            claseArbolB.crearArchivo(raizB)
        
        elif num == "16":  
            raizB = claseListaCircular.RetornarRaizArbolB("Julio", "123")
            claseArbolB.crearArchivo(raizB)   
            
        elif num == "100":
            claseListaCircular.InsertarFinal("Luis", "123")
            raizArbolB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RaizRetornada = claseArbolB.crearNodoInsertarUsuario("10", "Nueva", "C100", raizArbolB)
            claseListaCircular.ActualizarRaiz("Luis", "123", RaizRetornada)
            
        elif num == "101":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB("10", "Nueva", "C100", raizB)            
            NuevaRaizAVL = claseArbolAVL.CrearNodo("Texto", "Hola", RetornarCarpeta.RiazNodoAVL)
            NuevaRaizB = claseArbolB.ActualizarRaizAVL_De_ArbolB("10", raizB, NuevaRaizAVL)
            claseListaCircular.ActualizarRaiz("Luis", "123", NuevaRaizB)            
            
            
        elif num == "102":
            raizB = claseListaCircular.RetornarRaizArbolB("Luis", "123")
            RetornarCarpeta = claseArbolB.retornarNodoArbolB("10", "Nueva", "C100", raizB)            
            NuevaRaizAVL = claseArbolAVL.CrearNodo("Nada", "Hola", RetornarCarpeta.RiazNodoAVL)
            NuevaRaizB = claseArbolB.ActualizarRaizAVL_De_ArbolB("10", raizB, NuevaRaizAVL)
            claseListaCircular.ActualizarRaiz("Luis", "123", NuevaRaizB)   
            
        elif num == "103":
            raizArbolB = claseListaCircular.RetornarRaizArbolB("Luis", "123") #Buscamos en el Nodo de la lista el ArbolB
            RetornarCarpeta = claseArbolB.retornarNodoArbolB("10", "Nueva", "C100", raizArbolB) #Retorno Carpeta
            datosDeArchivoAVL = claseArbolAVL.retornarArchivos(RetornarCarpeta.RiazNodoAVL) #Retornamos Archivos Dentro de Carpeta
            print(datosDeArchivoAVL)	            