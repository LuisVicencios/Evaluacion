from datetime import date
import getpass
import sys

from config.db_config import ConexionOracle, validar_tablas
from model.personas import UsuarioModel, pacienteModel, DoctorModel
from controller.personas import UsuarioController
from controller.personas import PacienteController
from controller.personas import DoctorController

def conectarBD():
    """
        Realiza conexión a BD utilizando funcion predefinida.
    """
    db = ConexionOracle("system", "vicencio0195", "localhost:1521/xe")
    db.conectar()
    validar_tablas(db)
    return db


def iniciar_sesion(usuario_ctrl):
    """
    Busca el usuario en la BD y verifica la clave hasheada mediante bcrypt.
    
    """
    
    print("\n--- INICIO DE SESION ---")
    nombre_usuario = input("Usuario: ")
  
    if nombre_usuario.lower() == 'q':
        return 'QUIT'
        
   
    clave_ingresada = getpass.getpass("Clave: ") 
    
    try:
        usuario_data = usuario_ctrl.modelo.buscar_usuario_login(nombre_usuario) 
    except AttributeError:
        
        print("[ERROR CRITICO]: El metodo 'buscar_usuario_login' no esta definido en UsuarioModel.")
        return None
        

    if not usuario_data:
        print("[ERROR]: Credenciales o usuario no encontrado.")
        return None
        
    clave_bd_hash = usuario_data[2] 
    tipo_usuario = usuario_data[8]
    

    if usuario_ctrl.validar_clave(clave_ingresada, clave_bd_hash):
        print("\n Ingreso correcto.")
        return {
            "id": usuario_data[0],
            "nombre_usuario": usuario_data[1],
            "tipo": tipo_usuario.upper()
        }
    else:
        print("\n Credenciales incorrectas.")
        return None

def mostrar_menu_por_rol(tipo_usuario: str):

    """Muestra el menu seleccionado basado en el tipo"""

    tipo = tipo_usuario.upper()

    if tipo == "USUARIO":
        print("\n--- MENU DE ADMINISTRACIÓN ---")
        print("1. Listar Usuarios")
    elif tipo == "PACIENTE":
        print("\n--- MENU DE PACIENTE ---")
        print("1. Ver mi Información")
        print("2. Registrar una Cita")
    elif tipo == "DOCTOR":
        print("\n--- MENU DE DOCTOR ---")
        print("1. Listar Pacientes")
        print("2. Gestionar Agenda")
    else:
        print(f"\n[ERROR] Tipo de rol '{tipo}' no reconocido.")
        return
    print("0. Cerrar Sesion")
    opcion = input("Seleccione una opción: ")
    print(f"\n[INFO] Opción '{opcion}' seleccionada. Volviendo al menu principal.")

def registrar_usuario_completo(usuario_ctrl: UsuarioController, paciente_ctrl: PacienteController, doctor_ctrl: DoctorController):
    """
    Solicita todos los datos esenciales por teclado y redirige la llamada
    al controlador específico (Usuario, Paciente o Doctor).
    """

    print(f"\n--- INICIO DE REGISTRO ---")

    try:
        # --- Datos Genéricos (Comunes a todos) ---
        id_user = int(input("1. ID del Usuario: "))
        nombre_usuario = input("2. Nombre de Usuario: ")
        clave = getpass.getpass("3. Clave: ")
        nombre = input("4. Nombre: ")
        apellido = input("5. Apellido: ")
        fecha_nacimiento = date.fromisoformat(input("6. Fecha Nac. (YYYY-MM-DD): "))
        telefono = int(input("7. Teléfono: "))
        email = input("8. Email: ")
        
        tipo = input("9. Tipo (Paciente/Doctor/Usuario): ").upper() 
        
        if tipo == "PACIENTE":
        
            comuna = input("10. Comuna: ")
            fecha_primera_visita = date.fromisoformat(input("11. Fecha 1ra Visita (YYYY-MM-DD): "))

            return paciente_ctrl.registrar_paciente(id_user, nombre_usuario, clave, nombre, apellido, fecha_nacimiento,telefono, email, tipo, comuna, fecha_primera_visita)

        elif tipo == "DOCTOR":

            especialidad = input("10. Especialidad: ")
            horario_atencion = input("11. Horario Atención: ")
            fecha_ingreso = date.fromisoformat(input("12. Fecha Ingreso (YYYY-MM-DD): "))


            return doctor_ctrl.registrar_doctor(id_user, nombre_usuario, clave, nombre, apellido, fecha_nacimiento,telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso)

        elif tipo == "USUARIO" or tipo == "ADMIN":
            
             return usuario_ctrl.registrar_usuario(id_user, nombre_usuario, clave, nombre, apellido, fecha_nacimiento,telefono, email, tipo )
        
        else:
            print("[ERROR]: Tipo de usuario ingresado no es válido.")
            return False

    except ValueError:
        print("[ERROR]: Error en el formato de datos (número o fecha).")
        return False
    except Exception as e:
        # Atrapa errores como ID duplicado o fallo en la BD
        print(f"[ERROR]: Falló el registro: {e}")
        return False

def main():
    print("--- BIENVENIDO A CLINICA MEDIPLUS ---")

    
    try:
        db = conectarBD()
    except Exception as e:
        print(f"\n[ERROR FATAL]: Fallo al conectar. {e}")
        sys.exit(1)
    

    usuario_ctrl = UsuarioController(UsuarioModel)
    paciente_ctrl = PacienteController(pacienteModel)
    doctor_ctrl = DoctorController(DoctorModel)
   
    input("\nPresione Enter para registrar un USUARIO de prueba (Administrador)...")

    registro_exitoso = registrar_usuario_completo(usuario_ctrl, "Usuario", usuario_ctrl)

    if registro_exitoso:
        print(" Usuario registrado con éxito. Clave hasheada.")
    else:
        print(" Registro fallido (ID duplicado, validación o error de formato).")

    input("\nPresione Enter para probar el inicio de sesión...")

    usuario_logeado = None

    while usuario_logeado is None:
        resultado_login = iniciar_sesion(usuario_ctrl)
        if resultado_login == 'QUIT':
            db.desconectar()

            sys.exit()

        if resultado_login:
            usuario_logeado = resultado_login
        else:
            print("Intente de nuevo...")

    
    print(f"\n*** ACCESO EXITOSO PARA EL ROL: {usuario_logeado['tipo']} ***")
    mostrar_menu_por_rol(usuario_logeado['tipo'])

    db.desconectar()

    print("Aplicación finalizada.")

if __name__ == "__main__":
    main()