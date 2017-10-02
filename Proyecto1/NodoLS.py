class NodoLS:
	def __init__(self, idRegistro=None, TipoRegistro=None, Estructura=None, Descripcion=None, index=None, siguiente=None):
		self.idRegistro = idRegistro
		self.TipoRegistro = TipoRegistro
		self.Estructura = Estructura
		self.Descripcion = Descripcion
		self.index = index
		self.siguiente = siguiente