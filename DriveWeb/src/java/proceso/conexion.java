package proceso;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class conexion {
    
    public static OkHttpClient ClienteWeb = new OkHttpClient();
    public static String Usuario;
    public static String Contrasena;
    public static String carpeta;
    public static String archivo;
    
    
    /******************REGISTRAR USUARIO***********************/
    public String RegistrarUsuario(String usuario, String contrasena){
        RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", usuario)
                .add("contrasena", contrasena)                
                .build();
        return ConexionPythonRegistroUsuarios(formBody);
    }
    /******************REGISTRAR USUARIO***********************/
    public static String ConexionPythonRegistroUsuarios(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/registrarUsuario");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }    
    
    
    /******************LOGIN***********************/
    public String LoginUsuario(String usuario, String contrasena){
        RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", usuario)
                .add("contrasena", contrasena)
                .build();
        return ConexionPythonLoginUsuario(formBody);
    }       
    /******************LOGIN***********************/
    public static String ConexionPythonLoginUsuario(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/loginUsuario");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }
    
    
    /******************CREAR CARPETAS***********************/
    public String CrearCarpeta(String nombreCarpeta, String idCarpeta){
        RequestBody formBody = new FormEncodingBuilder()
                .add("nombreCarpeta", nombreCarpeta)
                .add("idCarpeta", idCarpeta)
                .add("usuario", "Luis")
                .add("contrasena", "123")
                .build();
        return ConexionPythonCrearCarpeta(formBody);
    } 
    /******************CREAR CARPETAS***********************/
    public static String ConexionPythonCrearCarpeta(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/crearCarpetaUsuario");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }    
     
    
    /******************CREAR ARCHIVOS***********************/
    public String CrearArchivo(String nombreCarpeta, String idCarpeta, String JSONFile){
        RequestBody formBody = new FormEncodingBuilder()
                .add("nombreCarpeta", nombreCarpeta)
                .add("idCarpeta", idCarpeta)
                .add("usuario", conexion.Usuario)
                .add("contrasena", conexion.Contrasena)
                .add("JSONFile", JSONFile)
                .build();
        return ConexionPythonCrearArchivo(formBody);
    }
    /******************CREAR ARCHIVOS***********************/
    public static String ConexionPythonCrearArchivo(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/crearArchivo");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }
    
    
    
    /******************OBTENER CARPETAS***********************/
    public String ObtenerCarpetas(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", conexion.Usuario)
                .add("contrasena", conexion.Contrasena)
                .build();
        return ConexionPythonObtenerCarpetas(formBody);
    } 
    /******************OBTENER CARPETAS***********************/
    public static String ConexionPythonObtenerCarpetas(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/RetornarCarpetas");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }
    
    
    
    /******************DESCARGAR ARCHIVO***********************/
    public String DescargarArchivo(String nombreArchivo, String idCarpeta){
        RequestBody formBody = new FormEncodingBuilder()
                .add("usuario", conexion.Usuario)
                .add("contrasena", conexion.Contrasena)
                .add("nombreArchivo", nombreArchivo)
                .add("idCarpeta", idCarpeta)                
                .build();
        return ConexionPythonDescargarArchivo(formBody);
    }    
    /******************DESCARGAR ARCHIVO***********************/
    public String ConexionPythonDescargarArchivo(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/RespuestaArchivo");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }
    
    /******************RECUPERAR ARCHIVOS***********************/
    public String RecuperarArchivos(String idCarpeta){
        RequestBody formBody = new FormEncodingBuilder()
                .add("idCarpeta", idCarpeta)
                .add("usuario", conexion.Usuario)
                .add("contrasena", conexion.Contrasena)
                .build();        
        return ConexionPythonRecuperarArchivos(formBody);
    }
    /******************RECUPERAR ARCHIVOS***********************/
    public static String ConexionPythonRecuperarArchivos(RequestBody formBody) 
    {
        try {
            URL url = new URL("http://127.0.0.5:5000/RetornarArchivos");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response respuestaPython = ClienteWeb.newCall(request).execute();
            return respuestaPython.body().string();
        }catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }catch (IOException ex) {
            java.util.logging.Logger.getLogger(conexion.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }        
    }
    
}
