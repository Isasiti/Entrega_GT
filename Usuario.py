class Usuario:
    def __init__(self):
        self.usuarios = {}
    def crear_nuevo_usuario(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios:
        #este print si es medio necesario#
            print("Error: El usuario ya existe.")
        else:
            self.usuarios[nombre_usuario] = contraseña
        #Como se hara esto en tkinter?#
            print(f"Usuario {nombre_usuario} creado correctamente.")
    def validar_credenciales(self, nombre_usuario, contraseña):
        if nombre_usuario in self.usuarios and self.usuarios[nombre_usuario] == contraseña:
            return True
        else:
            return False