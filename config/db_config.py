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
    
    def validar_tablas(db):
        """
        Se encarga de crear la tablas en caso de que estas no existan.
    """

    sql_LV_Usuario = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE Usuarios (
                        id NUMBER PRIMARY KEY,
                        nombre_usuario VARCHAR2(100),
                        clave varchar2(255),
                        nombre VARCHAR2(100),
                        apellido varchar2(100),
                        fecha_nacimiento, 
                        telefono varchar2(50),
                        email varchar2(100),
                        tipo varchar2(200)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    sql_LV_Paciente = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE clientes (
                        id_cliente NUMBER PRIMARY KEY,
                        nombre VARCHAR2(100),
                        telefono NUMBER,
                        nacionalidad VARCHAR2(50),
                        habitacion NUMBER,
                        CONSTRAINT fk_habitacion_cliente FOREIGN KEY (habitacion) REFERENCES habitaciones(id_habitacion)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    sql_inventario = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE inventario (
                        id_inventario NUMBER PRIMARY KEY,
                        nombre VARCHAR2(100),
                        tipo VARCHAR2(30),
                        cantidad NUMBER,
                        precio_costo NUMBER(8,2)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """

    sql_habitaciones = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE habitaciones (
                        id_habitacion NUMBER PRIMARY KEY,
                        numero_habitacion NUMBER UNIQUE,
                        cantidad_personas NUMBER,
                        estado VARCHAR2(15)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """

    sql_boletas = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE boletas (
                        id_boleta NUMBER PRIMARY KEY,
                        folio NUMBER,
                        usuario NUMBER,
                        cliente NUMBER,
                        CONSTRAINT fk_boleta_usuario FOREIGN KEY (usuario) REFERENCES usuarios(id_usuario),
                        CONSTRAINT fk_boleta_cliente FOREIGN KEY (cliente) REFERENCES clientes(id_cliente)
                    )
                ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
        """
    
    cursor = db.obtener_cursor()

    sentencias = [
        sql_habitaciones,
        sql_usuario,
        sql_inventario,
        sql_cliente,
        sql_boletas,
    ]

    try:
        for sql in sentencias:
            cursor.execute(sql)

        db.connection.commit()

        print("[INFO]: Tablas validadas/creadas correctamente")
    except Exception as e:
        db.connection.rollback()

        print("[ERROR]: Error al crear tablas:", e)
    finally:
        if cursor:
            cursor.close()