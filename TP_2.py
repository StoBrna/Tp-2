open('peaje25.txt', "r").read() 

letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

digits = (" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

def is_digit(character):
    if(character in digits):
        return True
    return False

def leer_idioma():
    with open('peaje25.txt', 'rt') as m:
        line = m.readline()
        if (line.__contains__("P")):
            idioma = "Portugués"
        else:
            idioma = 'Español'

    return idioma

def identificar_patente(patente):

    if len(patente) != 14:
        return "n"

    argentina = 0
    brazil = 0
    uruguay = 0
    paraguay = 0
    bolivia = 0
    chile = 0

    if(is_digit(patente[0])):
        chile += 1

    else:
        argentina += 1
        brazil += 1
        uruguay += 1
        paraguay += 1
        bolivia += 1

    if(is_digit(patente[1])):
        None

    else:
        argentina += 1
        brazil += 1
        uruguay += 1
        paraguay += 1
        bolivia += 1
        chile += 1

    if(is_digit(patente[2])):
        argentina += 1
        bolivia += 1

    else:
        brazil += 1
        uruguay += 1
        paraguay += 1
        chile += 1

    if(is_digit(patente[3])):
        argentina += 1
        brazil += 1
        uruguay += 1
        bolivia += 1

    else:
        paraguay += 1
        chile += 1

    if(is_digit(patente[4])):
        argentina += 1
        uruguay += 1
        paraguay += 1
        bolivia += 1

    else:
        brazil += 1
        chile += 1

    if(is_digit(patente[5])):
        brazil += 1
        uruguay += 1
        paraguay += 1
        bolivia += 1
        chile += 1
    else:
        argentina += 1

    if(is_digit(patente[6])):
        brazil += 1
        uruguay += 1
        paraguay += 1
        bolivia += 1
        chile += 1
    else:
        argentina += 1

    if argentina == 7:
        return "ar"
    elif brazil == 7:
        return "br"
    elif bolivia == 7:
        return "bo"
    elif uruguay == 7:
        return "uy"
    elif chile == 7:
        return "ch"
    elif paraguay == 7:
        return "pa"
    else:
        return "n"

def monto_pais(patente):
    print(patente[0])
    pais = None
    return

    if patente[9] == "0" or patente[9] == "3" or patente[9] == "4":
        pais = 300
    elif patente[9] == "1":
        pais = 200
    else:
        pais = 400

    return pais


def principal():

    count_argentina = 0
    count_brazil = 0
    count_chile = 0
    count_paraguay = 0
    count_bolivia = 0
    count_uruguay = 0
    count_none = 0

    idioma = leer_idioma()
    with open('peaje25.txt', 'rt') as m:
        patente = m.readline()
        patente = m.readline()
        patente = m.readline()
        monto = monto_pais(patente)
        while(patente != ""):
            patente_identificada = identificar_patente(patente)
            patente = m.readline()
            if patente_identificada == "ar":
                count_argentina += 1
            elif patente_identificada == "br":
                count_brazil += 1
            elif patente_identificada == "ch":
                count_chile += 1
            elif patente_identificada == "pa":
                count_paraguay += 1
            elif patente_identificada == "bo":
                count_bolivia += 1
            elif patente_identificada == "uy":
                count_uruguay += 1
            elif patente_identificada == "n":
                count_none += 1

        monto = monto_pais(patente)
        #print(monto)

    print('(r1) - Idioma a usar en los informes:', idioma)
    print()
    print('(r2) - Cantidad de patentes de Argentina:', count_argentina)
    print('(r2) - Cantidad de patentes de Bolivia:', count_bolivia)
    print('(r2) - Cantidad de patentes de Brasil:', count_brazil)
    print('(r2) - Cantidad de patentes de Chile:', count_chile)
    print('(r2) - Cantidad de patentes de Paraguay:', count_paraguay)
    print('(r2) - Cantidad de patentes de Uruguay:', count_uruguay)
    print('(r2) - Cantidad de patentes de otro país:', count_none)


principal()