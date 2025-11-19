from config.db_config import ConexionOracle

class InsumosModel :
    def __init__(self,id: int, nombre: str, tipo: str, stock: int, conexion: ConexionOracle):
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.db = conexion
        
    def agregar_producto(self, id, nombre, tipo, stock) -> bool:
        """
            Guarda el item actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from Insumos where nombre = :1"
            cursor.execute(consulta_validacion,(nombre,))
            
            if len(cursor.fetchall()) >0:
                print(f"[ERROR]: Ya existe este nombre de Insumo {nombre} ")
                
                return False
            else:
                consulta_insert = "insert into Insumos (id, nombre, tipo, stock) values (:1, :2, :3, :4)"
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
    
    def editar_insumos(self,nombre :str, *datos: tuple) -> bool:
        """
            Edita el item indicado solo si existe en la BD.\n
            Si es que no existe, lanzará el mensaje correspondiente.\n

            params
            - nombre_usuario : nombre del item a editar
            - datos : (nombre, tipo, stock)

            returns Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from Insumos where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))
            
            if len(cursor.fetchall()) > 0:
                if datos:
                    consulta_update = "update Insumos set id = :1, nombre = :2, tipo = :3, stock = :4"
                    cursor.execute(consulta_update, (nombre, datos[0], datos[1], datos[2], datos[3], nombre, ))
                    self.db.connection.commit()
                    print(f"[INFO]: {nombre} editado correctamente")
                    
                    return True
                else:
                    print(f"[ERROR]: Sin datos ingresados para {nombre}")
                    return False
            else:
                print(f"[ERROR]: {nombre} no existe en la tabla Insumos")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al editar {nombre} -> {e}")
            return False
        finally:
            if cursor:
                cursor.close()
    
    def mostrar_usuarios(self) -> list:
        """
            Muestra los Insumos actuales en la BD.

            returns List
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta = "select id, nombre, tipo, stock from Insumos "
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
                
    def eliminar_usuario(self, nombre: str) -> bool:
        """
            Elimina el item indicado, validando que exista en la BD.

            params
            - nombre : item a eliminar

            return Boolean
        """
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select * from Insumos Where nombre = :1"
            cursor.execute(consulta_validacion, (nombre,))
            
            if len(cursor.fetchall()) > 0:
                consulta_delete = "delete from Insumos where nombre = :5"
                cursor.execute(consulta_delete, (nombre,))
                self.db.connection.commit()
                print(f"[INFO]: {nombre} eliminado correctamente")
                
                return True
            else:
                print(f"[ERROR]: {nombre} no existe e la tabla Insumos")
                
                return False
        except Exception as e:
            print(f"[ERROR]: Error al eliminar {nombre} -> {e }")
            
            return False
        finally:
            if cursor:
                cursor.close()

class agenda():
    def __init__(self,id :int, fecha_consulta: str, estado: str, conexion: ConexionOracle)
        self.id = id
        self.fecha_consulta = fecha_consulta
        self.estado = estado
        self.db = conexion
    
    def CrearAgenda