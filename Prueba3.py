cp = input("Ingrese el código postal del lugar de destino: ")

# Establecer una bandera y poner en una tupla los numeros naturales

ban = True
reales = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
provincia = ("Salta", "Provincia de Buenos Aires", "Ciudad Autónoma de Buenos Aires", "San Luis", "Entre Ríos",
             "La Rioja", "Santiago del Estero", "Chaco", "San Juan", "Catamarca", "La Pampa", "Mendoza", "Misiones",
             "Formosa", "Neuquén", "Río Negro", "Santa Fe", "Tucumán", "Chubut", "Tierra del Fuego", "Corrientes",
             "Córdoba", "Jujuy", "Santa Cruz")
pais_destino = 0
region_Brasil = 0

if len(cp) > 9 or len(cp) < 4:
    ban = False
    if ban == False:
        cp = "Otros Países"
        provincia = "No Aplica"

else:

    if len(cp) == 4:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales:
            cp = "Bolivia"
            pais_destino = "Bolivia"
            provincia = "No Aplica"
        else:
            cp = "Otros países"
            provincia = "No Aplica"
    else:
        if len(cp) == 5:
            if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales:

                if cp[0] == "1":
                    pais_destino = "Uruguay Montevideo"
                    cp = "Uruguay"
                    provincia = "No Aplica"
                else:
                    cp = "Uruguay"
                    pais_destino = "Uruguay No Montevideo"
                    provincia = "No Aplica"
            else:
                cp = "Otros países"
                provincia = "No Aplica"
        else:
            if len(cp) == 6:
                if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                        reales and cp[5] in reales):
                    cp = "Paraguay"
                    provincia = "No Aplica"
                else:
                    cp = "Otros países"
                    provincia = "No Aplica"
            else:
                if len(cp) != 6 and len(cp) == 7:
                    if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                            reales and cp[5] in reales and cp[6] in reales):
                        cp = "Chile"
                        provincia = "No Aplica"
                    else:
                        cp = "Otros países"
                        provincia = "No Aplica"
                else:
                    if len(cp) == 9:
                        if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                                reales and cp[5] in reales and cp[6] in reales and cp[7] in reales and cp[8] in reales):
                            cp = "Brasil"
                            provincia = "No Aplica"
                            if cp[0] == "8" or cp[0] == 9:
                                region_Brasil = "a"
                            elif cp[0] == "0" or cp[0] == "1" or cp[0] == "2" or cp[0] == "3":
                                region_Brasil = "b"
                            elif cp[0] == "4" or cp[0] == "5" or cp[0] == "6" or cp[0] == "7":
                                region_Brasil = "c"

                        else:
                            cp = "Otros países"
                            provincia = "No Aplica"
                    else:
                        if len(cp) == 8 and (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales
                                             and cp[5] not in reales and cp[1] in reales and cp[2] in reales and cp[3]
                                             in reales and cp[4] in reales):
                            if cp[7] == "A":
                                provincia = (provincia[0])
                            elif cp[7] == "B":
                                provincia = (provincia[1])
                            elif cp[7] == "C":
                                provincia = (provincia[2])
                            elif cp[7] == "D":
                                provincia = (provincia[3])
                            elif cp[7] == "E":
                                provincia = (provincia[4])
                            elif cp[7] == "F":
                                provincia = (provincia[5])
                            elif cp[7] == "G":
                                provincia = (provincia[6])
                            elif cp[7] == "H":
                                provincia = (provincia[7])
                            elif cp[7] == "J":
                                provincia = (provincia[8])
                            elif cp[7] == "K":
                                provincia = (provincia[9])
                            elif cp[7] == "L":
                                provincia = (provincia[10])
                            elif cp[7] == "M":
                                provincia = (provincia[11])
                            elif cp[7] == "N":
                                provincia = (provincia[12])
                            elif cp[7] == "P":
                                provincia = (provincia[13])
                            elif cp[7] == "Q":
                                provincia = (provincia[14])
                            elif cp[7] == "R":
                                provincia = (provincia[15])
                            elif cp[7] == "S":
                                provincia = (provincia[16])
                            elif cp[7] == "T":
                                provincia = (provincia[17])
                            elif cp[7] == "U":
                                provincia = (provincia[18])
                            elif cp[7] == "V":
                                provincia = (provincia[19])
                            elif cp[7] == "W":
                                provincia = (provincia[20])
                            elif cp[7] == "X":
                                provincia = (provincia[21])
                            elif cp[7] == "Y":
                                provincia = (provincia[22])
                            elif cp[7] == "Z":
                                provincia = (provincia[23])
                            else:
                                provincia = "No aplica"
                            if (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[
                                5] not in reales and cp[1] in reales
                                    and cp[2] in reales and cp[3] in reales and cp[4] in reales):
                                cp = "Argentina"
                            else:
                                cp = "Otros países"
                        else:
                            provincia = "No aplica"
