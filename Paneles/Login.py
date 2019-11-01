import sys
from Utiles.Verificar import verificar
from UI.UI_login import *
from Constantes import ADMINISTRADOR
class Login():
    
    def __init__(self):
        self.UIl = UI_login()
        self.usuario = None
        self.contrasena = None
        self.tipoCuenta = None
        self.UIl.sigValidar.connect(self.validar)
    #-----------------FUNCIONES-----------------
    def validar(self):
        self.usuario = self.UIl.getUsuario()
        self.contrasena = self.UIl.getContrasena()
        entrar, Tipo_cuenta = verificar(self.usuario, self.contrasena)
        if(entrar):
            self.UIl.abrirInventario(Tipo_cuenta)
        else:
            self.UIl.throwMsgErrorProceso()
            
    def show(self):
        self.UIl.show()
    def close(self):
        self.UIl.close()