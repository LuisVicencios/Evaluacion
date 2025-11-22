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
    
    def listar_insumos(self) -> list:
        """
            Muestra los usuarios registrados en BD.\
            returns Lista vacía si es que no hay usuarios, o lista de usuarios registrados.
        """
        insumos = self.modelo.mostrar_insumos()

        if len(insumos) > 0:
            return [{ "id": i[0], "nombre": i[1], "tipo": i[2], "stock": i[3]} for i in insumos]
        
        else:
            return []
    
class AgendaController:
         
    def __init__(self, modelo: AgendaModel):
        self.modelo = modelo
        
    def registrar_agenda(self,id :int, fecha_consulta: str, estado: str) -> bool:
        
        if not id or not fecha_consulta or not estado:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(estado):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.Crear_Agenda(id, fecha_consulta, estado)
        
    def listar_agenda(self) -> list:
        
        agenda = self.modelo.mostrar_agenda()

        if len(agenda) > 0:
            return [{ "id": a[0], "fecha_consulta": a[1], "estado": a[2]} for a in agenda]
        
        else:
            return []
        
class ConsultasController:
         
    def __init__(self, modelo: ConsultasModel):
        self.modelo = modelo
        
    def registrar_insumo(self,id: int, fecha: str, comentarios: str) -> bool:

        if not id or not fecha or not comentarios:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(comentarios):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_consulta(id, fecha, comentarios)
        
    def listar_consultas(self) -> list:
        
        consultas = self.modelo.mostrar_consultas()

        if len(consultas) > 0:
            return [{ "id": c[0], "fecha": c[1], "comentarios": c[2]} for c in consultas]
        
        else:
            return []
        
class RecetasController:
         
    def __init__(self, modelo: RecetasModel):
        self.modelo = modelo
        
    def registrar_insumo(self, id: int, descripcion: str) -> bool:

        if not id or not descripcion:
            print("[Error]: Datos faltantes para registro de usuario.")
     
            return False
        
        if patron.search(descripcion):
            print("[ERROR]: No se puede ingresar codigoSQL en los string.")
            
            return False
        else:
            return self.modelo.crear_Receta(id, descripcion)
    
    def listar_recetas(self) -> list:
        
        recetas = self.modelo.mostrar_recetas()

        if len(recetas) > 0:
            return [{ "id": r[0], "fecha_consulta": r[1]} for r in recetas]
        
        else:
            return []