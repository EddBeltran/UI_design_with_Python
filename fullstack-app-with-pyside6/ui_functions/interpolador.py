import numpy as np

def interpolador_lineal(x, y, nodos, ultimo_punto=False):
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
    if nodos > len(x):
        puntos_x, puntos_y, distancia = np.zeros(0), np.zeros(0), np.zeros(len(x)-1)
        puntos_por_segmento, fraccion_punto = np.zeros(len(x)-1), np.zeros(len(x)-1)
    
        for i in range(0, len(distancia)):
            distancia[i] = ((x[i+1] - x[i]) ** 2 + (y[i+1] - y[i]) ** 2) ** 0.5 #calculamos las distancias entre cada segmento de recta
        dist_tot = sum( distancia )
        
        #Primera distribución de puntos a lo largo de los segmentos que conforman la polilinea
        for i in range(0, len(distancia)):
            dist_ratio = (distancia[i] / dist_tot)                         #  Razon entre distancia entre cada segmento y distancia total de la polilinea  
            fraccion_punto[i] = dist_ratio*nodos - int(dist_ratio*nodos)   #  Guardamos las fraccciones de los puntos
            puntos_por_segmento[i] = int(dist_ratio*nodos)                  #  Calculamos los puntos a distribuir en cada segmento
           
        nodos_real = int(sum(puntos_por_segmento))   # Calculamos cuantos nodos totales tiene la polilinea 
        diff_nodos = (nodos - 1) - nodos_real        # Restamos 1 a nodos debido a que no se cosidera el ultimo punto (utimo=False)
        
        frac_por_punto_mas_a_menos = np.sort(fraccion_punto)[::-1]
        frac_por_punto_menos_a_mas = np.sort(fraccion_punto)[::1]
        limite_for = abs(diff_nodos)

        for j in range(0, limite_for):
            if diff_nodos > 0:
                index, = np.where(fraccion_punto == frac_por_punto_mas_a_menos[j])
                puntos_por_segmento[index[0]] = puntos_por_segmento[index[0]] + 1
                fraccion_punto[index[0]] = 0
            else:
                index, = np.where(fraccion_punto == frac_por_punto_menos_a_mas[j])
                puntos_por_segmento[index[0]] = puntos_por_segmento[index[0]] - 1
                fraccion_punto[index[0]] = 1
        
        #Se genera la interpolación para cada segmento de recta y se agregan a un solo arreglo
        for i in range(0, len(distancia)):
            sub_puntos_x = np.linspace(x[i],x[i+1], int(puntos_por_segmento[i]), endpoint=False) 
            sub_puntos_y = np.linspace(y[i],y[i+1], int(puntos_por_segmento[i]), endpoint=False)
            puntos_x = np.append(puntos_x, sub_puntos_x)
            puntos_y = np.append(puntos_y, sub_puntos_y)
        
        if (ultimo_punto):
            puntos_x = np.append(puntos_x, x[len(x)-1])
            puntos_y = np.append(puntos_y, y[len(y)-1])
    else:
        print("Nodos debe ser mayor a los puntos de control")
        puntos_x, puntos_y = x, y

    return puntos_x, puntos_y


def interp_cuadratic_bezier(x, y, nodos, ultimo_punto=False):
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
    delta = (0.9963*(nodos-1))**(-0.998) # Correlación para obtener los puntos deseados
    t = 0
    while t<1:
        xs = (1-t)**2 * x[0] + 2*(1-t)*t*x[1] + t**2*x[2]
        ys = (1-t)**2 * y[0] + 2*(1-t)*t*y[1] + t**2*y[2]
        x_curva = np.append(x_curva, xs); y_curva = np.append(y_curva, ys)
        t = t + delta
    # Se elimina el ultimo punto si ultimo_punto = False
    if (ultimo_punto):
        x_curva = np.append(x_curva, x[2]); y_curva = np.append(y_curva, y[2])
    
    return x_curva, y_curva


def interp_cubic_bezier(x, y, nodos, ultimo_punto=False):
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
    delta = (0.9963*(nodos-1))**(-0.998) # Correlación para obtener los puntos deseados
    t = 0
    while t<1:
        xs = (1-t)**3*x[0] + 3*t*(1-t)**2*x[1] + 3*t**2*(1-t)*x[2] + t**3*x[3]
        ys = (1-t)**3*y[0] + 3*t*(1-t)**2*y[1] + 3*t**2*(1-t)*y[2] + t**3*y[3]
        x_curva = np.append(x_curva, xs); y_curva = np.append(y_curva, ys)
        t = t + delta
    # Se elimina el ultimo punto si ultimo_punto = False
    if (ultimo_punto):
        x_curva = np.append(x_curva, x[2]); y_curva = np.append(y_curva, y[2])

    return x_curva, y_curva

def calculate_control_point_cuadratic_bezier(x, y):
    u = 0.5
    x2 = (1/(2*(1-u)*u))*x[1] - ((1-u)/(2*u))*x[0] - (u/(2*(1-u)))*x[2]
    y2 = (1/(2*(1-u)*u))*y[1] - ((1-u)/(2*u))*y[0] - (u/(2*(1-u)))*y[2]
    return x2, y2

def calculate_control_points_cubic_bezier(x, y):
    r = 2
    x2 = (x[0] + r * x[1]) / (1 + r)
    y2 = (y[0] + r * y[1]) / (1 + r)

    x3 = (x[2] + r * x[1]) / (1 + r)
    y3 = (y[2] + r * y[1]) / (1 + r)
    return x3, y3, x3, y3


def euclidian_distance(x,y):
    distancia = np.zeros(len(x)-1)
    for i in range(0, distancia):
        distancia[i] = ((x[i+1] - x[i]) ** 2 + (y[i+1] - y[i]) ** 2) ** 0.5 #calculamos las distancias entre cada segmento de recta
    
    return sum( distancia )

