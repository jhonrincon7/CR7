def sumar():#DEFINIR FUNCION
    #AQUI EMPIEZA EL CODIGO DE MI FUNCION
    print("El resultado es", a+b)

sumar(-7.5, 5.2)#LLAMAR FUNCION

def restar(num1, num2):
    resultado = num1 - num2
    print("Este es el resultado de la resta:", resultado)

frutas = []
def agregar_fruta(fruta):
    fruta.append(fruta)
    print(frutas)

agregar_fruta("Fresa")
print(frutas)

#==============
concesionario = [
    {"marca": "toyota", "modelo": "corolla", "precio": 110},
    {"marca": "mazda", "modelo": "cx-3", "precio": 90},
    {"marca": "renault", "modelo": "logan", "precio": 80},
]
#UPPER: todo a mayusculas
#LOWER: todo en minusculas
#CAPITALIZE: la primera letra de cada palabra en mayuscula
#TITLE: la primera letra de una frase en mayuscula
def buscar_vehiculo(lista_carros, marca_busqueda):
    for carro in lista_carros:
        if carro["marca"].lower() == marca_busqueda.lower()
            return carro
    return None

carro = input("Ingrese la marca a buscar: ")
resultado = buscar_vehiculo(concesionario, carro)

if resultado != None:
    print(f"Vehiculo encontrado: Marca: {resultado["marca"]}, ")
else:
    print("Vehiculo no encontrado")