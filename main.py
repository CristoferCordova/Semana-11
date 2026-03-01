from modelos.producto import Producto
from servicios.inventario import Inventario

# ==========================================
# CUMPLIMIENTO DE REQUISITOS:
# Requisito 5: Interfaz de Usuario. Menú interactivo en la consola que permite
# realizar todas las operaciones solicitadas.
# ==========================================

def mostrar_menu():
    print("\n" + "="*45)
    print(" SISTEMA AVANZADO DE GESTION DE INVENTARIO")
    print("="*45)
    print("1. Anadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("="*45)
    return input("Elige una opcion: ")

def main():
    inventario = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Implementacion de la opcion Anadir
            id_prod = input("Ingrese ID unico del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad en stock: "))
                precio = float(input("Ingrese el precio: $"))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                
                if inventario.anadir_producto(nuevo_producto):
                    print("Producto anadido correctamente.")
                else:
                    print("Error: Ya existe un producto con ese ID.")
            except ValueError:
                print("Error: La cantidad debe ser un numero entero y el precio un numero decimal.")

        elif opcion == '2':
            # Implementacion de la opcion Eliminar
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_prod):
                print("Producto eliminado del inventario.")
            else:
                print("Error: Producto no encontrado.")

        elif opcion == '3':
            # Implementacion de la opcion Actualizar
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            cant_str = input("Nueva cantidad (presione Enter para omitir): ")
            precio_str = input("Nuevo precio (presione Enter para omitir): ")

            try:
                nueva_cant = int(cant_str) if cant_str.strip() else None
                nuevo_precio = float(precio_str) if precio_str.strip() else None

                if inventario.actualizar_producto(id_prod, nueva_cant, nuevo_precio):
                    print("Producto actualizado correctamente.")
                else:
                    print("Error: Producto no encontrado en el inventario.")
            except ValueError:
                print("Error: Asegurese de ingresar valores numericos validos.")

        elif opcion == '4':
            # Implementacion de la opcion Buscar
            nombre_buscar = input("Ingrese el nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre_buscar)
            if resultados:
                print("\nResultados de la busqueda:")
                for prod in resultados:
                    print(f"  - {prod}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Implementacion de la opcion Mostrar todos
            productos = inventario.mostrar_todos()
            if productos:
                print("\nInventario Actual:")
                for prod in productos:
                    print(prod)
            else:
                print("El inventario esta vacio.")

        elif opcion == '6':
            print("Guardando datos y saliendo del sistema... Hasta luego.")
            break
        
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()