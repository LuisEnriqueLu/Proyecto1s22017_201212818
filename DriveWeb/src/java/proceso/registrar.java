package proceso;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class registrar extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
            response.setContentType("text/html;charset=UTF-8");
            try (PrintWriter out = response.getWriter()) 
            {
                String usuario = request.getParameter("usuario");
                String contrasena = request.getParameter("contrasena");
                
                conexion conectar = new conexion();
                String respuesta = conectar.RegistrarUsuario(usuario, contrasena);
                //request.setAttribute("respuestaPython", respuesta);
                //request.getRequestDispatcher("Principal.jsp").forward(request, response);
                response.setStatus(HttpServletResponse.SC_RESET_CONTENT);
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
