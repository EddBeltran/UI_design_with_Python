
import numpy as np


def ARRtoLIST(grid_2dx, grid_2dy, nxGrid, nyGrid):
    
    gridx = []
    gridy = []
    
    for j in range(0, nyGrid):
        for i in range(0, nxGrid):
            gridx.append(grid_2dx[i][j])
            gridy.append(grid_2dy[i][j])
            
    return gridx, gridy



def LISTtoARR(grid_2dx, grid_2dy, nxGrid, nyGrid):
    gridx = np.zeros((nxGrid, nyGrid))
    gridy = np.zeros((nxGrid, nyGrid))
    
    for j in range(0, nyGrid):
        for i in range(0, nxGrid):
            gridx[i][j] = grid_2dx[i+j*nxGrid]
            gridy[i][j] = grid_2dy[i+j*nxGrid]
            
    return gridx, gridy
    
    

def loadGrid(fdatos, NX, NY):
    datax = []                #  Creamos una lista para la primera columna
    datay = []                #  Creamos una lista para la segunda columna
    lineas = fdatos.readlines() # Leemos el fichero línea a línea
    for linea in lineas:
        x, y = linea.split()     # Se separa cada línea en dos columnas
        datax.append(float(x)) # Añado el elemento x a la lista x_datos
        datay.append(float(y)) # Añado el elemento y a la lista y_datos
    fdatos.close()
    
    gridx=np.zeros((NX,NY))
    gridy=np.zeros((NX,NY))
    
    for j in range(0,NY):
        for i in range(0,NX):
            gridx[i][j] = float(datax[i+j*NX])				# Los coeficientes se convierten en cadenas para
            gridy[i][j] = float(datay[i+j*NX])				# Los coeficientes se convierten en cadenas para
            
    return(gridx, gridy)

              
def get_UniformMesh2D(nxGrid, nyGrid, Hx, Hy):
    grid_2dx = np.zeros((nxGrid, nyGrid))
    grid_2dy = np.zeros((nxGrid, nyGrid))
    
    deltaHx=(Hx/(nxGrid-1))
    deltaHy=(Hy/(nyGrid-1))
    
    for j in range(0, nyGrid):
        for i in range(0, nxGrid):
            grid_2dx[i][j] = deltaHx*(i)
            grid_2dy[i][j] = deltaHy*(j)    
    return(grid_2dx, grid_2dy)
    

def gridCenters(nxGrid, nyGrid, gridx, gridy, gCentersx, gCentersy):
    for j in range(0, nyGrid-1):
        for i in range (0, nxGrid-1):
            gCentersx[i+1][j+1] = (gridx[i][j]+gridx[i+1][j]+gridx[i+1][j+1]+gridx[i][j+1])/4.0
            gCentersy[i+1][j+1] = (gridy[i][j]+gridy[i+1][j]+gridy[i+1][j+1]+gridy[i][j+1])/4.0
            #print("i=",i+1,"j=",j+1,"\t grx =", gCentersx[i+1][j+1])
    
    for i in range (0, nxGrid-1):    
        gCentersx[i+1][0] = (gridx[i][0] + gridx[i+1][0])/2.0
        gCentersy[i+1][0] = (gridy[i][0] + gridy[i+1][0])/2.0
        gCentersx[i+1][nyGrid] = (gridx[i][nyGrid-1] + gridx[i+1][nyGrid-1])/2.0
        gCentersy[i+1][nyGrid] = (gridy[i][nyGrid-1] + gridy[i+1][nyGrid-1])/2.0
    
    for j in range(0, nyGrid-1):
        gCentersx[0][j+1] = (gridx[0][j] + gridx[0][j+1])/2.0
        gCentersy[0][j+1] = (gridy[0][j] + gridy[0][j+1])/2.0
        gCentersx[nxGrid][j+1] = (gridx[nxGrid-1][j] + gridx[nxGrid-1][j+1])/2.0
        gCentersy[nxGrid][j+1] = (gridy[nxGrid-1][j] + gridy[nxGrid-1][j+1])/2.0
    
    
    gCentersx[0][0] = gridx[0][0];	
    gCentersy[0][0] = gridy[0][0];
    
    gCentersx[nxGrid][0] = gridx[nxGrid-1][0];	
    gCentersy[nxGrid][0] = gridy[nxGrid-1][0];	
    	
    gCentersx[0][nyGrid] = gridx[0][nyGrid-1];	
    gCentersy[0][nyGrid] = gridy[0][nyGrid-1];
    
    gCentersx[nxGrid][nyGrid] = gridx[nxGrid-1][nyGrid-1]
    gCentersy[nxGrid][nyGrid] = gridy[nxGrid-1][nyGrid-1]

#for j in range(0,ny):
 #   for i in range(0,nx):
  #      print("grx: ", gCentersx[i][j])
  
