class Articulos:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            return f"Venta de {cantidad_vendida} {self.nombre}s por un total de ${total_venta}"
        else:
            return f"No hay suficientes {self.nombre}(s) en existencia para la venta."

    def agregar_existencia(self, cantidad_agregada):
        self.cantidad += cantidad_agregada

    def __str__(self):
        return f"{self.nombre} - Existencia: {self.cantidad} Precio: ${self.precio}"

if __name__ == "__main__":
    articulo1 = Articulos("Soda", 50, 2.0)
    articulo2 = Articulos("Leche", 30, 1.60)

    print(articulo1)
    print(articulo2)

    print(articulo1.vender(10))
    print(articulo1)
    print(articulo1.vender(60))
    print(articulo1)

    articulo1.agregar_existencia(15)
    print(articulo1)