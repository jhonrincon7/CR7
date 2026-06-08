listas = [1,2,3]

listas.append(4)
print(listas)

listas.pop()
print(listas)

listas.pop(1)
print("Imprimiendo el resultado del pop(1)", listas)

listas.insert(1, "Hola")
print("Imprimiendo resultado del insert", listas)

#TUPLAS
tuplas = (1,2,3)
print("Esto es una tupla", tuplas)

#DICCIONARIO {} KEY = LLAVE, VALUE = VALOR
diccionarios = {
    "id": 1,
    "Nombre": "Jhon"
}

print("Estoy imprimiendo el valor de una llave",diccionarios["Nombre"])
diccionarios["apellido"] = "Rincon" #AGREGAR UN DATO NUEVO
print("Agregue una nueva llave al diccionario", diccionarios)

diccionarios["Nombre"] = "Kratos" #USANDO LLAVE EXISTENTE, SE MODIFICA EL VALOR
print("Imprimir diccionario modificado", diccionarios)

del diccionarios["apellido"]
print("Eliminado un elemento del diccionario", diccionarios)