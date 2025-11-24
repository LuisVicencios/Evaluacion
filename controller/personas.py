from model.personas import UsuarioModel, pacienteModel, DoctorModel
import re

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class UsuarioController:
    """
        Controlador del usuario.\n
        Métodos para registrar y mostrar usuarios, gestiona la insersion de codigo SQL,
        y que no falten datos necesarios.
    """
    def __init__(self, modelo: UsuarioModel):
        self.modelo = modelo

    def registrar_usuario(self,id: int, nombre_usuario: str, clave: str, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str) -> bool:
        """
            Recibe atributos de UsuarioModel, realiza registro en BD.\n
            returns Boolean
        """
        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo:
            print("[Error]: Datos faltantes para registro de usuario.")
    
            return False
        if patron.search(nombre_usuario) or patron.search(clave) or patron.search(nombre) or patron.search(apellido) or patron.search(email) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")

            return False
        
        return self.modelo.Crear_usuario(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)
        
    def listar_usuarios(self) -> list:
        """
            Muestra los usuarios registrados en BD.\
            returns Lista vacía si es que no hay usuarios, o lista de usuarios registrados.
        """
        usuarios = self.modelo.mostrar_usuarios()

        if len(usuarios) > 0:
            return [{ "id": u[0], "nombre_usuario": u[1], "clave": u[2], "nombre": u[3], "apellido": u[4], "fecha_nacimiento": u[5], "telefono": u[6], "email": u[7], "tipo": u[8] } for u in usuarios]
        
        else:
            return []

class PacienteController:
    def __init__(self, modelo: pacienteModel):
        self.modelo = modelo
        
    def registrar_paciente(self,id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: int) -> bool:
        
        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo or not comuna or not fecha_primera_visita:
            print("[Error]: Datos faltantes para registro de pacientes.")
            return False
        
        if patron.search(nombre_usuario) or patron.search(clave) or patron.search(nombre) or patron.search(apellido) or patron.search(email) or patron.search(tipo) or patron.search(comuna):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")

            return False
        
        return self.modelo.crear_paciente(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita)
        
    def listar_paciente(self) -> list:
        
        pacientes = self.modelo.mostrar_pacientes()

        if len(pacientes) > 0:
            return [{ "id": p[0], "nombre_usuario": p[1], "clave": p[2], "nombre": p[3], "apellido": p[4], "fecha_nacimiento": p[5], "telefono": p[6], "email": p[7], "tipo": p[8], "comuna": p[9], "fecha_primera_visita": p[10] } for p in pacientes]
        
class DoctorController:
    def __init__(self, modelo:DoctorModel):
        self.modelo = modelo
        
    def registrar_doctor(self, id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str,especialidad: str, horario_atencion: str, fecha_ingreso: int ) -> bool:
        
        if not id or not nombre_usuario or not clave or not nombre or not apellido or not fecha_nacimiento or not telefono or not email or not tipo or not especialidad or not horario_atencion or not fecha_ingreso:
            print("[ERROR]: Datos faltantes para registro de doctores")
            return False
        
        if patron.search(nombre_usuario) or patron.search(clave) or patron.search(nombre) or patron.search(apellido) or patron.search(email) or patron.search(tipo) or patron.search(especialidad) or patron.search(horario_atencion):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")

            return False
        return self.modelo.crear_Doctor(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso)
    def listar_doctores(self) -> list:
        doctores = self.modelo.mostrar_doctores()
        
        if len(doctores) > 0:
            return [{ "id": d[0], "nombre_usuario": d[1], "clave": d[2], "nombre": d[3], "apellido": d[4], "fecha_nacimiento": d[5], "telefono": d[6], "email": d[7], "tipo": d[8], "especialidad": d[9], "horario_atencion": d[10], "fecha_ingreso": d[11] } for d in doctores]
        
        