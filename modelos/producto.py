# ==========================================
# CUMPLIMIENTO DE REQUISITOS:
# Requisito 1: Clase Producto. Contiene atributos privados (ID, nombre, cantidad, precio)
# e implementa métodos para obtener (getters) y establecer (setters) estos atributos.
# ==========================================

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Requisito 1: Métodos para obtener atributos (Getters)
    @property
    def id_producto(self):
        return self.__id_producto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def precio(self):
        return self.__precio

    # Requisito 1: Métodos para establecer atributos (Setters)
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Métodos auxiliares para el Requisito 4 (Almacenamiento y Serialización)
    def a_diccionario(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id"], datos["nombre"], datos["cantidad"], datos["precio"])

    def __str__(self):
        return f"ID: {self.id_producto} | Producto: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"