import sympy
import concurrent.futures


def tCalculaPrimo(data):
    primos = 0
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            primos += 1
    return primos

def resolve_trhread(data, threads):
    #resultado melhor que o simples: 1 (5), 3 (1), 33 (1), 42 (1), 48 (1), 50 (1), 69 (1)
    if threads == 0:
        ThreadsQtdd = 1
    else:
        ThreadsQtdd = threads
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(tCalculaPrimo, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            #futures.append(future.result())
            primos += future.result()
    return primos
