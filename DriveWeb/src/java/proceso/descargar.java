package proceso;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class descargar extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
            response.setContentType("text/html;charset=UTF-8");
            try (PrintWriter out = response.getWriter()) {
                
                String codigoCarpeta = "";
                String numeroAConcatenar;
                int posicionCaracter = 0;
                int codigoAscii;
                String Carpeta = conexion.carpeta;

                for (posicionCaracter = 0; posicionCaracter<Carpeta.length(); posicionCaracter++)
                {
                    codigoAscii = Carpeta.charAt(posicionCaracter);
                    numeroAConcatenar = Integer.toString(codigoAscii);
                    codigoCarpeta = codigoCarpeta + numeroAConcatenar;
                }

                conexion conectar = new conexion();
                String respuestaPython = conectar.DescargarArchivo(conexion.archivo, codigoCarpeta);
                FileJsonDTO fileObject = ParserJson.parseStrToObject(respuestaPython, FileJsonDTO.class); 
                try (FileOutputStream archivo = new FileOutputStream("C:\\Users\\l_enr\\Desktop\\"+fileObject.getFileName())) {
                    archivo.write(fileObject.getFileBytes());
                    archivo.close(); 
                }
                out.print("Archivo Descargado");
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
