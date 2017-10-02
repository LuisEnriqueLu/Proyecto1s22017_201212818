package proceso;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.commons.fileupload.*;
import org.apache.commons.fileupload.disk.*;
import org.apache.commons.fileupload.servlet.*;

public class cargarArchivos extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
            response.setContentType("text/html;charset=UTF-8");
            try (PrintWriter out = response.getWriter()) {
                
            FileItemFactory itemfactory = new DiskFileItemFactory(); 
            ServletFileUpload upload = new ServletFileUpload(itemfactory);
            String JSONString = "";
            try{
                List<FileItem> items = upload.parseRequest(request);
                for(FileItem item:items)
                {
                    FileItem archivoItem = (FileItem) item;
                    if (!archivoItem.isFormField())
                    {                    
                        BufferedInputStream buffer = new BufferedInputStream(archivoItem.getInputStream());
                        byte[] ArregloBytes = new byte[(int) archivoItem.getSize()];
                        buffer.read(ArregloBytes);
                        buffer.close();

                        FileJsonDTO JSON = new FileJsonDTO();
                        JSON.setFileBytes(ArregloBytes);
                        JSON.setFileName(archivoItem.getName());
                        JSONString = ParserJson.parseObjectToStr(JSON);
                  
                        String codigoCarpeta = "";
                        String codigoArchivo = "";
                        String numeroAConcatenar;
                        String ArchivoConcatenar;
                        int posicionCaracter = 0;
                        int posicionCaracter2 = 0;
                        int codigoAscii;
                        int codigoAscii2;

                        for (posicionCaracter = 0; posicionCaracter<conexion.carpeta.length(); posicionCaracter++)
                        {
                            codigoAscii = conexion.carpeta.charAt(posicionCaracter);
                            numeroAConcatenar = Integer.toString(codigoAscii);
                            codigoCarpeta = codigoCarpeta + numeroAConcatenar;
                        }
                       
                        conexion conectar = new conexion();
                        String respuesta = conectar.CrearArchivo(conexion.carpeta, codigoCarpeta, JSONString);
                        
                        
                         //Traer Todos los archivos
                        String Objetoarchivo = conectar.RecuperarArchivos(codigoCarpeta);
                        String [] cargar_datos;
                        String Archivo ="";
                        
                        cargar_datos = Objetoarchivo.split("@");                
                        
                        
                        for(int x=0; x<cargar_datos.length; x++)
                        {   
                            Archivo += "<form action=\"selecionarArchivos\">"
                                    + "<div class=\"col-sm-4\"><div class=\"well\" style=\"background-color: rgba(0,0,0,0.2)\"><button type=\"submit\" class=\"btn btn-primary btn-block\" name=\"nombreArchivos\" value=\""+cargar_datos[x] +"\">"+ cargar_datos[x]+ " <span class=\"glyphicon glyphicon-file\"></span></button></div></div>"
                                    + "</form>";
                        }
                        
                        
                        request.setAttribute("Objetoarchivo", Archivo);
                        request.getRequestDispatcher("CargarArchivo.jsp").forward(request, response);                                   
                    }
                }
            }
            catch(FileUploadException e){
                out.println("Carga Sin Exito");
            }
            catch(Exception ex){
                out.println("No se puede Guardar");
            }                     
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {        
            processRequest(request, response);        
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {        
            processRequest(request, response);        
    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }
}
