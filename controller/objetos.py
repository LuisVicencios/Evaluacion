import re
from model.objetos import InsumosModel, ConsultasModel, RecetasModel, AgendaModel
from datetime import date

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class InsumoController:
    """
        controlador de insumos, contiene metodos que utilizan el modelo,
        controla las insersiones de codigo SQL y tambien que no falte ningun tipo de dato
    """
    
    def __init__(self, modelo:InsumosModel):
        self.modelo = modelo
        
    def registrar_insumo(self,id: int, nombre: str, tipo: str, stock: int) -> bool:
        """
            Realiza registro dentro de BD usando funciones modelo.
            
            parametros
            - id: id del item
            - nombre: nombre del item
            - tipo: tipo del item
            - stock: cantidad de productos
            
            return Boolean
        """
        if not id or not nombre or not tipo or not stock:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
    
        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")

            return False
        else:
            return self.modelo.agregar_producto(id, nombre, tipo, stock)
    
    
    
class AgendaController:
         
    def __init__(self, modelo: AgendaModel):
        self.modelo = modelo
        
    def registrar_agenda(self,id :int, fecha_consulta: date, estado: str) -> bool:
        
        if not id or not fecha_consulta or not estado:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(estado) or patron.search(fecha_consulta):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.Crear_Agenda(id, fecha_consulta, estado)
        
        
class ConsultasController:
         
    def __init__(self, modelo: ConsultasModel):
        self.modelo = modelo
        
    def registrar_consulta(self,id: int, fecha: date, comentarios: str) -> bool:

        if not id or not fecha or not comentarios:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(comentarios):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_consulta(id, fecha, comentarios)
        
        
class RecetasController:
         
    def __init__(self, modelo: RecetasModel):
        self.modelo = modelo
        
    def registrar_receta(self, id: int, descripcion: str) -> bool:

        if not id or not descripcion:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(descripcion):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_Receta(id, descripcion)
    