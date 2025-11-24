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
    
def validar_tablas(db: ConexionOracle):
    """
    Se encarga de crear la tablas en caso de que estas no existan.
    """

    LV_Usuarios = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Usuarios (
                        id integer PRIMARY KEY,
                        nombre_usuario VARCHAR2(100),
                        clave varchar2(255),
                        nombre VARCHAR2(100),
                        apellido varchar2(100),
                        fecha_nacimiento date, 
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
    
    LV_Insumos = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Insumos (
                        id integer PRIMARY KEY,
                        nombre varchar2(100),
                        tipo varchar2(100),
                        stock integer,
                        precio_unitario integer
                        )
                    ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
            """
    
    LV_Pacientes = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Paciente  (
                        id  integer PRIMARY KEY,
                        comuna VARCHAR2(100),
                        fecha_primera_visita date ,
                        CONSTRAINT fk_paciente_usuario FOREIGN KEY (id) REFERENCES LV_Usuarios(id)
                        )
                    ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
            """
    
    LV_Doctores = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Doctores (
                        id  integer PRIMARY KEY,
                        especialidad varchar2(100),
                        horario_atencion varchar2(100),
                        fecha_ingreso date,
                        CONSTRAINT fk_doctor_usuario FOREIGN KEY (id) references LV_Usuarios(id)
                        )
                    ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
            """

    LV_Agenda = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Agenda (
                        id  integer PRIMARY KEY,
                        id_doctor number ,
                        id_paciente number ,
                        fecha_consulta varchar2(100),
                        estado varchar2(100),
                        CONSTRAINT fk_agenda_doctor FOREIGN KEY (id) REFERENCES LV_Doctores (id),
                        CONSTRAINT fk_agenda_paciente FOREIGN KEY (id) REFERENCES LV_Pacientes (id)
                        )
                    ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
            """


    
    LV_Consultas = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Consultas (
                        id NUMBER PRIMARY KEY,
                        id_doctor integer,
                        id_paciente integer,
                        descripcion varchar2(200),
                        constraint fk_consulta_doctor FOREIGN KEY (id) REFERENCES LV_Doctores (id),
                        constraint fk_consulta_paciente FOREIGN KEY (id) REFERENCES LV_pacientes (id)
                        )
                    ';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -955 THEN
                        RAISE;
                    END IF;
            END;
            """

    LV_Recetas = """
            BEGIN
                EXECUTE IMMEDIATE '
                    CREATE TABLE LV_Recetas (
                        id integer PRIMARY KEY,
                        descripcion varchar2(200),
                        CONSTRAINT fk_receta_consulta FOREIGN KEY (id) references LV_Consultas (id)
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
        LV_Usuarios,  
        LV_Insumos,     
        LV_Pacientes,   
        LV_Doctores,    
        LV_Agenda,      
        LV_Consultas,   
        LV_Recetas,     
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