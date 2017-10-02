package proceso;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class crearCarpeta extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
                
                String carpeta = request.getParameter("carpeta");
                String [] cargar_datos;
                String ObjetoCarpetas ="";
                
                String codigoCarpeta = "";
                String numeroAConcatenar;
                int posicionCaracter = 0;
                int codigoAscii;

                for (posicionCaracter = 0; posicionCaracter<carpeta.length(); posicionCaracter++)
                {
                    codigoAscii = carpeta.charAt(posicionCaracter);
                    numeroAConcatenar = Integer.toString(codigoAscii);
                    codigoCarpeta = codigoCarpeta + numeroAConcatenar;
                }
                
                conexion conectar = new conexion();
                String respuesta = conectar.CrearCarpeta(carpeta, codigoCarpeta);                
                String RespuestaCarpetas = conectar.ObtenerCarpetas();                
                cargar_datos = RespuestaCarpetas.split("@");                
            
                for(int x=0; x<cargar_datos.length; x++)
                {   
                    ObjetoCarpetas += "<form action=\"selecionarCarpetas\">"
                            + "<div class=\"col-sm-4\"><div class=\"well\" style=\"background-color: rgba(0,0,0,0.2)\"><button type=\"submit\" class=\"btn btn-success btn-block\" name=\"nombreCarpeta\" value=\""+cargar_datos[x] +"\">"+ cargar_datos[x]+ " <span class=\"glyphicon glyphicon-folder-open\"></span></button></div></div>"
                            + "</form>";
                }              
                
                request.setAttribute("ObjetoCarpetas", ObjetoCarpetas);
                request.getRequestDispatcher("Principal.jsp").forward(request, response);
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