def gridCenters2(gridx, gridy, nxGrid, nyGrid):
    gCentersx = np.zeros((nxGrid+1, nyGrid+1))
    gCentersy = np.zeros((nxGrid+1, nyGrid+1))
    
    for j in range(0, nyGrid-1):
        for i in range (0, nxGrid-1):
            gCentersx[i+1][j+1] = (gridx[i][j]+gridx[i+1][j]+gridx[i+1][j+1]+gridx[i][j+1])/4.0
            gCentersy[i+1][j+1] = (gridy[i][j]+gridy[i+1][j]+gridy[i+1][j+1]+gridy[i][j+1])/4.0
            #print("i=",i+1,"j=",j+1,"\t grx =", gCentersx[i+1][j+1])
    
    for i in range (0, nxGrid-1):    
        gCentersx[i+1][0] = (gridx[i][0] + gridx[i+1][0])/2.0
        gCentersy[i+1][0] = (gridy[i][0] + gridy[i+1][0])/2.0
        gCentersx[i+1][nyGrid] = (gridx[i][nyGrid-1] + gridx[i+1][nyGrid-1])/2.0
        gCentersy[i+1][nyGrid] = (gridy[i][nyGrid-1] + gridy[i+1][nyGrid-1])/2.0
    
    for j in range(0, nyGrid-1):
        gCentersx[0][j+1] = (gridx[0][j] + gridx[0][j+1])/2.0
        gCentersy[0][j+1] = (gridy[0][j] + gridy[0][j+1])/2.0
        gCentersx[nxGrid][j+1] = (gridx[nxGrid-1][j] + gridx[nxGrid-1][j+1])/2.0
        gCentersy[nxGrid][j+1] = (gridy[nxGrid-1][j] + gridy[nxGrid-1][j+1])/2.0
    
    
    gCentersx[0][0] = gridx[0][0];	
    gCentersy[0][0] = gridy[0][0];
    
    gCentersx[nxGrid][0] = gridx[nxGrid-1][0];	
    gCentersy[nxGrid][0] = gridy[nxGrid-1][0];	
    	
    gCentersx[0][nyGrid] = gridx[0][nyGrid-1];	
    gCentersy[0][nyGrid] = gridy[0][nyGrid-1];
    
    gCentersx[nxGrid][nyGrid] = gridx[nxGrid-1][nyGrid-1]
    gCentersy[nxGrid][nyGrid] = gridy[nxGrid-1][nyGrid-1]
    
    return(gCentersx, gCentersy)
  
  
def metrics_Faces2d(nx, ny, gridx, gridy, Xxhi, Xeta, Yxhi, Yeta):   
    
    for j in range(1,ny-1):
        for i in range(1,nx-1):
            
            Xxhi[i][j] = ((gridx[i][j] - gridx[i-1][j]) + (gridx[i][j-1] - gridx[i-1][j-1]))/2.0
            Xeta[i][j] = ((gridx[i][j] - gridx[i][j-1]) + (gridx[i-1][j] - gridx[i-1][j-1]))/2.0
            
            Yxhi[i][j] = ((gridy[i][j] - gridy[i-1][j]) + (gridy[i][j-1] - gridy[i-1][j-1]))/2.0
            Yeta[i][j] = ((gridy[i][j] - gridy[i][j-1]) + (gridy[i-1][j] - gridy[i-1][j-1]))/2.0
            #print("Xeta[i][j]=", Xeta[i][j])
    
    
    """
    for i in range(0,nx):
        Xxhi[i][0] = 0.0
        Xeta[i][0] = 0.0
        Yxhi[i][0] = 0.0
        Yeta[i][0] = 0.0
        
        Xxhi[i][ny-1] = 0.0
        Xeta[i][ny-1] = 0.0
        Yxhi[i][ny-1] = 0.0
        Yeta[i][ny-1] = 0.0
            
    for j in range(0,ny):
        Xxhi[0][j] = 0.0
        Xeta[0][j] = 0.0
        Yxhi[0][j] = 0.0
        Yeta[0][j] = 0.0
        
        Xxhi[nx-1][j] = 0.0
        Xeta[nx-1][j] = 0.0
        Yxhi[nx-1][j] = 0.0
        Yeta[nx-1][j] = 0.0
   """

    for i in range(1,nx-1):
        Xxhi[i][0] = Xxhi[i][1]
        Xeta[i][0] = Xeta[i][1]
        Yxhi[i][0] = Yxhi[i][1]
        Yeta[i][0] = Yeta[i][1]
        
        Xxhi[i][ny-1] = Xxhi[i][ny-2]
        Xeta[i][ny-1] = Xeta[i][ny-2]
        Yxhi[i][ny-1] = Yxhi[i][ny-2]
        Yeta[i][ny-1] = Yeta[i][ny-2]
            
    for j in range(1,ny-1):
        Xxhi[0][j] = Xxhi[1][j]
        Xeta[0][j] = Xeta[1][j]
        Yxhi[0][j] = Yxhi[1][j]
        Yeta[0][j] = Yeta[1][j]
        
        Xxhi[nx-1][j] = Xxhi[nx-2][j]
        Xeta[nx-1][j] = Xeta[nx-2][j]
        Yxhi[nx-1][j] = Yxhi[nx-2][j]
        Yeta[nx-1][j] = Yeta[nx-2][j]
    
    """
    Xxhi[0][0]=Xxhi[1][0]; Xeta[0][0]=Xeta[1][0];  Yxhi[0][0]=Yxhi[1][0]; Yeta[0][0]=Yeta[1][0];
    Xxhi[nx-1][0]=Xxhi[nx-2][0]; Xeta[nx-1][0]=Xeta[nx-2][0];  Yxhi[nx-1][0]=Yxhi[nx-2][0]; Yeta[nx-1][0]=Yeta[nx-2][0];

    Xxhi[0][ny-1]=Xxhi[0][ny-2]; Xeta[0][0]=Xeta[1][0];  Yxhi[0][0]=Yxhi[1][0]; Yeta[0][0]=Yeta[1][0];
    Xxhi[nx-1][0]=Xxhi[nx-2][0]; Xeta[nx-1][0]=Xeta[nx-2][0];  Yxhi[nx-1][0]=Yxhi[nx-2][0]; Yeta[nx-1][0]=Yeta[nx-2][0];
    """



