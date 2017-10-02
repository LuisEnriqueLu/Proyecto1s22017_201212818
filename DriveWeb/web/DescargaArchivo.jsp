<%@page import="proceso.conexion"%>
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
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>        
        <script src="js/login.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-fixed-top" style="background-color: rgba(0,0,0,0.2);">
            <div class="container-fluid">
                <div class="nav navbar-nav">
                    <ul class="nav navbar-nav navbar-left">
                        <li><a style="padding-left: 0px; color: white; background-color: transparent; font-size: 25px"><img src="img/drive6.png" width="30" height="35" style="padding-bottom:6px">   BIENVENIDO A DRIVE USAC</a></li>                    
                    </ul>
                </div>
            </div>            
        </nav>
        <div class="container-fluid" style="color: white;">
            <div class="row content">
                <div class="col-sm-2 sidenav hidden-xs" style="text-align: center">
                    <h1>DRIVE USAC</h1>
                    <form action="descargar" method="POST" enctype="multipart/form-data">
                        <div class="form-group row">
                          <div class="col-xs-12">
                            <h2>Nombre Archivo</h2>                            
                          </div>
                        </div>
                        <ul class="nav nav-pills nav-stacked">
                            <button type="submit" class="btn btn-default">Descargar Archivo <span class="glyphicon glyphicon-download"></span></button>
                        </ul>                        
                    </form>                                      
                </div> 
            </div>
        </div>        
        <footer class="footer" style="background-color: rgba(0,0,0,.2); text-align: center; position: fixed; bottom: 0px; width: 100%; height: 45px;">
            <div class="container" style="margin-top: 12px">
                <span style="color: white;">Copyright &copy; DRIVE USAC 2017</span>
            </div>
        </footer>                
    </body>
</html>
