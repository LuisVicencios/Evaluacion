from config.db_config import ConexionOracle
class InsumosModel :
    def __init__(self,id: int, nombre: str, tipo: str, stock: int, conexion: ConexionOracle):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock
        self.db = conexion
        
    def agregar_producto(self, id, nombre, tipo, stock):
        """
            Guarda el producto actual si es que este no existe en la BD.\n
            Si es que ya existe, lanzará un mensaje de existencia.\n
            returns Boolean
        """
        
        cursor = self.db.obtener_cursor()
        
        try:
            consulta_validacion = "select nombre from Insumos where nombre = :2"
            cursor.execute(consulta_validacion,(nombre))
            
            if len(cursor.fetchall()) >0:
                print(f"{nombre} encontrado")
                return False
            
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