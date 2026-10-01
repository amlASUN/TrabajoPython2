IVA = 0.21 # Constante de IVA
Precio = float(input("Introduce el precio del producto a calcular:")) # Float para poder usar números con comas e integrar al programa el dato.
PrecioTotal = Precio + (Precio*IVA) # Operación + Ejecución.
print(PrecioTotal) # Salida del resultado.