"""
Marco Holguín-Veras
22-0367
Refinando código
En este ejercicio, se refinará un código dado y se publicará en un repositorio de Github
"""

import sys
def costs_list():
    """Función que devuelve una lista de costos del archivo gift_costs.txt"""
    with open('gift_costs.txt', 'r', encoding='UTF-8') as archivo:
        gift_costs = list(archivo)
        try:
            gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
            archivo.close()  # cerrar el archivo después de usarlo y no ser necesario
        except ValueError:
            print('Los datos deben ser dígitos.')
            sys.exit()

    return gift_costs


def total(gift_costs):
    """Función que suma los precios de la lista de costos para conseguir un total"""
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  # los costos menores a 1000 no se le agrega impuesto

    return total_price


def main():
    """Función principal que llama ambas funciones e imprime el total"""
    return print(total(costs_list()))


if __name__ == '__main__':
    main()
