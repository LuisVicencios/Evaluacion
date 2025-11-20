import re
from model.personas import UsuarioModel
class UsuarioController:
    """
        Controlador del usuario.\n
        Métodos para registrar y mostrar usuarios.
    """
    def __init__(self, modelo: UsuarioModel):
        self.modelo = modelo

    def registrar_usuario(self,id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str) -> bool:
        """
            Recibe atributos de UsuarioModel, realiza registro en BD.\n
            returns Boolean
        """
        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo:
            print("[Error]: Datos faltantes para registro de usuario.")
            return False
        
        return self.modelo.crear(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
        
    def listar_usuarios(self) -> list:
        """
            Muestra los usuarios registrados en BD.\
            returns Lista vacía si es que no hay usuarios, o lista de usuarios registrados.
        """
        usuarios = self.modelo.mostrar_todos()

        if len(usuarios) > 0:
            return [{ "id": u[0], "nombre_usuario": u[1], "clave": u[2], "nombre": u[3], "apellido": u[4], "fecha_nacimiento": u[5], "telefono": u[6], "email": u[7], "tipo": u[8] } for u in usuarios]
        
        else:
            return []