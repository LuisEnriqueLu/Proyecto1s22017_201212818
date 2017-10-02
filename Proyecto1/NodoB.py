from NodoAVL import NodoAVL

class NodoB:
	def __init__(self, idNombre=None, nombreCarpeta=None, direccion=None):
		self.idNombre = idNombre
		self.nombreCarpeta = nombreCarpeta
		self.direccion = direccion
		self.RiazNodoAVL = None
		
	def getAVLraiz(self):
		return self.RiazNodoAVL

	def setAVLraiz(self, nuevoNodo):
		self.RiazNodoAVL = nuevoNodo		
		
		
	