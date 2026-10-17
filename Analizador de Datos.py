inventario = {
    "Laptop": 800.00,
    "Mouse": 25.00,
    "Teclado": 45.00,
    "Monitor": 250.00,
    "Audífonos": 15.00
}

def calcular_total(productos):
    total = 0
    for producto in productos:
        total += productos[producto]
    return total

def encontrar_mas_caro(productos):
    producto_mas_caro = None
    precio_mas_alto = 0
    for producto in productos:
        if productos[producto] > precio_mas_alto:
            precio_mas_alto = productos[producto]
            producto_mas_caro = producto
    return producto_mas_caro, precio_mas_alto

total_inventario = calcular_total(inventario)
producto_mas_caro, precio_mas_alto = encontrar_mas_caro(inventario)

print(f"Total del inventario: ${total_inventario:.2f}")
print(f"Producto más caro: {producto_mas_caro} (${precio_mas_alto:.2f})")