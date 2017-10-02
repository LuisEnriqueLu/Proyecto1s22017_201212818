from NodoLS import NodoLS
class ListaSimple:
	def __init__(self):
		self.raiz = None
		self.indiceLista = 0
		self.contadorRegistro = 0
	
	def insertar(self, TipoRegistro, Estructura, Descripcion):
		self.contadorRegistro +=1
		if self.raiz == None:			
			nodo = NodoLS(self.contadorRegistro, TipoRegistro, Estructura, Descripcion, self.indiceLista)
			self.raiz = nodo
			self.indiceLista = self.indiceLista + 1
		else :
			aux = self.raiz
			while aux.siguiente != None:
				aux = aux.siguiente				
			
			nodo = NodoLS(self.contadorRegistro, TipoRegistro, Estructura, Descripcion, self.indiceLista)
			self.indiceLista = self.indiceLista + 1
			aux.siguiente = nodo
				
	
	def consultarLista(self):
		aux = self.raiz
		dato = ""
		if aux == None:			
			return "Lista Vacia"			
		else :
			while aux != None:
				if aux.index != None:
					dato += str(aux.idRegistro) + " -> "+ str(aux.TipoRegistro) + " -> " + str(aux.Estructura) + " -> " + aux.Descripcion + "; \n"										
				aux = aux.siguiente
			return str(dato) 
	
	def consultarRegistro(self, idRegistro):
		aux = self.raiz
		dato = ""
		if aux == None:			
			return "Lista Vacia"			
		else :
			while aux != None:
				if aux.index != None:
					if aux.idRegistro == idRegistro:
						dato = aux.TipoRegistro
						return dato
				aux = aux.siguiente
		
				
	def crearArchivo(self):
		archivo=open('ListaSimple.txt','w')
		archivo.close()
		self.grabarArchivo()
	
	def grabarArchivo(self):
		temp = self.raiz
		cont1 = 0
		
		archivo=open('ListaSimple.txt','a')
		archivo.write('digraph G{\n')
		
		while temp!=None:
			archivo.write(str(temp.TipoRegistro) + "_nodo_" + str(cont1) + " [label=ID_"+str(temp.idRegistro)+"_"+str(temp.TipoRegistro)+"]\n")
			cont1=cont1+1
			temp = temp.siguiente
		cont1 = 0
		cont2 = cont1+1
		temp = self.raiz
		
		while temp!=None:
			if temp.siguiente!=None:
				archivo.write(str(temp.TipoRegistro)+"_nodo_"+str(cont1)+"->"+str(temp.siguiente.TipoRegistro)+"_nodo_"+str(cont2)+"\n")
				cont1=cont1+1
				cont2=cont2+1
			temp = temp.siguiente
			
		archivo.write('}')
		archivo.close()
		return "Archivo Creado"	
	
	
	def crearArchivoByte(self):
		archivo=open('C:\\Users\\l_enr\\Desktop\\ArchivoByte.txt','w')
		archivo.close()
		self.grabarArchivoByte()	
	
	
	def grabarArchivoByte(self):
		temp = self.raiz
		
		archivo=open('C:\\Users\\l_enr\\Desktop\\ArchivoByte.txt','a')
		archivo.write(str(temp.TipoRegistro))
		
		return "Archivo Creado"		