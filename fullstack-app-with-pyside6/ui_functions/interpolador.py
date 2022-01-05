import numpy as np

def interp_polilinea(x, y, nodos, ultimo_punto=False):
    """Esta función genera los puntos intermedios (`nodos`) para una polilinea dados los puntos p1(`x1`, `y1`),
    p2(`x2`, `y2`), ..., pk(`xk`, `yk`).    

    Parametros
    ----------
    x, y : array_like or list.
        Arreglos a la entrada, `x` -> [`x1`,`x2`, ..., `xk`], `y`-> [`y1`,`y2`, ..., `yk`].
    nodos : int.
        Puntos distribuidos a lo largo de la polilinea.
    ultimo_punto: bool. Por default no se agrega el ultimo punto del segmento.

    Retorna
    -------
    ndarray, ndarray. 
        Arreglos de puntos para x e y dentro de una linea recta.
    """
    puntos_x, puntos_y, distancia = np.zeros(0), np.zeros(0), np.zeros(len(x)-1)
    puntos_por_arreglo, fraccion_punto = np.zeros(len(x)-1), np.zeros(len(x)-1)

    for i in range(0, len(distancia)):
        distancia[i] = ((x[i+1] - x[i]) ** 2 + (y[i+1] - y[i]) ** 2) ** 0.5 #calculamos las distancias entre cada segmento de recta
    dist_tot = sum( distancia )
    
    #Primera distribución de puntos a lo largo de los segmentos que conforman la polilinea
    for i in range(0, len(distancia)):
        dist_ratio = (distancia[i] / dist_tot)                         #  Razon entre distancia entre cada segmento y distancia total de la polilinea  
        fraccion_punto[i] = dist_ratio*nodos - int(dist_ratio*nodos)   #  Guardamos las fraccciones de los puntos
        puntos_por_arreglo[i] = int(dist_ratio*nodos)                  #  Calculamos los puntos a distribuir en cada segmento
       
    nodos_real = int(sum(puntos_por_arreglo))    # Calculamos cuantos nodos totales tiene la polilinea 
    diff_nodos = nodos - nodos_real              # Calculamos la diferencia entre nodos ideales y reales
    ordenar_arr = np.sort(fraccion_punto)[::-1]  # Invertimos el arreglo de fracciones de punto
    
    #Segunda distribucion de puntos   -->  dependiendo de la diferencia entre nodos, se agregan 1 punto a los segmentos con mayor fraccion de punto 
    for j in range(0, diff_nodos - 1):
        for i in range(0, len(distancia)):
            if ordenar_arr[j] == fraccion_punto[i]:
                puntos_por_arreglo[i] = puntos_por_arreglo[i] + 1
    
    #Se genera la interpolación para cada segmento de recta y se agregan a un solo arreglo
    for i in range(0, len(distancia)):
        sub_puntos_x = np.linspace(x[i],x[i+1], int(puntos_por_arreglo[i]), endpoint=False) 
        sub_puntos_y = np.linspace(y[i],y[i+1], int(puntos_por_arreglo[i]), endpoint=False)
        
        puntos_x = np.append(puntos_x, sub_puntos_x)
        puntos_y = np.append(puntos_y, sub_puntos_y)
    
    if (ultimo_punto):
        puntos_x = np.append(puntos_x, x[len(x)-1])
        puntos_y = np.append(puntos_y, y[len(y)-1])

    return puntos_x, puntos_y


def interp_linea(x, y, nodos, ultimo_punto=False):
    """Esta función genera los puntos intermedios (`nodos`) para una linea recta dados los puntos p1(`x1`, `y1`) y
    p2(`x2`, `y2`).    

    Parametros
    ----------
    x, y : array_like or list.
        Arreglos a la entrada, `x` -> [`x1`,`x2`], `y`-> [`y1`,`y2`].
    nodos : int.
        Puntos dentro del segmento de recta.
    ultimo_punto: bool. Por default no se agrega el ultimo punto del segmento.

    Retorna
    -------
    ndarray, ndarray. 
        Arreglos de puntos para x e y dentro de una linea recta.
    """
    puntos_x = np.linspace(x[0],x[1], nodos-1, endpoint=False)
    puntos_y = np.linspace(y[0],y[1], nodos-1, endpoint=False)

    if (ultimo_punto):
        puntos_x = np.append(puntos_x, x[1]); puntos_y = np.append(puntos_y, y[1])
    
    return puntos_x, puntos_y


def interp_curva_bezier(x, y, nodos, ultimo_punto=False):
    """Esta función genera los puntos intermedios (`nodos`) de curva  dada la formula de Bezier y  los puntos p1(`x1`, `y1`),
    p2(`x2`, `y2`) y p3(`x3`, `y3`).    

    Parametros
    ----------
    x, y : array_like or list.
        Arreglos a la entrada, `x` -> [`x1`,`x2`,`x3`], `y`-> [`y1`,`y2`,`y3`].
    nodos : int.
        Puntos dentro de la curva de Bezier.
    ultimo_punto: bool. Por default no se agrega el ultimo punto a la curva.

    Retorna
    -------
    ndarray, ndarray.
        Arreglos de puntos para x e y dentro de la curva.
    """
    x_curva, y_curva = np.zeros(0), np.zeros(0)
    u, k = 0.5, 2   #u es un parametro de ajuste para determinar en segundo punto de la curva
    
    # Se calcula el punto maximo/minimo que pasa por la curva
    x2 = (1/(2*(1-u)*u))*x[k-1] - ((1-u)/(2*u))*x[k-2] - (u/(2*(1-u)))*x[k]
    y2 = (1/(2*(1-u)*u))*y[k-1] - ((1-u)/(2*u))*y[k-2] - (u/(2*(1-u)))*y[k]
    
    delta = (0.9963*(nodos-1))**(-0.998) # La correlación genera el delta ideal que se adecua al numero de nodos deseado
    
    #Se genera la curva de Bezier de acuerdo al delta
    t = 0
    while t<1:
        xs = (1-t)**2 * x[k-2] + 2*(1-t)*t*x2 + t**2*x[k]
        ys = (1-t)**2 * y[k-2] + 2*(1-t)*t*y2 + t**2*y[k]
        x_curva = np.append(x_curva, xs); y_curva = np.append(y_curva, ys)
        t = t + delta
    
    # Se elimina el ultimo punto si ultimo_punto = False
    if (ultimo_punto):
        x_curva = np.append(x_curva, x[2]); y_curva = np.append(y_curva, y[2])
    
    #print("nodos", len(x_curva))
    return x_curva, y_curva


"""
import matplotlib.pyplot as plt

x , y = interp_polilinea([1,6,20], [1,10, 5], 10, ultimo_punto=False)
plt.plot(x,y, 'bo-')
plt.show()

"""