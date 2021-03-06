"""
N oferentes, N candidatos

Inicialmente todos estan sin pareja
Mientras haya oferentes libres que no hayan agotados sus opciones (1) 
    Seleccionar O un oferente de 1
    Sea C el candidato de > preferencia de O al que no le propuso
    Si C esa disponible
        (O, C) se comprometen
    Si no
        Sea O' el oferente actual de C
        Si C prefiere a O sobre O'
            (O, C) se comprometen y O' queda libre
"""

# ranking_oferentes diccionario con clave 'oferente' y valor lista ordenada de lista de candidatos con igual prioridad
# ranking_candidatos diccionario con clave 'candidato'  y valor diccionario con clave 'oferente' y valor ranking

def gale_shapley(oferentes, ranking_oferentes, ranking_candidatos):
    parejas = {}
    oferentes_libres = oferentes[:]
    while (oferentes_libres):
        oferente  = oferentes_libres.pop()
        candidato = ranking_oferentes[oferente].first().pop()
        if not ranking_oferentes[oferente].first():
            ranking_oferentes[oferente].popleft()
        
        if not candidato in parejas:
            parejas[candidato] = oferente
            continue
        
        oferente_actual = parejas[candidato]
  
        r_oferente, r_oferente_actual = [ranking_candidatos[candidato][o] for o in [oferente, oferente_actual]]
          
        if r_oferente < r_oferente_actual:
            parejas[candidato] = oferente
            oferentes_libres.append(oferente_actual)
        
        else:
            oferentes_libres.append(oferente)
     
    return parejas

