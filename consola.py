import mysql.connector

db= mysql.connector.connect(user='root', password="1234",host="localhost", database="grafos",auth_plugin="mysql_native_password")
cursor = db.cursor()


def crear_conexion(ciu1_nombre, ciu2_nombre):
    cursor = db.cursor()
    cursor.callproc('crear_conexion', (ciu1_nombre, ciu2_nombre))
    db.commit()
    cursor.close()
    db.close()
    print(f'Conexión creada entre {ciu1_nombre} y {ciu2_nombre}.')

def leer_conexion(ciu_nombre):
    cursor = db.cursor()
    cursor.callproc('leer_conexion', (ciu_nombre,))
    for result in cursor.stored_results():
        conexiones = result.fetchall()
        print(f'Conexiones de {ciu_nombre}:')
        for conexion in conexiones:
            print(conexion)
    cursor.close()


def actualizar_conexion(ciu_id, nueva_ciudad1, nueva_ciudad2):
    cursor = db.cursor()
    cursor.callproc('actualizar_conexion', (ciu_id, nueva_ciudad1, nueva_ciudad2))
    db.commit()
    cursor.close()
    print(f'Conexión con ID {ciu_id} actualizada a {nueva_ciudad1} - {nueva_ciudad2}.')

def eliminar_conexion(ciu1_nombre, ciu2_nombre):
    cursor = db.cursor()
    cursor.callproc('eliminar_conexion', (ciu1_nombre, ciu2_nombre))
    db.commit()
    cursor.close()
    print(f'Conexión eliminada entre {ciu1_nombre} y {ciu2_nombre}.')


def menu():
    while True:
        print("\n =========BIENVENIDO A CONEXIONES COLOMBIA:=========")
        print("1. Crear una conexión")
        print("2. Leer las conexiones")
        print("3. Actualizar una conexión")
        print("4. Eliminar una conexión")
        print("5. Salir")
        
        opcion = input("\nPOR FAVOR SELECCIONE UNA OPCIÓN: ")
        
        if opcion == '1':
            ciu1_nombre = input("Ingrese la ciudad 1: ")
            ciu2_nombre = input("Ingrese la ciudad 2: ")
            crear_conexion(ciu1_nombre, ciu2_nombre)
        elif opcion == '2':
            ciu_nombre = input("Ingrese el nombre de la ciudad para ver sus conexiones: ")
            leer_conexion(ciu_nombre)    
        elif opcion == '3':
            id = int(input("Ingrese el cone_Id de la conexión a actualizar: "))
            nueva_ciudad1 = input("Ingrese la nueva ciudad 1: ")
            nueva_ciudad2 = input("Ingrese la nueva ciudad 2: ")
            actualizar_conexion(id, nueva_ciudad1, nueva_ciudad2)
        elif opcion == '4':
            ciu1_nombre = input("Ingrese la ciudad 1 a eliminar: ")
            ciu2_nombre = input("Ingrese la ciudad 2 a eliminar: ")
            eliminar_conexion(ciu1_nombre, ciu2_nombre)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()