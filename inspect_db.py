import mysql.connector

try:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1077997121",
        database="personajes"
    )
    cursor = cnx.cursor()
    cursor.execute("SHOW COLUMNS FROM personajes")
    cols = cursor.fetchall()
    print("Columnas en la tabla 'personajes':")
    for c in cols:
        print(c)
    cursor.close()
    cnx.close()
except Exception as e:
    print("Error al inspeccionar la tabla:", e)
