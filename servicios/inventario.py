import json
import os
from modelos.producto import Producto

# ==========================================
# CUMPLIMIENTO DE REQUISITOS:
# Requisito 2: Clase Inventario. Utiliza una colección (diccionario).
# Requisito 3: Integración de Colecciones. El diccionario optimiza la búsqueda por ID.
# Requisito 4: Almacenamiento en Archivos. Métodos guardar_en_archivo y cargar_desde_archivo.
# ==========================================

class Inventario:
    def __init__(self, archivo_datos="inventario.json"):
        self.archivo_datos = archivo_datos
        
        # Requisito 2 y 3: Uso de un diccionario para almacenar productos.
        # La clave es el ID para búsquedas en tiempo constante O(1).
        self.productos = {} 
        
        # Al instanciar, cargamos los datos persistentes
        self.cargar_desde_archivo()

    # Requisito 2: Añadir nuevos productos
    def anadir_producto(self, producto):
        if producto.id_producto in self.productos:
            return False  # El ID ya existe
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()
        return True

    # Requisito 2: Eliminar productos por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            return True
        return False

    # Requisito 2: Actualizar cantidad o precio de un producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            self.guardar_en_archivo()
            return True
        return False

    # Requisito 2 y 3: Buscar y mostrar productos por nombre (Usa comprensión de listas)
    def buscar_por_nombre(self, nombre):
        resultados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        return resultados

    # Requisito 2: Mostrar todos los productos en el inventario
    def mostrar_todos(self):
        return list(self.productos.values())

    # ==========================================
    # Requisito 4: Almacenamiento en Archivos (Serialización y Deserialización)
    # ==========================================
    def guardar_en_archivo(self):
        with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
            # Serialización: Convertir objetos Producto a formato JSON
            datos_json = {id_prod: prod.a_diccionario() for id_prod, prod in self.productos.items()}
            json.dump(datos_json, archivo, indent=4)

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                    datos_json = json.load(archivo)
                    # Deserialización: Convertir JSON a objetos Producto
                    self.productos = {id_prod: Producto.desde_diccionario(info) for id_prod, info in datos_json.items()}
            except json.JSONDecodeError:
                self.productos = {}