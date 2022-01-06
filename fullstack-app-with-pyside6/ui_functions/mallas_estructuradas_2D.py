#   CENTRO NACIONAL DE INVESTIGACIÓN Y DESARROLLO TECNOLÓGICO
#   C E N I D E T 
#   Codigo original desarrollado por Dr. Victor Leonardo Teja 
#   Modificación del codigo original por Eduardo Beltrán, Nov 2021

import numpy as np
import math as mt

#-----------------------------------------------------------------------------#
# Interpolacion transfinita 2D -----------------------------------------------#
#-----------------------------------------------------------------------------#
def interpolacion_transfinita_2D(x, y, nodos_x, nodos_y):
    """Es un metodos algebraico que transforma el dominio original en uno canonico,
    mediante funciones de interpolación y partiendo de los nodos del contorno se generan los puntos interiores de la malla.    

    Parametros
    ----------
    x, y : array_like or list.
        Arreglos/listas 1D con las coordenadas del contorno a mallar `x` -> [`x1`,`x2`, ..., `xk`], `y`-> [`y1`,`y2`, ..., `yk`].
    nodos_x, nodos_y : int, int.
        Puntos distribuidos a lo largo 4 cuatro fronteras del dominio.

    Retorna
    -------
    ndarray, ndarray. 
        Arreglos en 2D para x e y de la malla.
    """

    malla_x, malla_y = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    xi, eta = np.zeros(nodos_x), np.zeros(nodos_y)
    frontera_norte_x, frontera_sur_x, frontera_norte_y, frontera_sur_y  = np.zeros(nodos_x), np.zeros(nodos_x), np.zeros(nodos_x), np.zeros(nodos_x)
    frontera_este_x, frontera_oeste_x, frontera_este_y, frontera_oeste_y  = np.zeros(nodos_y), np.zeros(nodos_y), np.zeros(nodos_y), np.zeros(nodos_y)
    
    #------- Asignación de las Fronteras para x e y --------#
    for i in range (0, nodos_x):
        frontera_sur_x[i] = x[i]
        frontera_sur_y[i] = y[i]

        frontera_norte_x[i] = x[nodos_x + nodos_y + nodos_x-1-(i+2)]
        frontera_norte_y[i] = y[nodos_x + nodos_y + nodos_x-1-(i+2)]
    
    for i in range (0, nodos_y):
        frontera_este_x[i] = x[nodos_x + i-1]
        frontera_este_y[i] = y[nodos_x + i-1]
        
        frontera_oeste_x[i] = x[(2*nodos_x + 2*nodos_y-2)-(i+2)]
        frontera_oeste_y[i] = y[2*nodos_x + 2*nodos_y-2-(i+2)]

    #  Calculo de xi e eta --> paramentros necesarios para hacer el cambio de coordenadas -----------#
    d_xi=1.0E+00/(nodos_x-1)
    for i in range (1, nodos_x):
        xi[i]=d_xi*(i)

    d_eta=1.0E+00/(nodos_y-1)
    for i in range (1, nodos_y):
        eta[i]=d_eta*(i)
    
    # Generacion de los puntos internos de la malla   
    for i in range (1, nodos_x-1):
        for j in range (1, nodos_y-1):
            malla_x[i][j]=((1.0E+00-eta[j])*frontera_sur_x[i]+eta[j]*frontera_norte_x[i]+
                         (1.0E+00-xi[i])*frontera_oeste_x[j]+xi[i]*frontera_este_x[j]-
                         (xi[i]*eta[j]*frontera_norte_x[nodos_x-1]+xi[i]*(1.0E+00-eta[j])*frontera_sur_x[nodos_x-1]+
                         eta[j]*(1.0E+00-xi[i])*frontera_norte_x[0]+
                         (1.0E+00-xi[i])*(1.0E+00-eta[j])*frontera_sur_x[0]))
            
            malla_y[i][j]=((1.0E+00-eta[j])*frontera_sur_y[i]+eta[j]*frontera_norte_y[i]+
                         (1.0E+00-xi[i])*frontera_oeste_y[j]+xi[i]*frontera_este_y[j]-
                         (xi[i]*eta[j]*frontera_norte_y[nodos_x-1]+xi[i]*(1.0E+00-eta[j])*frontera_sur_y[nodos_x-1]+
                         eta[j]*(1.0E+00-xi[i])*frontera_norte_y[0]+
                         (1.0E+00-xi[i])*(1.0E+00-eta[j])*frontera_sur_y[0]))
    
    #---  Asignación de los limites de la geometria en las fronteras ---#
    for i in range (0, nodos_x):
        malla_x[i][0] = frontera_sur_x[i]    #  Frontera Sur
        malla_y[i][0] = frontera_sur_y[i]    #  Frontera Sur
        
        malla_x[i][nodos_y-1] = frontera_norte_x[i]  #  Frontera Norte
        malla_y[i][nodos_y-1] = frontera_norte_y[i]  #  Frontera Norte
    
    for i in range(1, nodos_y-1):
        malla_x[0][i] = frontera_oeste_x[i]        #  Frontera Oeste
        malla_y[0][i] = frontera_oeste_y[i]        # Frontera Oeste

        malla_x[nodos_x-1][i] = frontera_este_x[i]   #  Frontera Este
        malla_y[nodos_x-1][i] = frontera_este_y[i]   # Frontera Este  
    
    return malla_x, malla_y



