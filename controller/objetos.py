import re
from model.objetos import InsumosModel, ConsultasModel, RecetasModel, AgendaModel

SUS_KEYS = [
    r";", r"--", r"/\*", r"\bOR\b", r"\bAND\b", r"\bUNION\b",
    r"\bSELECT\b", r"\bINSERT\b", r"\bUPDATE\b", r"\bDELETE\b",
    r"\bDROP\b", r"\bEXEC\b"
]

patron = re.compile("|".join(SUS_KEYS), re.IGNORECASE)

class InsumoController:
    """
        controlador de insumos, contiene metodos que utilizan el modelo.
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
        
        if patron.search(nombre) or patron.search(tipo):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.agregar_producto(id, nombre, tipo, stock)
        
class AgendaController:
         
    def __init__(self, modelo: AgendaModel):
        self.modelo = modelo
        
    def registrar_insumo(self,id :int, fecha_consulta: str, estado: str) -> bool:
        
        if patron.search(estado):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.Crear_Agenda(id, fecha_consulta, estado)
        
class ConsultasController:
         
    def __init__(self, modelo: ConsultasModel):
        self.modelo = modelo
        
    def registrar_insumo(self,id: int, fecha: str, comentarios: str) -> bool:
        
        if patron.search(comentarios):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_consulta(id, fecha, comentarios)
        
class RecetasController:
         
    def __init__(self, modelo: RecetasModel):
        self.modelo = modelo
        
    def registrar_insumo(self, id: int, descripcion: str) -> bool:
        
        if patron.search(descripcion):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_Receta(id, descripcion)