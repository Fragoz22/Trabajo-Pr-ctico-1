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

else:

    if len(cp) == 4:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales:
            cp = "Bolivia"
            pais_destino = "Bolivia"
        else:
            cp = "Otros países"
    else:
        if len(cp) == 5:
            if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales:

                if cp[0] == "1":
                    pais_destino = "Uruguay Montevideo"
                    cp = "Uruguay"
                else:
                    cp = "Uruguay"
                    pais_destino = "Uruguay No Montevideo"
            else:
                cp = "Otros países"
        else:
            if len(cp) == 6:
                if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                        reales and cp[5] in reales):
                    cp = "Paraguay"
                else:
                    cp = "Otros países"
            else:
                if len(cp) != 6 and len(cp) == 7:
                    if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                            reales and cp[5] in reales and cp[6] in reales):
                        cp = 'Chile'
                    else:
                        cp = "Otros países"
                else:
                    if len(cp) == 9:
                        if (cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in
                                reales and cp[5] in reales and cp[6] in reales and cp[7] in reales and cp[8] in reales):
                            cp = "Brasil"
                            if cp[0] == "8" or cp[0] == 9:
                                region_Brasil = "a"
                            elif cp[0] == "0" or cp[0] == "1" or cp[0] == "2" or cp[0] == "3":
                                region_Brasil = "b"
                            elif cp[0] == "4" or cp[0] == "5" or cp[0] == "6" or cp[0] == "7":
                                region_Brasil = "c"
                        else:
                            cp = "Otros países"
