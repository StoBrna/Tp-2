open('peajes.txt', "r").read()

letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

digits = ('', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

def leer_idioma():
    with open('peajes.txt', 'rt') as m:
        line = m.readline()
        if line[8] == "P":
            idioma = "Portugués"
        else:
            idioma = 'Español'

    return idioma

def identificar_pais():
    argentina = 0
    brazil = 0
    uruguay = 0
    paraguay = 0
    bolivia = 0
    chile = 0

    if len(patent) != 7:
        None

    else:
        if patent[0] in digits:
            chile += 1

        else:
            argentina += 1
            brazil += 1
            uruguay += 1
            paraguay += 1
            bolivia += 1

        if patent[1] in digits:
            None

        else:
            argentina += 1
            brazil += 1
            uruguay += 1
            paraguay += 1
            bolivia += 1
            chile += 1

        if patent[2] in digits:
            argentina += 1
            bolivia += 1

        else:
            brazil += 1
            uruguay += 1
            paraguay += 1
            chile += 1

        if patent[3] in digits:
            argentina += 1
            brazil += 1
            uruguay += 1
            bolivia += 1

        else:
            paraguay += 1
            chile += 1

        if patent[4] in digits:
            argentina += 1
            uruguay += 1
            paraguay += 1
            bolivia += 1
            chile += 1

        else:
            brazil += 1

        if patent[5] in digits:
            brazil += 1
            uruguay += 1
            paraguay += 1
            bolivia += 1

        else:
            argentina += 1
            chile += 1

        #if chile == 6 and len(patent) == 6:
            #None

        if patent[6] in digits:
            brazil += 1
            uruguay += 1
            paraguay += 1
            bolivia += 1
        else:
            argentina += 1
            chile += 1

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
idioma = leer_idioma()

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
    cabinas brasileñas:', prom, '\bkm')'''