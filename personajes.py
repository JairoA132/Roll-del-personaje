import mysql.connector

# --- Conexión a la base de datos ---
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1077997121",  # cambia si tu clave es diferente
        database="personajes"
    )

conexion = conectar()

if conexion.is_connected():
    print("Conexión exitosa a la base de datos para los personajes \n.")
else:
    print("No se pudo establecer la conexión a la base de datos para los personajes.")

# --- Clasificar personaje ---
def clasificar_personaje(stats):
    max_stat = max(stats, key=stats.get)

    if max_stat == "fuerza":
        return "Agresor"
    elif max_stat == "defensa":
        return "Tanque"
    elif max_stat == "velocidad":
        return "Velocista"
    elif max_stat == "inteligencia":
        return "Estratega"
    elif max_stat == "energia":
        return "Energético"
    else:
        return "Indefinido"


# --- Ver personajes ---
def ver_personajes():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personajes")
    resultados = cursor.fetchall()

    print("\n=== LISTA DE PERSONAJES ===")
    for personaje in resultados:
        print(f"{personaje['id']}. {personaje['nombre']} ({personaje['tipo']}) - "
              f"F:{personaje['fuerza']} D:{personaje['defensa']} "
              f"V:{personaje['velocidad']} I:{personaje['inteligencia']} "
              f"E:{personaje['energia']}")

    cursor.close()
    conexion.close()


# --- Agregar personaje ---
def agregar_personaje():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== CREAR NUEVO PERSONAJE ===")
    nombre = input("Nombre del personaje: ")
    fuerza = int(input("Fuerza (1-100): "))
    defensa = int(input("Defensa (1-100): "))
    velocidad = int(input("Velocidad (1-100): "))
    inteligencia = int(input("Inteligencia (1-100): "))
    energia = int(input("Energía (1-100): "))

    stats = {
        "fuerza": fuerza,
        "defensa": defensa,
        "velocidad": velocidad,
        "inteligencia": inteligencia,
        "energia": energia
    }

    tipo = clasificar_personaje(stats)

    sql = """
    INSERT INTO personajes (nombre, fuerza, defensa, velocidad, inteligencia, energia, tipo)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nombre, fuerza, defensa, velocidad, inteligencia, energia, tipo)

    cursor.execute(sql, valores)
    conexion.commit()

    print(f" Personaje '{nombre}' agregado correctamente como {tipo}.")
    cursor.close()
    conexion.close()


# --- Eliminar personaje ---
def eliminar_personaje():
    conexion = conectar()
    cursor = conexion.cursor()
    ver_personajes()
    personaje = input("Ingrese el ID del personaje")
    sql = "DELETE FROM personajes WHERE id = %s"
    valor = (personaje, )
    cursor.execute(sql, valor)
    conexion.commit()
    print(f" Personaje con ID '{personaje}' eliminado correctamente.")
    cursor.close()
    conexion.close()