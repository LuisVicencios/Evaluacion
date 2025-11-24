class UsuariosView:
    @staticmethod
    def mostrar_usuarios(Usuarios: list) -> None:
           
        if len(Usuarios) > 0:
            print("\n- Lista de Usuarios -")

            for u in Usuarios:
                print(f"--- id: {u['id']} | nombre_usuario: {u['nombre_usuario']} | clave: {u['clave']} | nombre: {u['nombre']} | apellido: {u['apellido']} | fecha_nacimiento: {u['fecha_nacimiento']} | telefono: {u['email']} | tipo: {u['tipo']}")
        else:
            print("[ERROR]: Sin Usuarios registradas")

class PacientesView:
    @staticmethod
    def mostrar_paciente(Pacientes: list) -> None:
       
        if len(Pacientes) > 0:
            print("\n- Lista de Pacientes -")

            for p in Pacientes:
                print(f"--- id: {p['id']} | nombre_usuario: {p['nombre_usuario']} | clave: {p['clave']} | nombre: {p['nombre']} | apellido: {p['apellido']} | fecha_nacimiento: {p['fecha_nacimiento']} | telefono: {p['email']} | tipo: {p['tipo']} | comuna: {p['comuna']} | fecha_primera_visita: {p['fecha_primera_visita']}")
        else:
            print("[ERROR]: Sin Pacientes registrados")

class DoctoresView:
    @staticmethod
    def mostrar_doctores(Doctores: list) -> None:
           
        if len(Doctores) > 0:
            print("\n- Lista de Doctores -")

            for d in Doctores:
                print(f"--- id: {d['id']} | nombre_usuario: {d['nombre_usuario']} | clave: {d['clave']} | nombre: {d['nombre']} | apellido: {d['apellido']} | fecha_nacimiento: {d['fecha_nacimiento']} | telefono: {d['email']} | tipo: {d['tipo']} | especialidad: {d['especialidad']} | horario_atencion: {d['horario_atencion']} | fecha_ingreso: {d['fecha_ingreso']}")
        else:
            print("[ERROR]: Sin Doctores registradas")


