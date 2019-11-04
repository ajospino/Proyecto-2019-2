def prepararCorreo(v1,v2):
    html = """\
    <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title></title>
        </head>
        <body style="background-color: #000000 ">

        <!--Copia desde aquí-->
        <table style="max-width: 600px; padding: 10px; margin:0 auto; border-collapse: collapse;">
            <tr>
                <td style="background-color: #000000; text-align: left; padding: 0">
                </td>
            </tr>

            <div style="text-align: center">
                <a href="link">
                
                <img src="https://i.imgur.com/hjH441i.png" align="center"></a>
                </div>

            <tr>
                <td style="background-color: #222831">
                    <div style="color: #222831; margin: 4% 10% 2%; text-align: justify;font-family: sans-serif">
                        <h1 align="center" style="color: #7c0a02; margin: 0 0 7px">%s</h1>
                        <p align="center" style="color: #3c4245; margin: 2px; font-size: 15px">
                            FECHA %s</p>
                            <p align="center" style="color: #ecf0f1; margin: 5px; font-size: px">
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
    return html