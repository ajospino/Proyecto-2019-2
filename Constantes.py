import random

#Variables globales
ICONO = 'Imagenes/Logo.png'
ADMINISTRADOR = 'Administrador/a'
EMPLEADO = 'Empleado/a'
TIPO_CUENTA = [ADMINISTRADOR, EMPLEADO]

#Clase enviar correo 
EMAIL = 'sadv.system@gmail.com'
CONTRASEÑA = 'CAMO@@134'
ASUNTO = 'Tu lista de codigos de DIEM '
CODIGOS = 'Utiles/Tus-Codigos.pdf'

IMAGEN_RANDOM = 'Imagenes/'+ str(random.randrange(1, 15)) + '.jpg'

html = """\
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body style="background-color: #222831 ">

    <!--Copia desde aquí-->
    <table style="max-width: 600px; padding: 10px; margin:0 auto; border-collapse: collapse;">
        <tr>
            <td style="background-color: #222831; text-align: left; padding: 0">
            </td>
        </tr>

        <div style="text-align: center">
            <a href="link">
            
            <img src="https://i.postimg.cc/gcgjkHCw/DIEM-T.png" align="center"></a>
            </div>

        <tr>
            <td style="background-color: #222831">
                <div style="color: #222831; margin: 4% 10% 2%; text-align: justify;font-family: sans-serif">
                    <h1 align="center" style="color: #ff6600; margin: 0 0 7px">Tu Factura</h1>
                    <p align="center" style="color: #ecf0f1; margin: 2px; font-size: 15px">
                        Listo, Ya tienes tus codigos.<br>
                        Guarda este correo  y tu facttura<br>
                        por si pierdes tus codigos o pasa algo con tu cuenta</p>
                        <p align="center" style="color: #ecf0f1; margin: 5px; font-size: px">
                            <b>codigos</b></p>
                    </ul>
                    <div style="width: 100%;margin:10px 0; display: inline-block;text-align: center">
            
                    </div>
                    <div style="width: 100%; text-align: center">
                        <a style="text-decoration: none; margin: 10px; border-radius: 5px; padding: 11px 23px; color: white; background-color: #3498db" href="http://diem.com.co/">Ir a la página</a>	
                    </div>
                    <p style="color: #b3b3b3; font-size: 12px; text-align: center;margin: 30px 0 0">DIEM.COM.CO</p>
                </div>
            </td>
        </tr>
    </table>
    <!--hasta aquí-->

    </body>
    </html>



    """ 



    