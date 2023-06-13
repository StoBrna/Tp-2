open('peajes.txt', "r").read()

def leer_idioma():
    with open('peajes.txt', 'rt') as open:
        line = m.readline()
        if line[8] == "P":
            idioma = "Portugués"
        else:
            idioma = 'Español'

    return idioma


'''
 code = int(line[0:4])
 country = line[4:7]
 year = int(line[7:11])
 print('Código postal:', code)
 print('País:', country)
 print('Año:', year)

 m.close()

'''


def principal():
    print('(r1) - Idioma a usar en los informes:', idioma)
    print()


principal()

'''
    print('(r2) - Cantidad de patentes de Argentina:', carg)
    print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    print('(r2) - Cantidad de patentes de Brasil:', cbra)
    print('(r2) - Cantidad de patentes de Chile:', cchi)
    print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    print('(r2) - Cantidad de patentes de Uruguay:', curu)
    print('(r2) - Cantidad de patentes de otro país:', cotr)
    print()
    print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)
    print()
    print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de
    aparición:', cpp)
    print()
    print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró
    ese importe:', maypat)
    print()
    print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
    print()
    print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por
    cabinas brasileñas:', prom, '\bkm')

''