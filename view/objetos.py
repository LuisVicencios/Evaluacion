class InsumosView:
    """
        Vista de Insumos, muestra información en pantalla.
    """
    @staticmethod
    def mostrar_insumos(insumos: list) -> None:
        """
            Recibe la lista de los insumos.\n
            Si recibe al menos uno, mostrará la lista en consola.
        """
        if len(insumos) > 0:
            print("\n- Lista de Insumos -")

            for i in insumos:
                print(f"--- id: {i['id']} | Nombre: {i['nombre']} | tipo: {i['tipo']} | stock: {i['stock']}")
        else:
            print("[ERROR]: Sin Insumos registrados")

class AgendaView:
    @staticmethod
    def mostrar_agendas(agenda: list) -> None:
        if len(agenda) > 0:
            print("\n- Lista de agenda -")

            for a in agenda:
                print(f"--- id: {a['id']} | fecha_consulta: {a['fecha_consulta']} | estado: {a['estado']}")
        else:
            print("[ERROR]: Sin Agendas registrados")

class ConsultasView:
    @staticmethod
    def mostrar_Consultas(Consultas: list) -> None:
       
        if len(Consultas) > 0:
            print("\n- Lista de Consultas -")

            for c in Consultas:
                print(f"--- id: {c['id']} | fecha: {c['fecha']} | comentario: {c['comentario']}")
        else:
            print("[ERROR]: Sin consultas registradas")

