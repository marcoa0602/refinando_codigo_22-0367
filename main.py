"""
Marco Holguín-Veras
22-0367
Refinando código
En este ejercicio, se refinará un código dado y se publicará en un repositorio de Github
"""


def costs_list():
    archivo = open('gift_costs.txt', 'r')
    gift_costs = list(archivo)
    gift_costs = [int(c) for c in gift_costs]  # convierte strings a int
    archivo.close()  # cerrar el archivo después de usarlo y no ser necesario
    return gift_costs


def total(gift_costs):
    total_price = 0
    for cost in gift_costs:
        if cost > 1000:
            total_price += cost * 1.16  # agrega impuestos
        else:
            total_price += cost  # los costos menores a 1000 no se le agrega impuesto

    return total_price


def main():
    print(total(costs_list()))
    # llama a los dos funciones y luego imprime el resultado

if __name__ == '__main__':
    main()
    