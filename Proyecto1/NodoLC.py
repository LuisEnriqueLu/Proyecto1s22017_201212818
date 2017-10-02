from Pagina import Pagina

class NodoLC:
	def __init__(self, idDato=None, Nombre=None, Pass=None, RaizArbolB=Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)):
		self.idDato = idDato
		self.Nombre = Nombre
		self.Pass = Pass
		self.siguiente = None
		self.anterior = None
		self.RaizArbolB = RaizArbolB
		
	def getRaizB(self):
		return self.RaizArbolB

	def setRaizB(self, nuevoNodo):
		self.RaizArbolB = nuevoNodo			