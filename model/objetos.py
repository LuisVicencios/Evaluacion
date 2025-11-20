from config.db_config import ConexionOracle

class InsumosModel :
    def __init__(self,id: int, nombre: str, tipo: str, stock: int, conexion: ConexionOracle):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.db = conexion
        
    def agregar_producto(self, id, nombre, tipo, stock) -> bool:
        """
            Guarda el producto actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Insumos where id = :1"
            cursor.execute(consulta_validacion,(id))
            
            if len(cursor.fetchall()) >0:
                print(f"[ERROR]: Ya existe esta ID: {id} ")
                
                return False
            else:
                consulta_insert = "insert into LV_Insumos (id, nombre, tipo, stock) values (:1, :2, :3, :4)"
                cursor.execute(consulta_insert, (id, nombre, tipo, stock))
                self.db.connection.commit()
                print(f"[INFO]: {nombre} agregado correctamente")
                
                return True
        
        except Exception as e:
            print(f"[ERROR]: No se puede agregar insumo {nombre} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close()
    
    def editar_insumos(self,id: int, *datos: tuple) -> bool:
        """
            Edita el insumo indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - id : nombre del item a editar
            - datos : (nombre, tipo, stock)

            returns Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Insumos where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Insumos set id = :1, nombre = :2, tipo = :3, stock = :4"
                    cursor.execute(consulta_update, (id, datos[0], datos[1], datos[2], datos[3], id, ))
                    self.db.connection.commit()
                    print(f"[INFO]: ID {id}, editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")
                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla LV_Insumos")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_usuarios(self)-> list :
        """
            Muestra los Insumos actuales en la BD.

            returns List
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta = "select id, nombre, tipo, stock from LV_Insumos "
            cursor.execute(consulta)
            datos = cursor.fetchall()
            
            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: sin datos encontrados para Insumos")
                
                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener Insumos desde BD -> {e}")
            
            return []
        
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_usuario(self, id: int) -> bool :
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - id : item a eliminar

            return Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Insumos Where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Insumos where nombre = :5"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")
                
                return True
            else:
                print(f"[ERROR]: {id} no existe e la tabla Insumos")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e }")
            
            return False
        finally:
            if cursor:
                cursor.close()

class AgendaModel():
    def __init__(self,id :int, fecha_consulta: str, estado: str, conexion: ConexionOracle):
        self.id = id
        self.fecha_consulta = fecha_consulta
        self.estado = estado
        self.db = conexion
    
    def Crear_Agenda (self, id: int, fecha_consulta: str, estado: str) -> bool:
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Agenda where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un item en agenda con id {id}")
                
                return False
            else:
                consulta_insert = "insert into LV_Agenda (id, fecha_consulta, estado) values (:1, :2, :3)"
                cursor.exeute(consulta_insert( id, fecha_consulta, estado))
                self.db.connection.commit()
                print(f"[INFO]: {id} guardado correctamente")
                
                return True
        except Exception as e:
            print(f"[ERROR]: error al guardar {id} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close() 
    
    def editar_agenda(self, id: int, *datos: tuple) -> bool:
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Agenda where id = :1"
            cursor.execute(consulta_validacion, (id,))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Agenda set id = :1, fecha_consulta = :2, estado = :3 where id = :1"           
                    cursor.execute(consulta_update,( id, datos[0], datos[1], datos[2], id ,))
                    self.db.connection.commit()
                    print(f"[INFO]: {id} editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")
                
                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla LV_Agenda")    
                
                return False
        except Exception as e:
            print(f"[ERROR]: error al editar {id} -> {e}")
            
            return False
        finally:
            if cursor:
                cursor.close()
                
    def mostrar_agenda(self) -> list:
        cursor = self.db.obtener_cusror()
        
        try:
            consulta = "select * from LV_Agenda"
            cursor.execute(consulta)
            datos = cursor.fetchall()
            
            if len(datos) > 0:
                return datos
            else:
                print("[ERROR]: sin datos encontrados para LV_Agenda")
                
                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")
            
            return []
        finally:
            if cursor:
                cursor.close()
                
    def eliminar_Agenda(self, id: int) -> bool:
        
        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from LV_Agenda where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Agenda where id = :1"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {id} no existe en la tabla de LV_Agenda.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()           
                
class ConsultasModel():
    def __init__(self,id: int, fecha: str, comentarios: str, conexion: ConexionOracle ):
        self.id = id
        self.fecha = fecha
        self.comentarios = comentarios
        self.db = conexion
        
    def crear_consulta(self, id, fecha, comentarios) -> bool:
        
        cursor = cursor.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con la id {id}")

                return False
            else:
                consulta_insert = "insert into LV_Consultas (id, fecha, comentarios) values (:1, :2, :3)"
                cursor.execute(consulta_insert, (id, fecha, comentarios))
                self.db.connection.commit()
                print(f"[INFO]: {id} guardado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def editar_consultas(self, id: int, *datos: tuple) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from LV_Consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Consultas set id = :1, fecha = :2, comentarios = :3 where id = :1 "
                    cursor.execute(consulta_update, (id, datos[0], datos[1], datos[2], id,))
                    self.db.connection.commit()
                    print(f"[INFO]: {id} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")

                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla de LV_Consultas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_consultas(self) -> list:
       
        cursor = self.db.obtener_cursor()

        try:
            consulta = "select * from LV_consultas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para LV_Consultas.")

                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_Consulta(self, id: int) -> bool:
      
        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from LV_Consultas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Consultas where id = :1"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {id} no existe en la tabla de LV_Consultas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

                
class RecetasModel():
    def __init__(self, id: int, descripcion: str, conexion: ConexionOracle):
        self.id = id
        self.descripcion = descripcion
        self.db = conexion
        
    def crear_Receta(self, id, descripcion) -> bool:
        
        cursor = cursor.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from LV_Recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                print(f"[ERROR]: Ya existe un ítem con la id {id}")

                return False
            else:
                consulta_insert = "insert into LV_Recetas (id, descripcion) values (:1, :2)"
                cursor.execute(consulta_insert, (id, descripcion))
                self.db.connection.commit()
                print(f"[INFO]: {id} guardado correctamente")

                return True
        except Exception as e:
            print(f"[ERROR]: Error al guardar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def editar_consultas(self, id: int, *datos: tuple) -> bool:

        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from LV_Recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update LV_Recetas set id = :1, descripcion = :2 where id = :1 "
                    cursor.execute(consulta_update, (id, datos[0], datos[1], id,))
                    self.db.connection.commit()
                    print(f"[INFO]: {id} editado correctamente")

                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {id}")

                    return False
            else:
                print(f"[ERROR]: {id} no existe en la tabla de LV_Recetas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()

    def mostrar_consultas(self) -> list:
       
        cursor = self.db.obtener_cursor()

        try:
            consulta = "select * from LV_Recetas"
            cursor.execute(consulta)
            datos = cursor.fetchall()

            if len(datos) > 0:
                return datos
            else:
                print("[INFO]: Sin datos encontrados para LV_Recetas.")

                return []
        except Exception as e:
            print(f"[ERROR]: Error al obtener items desde BD -> {e}")

            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_Consulta(self, id: int) -> bool:
      
        cursor = self.db.obtener_cursor()

        try:
            consulta_validacion = "select * from LV_Recetas where id = :1"
            cursor.execute(consulta_validacion, (id,))

            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from LV_Recetas where id = :1"
                cursor.execute(consulta_delete, (id,))
                self.db.connection.commit()
                print(f"[INFO]: {id} eliminado correctamente")

                return True
            else:
                print(f"[ERROR]: {id} no existe en la tabla de LV_Recetas.")

                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {id} -> {e}")

            return False
        finally:
            if cursor:
                cursor.close()
        