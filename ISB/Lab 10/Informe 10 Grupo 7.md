# INFORME LABORATORIO 10
## Lista de Participantes - Grupo 9

- Andrea Razuri Madrid
- Isabel Leon Luna
- Johanni Bohorquez Gutierrez
- Claudia Camacho Grimaldi
- Jaime Arista Cutipa 

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Metodología](#4-metodología)
3. [Resultados](#5-resultados)
4. [Discusión](#6-discusión)
5. [Conclusión](#5-conclusión)
6. [Bibliografía](#8-bibliografía)


## 1. Introducción

## 2. Metodología

### 2.1. Dataset

### 2.2. Análisis de componentes independientes (ICA)

Para el análisis de los datos de EEG, se utilizó el método de Análisis de Componentes Independientes (ICA) con el objetivo de identificar y eliminar componentes artefactuales. Inicialmente, se realizó una evaluación visual de los componentes ICA utilizando tres criterios principales: pendiente espectral, perifericidad y suavidad espacial, tal como se describe en la literatura [x].

- Pendiente Espectral: Este criterio mide la pendiente del espectro de potencia de un componente independiente en el rango de frecuencias de 7 a 75 Hz. Los componentes de origen muscular tienden a tener pendientes positivas debido a la alta potencia en frecuencias típicas de EMG, mientras que los componentes de origen neural muestran pendientes negativas.

- Perifericidad: Este criterio evalúa la fuerza de un componente en cada electrodo ponderada por la distancia desde el vértice de la cabeza. Los componentes que tienen origen cerca del borde del casco son más probables de ser artefactos musculares, mientras que los componentes de origen neural se encuentran más cerca del centro del casco.

- Suavidad Espacial: Este criterio calcula la diferencia relativa en magnitud entre pares de electrodos ponderados por la distancia entre ellos. Los componentes que representan una mezcla de varias fuentes tienden a tener grandes variaciones locales y, por lo tanto, altos valores de suavidad espacial.

Después de la evaluación visual, se implementó un proceso de detección automática de artefactos utilizando el método find_bads_muscle de la librería mne [y]. Este método proporciona una identificación automática de componentes contaminados por EMG, basándose en un análisis más robusto de las características espectrales y espaciales.

Finalmente, se decidió tomar en cuenta el método automático para la exclusión de componentes debido a su mayor precisión en la identificación de artefactos; además, se añadió uno de los identificados en la inspección visual. Los componentes identificados como artefactos fueron excluidos del conjunto de datos utilizando la función apply de mne, y los datos corregidos se almacenaron en un nuevo archivo en formato .edf para su posterior análisis.

### 2.3 Preprocesamiento: normalización y alineamiento de la señal

### 2.4 Extracción de características

## 3. Resultados

### 3.1. Filtrado espacial


| <img src="resultados_ICA/ICA0.png" alt="Imagen 1" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA1.png" alt="Imagen 2" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA2.png" alt="Imagen 3" style="width:300px; height:200px;"> |
| <img src="resultados_ICA/ICA3.png" alt="Imagen 4" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA4.png" alt="Imagen 5" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA5.png" alt="Imagen 6" style="width:300px; height:200px;"> |
| <img src="resultados_ICA/ICA6.png" alt="Imagen 7" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA7.png" alt="Imagen 8" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA8.png" alt="Imagen 9" style="width:300px; height:200px;"> |
| <img src="resultados_ICA/ICA9.png" alt="Imagen 10" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA10.png" alt="Imagen 11" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA11.png" alt="Imagen 12" style="width:300px; height:200px;"> |
| <img src="resultados_ICA/ICA12.png" alt="Imagen 13" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA13.png" alt="Imagen 14" style="width:300px; height:200px;"> | <img src="resultados_ICA/ICA14.png" alt="Imagen 15" style="width:300px; height:200px;"> |



<table>
  <tr>
    <td><img src="resultados_ICA/ICA0.png" alt="Imagen 1" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA1.png" alt="Imagen 2" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA2.png" alt="Imagen 3" style="width:300px; height:200px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA3.png" alt="Imagen 4" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA4.png" alt="Imagen 5" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA5.png" alt="Imagen 6" style="width:300px; height:200px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA6.png" alt="Imagen 7" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA7.png" alt="Imagen 8" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA8.png" alt="Imagen 9" style="width:300px; height:200px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA9.png" alt="Imagen 10" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA10.png" alt="Imagen 11" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA11.png" alt="Imagen 12" style="width:300px; height:200px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA12.png" alt="Imagen 13" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA13.png" alt="Imagen 14" style="width:300px; height:200px;"></td>
    <td><img src="resultados_ICA/ICA14.png" alt="Imagen 15" style="width:300px; height:200px;"></td>
  </tr>
</table>





### 3.2. Señal procesada

### 3.3 Extracción de características

## 4. Discusión

### 4.1. Análisis de filtrado espacial y procesamiento 


### 4.2 Análisis de características extraídas



## 5. Conclusión



## 6. Bibliografía

[x]  Dhani Dharmaprani, H. K. Nguyen, T. W. Lewis, D. DeLosAngeles, J. O. Willoughby, and K. J. Pope, “A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components,” PubMed, Aug. 2016, doi: https://doi.org/10.1109/embc.2016.7590828.
‌

[y] “mne.preprocessing.ICA — MNE 1.8.0.dev67+g69f7d88f2 documentation,” Mne.tools, Jun. 13, 2024. https://mne.tools/dev/generated/mne.preprocessing.ICA.html#mne.preprocessing.ICA.find_bads_ecg (accessed Jun. 15, 2024).
‌
