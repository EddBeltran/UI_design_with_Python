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





#-----------------------------------------------------------------------------------------#
# Generador de mallas estructurales con EDPs ---------------------------------------------#
#-----------------------------------------------------------------------------------------#
def mallador_estructural(x, y, nodos_x, nodos_y, itermax=200):
    """Es un metodos algebraico que transforma el dominio original en uno canonico,
    mediante funciones de interpolación y partiendo de los nodos del contorno se generan los puntos interiores de la malla.    

    Parametros
    ----------
    x, y : array_like or list.
        Arreglos/listas 1D con las coordenadas del contorno a mallar `x` -> [`x1`,`x2`, ..., `xk`], `y`-> [`y1`,`y2`, ..., `yk`].
    nodos_x, nodos_y : int, int.
        Puntos distribuidos a lo largo 4 cuatro fronteras del dominio.
    itermax: int.
        Iteraciones maximas del solver.
    Retorna
    -------
    ndarray, ndarray. 
        Arreglos en 2D para x e y de la malla.
    """
    eps = 1.0E-07 #parametros del solver

    # Generacion de las coordenadas iniciales mediante Interpolación Transfinita Lineal en 2D que genera las 
    # coordenadas iniciales para los puntos interiores
    malla_inicial_x, malla_inicial_y  = interpolacion_transfinita_2D(x, y, nodos_x, nodos_y)

    AE,AW,AN,AS,AP,BBX = coeficientes_malla_x(nodos_x, nodos_y, malla_inicial_x, malla_inicial_y) #CONTROLGX,LINY1,LINY2,AX1,AX2,BX1,BX2,  CX,DX1,CXX1,CXX2,CXY1,CXY2)
    #malla_final_x = solver.algoritmo_thomas_2D(nodos_x, nodos_y, AP, AE, AW, AN, AS, BBX, malla_inicial_x, itermax, eps)

    AE,AW,AN,AS,AP,BBY = coeficientes_malla_y(nodos_x, nodos_y, malla_inicial_x, malla_inicial_y) #CONTROLGY,LINX1,LINX2,AY1,AY2,BY1,BY2,  CY,DY1,CYX1,CYX2,CYY1,CYY2,NX,NY,GRIDXA,GRIDYA,  YN,YS,YE,YW,   AE,AW,AN,AS,AP,BBY,NIMAX,NJMAX)
    #malla_final_y = solver.algoritmo_thomas_2D(nodos_x, nodos_y, AP, AE, AW, AN, AS, BBY, malla_inicial_y, itermax, eps)

    #return malla_final_x, malla_final_y






#-------------------------------------------------------------------#
# Funciones auxiliares ---------------------------------------------#
#-------------------------------------------------------------------#
"""
def asignacion_fronteras(puntos, nodos_x, nodos_y):
    frontera_norte, frontera_sur = np.zeros(nodos_x), np.zeros(nodos_x)
    frontera_este, frontera_oeste = np.zeros(nodos_y), np.zeros(nodos_y)

    for i in range (0, nodos_x):
        frontera_sur[i] = puntos[i]
        frontera_norte[i] = puntos[nodos_x + nodos_y + nodos_x-1-(i+2)]

    for i in range (0, nodos_y):
        frontera_este[i] = puntos[nodos_x + i-1]
        frontera_oeste[i] = puntos[(2*nodos_x + 2*nodos_y-2)-(i+2)]
    
    return frontera_sur, frontera_este, frontera_norte, frontera_oeste
"""


