from config.db_config import ConexionOracle

class UsuarioModel :
    def __init__(self,id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str, conexion: ConexionOracle):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.tipo = tipo
        self.db = conexion
        
    def Crear_usuario(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) -> bool:
        """
            Guarda el item actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Usuarios where id = :1"
            cursor.execute(consulta_validacion,(id,))
            
            if len(cursor.fetchall()) >0:
                print(f"[ERROR]: Ya existe este usuario ID: {id} ")
                
                return False
            else:
                consulta_insert = "insert into LV_Usuarios (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo) values (:1, :2, :3, :4, :5, :6, :7, :8, :9)"
                cursor.execute(consulta_insert, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo))
                self.db.connection.commit()
                print(f"[INFO]: {nombre_usuario} creado correctamente")
                
                return True
        
        except Exception as e:
            print(f"[ERROR]: No se puede crear usuario {nombre_usuario} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_usuarios(self,id  :int, nombre_usuario: str, *datos: tuple) -> bool:
        """
            Edita el item indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - nombre_usuario : nombre del item a editar
            - datos : (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo)

            returns Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Usuarios where id = :1"
            cursor.execute(consulta_validacion, (id))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Usuarios set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8 where id = :9"
                    cursor.execute(consulta_update, (id, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos [7], id,))
                    self.db.connection.commit()
                    print("[INFO]: Usuario editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")
                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla Usuarios")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_usuarios(self) -> list:
        """
            Muestra los usuarios actuales en la BD.

            returna una Lista con todos los usuarios registrados
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta = "select * from LV_Usuarios "
            cursor.execute(consulta)
            datos = cursor.fetchall()
            
            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: sin datos encontrados para Usuarios")
                
                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener usuarios desde BD -> {e}")
            
            return []
        
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_usuario(self, id: int) -> bool:
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - id : item a eliminar

            return Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Usuarios Where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Usuarios where id = :1"
                cursor.execute(consulta_delete, (id))
                self.db.connection.commit()
                print(f"[INFO]: ID {id} eliminado correctamente")
                
                return True
            else:
                print(f"[ERROR]: {id} no existe en la tabla Usuarios")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e }")
            
            return False
        finally:
            if cursor:
                cursor.close()
        
class pacienteModel(UsuarioModel):
    def __init__(self,id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: int, conexion: ConexionOracle):
            super().__init__(id, nombre_usuario ,clave , nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
            self.comuna = comuna
            self.fecha_primera_visita = fecha_primera_visita

    def crear_paciente(self, id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: str, telefono: int, email: str, tipo: str, comuna: str, fecha_primera_visita: int) -> bool:
        
        cursor = self.db.obtener_cursor()

        try:
            validacion = "select * from LV_Pacientes where id = :1"
            cursor.execute(validacion, (id,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe esta id de paciente {id} ")
                
                return False
            else:
                consulta_insert = "insert into LV_Pacientes (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
                cursor.execute(consulta_insert, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita))
                self.db.connection.commit()
                print(f"[INFO]: paciente {nombre_usuario} creado correctamente id {id}")
                
                return True
        
        except Exception as e:
            print(f"[ERROR]: No se pudo registrar paciente {nombre_usuario} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_paciente(self,id: int, *datos: tuple) -> bool:
    
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Pacientes where id= :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Pacientes set  nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8, comuna = :9, fecha_primera_visita = :10 where id = :11"
                    cursor.execute(consulta_update, (id, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10],  id,))
                    self.db.connection.commit()
                    print(f"[INFO]: {id} editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")
                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla Pacientes")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_pacientes(self) -> list:
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta = "select id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, comuna, fecha_primera_visita from LV_Pacientes "
            cursor.execute(consulta)
            datos = cursor.fetchall()
            
            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: sin datos encontrados para Pacientes")
                
                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener Pacientes desde BD -> {e}")
            
            return []
        
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_pacientes(self,id: int) -> bool:
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Pacientes Where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Pacientes where id = :1"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")
                
                return True
            else:
                print(f"[ERROR]: {id} no existe e la tabla Pacientes")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e }")
            
            return False
        finally:
            if cursor:
                cursor.close()

class DoctorModel(UsuarioModel):
    def __init__(self,id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento:int , telefono: int, email: str, tipo: str, especialidad: str, horario_atencion: str, fecha_ingreso: int, conexion: ConexionOracle):
            super().__init__(id, nombre_usuario ,clave , nombre, apellido, fecha_nacimiento, telefono, email, tipo, conexion)
            self.especialidad = especialidad
            self.horario_atencion = horario_atencion
            self.fecha_ingreso = fecha_ingreso

    def crear_Doctor(self, id: int, nombre_usuario: str, clave: int, nombre: str, apellido: str, fecha_nacimiento: int, telefono: int, email: str, tipo: str,especialidad: str, horario_atencion: str, fecha_ingreso: int ) -> bool:
        
        cursor = self.db.obtener_cursor()

        try:
            validacion = "select * from LV_Doctores where id = :1"
            cursor.execute(validacion, (id,))
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe esta id para doctor {id} ")
                
                return False
            else:
                consulta_insert = "insert into LV_Doctores (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
                cursor.execute(consulta_insert, (id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso))
                self.db.connection.commit()
                print(f"[INFO]: Doctor {nombre_usuario} creado correctamente")
                
                return True
        
        except Exception as e:
            print(f"[ERROR]: No se pudo registrar Doctor {id} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_Doctores(self,id :int, *datos: tuple) -> bool:
       
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Doctores where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Doctores set nombre_usuario = :1, clave = :2, nombre = :3, apellido = :4, fecha_nacimiento = :5, telefono = :6, email = :7, tipo = :8, especialidad = :9, horario_atencion = :10, fecha_ingreso = :11 where id = :12"
                    cursor.execute(consulta_update, (id, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11], id,))
                    self.db.connection.commit()
                    print(f"[INFO]: {id} editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")
                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla LV_Doctores")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_doctores(self) -> list:
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta = "select  id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, telefono, email, tipo, especialidad, horario_atencion, fecha_ingreso from LV_Doctores "
            cursor.execute(consulta)
            datos = cursor.fetchall()
            
            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: sin datos encontrados para Doctores")
                
                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener Doctores desde BD -> {e}")
            
            return []
        
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_usuario(self,id: int) -> bool:
       
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Doctores Where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Doctores where id = :1"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")
                
                return True
            else:
                print(f"[ERROR]: {id} no existe en la tabla LV_Doctores")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e }")
            
            return False
        finally:
            if cursor:
                cursor.close()