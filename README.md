# Stratigraphic-Sections
Perfil estratigráfico de La Formación Los Monos, entre los 2000 a los 2200 metros
![Formación Los Monos Primer Vistazo](https://github.com/carlosmcastro/Stratigraphic-Sections/blob/master/formacion_los_monos.png)
La interpretación se realizo por cada segmento de 20 metros (dato por defecto almacenado en la variable `espaciado_y`).
La función `prod_barra` es la encargada de las barras horizontales.
Cuenta de 4 parametros:
```
prod_barra(profundidad_inicial, sedimento, porcion_espaciado, porcion_contribucion)
```
`porcion_espaciado` hace referencia al porcentaje de los 20 metros al que pertenece la barra,  `porcion_contribucion` a el porcentaje que contribuye el sedimento en el porcentaje anterior.

Por ejemplo las primeras dos lineas:
```
prof_sig = prod_barra(2000, "Lutita", .25, .4)
prof_sig = prod_barra(prof_sig, "Limoarcillita", .25, .6)
```
Indican que se grafica Lutita con un grosor correspondiente al 40% de los primeros 5 metros del pozo.
La función `prod_barra` retorna la profundidad contigua que sirve para el siguiente parametro inicial.
Que ahora es Limoarcillita con un grosor correspondiente al 60% de los primeros 5 metros del pozo.
