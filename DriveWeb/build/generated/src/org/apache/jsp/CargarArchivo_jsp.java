package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import proceso.conexion;

public final class CargarArchivo_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html style=\"min-height: 100%; position: relative;\">\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>DRIVE USAC</title>\n");
      out.write("        <link rel=\"shortcut icon\" href=\"img/drive6.png\"/>\n");
      out.write("        <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n");
      out.write("        <link href=\"css/bootstrap.css\" rel=\"stylesheet\">\n");
      out.write("        <link href=\"css/login.css\" rel=\"stylesheet\">\n");
      out.write("        <link href=\"fonts/font-awesome.min.css\" rel=\"stylesheet\">\n");
      out.write("        <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>\n");
      out.write("        <script src=\"js/bootstrap.min.js\"></script>        \n");
      out.write("        <script src=\"js/login.js\"></script>\n");
      out.write("        <script type=\"text/javascript\">\n");
      out.write("        $(function() {\n");
      out.write("            $(\"label[for=file]\").click(function(event) {\n");
      out.write("                event.preventDefault();\n");
      out.write("                $(\"#file\").click();\n");
      out.write("            });\n");
      out.write("        });\n");
      out.write("        </script>\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("        <nav class=\"navbar navbar-fixed-top\" style=\"background-color: rgba(0,0,0,0.2);\">\n");
      out.write("            <div class=\"container-fluid\">\n");
      out.write("                <div class=\"nav navbar-nav\">\n");
      out.write("                    <ul class=\"nav navbar-nav navbar-left\">\n");
      out.write("                        <li><a style=\"padding-left: 0px; color: white; background-color: transparent; font-size: 25px\"><img src=\"img/drive6.png\" width=\"30\" height=\"35\" style=\"padding-bottom:6px\">   BIENVENIDO A DRIVE USAC</a></li>                    \n");
      out.write("                    </ul>\n");
      out.write("                </div>\n");
      out.write("            </div>            \n");
      out.write("        </nav>\n");
      out.write("        <div class=\"container-fluid\" style=\"color: white;\">\n");
      out.write("            <div class=\"row content\">\n");
      out.write("                <div class=\"col-sm-3 sidenav hidden-xs\" style=\"text-align: center\">\n");
      out.write("                    <h1>DRIVE USAC</h1>\n");
      out.write("                        <table>\n");
      out.write("                            <tr>                \n");
      out.write("                                <form action=\"cargarArchivos\" method=\"POST\" enctype=\"multipart/form-data\">\n");
      out.write("                                    <div class=\"row\">\n");
      out.write("                                        <div class=\"col-lg-12\">\n");
      out.write("                                            <label for=\"file\">\n");
      out.write("                                                <div class=\"input-group\">\n");
      out.write("                                                    <span class=\"input-group-btn\">\n");
      out.write("                                                        <button class=\"btn btn-default\" type=\"button\">Cargar Archivo</button>\n");
      out.write("                                                    </span>\n");
      out.write("                                                        <input type=\"text\" class=\"form-control\" id=\"info\" readonly=\"\" style=\"background: #fff;\" placeholder=\"Ningun Archivo Seleccionado\">\n");
      out.write("                                                </div>                                                \n");
      out.write("                                            </label>\n");
      out.write("                                            <div class=\"input-group\">\n");
      out.write("                                                    <button type=\"submit\" class=\"btn btn-default\">Subir Archivo  <span class=\"glyphicon glyphicon-upload\"></span></button>                                                    \n");
      out.write("                                            </div>\n");
      out.write("                                        </div>\n");
      out.write("                                    </div>            \n");
      out.write("                                    <input type=\"file\" style=\"display: none;\" onchange=\"$('#info').val($(this).val().split(/[\\\\|/]/).pop());\" name=\"file\" id=\"file\">\n");
      out.write("                                </form>                                \n");
      out.write("                            </tr>                                \n");
      out.write("                        </table>                    \n");
      out.write("                </div> \n");
      out.write("                <div class=\"col-sm-5 sidenav hidden-xs\" style=\"text-align: center\">\n");
      out.write("                    <h1>Archivo</h1>                    \n");
      out.write("                </div> \n");
      out.write("                <div class=\"col-sm-4 sidenav hidden-xs\" style=\"text-align: center\">\n");
      out.write("                    <h1>Descargar Archivo</h1>\n");
      out.write("                    <form action=\"descargar\" method=\"POST\" enctype=\"multipart/form-data\">\n");
      out.write("                        <div class=\"form-group row\">\n");
      out.write("                          <div class=\"col-xs-12\">\n");
      out.write("                            <h2>Nombre Archivo</h2>                            \n");
      out.write("                          </div>\n");
      out.write("                        </div>\n");
      out.write("                        <ul class=\"nav nav-pills nav-stacked\">\n");
      out.write("                            <button type=\"submit\" class=\"btn btn-default\">Descargar Archivo <span class=\"glyphicon glyphicon-download\"></span></button>\n");
      out.write("                        </ul>                        \n");
      out.write("                    </form>                                \n");
      out.write("                </div> \n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("        <footer class=\"footer\" style=\"background-color: rgba(0,0,0,.2); text-align: center; position: fixed; bottom: 0px; width: 100%; height: 45px;\">\n");
      out.write("            <div class=\"container\" style=\"margin-top: 12px\">\n");
      out.write("                <span style=\"color: white;\">Copyright &copy; DRIVE USAC 2017</span>\n");
      out.write("            </div>\n");
      out.write("        </footer>\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
