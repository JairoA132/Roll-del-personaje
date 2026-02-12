import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# --- Conexión a la base de datos ---
def conectar():
    """Conecta a la base de datos MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1077997121",  # cambia si tu clave es diferente
        database="personajes"
    )

# --- Función para graficar un personaje ---
def graficar_personaje(nombre_personaje):
    """
    Busca un personaje en la base de datos por nombre y muestra un gráfico radar
    con sus atributos (fuerza, defensa, velocidad, inteligencia, energía).
    """
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    # Buscar el personaje en la base de datos
    cursor.execute("SELECT * FROM personajes WHERE nombre = %s", (nombre_personaje,))
    personaje = cursor.fetchone()

    if not personaje:
        print(f"⚠️ No se encontró el personaje '{nombre_personaje}'.")
        conexion.close()
        return

    # --- Preparar datos para el gráfico ---
    atributos = ["fuerza", "defensa", "velocidad", "inteligencia", "energia"]
    valores = [personaje[a] for a in atributos]

    # Cerrar el círculo del radar chart
    valores += valores[:1]
    angulos = np.linspace(0, 2 * np.pi, len(atributos) + 1)

    # --- Crear el gráfico ---
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)

    ax.plot(angulos, valores, linewidth=2, linestyle='solid', label=personaje["nombre"])
    ax.fill(angulos, valores, alpha=0.25)

    # --- Personalizar el gráfico ---
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(atributos)
    ax.set_title(f"Estadísticas de {personaje['nombre']} ({personaje['tipo']})")
    plt.legend(loc='upper right')

    plt.show()

    cursor.close()
    conexion.close()