def coeficientes_malla_x(puntos, nodos_x, nodos_y, malla_inicial_x, malla_inicial_y): #COEFICIENTEGX(CONTROLGX,LINY1,LINY2,AX1,AX2,BX1,BX2,   CX,DX,CXX1,CXX2,CXY1,CXY2,NX,NY,GRIDX,GRIDY,   FXN,FXS,FXE,FXW,    AE,AW,AN,AS,AP,BBX,NIMAX,NJMAX):
    """ Se calculan los coeficientes de las EDPs discretizadas.
    Parametros
    ----------
    puntos: array_like or list.
        Arreglo/lista 1D con las puntos del dominio en x o y -> puntos = [p1, p2, ..., pk].
    nodos_x, nodos_y: int, int.
        Puntos distribuidos a lo largo 4 cuatro fronteras del dominio en la dirección x e y.
    puntos: array_like.
        Arreglo 2D con las coordenadas de la malla generada mediante interpolacion transfinita.

    Retorna
    -------
    ndarray, ndarray, ndarray, ndarray, ndarray, ndarray. 
        Arreglos 2D de los coeficientes AE,AW,AN,AS,AP,BBX.
    """
    #------- Coeficientes de las EDP´s discretizadas ---------------------#
    AN, AS, AE, AW  = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    ANE, ASE, ANW, ASW  = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    AP, BBX = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    QX, PX = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    

    #---- Funciones de Control para atracción de Líneas en las fronteras -----*
    #--- esta pendiente esa parte           
    #PX[i][j] = 0 #-SUMP1-SUMP2
    #QX[i][j] = 0 #-SUMQ1-SUMQ2
    
    # Calculo de los coeficientes
    for i in range (1, nodos_x-1):
        for j in range (1, nodos_y-1):
            Xn = malla_inicial_x[i][j+1]
            Xs = malla_inicial_x[i][j-1]
            Xe = malla_inicial_x[i+1][j]
            Xw = malla_inicial_x[i-1][j]
            
            Yn = malla_inicial_y[i][j+1]
            Ys = malla_inicial_y[i][j-1]
            Ye = malla_inicial_y[i+1][j]
            Yw = malla_inicial_y[i-1][j]
            
            ALFA = ((Xn-Xs)/2.0)**2+((Yn-Ys)/2.0)**2
            GAMA = ((Xe-Xw)/2.0)**2+((Ye-Yw)/2.0)**2
            BETA = ((Xe-Xw)/2.0)*((Xn-Xs)/2.0)+((Ye-Yw)/2.0)*((Yn-Ys)/2.0)
            XJAC = 1/(((Xe-Xw)/2.0)*((Yn-Ys)/2.0)-((Xn-Xs)/2.0)*((Ye-Yw)/2.0))
            
            AP[i][j] = 2.0*(ALFA+GAMA)
            AE[i][j] = ALFA+PX[i][j]/(2*XJAC**2)
            AW[i][j] = ALFA-PX[i][j]/(2*XJAC**2)
            AN[i][j] = GAMA+QX[i][j]/(2*XJAC**2)
            AS[i][j] = GAMA-QX[i][j]/(2*XJAC**2)
            ANE[i][j]= -BETA/2.0
            ASE[i][j]= BETA/2.0
            ANW[i][j]= BETA/2.0
            ASW[i][j]= -BETA/2.0
            BBX[i][j]= (ANE[i][j]*malla_inicial_x[i+1][j+1]+ASE[i][j]*malla_inicial_x[i+1][j-1]+
                       ANW[i][j]*malla_inicial_x[i-1][j+1]+ASW[i][j]*malla_inicial_x[i-1][j-1])
        
    #------ Condiciones de Frontera -------*
    #frontera_sur_x, frontera_este_x, frontera_norte_x, frontera_oeste_x = asignacion_fronteras(puntos, nodos_x, nodos_y)

    for i in range (0, nodos_y):
        AP[0][i]  = 1.0		#Frontera Oeste
        #BBX[0][i] = frontera_oeste_x[i]
    
        AP[nodos_x-1][i]  = 1.0      	#Frontera Este
        #BBX[nodos_x-1][i] = frontera_este_x[i]
    
    for i in range (1, nodos_x-1):
        AP[i][0]  = 1.0		#Frontera Sur
        #BBX[i][0] = frontera_sur_x[i]
    
        AP[i][nodos_y-1]  = 1.0	    #Frontera Norte
        #BBX[i][nodos_y-1] = frontera_norte_x[i]
    
    #Calculo del residual FHI = variable generica
    #ERRORGX=RESIDUOFHI(1,1,NX-1,NY-1,AE,AW,AN,AS,AP,BBX,GRIDX,NIMAX,NJMAX)
    
    return AE,AW,AN,AS,AP,BBX



