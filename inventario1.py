# Inicialización del inventario
inventario = {
    'Manzanas': {'cantidad': 50, 'precio': 1.50},
    'Leche': {'cantidad': 20, 'precio': 2.75},
    'Pan': {'cantidad': 10, 'precio': 3.00},
}

while True:
    print("\n--- MENU DE GESTION DE INVENTARIOS ---")
    print("1. Añadir Producto")
    print("2. Actuar Stock")
    print("3. Eliminar Producto")
    print("4. Ver Inventario")
    print("5. Buscar Producto")
    print("6. Resumen de Inventario")
    print("7. Salir")
    print("-----------------------------------------")

    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        # logica para añadir producto
        print("\n--- Añadir Nuevo producto ---")
        entrada = input("Ingrese el nombre del producto: ")
        nombre_producto = entrada.strip().capitalize()
        if nombre_producto in inventario:
            print(
                f"Error: El producto '{nombre_producto}' ya existe.")
        else: 
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad inicial: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero entero para la cantidad.")
                    while True:
                        try:
                            precio = float(input("Ingrese el precio unitario: "))
                            if precio < 0:
                                print("El precio no puede ser negativo. Intente de nuevo.")
                            else:
                                break
                        except ValueError: 
                            print("Entrada invalida. Por favor, ingrese un numero para el precio.")
                            inventario[nombre_producto] = {'cantidad': cantidad,'precio': precio}
                            print(f"Producto: '{nombre_producto}' añadido exitosamente.")
                        
    elif opcion == '2':
        #logica para Actualizar Stock de Producto
        print("\n--- Actualizar Stock de Producto ---")
        nombre_a_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
        if nombre_a_actualizar not in inventario:
            print(f"Error: El producto '{nombre_a_actualizar}'no se encuentra en el inventario.")
        else:
            print(f"Producto '{nombre_a_actualizar}' encontrado. Catidad actual: {inventario[nombre_a_actualizar]['cantidad']}.")
            while True: 
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombre_a_actualizar}': "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                    else:
                        break
                except ValueError: 
                    print("Entrada invalida. Por favor, ingrese un numero entero para la cantidad.")
                    inventario[nombre_a_actualizar]['cantidad'] = nueva_cantidad
                    print(f"Stock de '{nombre_a_actualizar}' actualizado a {nueva_cantidad}. ")

    elif opcion == '3':
        # LOGICA PARA ELIMINAR EL PRODUCTO
        print("\n--- Eliminar Producto ---")
        nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
        if nombre_a_eliminar not in inventario:
            print(f"Error: El producto '{nombre_a_eliminar}' no se encuentra en el inventario.")
        else: 
            confirmacion = input(f"Esta seguro de que desea eliminar '{nombre_a_eliminar}' del inventario? (s/n): ").lower()
            if confirmacion == "s":
                del inventario[nombre_a_eliminar]
                print(f"Producto '{nombre_a_eliminar}' eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
    elif opcion =='4':
        #LOGICA PARA VER INVENTARIO
        print("\n--- Ver Inventario ---")
        if not inventario:
            print("El inventario esta vacio. ")
        else: 
            for nombre, detalles in inventario.items():
                print(f"Nombre:{nombre}, Cantidad:{detalles['cantidad']}, Precio: ${detalles['precio']: .2f}")

    elif opcion == '5':
        # LOGICA PARA BUSCAR EL PRODUCTO 
        print("\n---- Buscar Producto ----")
        termino_busqueda = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
        productos_encontrados = []
        for nombre, detalles in inventario.items():
            if termino_busqueda in nombre.lower():
                productos_encontrados.append((nombre,detalles))
                if productos_encontrados:
                    print("\n--- Resultados de la Búsqueda ----")
                    for nombre, detalles in productos_encontrados:
                        print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, Precio: ${detalles['precio']: .2f}")
                    else:
                        print(f"No se encontraron productos que coincidan con '{termino_busqueda}'.")

    elif opcion == '6':
        #LOGICA PARA RESUMEN DE INVENTARIO
        print("\n--- Resumen de Inventario ----")
        valor_total_inventario = 0 
        for detalles in inventario.values():
            valor_total_inventario += detalles['cantidad']*detalles['precio']
            print(f"Valor Total del del Inventario: ${valor_total_inventario: .2f}")

            umbral_bajo_stock = 5
            productos_bajo_stock = []
            for nombre, detalles in inventario.items():
                if detalles['cantidad'] < umbral_bajo_stock: productos_bajo_stock.append(nombre)
                
                if productos_bajo_stock: 
                    print("Productos con bajo stock (cantidad < {}):".format(umbral_bajo_stock))
                    for p in productos_bajo_stock:
                        print(f"- {p} (Cantidad:{inventario[p]['cantidad']})")
                    else: 
                        print("No hay productos con bajo stock. ")
                        algun_producto_agotado = any(detalles['cantidad'] == 0 for detalles  in inventario.values())

                        if algun_producto_agotado:
                            print("Advertencia! Hay al menos un producto agotado en el inventario.")
                        else: 
                            print("No hay productos agotados en el inventario.")
    elif opcion == '7':
        # Logica para Salir
        print("Saliendo del programa. Hasta pronto!")
        break # sale del bucle principal
    else: 
        print("Opcion invalida. Por favor, intente de nuevo")
