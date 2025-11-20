## 1. Función para obtener el doble de cada elemento
def doble(lista):
    """
    Retorna una nueva lista con el doble de cada valor de la lista de entrada.
    """
    lista_doble = []
    for valor in lista:
        lista_doble.append(valor * 2)
    return lista_doble

## 2. Función para contar valores dentro de un rango
def cantidadEntre(lista, desde, hasta):
    """
    Retorna la cantidad de valores en la lista que se encuentran
    en el rango [desde, hasta] (ambos inclusive).
    """
    contador = 0
    for valor in lista:
        # Verifica si el valor es mayor o igual que 'desde' Y menor o igual que 'hasta'
        if valor >= desde and valor <= hasta:
            contador += 1
    return contador

## 3. Función para contar valores negativos
def cantidadNegativos(lista):
    """
    Retorna la cantidad de valores negativos existentes en la lista.
    """
    contador_negativos = 0
    for valor in lista:
        # Un número es negativo si es estrictamente menor que cero
        if valor < 0:
            contador_negativos += 1
    return contador_negativos

## 4. Función para imprimir la lista y su promedio
def promedio(lista):
    """
    Imprime el contenido de la lista con su índice y calcula e imprime el promedio.
    NO utiliza funciones de agregación (como sum()).
    """
    # 1. Verificar si la lista está vacía para evitar división por cero
    if not lista:
        print("La lista está vacía. No se puede calcular el promedio.")
        return

    suma_total = 0
    
    # Recorrer la lista usando enumerate para obtener el índice y el valor
    for indice, valor in enumerate(lista):
        # Imprimir el contenido de la lista (Índice -> Valor)
        print(f"{indice} -> {valor}")
        
        # Acumular la suma total (No se usa la función sum())
        suma_total += valor
    
    # Calcular el promedio
    # Se utiliza el tamaño de la lista como el divisor
    longitud = len(lista)
    
    # Se añade una pequeña corrección de formato si la división resulta en un número sin decimales
    # Esto asegura que el resultado sea un float
    promedio_calculado = suma_total / longitud
    
    # Imprimir el resultado final
    print(f"Promedio: {promedio_calculado}")


# --- EJEMPLOS DE USO Y RESULTADOS ESPERADOS ---
lista_prueba = [1, 1, 2, 3, 5, -4, 10]

print("--- Prueba de 'doble' ---")
resultado_doble = doble(lista_prueba)
print(f"Lista original: {lista_prueba}")
print(f"Resultado doble: {resultado_doble}")
# Resultado esperado: [2, 2, 4, 6, 10, -8, 20]
print("-" * 25)

print("--- Prueba de 'cantidadEntre' ---")
rango_desde = 3
rango_hasta = 11
resultado_cantidad = cantidadEntre(lista_prueba, rango_desde, rango_hasta)
print(f"Lista: {lista_prueba}, Rango: [{rango_desde}, {rango_hasta}]")
print(f"Cantidad encontrada: {resultado_cantidad}")
# Resultado esperado: 3 (los números 3, 5 y 10 están en el rango)
print("-" * 25)

print("--- Prueba de 'cantidadNegativos' ---")
resultado_negativos = cantidadNegativos(lista_prueba)
print(f"Lista: {lista_prueba}")
print(f"Cantidad de negativos: {resultado_negativos}")
# Resultado esperado: 1 (el número -4)
print("-" * 25)

print("--- Prueba de 'promedio' ---")
lista_promedio = [1, 1, 2, 3, 5]
print(f"Lista para promedio: {lista_promedio}")
promedio(lista_promedio)
# Resultado esperado: Imprime 0 -> 1, 1 -> 1, ..., Promedio: 2.4
print("-" * 25)
