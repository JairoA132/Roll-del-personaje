from personajes import ver_personajes, agregar_personaje, eliminar_personaje
from graficos import graficar_personaje

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ver personajes")
        print("2. Agregar personaje")
        print("3. Eliminar personaje")
        print("4. Mostrar gráfica del personaje")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_personajes()
            opcion2 = input("Desea elegir algun personaje? : ")
            if opcion2 == "si":
                nombre_personaje = input(" Ingresa el nombre del personaje para graficar: ")
                graficar_personaje(nombre_personaje)
                print(f"{nombre_personaje} mostrado en gráfico.")

        elif opcion == "2":
            agregar_personaje()
        elif opcion == "3":
            eliminar_personaje()
        elif opcion == "4":
           graficar_personaje(input(" Ingresa el nombre del personaje para graficar: "))

        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
    print(" Personaje agregado exitosamente.")