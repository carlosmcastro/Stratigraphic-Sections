import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
import numpy as np

#Espacio y rango de profundiades.
espaciado_y = 20
inicio = 2000
fin = 2200

y = np.arange(inicio, fin+espaciado_y, espaciado_y)
#Esquema para maquetación de sedimentos en el perfil.
sedimentos = {
       "FA": {
	           "Indice": 1, 
			   "Visualizacion": ()
			   }, 
       "Arcillita": {
	           "Indice": 2, 
			   "Visualizacion": ('greenyellow', '/')
			   }, 
       "Limoarcillita": {
	           "Indice": 3, 
			   "Visualizacion": ('g', '*')
			   }, 
       "Lutita": {
	           "Indice": 4, 
			   "Visualizacion": ('mediumseagreen', '-')
			   }, 
       "Limolita arenosa": {
	           "Indice": 5, 
			   "Visualizacion": ()
			   }, 
       "Arenisca Fina": {
	           "Indice": 6, 
			   "Visualizacion": ("y", ".")
			   }, 
       "AM": {
	           "Indice": 7, 
			   "Visualizacion": ()
			   }, 
       "AG": {
	           "Indice": 8, 
			   "Visualizacion": ()
			   }, 
       "Con": {
	           "Indice": 9, 
			   "Visualizacion": ()
			   }, 
       "Dt": {
	           "Indice": 10, 
			   "Visualizacion": ()
			   }, 
       "Com": {
	           "Indice": 11, 
			   "Visualizacion": ()
			   }
}

#Etiquetas de sedimentos.
x_labels = sedimentos.keys()
x = np.arange(1,len(x_labels)+1)

#Marco y elementos a graficar.
fig, ax = plt.subplots()

#Tamaño al visualizar el marco.
fig.set_size_inches(15, 18.5, forward=True)

#Genera el estrato secuencialmente.
def prod_barra(profundidad_inicial, sedimento, porcion_espaciado, porcion_contribucion):
    
	#Ancho del estrato.
    anchura = espaciado_y*porcion_espaciado*porcion_contribucion
	
	#Propiedades de visualización.
    sdt = sedimentos[sedimento]
    label, color, hatch = sedimento, *sdt["Visualizacion"]
    
	#Objeto barra horizontal que representa el estrato.
    ax.barh([profundidad_inicial], [sdt["Indice"]], 
            height=anchura, 
            align='edge', label=label, color=color, hatch=hatch)
    
	#Retorna la profundidad que sigue.
    return profundidad_inicial+anchura

#Interpretación litográfica.
#2000
prof_sig = prod_barra(2000, "Lutita", .25, .4)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .6)
prof_sig = prod_barra(prof_sig, "Lutita", .5, .5)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .5, .5)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .3)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .7)
#2020
prof_sig = prod_barra(prof_sig, "Lutita", .25, .3)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .7)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .4)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .6)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .3)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .7)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .9)
#2040
prof_sig = prod_barra(prof_sig, "Lutita", .75, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .75, .9)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .1)
#2060
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .1)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Lutita", .5, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .5, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .5, .1)
#2080
prof_sig = prod_barra(prof_sig, "Lutita", .5, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .5, .8)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .1)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .6)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .3)
#2100
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .7)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .2)
prof_sig = prod_barra(prof_sig, "Lutita", .75, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .75, .8)
#2120
prof_sig = prod_barra(prof_sig, "Lutita", .75, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .75, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .75, .1)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
#2140
prof_sig = prod_barra(prof_sig, "Lutita", .5, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .5, .9)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .1)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
#2160
prof_sig = prod_barra(prof_sig, "Lutita", .75, .1)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .75, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .75, .1)
prof_sig = prod_barra(prof_sig, "Lutita", .25, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
#2180
prof_sig = prod_barra(prof_sig, "Lutita", .25, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .8)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .25, .2)
prof_sig = prod_barra(prof_sig, "Lutita", .5, .2)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .5, .7)
prof_sig = prod_barra(prof_sig, "Arenisca Fina", .5, .1)
#2200

#Configuramos los ejes.
ax.set_yticks(y)
ax.set_xticks(x)

#Establecemos las etiquetas de los sedimentos.
ax.set_xticklabels(x_labels)

#Invertimos el eje y para que se grafique como profundidad.
ax.invert_yaxis()

#Nombre del eje x.
ax.set_xlabel('Sedimentos')
#Nombre del eje y.
ax.set_ylabel('Profundidad')

#Color de fondo.
ax.set_facecolor('coral')

#Obtenemos las etiquetas y sus elementos asociados.
handles, labels = ax.get_legend_handles_labels()

#Filtramos por etiquetas unicas.
uniq_labels = set(labels)
uniq_handles = [handles[labels.index(label)] for label in uniq_labels]

#Generamos una leyenda. Ajustamos el ancho y el alto al visualizar.
ax.legend(uniq_handles, uniq_labels, handlelength=10, handleheight=3.2)

#Distribución de colores en la escala.
barra_blanco_y_negro = ('white', 'black')*3+('white',)

#Calculo de metricas para la escala.
unidades_metricas = (fin-inicio)/espaciado_y
#.9 porque los estratos ocupan un 90% de la altura en la grafica.
unidad_metrica_proporcion = (1*.9)/unidades_metricas
#El porcentaje total que le corresponde a la barra, en relación a la altura del grafico.
escalado_barra = unidad_metrica_proporcion*len(barra_blanco_y_negro)

#Generación del objeto correspondiente a la escala.
#Shrink, asigna la proporción de la altura
#aspect, el ancho
#pad, la distancia respecto al grafico.
#ticks, contiene una lista con un número mayor a 1, para no mostrar la escala de 0 a 1.
fig.colorbar(cm.ScalarMappable(cmap=ListedColormap(barra_blanco_y_negro)),  
			 label='Escala 1:2000', shrink=escalado_barra, aspect=60, pad=.009, ticks=[2])

#Graficamos.
plt.show()
