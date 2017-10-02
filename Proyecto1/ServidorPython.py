from ArbolB import ArbolB
from ListaDobleC import ListaDobleC
from ListaSimple import ListaSimple
from ArbolAVL import ArbolAVL
from flask import Flask, request, Response
import json

claseArbolB = ArbolB()
claseListaCircular = ListaDobleC()
claseListaSimple = ListaSimple()
claseArbolAVL = ArbolAVL()

app = Flask("Servidor_Python")

class Servidor():	
	#---------------------------LOGIN USUARIO--------------------------------------#
	@app.route('/loginUsuario',methods=['POST']) 
	def LoginUsuario():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])		
		response = claseListaCircular.Buscar(usuario, contrasena)
		claseListaSimple.insertar("Login", "Lista Circular", "Se logueo el Usuario " + str(usuario))
		return str(response)	
	
	
	#---------------------------REGISTRAR USUARIO---------------------------------#
	@app.route('/registrarUsuario',methods=['POST'])
	def RegistrarUsuario():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])		
		claseListaCircular.InsertarFinal(usuario, contrasena)
		claseListaSimple.insertar("Registro", "Lista Circular", "Se Creo el Usuario " + str(usuario))
		return "Usuario Registrado con Exito"	
	
	
	#---------------------------CREAR CARPETA---------------------------------#
	@app.route('/crearCarpetaUsuario',methods=['POST'])
	def crearCarpetaUsuario():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		nombreCarpeta = str(request.form['nombreCarpeta'])
		idCarpeta = str(request.form['idCarpeta'])
		idCarpeta2 = int(idCarpeta)
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena)#Buscamos en el Nodo de la lista el ArbolB
		RaizRetornada = claseArbolB.crearNodoInsertarUsuario(idCarpeta, nombreCarpeta, "C100", raizArbolB) #Crear Carpeta en el Arbol del Usuario Logeado
		claseListaCircular.ActualizarRaiz(usuario, contrasena, RaizRetornada)
		claseListaSimple.insertar("CrearCarpeta", "ARBOLB", "Se Creo una Nueva Carpeta" + str(nombreCarpeta))
		return "True"	
	
	
	#---------------------------RETORNAR CARPETAS---------------------------------#
	@app.route('/RetornarCarpetas',methods=['POST'])
	def RetornarCarpetas():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena) #Buscamos en el Nodo de la lista el ArbolB
		RaizRetornada = claseArbolB.RetornarArbolCompleto(raizArbolB)
		return RaizRetornada		
	
	
	#---------------------------CREAR ARCHIVO---------------------------------#
	@app.route('/crearArchivo',methods=['POST'])
	def crearArchivoCarpeta():
		archivoByte = request.form["JSONFile"] 
		objFile = json.loads(archivoByte)		
		
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		nombreCarpeta = str(request.form['nombreCarpeta'])
		idCarpeta = str(request.form['idCarpeta'])
		Archivo = objFile["fileBytes"]
		nombreArchivo = objFile["fileName"]
		
		raizB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena)
		RetornarCarpeta = claseArbolB.retornarNodoArbolB(idCarpeta, nombreCarpeta, "C100", raizB)
		NuevaRaizAVL = claseArbolAVL.CrearNodo(nombreArchivo, Archivo, RetornarCarpeta.RiazNodoAVL)
		NuevaRaizB = claseArbolB.ActualizarRaizAVL_De_ArbolB(idCarpeta, raizB, NuevaRaizAVL)
		claseListaCircular.ActualizarRaiz(usuario, contrasena, NuevaRaizB)            
		claseListaSimple.insertar("CrearArchivo", "ARBOLAVL", "Se Creo un Nuevo Archivo" + str(nombreArchivo))
		
		#Nuevo Arbol AVL
		#NuevaRaizAVL = claseArbolAVL.CrearNodo(nombreArchivo, Archivo, RetornarCarpeta.RiazNodoAVL)
		#Actualizar el nodo avl de la carpeta con ese nuevo Arbol AVL
		#Nueva Carpeta
		#Actualizar el arbol b con esa nueva carpeta
		#nuevaRaizB = claseArbolB.ActualizarRaizAVL_De_ArbolB(idCarpeta, raizB, NuevaRaizAVL)
		#Tengo arbol B
		#Actualizar el nodo lc con ese nuevo arbol
		#claseListaCircular.ActualizarRaiz(usuario, contrasena, nuevaRaizB)
		return usuario + contrasena + nombreCarpeta + idCarpeta + nombreArchivo + Archivo
	
	
	#---------------------------CREAR IMAGEN LISTA CIRCULAR------------------------------#
	@app.route('/CrearArchivoListaCircular')
	def CrearArchivoListaCircular():	
		claseListaCircular.grabarArchivo()
		return "Archivo Creado"
	
	
	
	#---------------------------CREAR IMAGEN LISTA SIMPLE BITACORA--------------------------#
	@app.route('/CrearArchivoListaSimple')
	def CrearArchivoListaSimple():	
		claseListaSimple.crearArchivo()
		return "Archivo Creado"
	
	
	
	#---------------------------CREAR IMAGEN ARBOL B--------------------------------------#
	@app.route('/CrearArchivoArbolB',methods=['POST'])
	def CrearArchivoArbolB():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena)
		claseArbolB.crearArchivo(raizArbolB)
		return "Archivo Creado"		
	
	
	
	#---------------------------CREAR IMAGEN ARBOL AVL--------------------------------------#
	@app.route('/CrearArchivoAVL',methods=['POST'])
	def CrearArchivoArbolAVL():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		nombreCarpeta = str(request.form['nombreCarpeta'])
		idCarpeta = str(request.form['idCarpeta'])		
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena) #Retorno Arbol B
		RetornarCarpeta = claseArbolB.retornarNodoArbolB(idCarpeta, nombreCarpeta, "C100", raizArbolB) #Retorno Carpeta
		claseArbolAVL.grabarArchivoUsuario(RetornarCarpeta.RiazNodoAVL)
		return "Archivo Creado"	
	
	
	#---------------------------RETORNAR ARCHIVO FISICO--------------------------------------#
	@app.route('/RespuestaArchivo',methods=['POST'])
	def RespuestaArchivo():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		nombreArchivo = str(request.form['nombreArchivo'])
		idCarpeta = str(request.form['idCarpeta'])		
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena) #Retorno Arbol B
		RetornarCarpeta = claseArbolB.retornarNodoArbolB(idCarpeta, idCarpeta, "C100", raizArbolB) #Retorno Carpeta
		datosDeArchivoAVL = claseArbolAVL.obtenerAVL(nombreArchivo, RetornarCarpeta.RiazNodoAVL)
		
		objFile = {"fileName" : str(datosDeArchivoAVL.nombre), "fileBytes": str(datosDeArchivoAVL.archivo)}
		jsonFile = json.dumps(objFile)
		return jsonFile 
	
	
	#---------------------------RETORNAR ARCHIVOS---------------------------------#
	@app.route('/RetornarArchivos',methods=['POST'])
	def RetornarArchivos():
		usuario = str(request.form['usuario'])
		contrasena = str(request.form['contrasena'])
		idCarpeta = str(request.form['idCarpeta'])		
		
		raizArbolB = claseListaCircular.RetornarRaizArbolB(usuario, contrasena) #Buscamos en el Nodo de la lista el ArbolB
		RetornarCarpeta = claseArbolB.retornarNodoArbolB(idCarpeta, idCarpeta, "C100", raizArbolB) #Retorno Carpeta
		datosDeArchivoAVL = claseArbolAVL.retornarArchivos(RetornarCarpeta.RiazNodoAVL) #Retornamos Archivos Dentro de Carpeta
		return datosDeArchivoAVL		
		
	
	if __name__ == "__main__":
		app.run(debug=True, host='127.0.0.5')
