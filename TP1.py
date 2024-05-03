# Inicio de TP 1


# Carga de datos

cp = input("Ingrese el código postal del lugar de destino: ")

# Establecer una bandera y poner en una tupla los numeros naturales

ban = True
reales = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
provincia = ("Salta", "Provincia de Buenos Aires", "Ciudad Autónoma de Buenos Aires", "San Luis", "Entre Ríos",
             "La Rioja", "Santiago del Estero", "Chaco", "San Juan", "Catamarca", "La Pampa", "Mendoza", "Misiones",
             "Formosa", "Neuquén", "Río Negro", "Santa Fe", "Tucumán", "Chubut", "Tierra del Fuego", "Corrientes",
             "Córdoba", "Jujuy", "Santa Cruz")

if len(cp) > 9 or len(cp) < 4:
    ban = False
    if ban == False:
        print("Otros Países")

else:

    if len(cp) == 4:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales:
            print("Bolivia")
        else:
            print("Otros países")

    if len(cp) == 5:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales:
            print("Uruguay")
        else:
            print("Otros países")

    if len(cp) == 6:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
    5] in reales:
            print("Paraguay")
        else:
            print("Otros países")

    if len(cp) == 7:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
        5] in reales and cp[6] in reales:
            print("Chile")
        else:
            print("Otros países")

    if len(cp) == 9:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
        5] in reales and cp[6] in reales and cp[7] in reales and cp[8] in reales:
            print("Brasil")
        else:
            print("Otros países")
    if len(cp) == 8:
        if (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[5] not in reales and cp[1] in reales
        and cp[2] in reales and cp[3] in reales and cp[4] in reales):
            print("Argentina")
        else:
            print("Otros países")
        if cp[7] == 'A':
            print(provincia[0])
        elif cp[7] == 'B':
            print(provincia[1])
        elif cp[7] == 'C':
            print(provincia[2])
        elif cp[7] == 'D':
            print(provincia[3])
        elif cp[7] == 'E':
            print(provincia[4])
        elif cp[7] == 'F':
            print(provincia[5])
        elif cp[7] == 'G':
            print(provincia[6])
        elif cp[7] == 'H':
            print(provincia[7])
        elif cp[7] == 'J':
            print(provincia[8])
        elif cp[7] == 'K':
            print(provincia[9])
        elif cp[7] == 'L':
            print(provincia[10])
        elif cp[7] == 'M':
            print(provincia[11])
        elif cp[7] == 'N':
            print(provincia[12])
        elif cp[7] == 'P':
            print(provincia[13])
        elif cp[7] == 'Q':
            print(provincia[14])
        elif cp[7] == 'R':
            print(provincia[15])
        elif cp[7] == 'S':
            print(provincia[16])
        elif cp[7] == 'T':
            print(provincia[17])
        elif cp[7] == 'U':
            print(provincia[18])
        elif cp[7] == 'V':
            print(provincia[19])
        elif cp[7] == 'W':
            print(provincia[20])
        elif cp[7] == 'X':
            print(provincia[21])
        elif cp[7] == 'Y':
            print(provincia[22])
        elif cp[7] == 'Z':
            print(provincia[23])
        else:
            print('No aplica')
