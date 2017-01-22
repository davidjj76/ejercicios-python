import operator


ciclistas = ['Miguel Indurain', 'Eddy Mercks', 'Bernard Hinault', 'Jacques Anquetil', 'Lance Amstrong']
tiempos = [[10158.1, 12458.0, 13985.3, 10336.0, 10369.8],
           [10245.3, 12478.4, 14123.1, 10236.9, 10398.7],
           [10102.6, 12697.4, 14025.2, 10486.4, 10245.6],
           [10100.7, 12500.8, 13987.6, 10247.3, 10457.7],
           [10152.2, 12453.9, 14100.7, 10364.5, 10211.1]]



def ordenar_clasificacion(clasificacion):
    # Ordenamos la clasificacion
    return sorted(clasificacion.items(), key=operator.itemgetter(1))


def ganador_de_la_vuelta(ciclistas, tiempos):

    try:
        indice = 0
        clasificacion_general = {}

        # Calculamos los tiempos totales de cada ciclista
        for ciclista in ciclistas:
            clasificacion_general[ciclista] = sum(tiempos[indice])
            indice += 1

        # Sacamos el ganador
        ganador = ordenar_clasificacion(clasificacion_general)[0]

        print("El ganador de la vuelta es " + ganador[0] + " con un tiempo de " + str(ganador[1]) + " segundos")

    except Exception as e:
        print(str(e))


def ganador_de_la_etapa(ciclistas, tiempos, etapa):

    try:
        if etapa not in range(1, len(tiempos[0]) + 1):
            raise ValueError('Numero de etapa no existe')

        indice = 0
        clasificacion_etapa = {}

        # Calculamos los tiempos de cada ciclista en la etapa
        for ciclista in ciclistas:
            clasificacion_etapa[ciclista] = tiempos[indice][etapa - 1]
            indice += 1

        # Sacamos el ganador
        ganador = ordenar_clasificacion(clasificacion_etapa)[0]

        print("El ganador de la etapa " + str(etapa) + " es " + ganador[0] + " con un tiempo de " + str(ganador[1]) + " segundos")

    except Exception as e:
        print(str(e))

def ganadores_de_etapa(ciclistas, tiempos):

    try:
        for etapa in range(1, len(tiempos[0]) + 1):
            ganador_de_la_etapa(ciclistas, tiempos, etapa)

    except Exception as e:
        print(str(e))



print("### Ganador de la vuelta ###")
ganador_de_la_vuelta(ciclistas, tiempos)
print()

print("### Ganador de etapa ###")
ganador_de_la_etapa(ciclistas, tiempos, 3)
print()

print("### Ganadores de etapa ###")
ganadores_de_etapa(ciclistas, tiempos)
print()