def mallador_elipticas_2D(gridx_inicial, gridy_inicial, nodos_x, nodos_y, itermax=200, error=0.001):
    """Genera una malla estructurada con ecuaciones diferenciales parciales dada una malla como aproximacion
    
    Parametros
    ----------
    gridx_inicial, gridy_inicial : array_like.
        Arreglo 2D con las coordenadas iniciales de una malla. 
    nodos_x, nodos_y : int, int.
        Puntos distribuidos a lo largo 4 cuatro fronteras del dominio.

    Retorna
    -------
    ndarray, ndarray. 
        Arreglos en 2D para x e y de la malla refinada.
    """
    alpha, beta, gamma = np.zeros((nodos_x,nodos_y)), np.zeros((nodos_x,nodos_y)), np.zeros((nodos_x,nodos_y))
    errX, errY = np.ones(itermax), np.ones(itermax)

    gridx_refinada = gridx_inicial; gridy_refinada = gridy_inicial
    #-------------------------------------Inicia el método iterativo-------------|
    for t in range (1, itermax):
        for i in range(1, nodos_x-1):
            for j in range(1, nodos_y-1):
                alpha[i,j] = (1/4)*((gridx_inicial[i,j+1]-gridx_inicial[i,j-1])**2 + (gridy_inicial[i,j+1] - gridy_inicial[i,j-1])**2)
                beta[i,j]  = (1/16)*((gridx_inicial[i+1,j]-gridx_inicial[i-1,j])*(gridx_inicial[i,j+1]-gridx_inicial[i,j-1]) + (gridy_inicial[i+1,j] - gridy_inicial[i-1,j])*(gridy_inicial[i,j+1] - gridy_inicial[i,j-1]))
                gamma[i,j] = (1/4)*((gridx_inicial[i+1,j]-gridx_inicial[i-1,j])**2 + (gridy_inicial[i+1,j] - gridy_inicial[i-1,j])**2)
                
                gridx_refinada[i,j] = ((-0.5)/(alpha[i,j] + gamma[i,j]+10e-9))*(2*beta[i,j]*(gridx_inicial[i+1,j+1] - gridx_inicial[i-1,j+1] - gridx_inicial[i+1,j-1] + gridx_inicial[i-1,j-1]) - alpha[i,j]*(gridx_inicial[i+1,j]+gridx_inicial[i-1,j]) - gamma[i,j]*(gridx_inicial[i,j+1]+gridx_inicial[i,j-1]))
                gridy_refinada[i,j] = ((-0.5)/(alpha[i,j] + gamma[i,j]+10e-9))*(2*beta[i,j]*(gridy_inicial[i+1,j+1] - gridy_inicial[i-1,j+1] - gridy_inicial[i+1,j-1] + gridy_inicial[i-1,j-1]) - alpha[i,j]*(gridy_inicial[i+1,j]+gridy_inicial[i-1,j]) - gamma[i,j]*(gridy_inicial[i,j+1]+gridy_inicial[i,j-1]))
        
        #calculamos el error
        errX[t] = np.linalg.norm(gridx_refinada)
        errY[t] = np.linalg.norm(gridy_refinada)
        
        #Neuman BC
        gridy_refinada[0,:] = gridy_refinada[1,:]                    #rigth
        #newY[nodos_x-1,:] = newY[nodos_x-2,:]    #left
        
        if t>2:
            err_x = errX[t] - errX[t-1]; err_y = errY[t] - errY[t-1]   
            if err_x < error and err_y < error: break
        
        gridx_inicial, gridy_inicial = gridx_refinada, gridy_refinada
    
    return gridx_inicial, gridy_inicial