#----------------------------------------------------------------------------//
def POLI_POINTS(x,y,NX_1):
    NX = NX_1 -1
    lim_for=len(x)
    d_tot=0
    cont = 0
    x1 = []
    y1 = []
    
    for i in range(1, lim_for):
        d = ((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5
        d_tot = d_tot + d
    
    factor = np.zeros(lim_for-1)
    num = 0
    while ((NX*4+1) != cont):
        num = num + 1
        print("num: ", num)
        
        
        if cont == 0:
            for i in range(1, lim_for):
                d = ((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5
                dn = round((d/d_tot)*(NX*4)-1)
                factor[i-1] = dn
        
        cont = np.sum(factor) + lim_for
        
        if (cont > NX*4+1):
            mayor = max(factor)
            index = np.where(factor == mayor)
            factor[index[0]] = factor[index[0]] - 1
        
        if (cont < NX*4+1):
            menor = min(factor)
            index = np.where(factor == menor)
            factor[index[0]] = factor[index[0]] + 1
          
    for i in range(1, lim_for):
        dn = int(factor[i-1])
        ss = dn
        
        x1.insert(len(x1), x[i-1])
        y1.insert(len(y1), y[i-1])
        
        for h in range(1, dn + 1):
            r = ss / h
            ss = ss - 1
            xs = (x[i] + r * x[i - 1]) / (1 + r)
            ys = (y[i] + r * y[i - 1]) / (1 + r)
            x1.append(xs)
            y1.append(ys)
            
    x1.insert(len(x1), x[0])
    y1.insert(len(y1), y[0])
    
    return (x1,y1)




#---------------------------------------------------------WELL COORDINATES---//
def SEPARATE_COORD(df, wells):
    x_prod = []
    y_prod = []
    
    x_inj = []
    y_inj = []
    
    for i in range(0,wells):
        index = 'WELL-' + str(i+1)
        if ((df.at[2, index]) == "Producer"):
            #print("producer",i)
            coord  = (df.at[1, index])
            coord_xy = coord.split(",")
            x_prod.append(float(coord_xy[0]))
            y_prod.append(float(coord_xy[1]))
        
        if ((df.at[2, index]) == "Injector"):
            #print("injector",i)
            coord  = (df.at[1, index])
            coord_xy = coord.split(",")
            x_inj.append(float(coord_xy[0]))
            y_inj.append(float(coord_xy[1]))   
            
    return(x_prod, y_prod, x_inj, y_inj)


def coord_point(x, y, gridxx, gridyy, nx, ny):
    suma_res = np.zeros(nx*ny)
    
    for j in range(0,ny):
        for i in range(0,nx):        
            res_x = abs(x - gridxx[i][j])
            res_y = abs(y - gridyy[i][j])
            suma_res[i+j*nx] = res_x + res_y
                
    
    min_res = min(suma_res)
    index_sum = np.where(suma_res == min_res)        
    c = index_sum[0]
    
    for j in range(0,ny):
        for i in range(0,nx):
            k = i+j*nx           
            if k ==c:
                nodo_x = i
                nodo_y = j
    
    #print("well x,y", x,y)    
    #print("gridx", gridxx[nodo_x][nodo_y], nodo_x)
    #print("gridy", gridyy[nodo_x][nodo_y], nodo_y)
    
    return (nodo_x, nodo_y)
    


#-----------------------------------------------------------------------------//
def REAL_NX_NY(lim):
    res=int(lim/4)
    a=(lim/4)-res
    if a==0:
        NX = int((lim / 4))
        NY = int((lim / 4))
            
    if a!=0:
        NX = int((lim / 4))+1
        NY = int((lim / 4))+1
    
    print("NX, NY: ",NX, NY)
        
    return(NX, NY)
    
  
