# MalladorCC

<div style="background:red;">
<img src="gif_mallador_cc.gif" width="500px" height="auto" />
</div>

## Descripción

Mallador CC es un programa de cómputo capaz de generar mallas estructuradas en dos dimensiones. Para la generar los puntos de la malla se emplea un método algebraico conocido como Interpolación Transfinita. Si se desea refinar la malla generada, es posible utilizar un algoritmo que emplea ecuaciones diferenciales parciales. Dichos métodos se describen a detalle en la tesis de maestría Generación de Mallas Numéricas para Geometrías Irregulares y Complejas, escrita por el Dr. Leonardo Teja.

## ¿Cómo utilizar la interfaz gráfica?
* Configurar el tamaño del lienzo y si se desea establecer los nodos de la malla
* Trazar líneas o curvas en cada una de las 4 fronteras 
* Ctrl + X para pasar a la siguiente frontera
* Ctrl + X para cerrar el contorno de la malla
* Utilizar el botón de TFI o PDE para visualizar la malla
* Modificar los nodos y actualizar
* Guardar los puntos en formato .csv

## Librerías que se requieren
•	PySide6
•	Matplotlib
•	Pandas
•	Numpy
•	Numba
•	PyInstaller

## Comandos para despliegue de archivos
