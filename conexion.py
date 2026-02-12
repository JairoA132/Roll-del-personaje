import mysql.connector

class CONFIGURACIONDB:
    HOST = "localhost"
    USER = "root"
    DATABASE = "Personajes"
    PASSWORD = "1077997121"

def conectar():
    """Devuelve una conexión activa a MySQL."""
    try:
        conexion = mysql.connector.connect(
            host=CONFIGURACIONDB.HOST,
            user=CONFIGURACIONDB.USER,
            password=CONFIGURACIONDB.PASSWORD,
            database=CONFIGURACIONDB.DATABASE
        )

        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
        return conexion

    except mysql.connector.Error as err:
        print(f"Error al conectar a MySQL: {err}")
        return None
