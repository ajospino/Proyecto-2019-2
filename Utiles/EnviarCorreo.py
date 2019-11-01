import os
import smtplib
import imghdr
from Constantes import *
from email.message import EmailMessage
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

def enviarCorreo(tipo,correo, pathArchivo):
    if(tipo == "FACTURA" or tipo =="NOTIF"):
        path = pathArchivo
    elif(tipo == "CODIGO"):
        path = "Codigos/TusCodigos.pdf"
    else:
        return
    
    EMAIL_ADDRESS = EMAIL
    EMAIL_PASSWORD = CONTRASEÑA
    msg = EmailMessage()
    msg['Subject'] = ASUNTO
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = correo

    msg.add_alternative(html, subtype = 'html')
    
    archivo = path
    with open(archivo, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'aplication', subtype ='octect-stream' , filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)