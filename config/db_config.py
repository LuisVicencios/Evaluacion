import oracledb

class ConexionOracle:
    """
        Clase para conexion de BD.
    """
    def __init__(self, usuario: str, password: str, url: str):
        self.usuario = usuario
        self.password = password
        self.url = url
        self.connection = None

    def conectar(self):
        """
            Genera la conexión con la bd según datos recibidos.\n
        """
        try:
            self.connection = oracledb.connect(
                user=self.usuario,
                password=self.password,
                dsn=self.url
            )
            print("[INFO]: Conectado a BD correctamente.")
            
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"[ERROR]: No se pudo conectar a BD → {error.message}")

    def desconectar(self):
        """
            Si es que hay una conexión activa, la finaliza.
        """
        if self.connection:
            self.connection.close()
            print("[INFO]: Conexión a BD cerrada correctamente.")

    def obtener_cursor(self):
        """
            Genera el cursor para BD.
        """
        if not self.connection:
            self.conectar()

        return self.connection.cursor()