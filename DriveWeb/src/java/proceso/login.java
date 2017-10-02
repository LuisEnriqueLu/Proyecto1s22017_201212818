package proceso;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class login extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException{
            response.setContentType("text/html;charset=UTF-8");
            try (PrintWriter out = response.getWriter()) 
            {
                String usuario = request.getParameter("usuario");
                String contrasena = request.getParameter("contrasena");
                    
                conexion.Usuario = usuario;
                conexion.Contrasena = contrasena;
                
                conexion conectar = new conexion();
                String respuesta = conectar.LoginUsuario(usuario, contrasena);                
                
                if(respuesta.equals("True"))
                {                    
                    request.setAttribute("respuestaPython", "Bienvenido " + conexion.Usuario);
                    request.getRequestDispatcher("Principal.jsp").forward(request, response);           
                }
                else{                    
                    request.setAttribute("errorMessage", "Usuario y/o Contraseña Invalido(s)");
                    request.getRequestDispatcher("Login.jsp").forward(request, response);
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
