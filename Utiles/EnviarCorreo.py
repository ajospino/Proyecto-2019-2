import Dependencias.os
import Dependencias.imghdr
from Dependencias.email.message import EmailMessage
import Dependencias.smtplib, Dependencias.getpass
from Dependencias.email.mime.multipart import MIMEMultipart
from Dependencias.email.mime.text import MIMEText
from Dependencias.email.mime.base import MIMEBase
from Dependencias.email.encoders import encode_base64
from Utiles.HtmlTemplate import prepararCorreo
from Utiles.Factura import fecha
from Constantes import EMAIL,CONTRASEÑA,ASUNTO 

def enviarCorreo(tipo,correo, pathArchivo, usuario):
    if(tipo == "FACTURA" ):
        html = prepararCorreo("Tu factura es",fecha())
        path = pathArchivo
    elif(tipo == "CODIGO"):
        html = prepararCorreo("Tus codigos son:",fecha())
        path = "Codigos/TusCodigos.pdf"
    elif( tipo =="NOTIF_VENTA"):
        html = prepararCorreo("Se ha realizado una venta:",fecha())
        path = None
    elif( tipo =="NOTIF_COMPRA"):
        html = prepararCorreo("Se ha realizado una compra:",fecha())
        path = None
    elif( tipo =="NOTIF_INGRESO"):
        html = prepararCorreo( usuario+" Ha ingresado al sistema",fecha())
        path = None
    else:
        return
    
    EMAIL_ADDRESS = EMAIL
    EMAIL_PASSWORD = CONTRASEÑA
    msg = EmailMessage()
    msg['Subject'] = ASUNTO
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = correo

    msg.add_alternative(html, subtype = 'html')
    
    if (path != None):
        
        archivo = path
        with open(archivo, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype = 'aplication', subtype ='octect-stream' , filename = file_name)
    
    with Dependencias.smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)