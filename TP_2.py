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
    #print(patente)
    if(is_digit(patente[0])):
        print("Empieza con numero")
    else:
        print("Empieza con letra")    


def principal():
    idioma = leer_idioma()
    print('(r1) - Idioma a usar en los informes:', idioma) 
    with open('peaje25.txt', 'rt') as m:
        patente = m.readline() 
        while(patente != ""):
            identificar_patente(patente)
            patente = m.readline()

principal()