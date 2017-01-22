import random
import operator
from decimal import Decimal

# numero de iteraciones
ITERACIONES = 1000
# array de amigos
amigos_original = ['Pixie', 'Dixie', 'Tom', 'Jerry', 'Piolín', 'Lucas', 'Correcaminos', 'Donald', 'Mickey', 'Pluto']
# diccionario donde acumularemos las distintas parejas y sus coincidencias
resultados = {}

def extraer_pareja(amigos):

    pareja = []
    for i in range(0, 2):
        pareja.append(amigos.pop(random.randint(0, len(amigos) - 1)))

    # clave del diccionario del tipo nombre_nombre
    # ordenamos la pareja para no repetir las combinaciones cruzadas, p.ej Mickey_Donald es igual a Donald_Mickey
    return '_'.join(sorted(pareja))


def iteracion(amigos):

    while len(amigos) > 1:
        key_pareja = extraer_pareja(amigos)
        if key_pareja in resultados:
            resultados[key_pareja] += 1
        else:
            resultados[key_pareja] = 1


# Hacemos las iteraciones
for i in range(0, ITERACIONES):
    amigos_copia = amigos_original[:]
    iteracion(amigos_copia)

# Todas las parejas con sus coincidencias
print (resultados)

# La suma de todas las coincidencias debe ser:
# iteraciones * numero de amigos / 2
print (sum(resultados.values()))

# Calculamos porcentajes
def porcentaje(valor):
    return round(float(valor) / ITERACIONES * 100, 2)
resultados = {k: porcentaje(v) for k, v in resultados.items()}

# Ordenamos los resultados por numero de coincidencias (descendente)
resultados = sorted(resultados.items(), key=operator.itemgetter(1), reverse=True)
print (resultados)

# Los cinco primeros
ganadores = resultados[:5]

print("####################")
print("####################")
print("####################")
print("####################")
print("Y los ganadores son:")
for pareja in ganadores:
    print(pareja[0].replace("_", " y ") + ": " +  str(pareja[1]) + "%")
