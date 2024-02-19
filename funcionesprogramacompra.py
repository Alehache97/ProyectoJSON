from datetime import datetime

import json
with open("listacompra.json") as fichero:
    datos=json.load(fichero)


def mostrar_menu():
    print("\nMENÚ LISTA DE COMPRA")
    print("--------------------------------------------------------------------------------------\n")
    print("1. Lista los nombres de supermercados y la dirección del mismo en los que puedo comprar los productos que tengo apuntado en mi lista de la compra y las diferentes opciones de compra que tengo para ese producto y su precio.")
    print("2. Contar el total de opciones de productos de mi lista de compras que tiene en oferta cada supermercado.")
    print("3. Pide por teclado un producto y un nombre de supermercado y muestra las diferentes opciones de compra que tiene a la venta dicho supermercado para ese producto.")
    print("4. Pide por teclado una opcion de producto y me dice el nombre de supermercado la dirección y la geolocalización de los supermercados donde puedo comprarlos.")
    print("5. Pide por teclado un producto y te muestra las opciones en oferta que ofrece cada super para el producto indicado y la duracion de la oferta.")
    print("6. Salir")

    while True:
        try:
            numero= int(input("Elige una opcion del menu: "))
            while numero <= 0 or numero > 6:
                print("El numero indicado no corresponde con ninguna opción del menu")
                numero= int(input("Elige una opcion del menu: "))
            break
        except ValueError:
            print ("Introduce un numero entero que corresponda con una de las opciones del menu")
    return numero

def listainformación():
    
    for producto in datos["lista_de_la_compra"]:
        print("-------------------------------------------------------------------------------------")
        print("El producto: ", producto["producto"])
        for var in producto["supermercados"]:
            print("Puedes comprarlo en el supermercado ", var["nombre"], "ubicado en ", var["direccion"])
            print ("Puedes elegir entre estas opciones en el supermercado", var["nombre"])
            for opcion in var["productos"]:
                print("{:<30} Precio: {:>0}".format(opcion["nombre"], opcion["precio"]))


def contaropcionproductoferta():
    total_ofertas_super = {}

    print("\nTotal de ofertas de productos que ofrece cada supermercado sobre los productos de mi lista de la compra. ")

    for prod in datos["lista_de_la_compra"]:
        for nombresuper in prod["supermercados"]:
            for opcion in nombresuper["productos"]:
                if opcion["oferta"]:
                    nombre_supermercado = nombresuper["nombre"]
                    if nombre_supermercado not in total_ofertas_super:
                        total_ofertas_super[nombre_supermercado] = 0
                    total_ofertas_super[nombre_supermercado] += 1

    for clave, valor in total_ofertas_super.items():
        print(clave,"->",valor)


def inputinfoproduct():
    print("\nIntroduce un producto y un nombre de supermercado y te muestro las diferentes opciones de compra que tiene a la venta dicho supermercado para ese producto.\n")

    nombre_prod = input("Introduce el nombre de un producto de la lista de la compra: ")
    nombre_super = input("Introduce un supermercado para ver sus diferentes opciones: ")

    producto_encontrado = False
    supermercado_encontrado = False

    for product in datos["lista_de_la_compra"]:
        if product["producto"].lower() == nombre_prod.lower():
            producto_encontrado = True
            for super in product["supermercados"]:
                if super["nombre"].lower() == nombre_super.lower():
                    supermercado_encontrado = True
                    print("Supermercado:", super["nombre"])
                    print("Dirección:", super["direccion"])
                    print("Productos disponibles:")
                    for opcion in super["productos"]:
                        print("  Nombre:", opcion["nombre"])
                        print("  Precio:", opcion["precio"])
            if not supermercado_encontrado:
                print("El supermercado indicado no ofrece dicho producto de tu lista de compras.")

    if not producto_encontrado:
        print("El producto indicado no está en tu lista de compras.")


def inputpruductosuper():

    print("\nIntroduce una opcion de producto y me dice el nombre de supermercado la dirección y la geolocalización de los supermercados donde puedo comprarlos.\n")


    nombre_prod = input("Introduce una opcion de producto de la lista de la compra: ")

    producto_encontrado = False

    for product in datos["lista_de_la_compra"]:
            for super in product["supermercados"]:
                for opcion in super["productos"]:
                    if nombre_prod.lower() == opcion["nombre"].lower():
                        producto_encontrado = True
                        print("Supermercado:", super["nombre"])
                        print("Dirección:", super["direccion"])
                        print("Geolocalización (latitud, longitud):",super["geolocalizacion"]["latitud"], ",", super["geolocalizacion"]["longitud"])
                        print()
    
    if not producto_encontrado:
        print("La opcion de producto no se encuentra en la lista de la compra.")

    


def inputprodinofert():

    print("\nIntroduce un producto y muestro las opciones en oferta que ofrece cada super para el producto indicado y la duracion de la oferta.\n")

    nombre_prod = input("Introduce el nombre de un producto de la lista de la compra: ")
    
    producto_encontrado = False

    for product in datos["lista_de_la_compra"]:
        if nombre_prod.lower() == product["producto"].lower():
            producto_encontrado = True
            for super in product["supermercados"]:
                for nomproduct in super["productos"]:
                    if nomproduct["oferta"]:
                        inicio_oferta = datetime.strptime(nomproduct["vigencia"]["inicio"], "%Y-%m-%d")
                        fin_oferta = datetime.strptime(nomproduct["vigencia"]["fin"], "%Y-%m-%d")
                        duracion_oferta = (fin_oferta - inicio_oferta).days
                        print("Nombre producto", "->", nomproduct["nombre"])
                        print("Nombre supermercado", "->", super["nombre"])
                        print("Duración de la oferta (en días):", duracion_oferta)
                        print()
                        
    if not producto_encontrado:
        print("El producto no se encuentra en la lista de la compra.")







    