def coeficientes_malla_y(puntos, nodos_x, nodos_y, malla_inicial_x, malla_inicial_y): #COEFICIENTEGX(CONTROLGX,LINY1,LINY2,AX1,AX2,BX1,BX2,   CX,DX,CXX1,CXX2,CXY1,CXY2,NX,NY,GRIDX,GRIDY,   FXN,FXS,FXE,FXW,    AE,AW,AN,AS,AP,BBX,NIMAX,NJMAX):
    """ Se calculan los coeficientes de las EDPs discretizadas.
    Parametros
    ----------
    puntos: array_like or list.
        Arreglo/lista 1D con las puntos del dominio en x o y -> puntos = [p1, p2, ..., pk].
    nodos_x, nodos_y: int, int.
        Puntos distribuidos a lo largo 4 cuatro fronteras del dominio en la dirección x e y.
    puntos: array_like.
        Arreglo 2D con las coordenadas de la malla generada mediante interpolacion transfinita.

    Retorna
    -------
    ndarray, ndarray, ndarray, ndarray, ndarray, ndarray. 
        Arreglos 2D de los coeficientes AE,AW,AN,AS,AP,BBX.
    """
    #------- Coeficientes de las EDP´s discretizadas ---------------------#
    AN, AS, AE, AW  = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    ANE, ASE, ANW, ASW  = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    AP, BBY = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    QX, PX = np.zeros((nodos_x, nodos_y)), np.zeros((nodos_x, nodos_y))
    

    #---- Funciones de Control para atracción de Líneas en las fronteras -----*
    #--- esta pendiente esa parte           
    #PX[i][j] = 0 #-SUMP1-SUMP2
    #QX[i][j] = 0 #-SUMQ1-SUMQ2
    
    # Calculo de los coeficientes
    for i in range (1, nodos_x-1):
        for j in range (1, nodos_y-1):
            Xn = malla_inicial_x[i][j+1]
            Xs = malla_inicial_x[i][j-1]
            Xe = malla_inicial_x[i+1][j]
            Xw = malla_inicial_x[i-1][j]
            
            Yn = malla_inicial_y[i][j+1]
            Ys = malla_inicial_y[i][j-1]
            Ye = malla_inicial_y[i+1][j]
            Yw = malla_inicial_y[i-1][j]
            
            ALFA = ((Xn-Xs)/2.0)**2+((Yn-Ys)/2.0)**2
            GAMA = ((Xe-Xw)/2.0)**2+((Ye-Yw)/2.0)**2
            BETA = ((Xe-Xw)/2.0)*((Xn-Xs)/2.0)+((Ye-Yw)/2.0)*((Yn-Ys)/2.0)
            XJAC = 1/(((Xe-Xw)/2.0)*((Yn-Ys)/2.0)-((Xn-Xs)/2.0)*((Ye-Yw)/2.0))
            
            AP[i][j] = 2.0*(ALFA+GAMA)
            AE[i][j] = ALFA+PX[i][j]/(2*XJAC**2)
            AW[i][j] = ALFA-PX[i][j]/(2*XJAC**2)
            AN[i][j] = GAMA+QX[i][j]/(2*XJAC**2)
            AS[i][j] = GAMA-QX[i][j]/(2*XJAC**2)
            ANE[i][j]= -BETA/2.0
            ASE[i][j]= BETA/2.0
            ANW[i][j]= BETA/2.0
            ASW[i][j]= -BETA/2.0
            BBY[i][j]= (ANE[i][j]*malla_inicial_y[i+1][j+1]+ASE[i][j]*malla_inicial_y[i+1][j-1]+
                       ANW[i][j]*malla_inicial_y[i-1][j+1]+ASW[i][j]*malla_inicial_y[i-1][j-1])
        
    #------ Condiciones de Frontera -------*
    #frontera_sur_y, frontera_este_y, frontera_norte_y, frontera_oeste_y = asignacion_fronteras(puntos, nodos_x, nodos_y)

    for i in range (0, nodos_y):
        AP[0][i]  = 1.0		#Frontera Oeste
        #BBY[0][i] = frontera_oeste_y[i]
    
        AP[nodos_x-1][i]  = 1.0      	#Frontera Este
        #BBY[nodos_x-1][i] = frontera_este_y[i]
    
    for i in range (1, nodos_x-1):
        AP[i][0]  = 1.0		#Frontera Sur
        #BBY[i][0] = frontera_sur_y[i]
    
        AP[i][nodos_y-1]  = 1.0	    #Frontera Norte
        #BBY[i][nodos_y-1] = frontera_norte_y[i]
    
    #Calculo del residual FHI = variable generica
    #ERRORGX=RESIDUOFHI(1,1,NX-1,NY-1,AE,AW,AN,AS,AP,BBX,GRIDX,NIMAX,NJMAX)
    
    return AE,AW,AN,AS,AP,BBY


"""
def condiciones_frontera(A,B, nodos_x,nodos_y, sur, este, norte, oeste):
    A[0][i]=1.0		       #Frontera Oeste
    B[0][i]=FXW[i]
    A[NX-1][i]=1.0      	#Frontera Este
    B[NX-1][i]=FXE[i]

for i in range (1, NX-1):
    AP[i][0]=1.0		#Frontera Sur
    BBX[i][0]=FXS[i]

    AP[i][NY-1]=1.0	    #Frontera Norte
    BBX[i][NY-1]=FXN[i]
"""