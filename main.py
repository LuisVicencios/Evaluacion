import bcrypt
from config.db_config import ConexionOracle

def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("system", "vicencio", "localhost:1521/xe")
    db.conectar()

    # validar_tablas(db)

    return db

def main():
    db = conectarBD()

    print("Inicio de sesión, ingrese sus credenciales\n")
    id_u = int(input("Ingrese su id: "))
    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)

    cursor = db.obtener_cursor()

    consulta = "insert into usuarios (id, nombre_usuario, clave) values (:1, :2, :3)"
    cursor.execute(consulta, (id_u, usuario, clave_encriptada))
    db.connection.commit()

    db.desconectar()

    if __name__ == "__main__":
        main()