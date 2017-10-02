from NodoLC import NodoLC
#from ArbolB import ArbolB

class ListaDobleC:
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.contador = 0		
	
	#Inserta al Inicio
	def InsertarInicio(self, Nombre, Pass):
		self.contador +=1
		if self.primero == None:
			self.primero = self.ultimo = NodoLC(self.contador, Nombre, Pass)
		else:			
			aux = NodoLC(self.contador, Nombre, Pass)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.primero.anterior = self.ultimo
		self.ultimo.siguiente = self.primero			
	
	#Inserta al Final
	def InsertarFinal(self, Nombre, Pass):
		self.contador +=1
		if self.primero == None:
			self.primero = self.ultimo = NodoLC(self.contador, Nombre, Pass)
		else:			
			aux = self.ultimo
			self.ultimo = aux.siguiente = NodoLC(self.contador, Nombre, Pass)
			self.ultimo.anterior = aux
		self.primero.anterior = self.ultimo
		self.ultimo.siguiente = self.primero		
	
	#Imprimir
	def ImprimirDatos(self):
		aux = self.primero
		while aux:
			print("Dato: -> " + str(aux.idDato))
			aux = aux.siguiente
			if aux == self.primero:
				break
			
	#Buscar Dato
	def Buscar(self, usuario, contrasena):
		aux = self.primero
		while aux != None:
			if aux.Nombre == usuario and aux.Pass == contrasena:
				#return aux.inicio.claves[0].nombreCarpeta
				return "True"
			aux = aux.siguiente
			if aux == self.primero:
				return "False"
	#Buscar RaizArbolB
	def RetornarRaizArbolB(self, usuario, contrasena):
		aux = self.primero
		while aux != None:
			if aux.Nombre == usuario and aux.Pass == contrasena:
				return aux.RaizArbolB				
			aux = aux.siguiente
			if aux == self.primero:
				return "False"
			
	#Buscar Actualizar RaizB del Nodo Circular
	def ActualizarRaiz(self, usuario, contrasena, NuevaRaiz):
		aux = self.primero
		while aux != None:
			if aux.Nombre == usuario and aux.Pass == contrasena:
				aux.RaizArbolB = NuevaRaiz
				#return aux.RaizArbolB				
			aux = aux.siguiente
			if aux == self.primero:
				return "False"
			
	
	#Buscar Actualizar RaizAVL
	def ActualizarRaizAVL(self, usuario, contrasena, NuevaRaiz):
		aux = self.primero
		while aux != None:
			if aux.Nombre == usuario and aux.Pass == contrasena:
				aux.RaizArbolB = NuevaRaiz
				#return aux.RaizArbolB				
			aux = aux.siguiente
			if aux == self.primero:
				return "False"		
	
	
	#Escribir Contenido del Archivo
	def grabarArchivo(self):
		cont1 = 0
		temp = self.primero		
		
		archivo=open('ListaCircular.txt','w')				
		archivo.write('digraph G{\n')		
		archivo.write("node [shape = record];\n");
		archivo.write("rankdir = LR;\n");		
		
		while temp != None:
			archivo.write(str(temp.Nombre) + "_nodo_" + str(cont1) + " [label="+str(temp.Nombre)+"]\n")
			cont1=cont1+1
			temp = temp.siguiente
			if temp == self.primero:
				break			
		
		cont1 = 0
		cont2 = cont1+1
		temp = self.primero		
		while temp != None:
			if temp.siguiente != None:
				archivo.write(str(temp.Nombre)+"_nodo_"+str(cont1)+"->"+str(temp.siguiente.Nombre)+"_nodo_"+str(cont2)+"\n")
				cont1=cont1+1
				cont2=cont2+1
			temp = temp.siguiente
			if temp == self.ultimo:
				break	
		
		contUltimo=cont1
		cont2 = cont1-1
		temp = self.ultimo			
		while temp != None:
			if temp.anterior != None:
				archivo.write(str(temp.Nombre)+"_nodo_"+str(cont1)+"->"+str(temp.anterior.Nombre)+"_nodo_"+str(cont2)+"\n")
				cont1=cont1-1
				cont2=cont2-1
			temp = temp.anterior
			if temp == self.primero:
				break		
		
		temp = self.primero
		temp2 = self.ultimo
		archivo.write(str(temp.Nombre)+"_nodo_"+str(0)+"->"+str(temp2.Nombre)+"_nodo_"+str(contUltimo)+"\n")
		archivo.write(str(temp2.Nombre)+"_nodo_"+str(contUltimo)+"->"+str(temp.Nombre)+"_nodo_"+str(0)+"\n")
		archivo.write('}')
		archivo.close()
		
		
	def RetornarNodoCircular(self, usuario, contrasena):
		aux = self.primero
		while aux != None:
			if aux.Nombre == usuario and aux.Pass == contrasena:
				return aux				
			aux = aux.siguiente
			if aux == self.primero:
				return "False"	