import time

def generador_primos():
    # Implementacion del algoritmo "Criba de Erastotenes"

    # Diccionario donde vamos almacenando los numeros no primos
    D = {};
    # Empezamos por 2, que es el primer numero primo
    q = 2;
    
    while True:
        if q not in D:
            # Si no esta en el diccionario, es primo
            yield q
            # Añadimos al diccionario un elemento con:
            # Clave; el primer multiplo de q que sabemos que no ya marcado
            # Valor: una lista iniciada con el numero primo
            D[q*q] = [q]
        else:
            # Si ya hemos marcado previamente el numero como no primo
            for p in D[q]:
                # Mueve cada testigo a su siguiente multiplo
                D.setdefault(p + q, []).append(p)
            # Borramos del diccionario para liberar memoria
            del D[q]
        # Siguiente numero
        q += 1

# Llamamos a la funcion, devuelve un generador
primes = generador_primos()

# Generamos numeros primos, con un sleep, para que se vayan viendo
print("Lista de numeros primos")
for i in primes:
    print(i);
    time.sleep(.200)

