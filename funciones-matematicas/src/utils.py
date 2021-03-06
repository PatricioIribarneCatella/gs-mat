#
# Calcula las variaciones de 'n' elementos
# tomados de a 'r' elementos. 
#
# El parámetro opcional 'filtrar'
# especifica si se deben remover los resultados
# que contienen los mismos elementos:
#
#   - True: se filtrar -> variaciones/permutaciones sin repetición
#   - False: no filtrar -> variaciones con repetición
#

#
# Calcula el producto cartesiano
# entre un vector consigo mismo
# con la cantidad de elementos 'repetir'
#
def producto(datos, repetir=1):

    replicas = [tuple(datos)] * repetir
    indices = [[]]
    
    for rep in replicas:
        indices = [x+[y] for x in indices for y in rep]
    
    for idx in indices:
        yield tuple(idx)
#
# Calcula las variaciones de 'n = len(data)'
# tomados de a 'r' elementos. Si r == n
# es equivalente a las permutaciones de 'n'
# elementos.
#
def calcular_variaciones(data, r=None, filtrar=True):
    
    n = data.size()

    r = n if r is None else r

    for indices in producto(range(n), r):
        if filtrar:
            # Filtra, luego de generar un set,
            # las posibilidades que no tengan como
            # longitud la especificada en 'r' (cantidad
            # de elementos a tomar)
            #
            if len(set(indices)) == r:
                yield tuple(data.get(i) for i in indices)
        else:
            yield tuple(data.get(i) for i in indices)

