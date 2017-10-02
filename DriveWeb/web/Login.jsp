<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html style="min-height: 100%; position: relative;">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>DRIVE USAC</title>
        <link rel="shortcut icon" href="img/drive6.png"/>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/login.css" rel="stylesheet">
        <link href="fonts/font-awesome.min.css" rel="stylesheet">
        <link href="css/estilos.ccs" rel="stylesheet">          
    </head>    
    <body style="margin:0; margin-bottom: 40px;">
        <link rel="stylesheet" href="//netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">        
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-md-offset-3">                    
                    <div class="panel panel-login">          
                        <div class="panel-body">                            
                            <div class="col-md-12">                        
                                <div class="col-lg-12">
                                    <h3 style="color: #2D3B55; text-align: center"><p class="glyphicon glyphicon-user"></p> BIENVENIDO A DRIVE USAC</h3> 
                                </div>                        
                            </div>
                            <div class="row" style="color: #2D3B55;">                                
                                <div class="col-lg-12">
                                    <%--Formulario para Iniciar Sesión--%>
                                    <form id="login-form" action="login" method="POST" role="form" style="display: block;">
                                        <h2><p class="glyphicon glyphicon-log-in"></p>  INICIAR SESIÓN</h2>
                                        <div class="form-group">
                                            <input type="text" name="usuario" tabindex="1" class="form-control" placeholder="Nombre de Usuario" required="">
                                        </div>
                                        <div class="form-group">
                                            <input type="password" name="contrasena" tabindex="2" class="form-control" placeholder="Contraseña" required="">
                                        </div>
                                        <div class="col-xs-6 form-group pull-left checkbox">
                                            <input id="checkbox1" type="checkbox" name="recordar">
                                            <label for="checkbox1">Récuerdame</label>   
                                        </div>
                                        <div class="col-xs-6 form-group pull-right">     
                                            <input type="submit" name="btnLogin" tabindex="4" class="form-control btn btn-login" value="Iniciar Sesión">
                                        </div>
                                    </form>
                                    <%--Formulario para Registro de Usuarios--%>
                                    <form id="register-form" action="registrar" method="POST" role="form" style="display: none;">
                                        <h2><p class="glyphicon glyphicon-log-out"></p>  REGISTRO DE USUARIOS</h2>
                                        <div class="form-group">
                                            <input type="text" name="usuario" tabindex="1" class="form-control" placeholder="Nombre de Usuario" required="">
                                        </div>
                                        <div class="form-group">
                                            <input type="password" name="contrasena" tabindex="2" class="form-control" placeholder="Contraseña" required="">
                                        </div>
                                        <div class="form-group">
                                            <div class="row">
                                                <div class="col-sm-6 col-sm-offset-3">
                                                    <input type="submit" name="register-submit" id="myBtn" tabindex="4" class="form-control btn btn-register" value="Registrar">
                                                </div>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <div class="panel-heading">
                            <div class="row">
                                <div class="col-xs-6 tabs">
                                    <a href="#" class="active" id="login-form-link"><div class="login">INICIAR SESIÓN</div></a>                                        
                                </div>
                                <div class="col-xs-6 tabs">
                                    <a href="#" id="register-form-link"><div class="register">REGISTRO DE USUARIOS</div></a>                                        
                                </div>
                            </div>                                
                        </div>                        
                    </div>                        
                </div>                    
            </div>
            <div class="row" style="margin-top:0px">
                <div class="col-md-6 col-md-offset-3">                    
                    <div class="col-lg-12">
                        <h3 style="color: #2D3B55; text-align: center">
                        <%
                            if(null!= request.getAttribute("errorMessage"))
                            {
                            out.print(request.getAttribute("errorMessage"));
                            }
                        %></h3>
                    </div>
                </div>
            </div>
            <div class="col-sm-4 text-center" style="color: #2D3B55;">                                
                <div id="myModal" class="modal">
                    <div class="modal-content">
                        <span class="close">&times;</span>
                        <p>REGISTRO DE USUARIOS</p>
                        <hr>
                        <div class="row" style="text-align: center;">                                
                            <div class="col-md-2" style="align-items: center">
                                <img class="img-responsive img-left" src="img/drive6.png" width="100" height="125">
                            </div>
                            <div class="col-md-10" style="text-align: center; margin-top: 15px">
                                <p style="font-size: 25px;">Usuario Registrado Correctamente!!</p>
                            </div>
                        </div>
                    </div>
                </div>   
            </div>
        </div>        
        <footer class="footer" style="background-color: rgba(0,0,0,.2); text-align: center; position: fixed; bottom: 0px; width: 100%; height: 45px;">
            <div class="container" style="margin-top: 12px">
                <span style="color: white;">Copyright &copy; DRIVE USAC 2017</span>
            </div>
        </footer> 
        <script src="js/jquery.js"></script>
        <script src="js/jquery1.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>        
        <script src="js/login.js"></script>  
    </body> 
</html>