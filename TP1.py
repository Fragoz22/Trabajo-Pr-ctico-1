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
        cp = "Otros Países"

else:

    if len(cp) == 4:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales:
            cp = "Bolivia"
        else:
            cp ="Otros países"

    if len(cp) == 5:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales:
            cp = "Uruguay"
        else:
           cp = "Otros países"

    if len(cp) == 6:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
    5] in reales:
            cp = "Paraguay"
        else:
            cp = "Otros países"

    if len(cp) == 7:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
        5] in reales and cp[6] in reales:
            cp = 'Chile'
        else:
            cp = "Otros países"

    if len(cp) == 9:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
        5] in reales and cp[6] in reales and cp[7] in reales and cp[8] in reales:
            cp = "Brasil"
        else:
            cp = "Otros países"
    if len(cp) == 8 and (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[5] not in reales
                         and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales):
        if cp[7] == 'A':
            provincia = (provincia[0])
        elif cp[7] == 'B':
            provincia = (provincia[1])
        elif cp[7] == 'C':
            provincia = (provincia[2])
        elif cp[7] == 'D':
            provincia = (provincia[3])
        elif cp[7] == 'E':
            provincia = (provincia[4])
        elif cp[7] == 'F':
            provincia = (provincia[5])
        elif cp[7] == 'G':
            provincia = (provincia[6])
        elif cp[7] == 'H':
            provincia = (provincia[7])
        elif cp[7] == 'J':
            provincia = (provincia[8])
        elif cp[7] == 'K':
            provincia = (provincia[9])
        elif cp[7] == 'L':
            provincia = (provincia[10])
        elif cp[7] == 'M':
            provincia = (provincia[11])
        elif cp[7] == 'N':
            provincia = (provincia[12])
        elif cp[7] == 'P':
            provincia = (provincia[13])
        elif cp[7] == 'Q':
            provincia = (provincia[14])
        elif cp[7] == 'R':
            provincia = (provincia[15])
        elif cp[7] == 'S':
            provincia = (provincia[16])
        elif cp[7] == 'T':
            provincia = (provincia[17])
        elif cp[7] == 'U':
            provincia = (provincia[18])
        elif cp[7] == 'V':
            provincia = (provincia[19])
        elif cp[7] == 'W':
            provincia = (provincia[20])
        elif cp[7] == 'X':
            provincia = (provincia[21])
        elif cp[7] == 'Y':
            provincia = (provincia[22])
        elif cp[7] == 'Z':
            provincia = (provincia[23])
        else:
            provincia = 'No aplica'
        if (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[5] not in reales and cp[1] in reales
        and cp[2] in reales and cp[3] in reales and cp[4] in reales):
            cp = 'Argentina'
        else:
            cp = "Otros países"
    else:
        cp = 'Otros paises'
        provincia = 'No aplica'

#CARGA DE DATOS DE DIRECCION Y ENVIO
direccion = input("Dirección del lugar de destino: ")
#ASIGNACION DE TUPLAS/VARIABLES
tipo = int(input("Tipo de envío: "))
tipo_envio = ('Carta Simple', 'Carta Certificada', 'Carta Expresa')
peso = ('p < 20', '20 <= p < 150 ', '150 <= p < 500', 'p < 150', '150 <= p < 500', 'p < 150', '150 <= p < 500')
precio = ('1100', '1800', '2450', '8300', '10900', '14300', '17900')
pais_destino = ('Bolivia, Paraguay, Uruguay (Montevideo)', 'Chile, Uruguay (no Montevideo)', 'Brasil (regiones 8 y 9)',
                'Brasil (regiones 0, 1, 2 y 3)', 'Brasil (regiones 4, 5, 6 y 7)', 'Otros países')
precio_porc = '0'

if cp == 'Argentina':
    if tipo == 0:
        tipo_envio = 'Carta simple'
        peso = (peso[0])
        precio = (precio[0])
    if tipo == 1:
        tipo_envio = 'Carta simple'
        peso = (peso[1])
        precio = (precio[1])
    if tipo == 3:
        tipo_envio = 'Carta simple'
        peso = (peso[2])
        precio = (precio[2])
    if tipo == 3:
        tipo_envio = 'Carta certificada'
        peso = (peso[3])
        precio = (precio[3])
    if tipo == 4:
        tipo_envio = 'Carta certificada'
        peso = (peso[4])
        precio = (precio[4])
    if tipo == 5:
        tipo_envio = 'Carta Expresa'
        peso = (peso[5])
        precio = (precio[5])
    if tipo == 6:
        tipo_envio = 'Carta Expresa'
        peso = (peso[6])
        precio = (precio[6])
else:
    if tipo == 0:
        tipo_envio = 'Carta simple'
        peso = (peso[0])
    if tipo == 1:
        tipo_envio = 'Carta simple'
        peso = (peso[1])
    if tipo == 3:
        tipo_envio = 'Carta simple'
        peso = (peso[2])
    if tipo == 3:
        tipo_envio = 'Carta certificada'
        peso = (peso[3])
    if tipo == 4:
        tipo_envio = 'Carta certificada'
        peso = (peso[4])
    if tipo == 5:
        tipo_envio = 'Carta Expresa'
        peso = (peso[5])
    if tipo == 6:
        tipo_envio = 'Carta Expresa'
        peso = (peso[6])
    if pais_destino[0] in pais_destino:
        precio_porc = (int(precio[0]) + (int(precio[0]) * 20)) / 100
    if pais_destino[1] in pais_destino:
        precio_porc = (int(precio[1]) + (int(precio[1]) * 25)) / 100
    if pais_destino[2] in pais_destino:
        precio_porc = (int(precio[2]) + (int(precio[2]) * 20)) / 100
    if pais_destino[3] in pais_destino:
        precio_porc = (int(precio[3]) + (int(precio[3]) * 25)) / 100
    if pais_destino[4] in pais_destino:
        precio_porc = (int(precio[4]) + (int(precio[4]) * 30)) / 100
    if pais_destino[5] in pais_destino:
        precio_porc = (int(precio[5]) + (int(precio[5]) * 50)) / 100

print(peso)
print(tipo_envio)
print(precio_porc)
