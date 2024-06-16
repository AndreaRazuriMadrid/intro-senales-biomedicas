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

El análisis de componentes independientes (ICA, por sus siglas en inglés) es una poderosa técnica utilizada para transformar vectores aleatorios multidimensionales observados en componentes que son estadísticamente lo más independientes posible entre sí, siendo aplicada en diversos campos como la separación ciega de fuentes y la extracción de características [a].

## 2. Metodología

### 2.1. Dataset
La señal con la que se trabajó pertenece a PhysioNet de acuerdo a registros de EEG de sujetos antes y durante la realización de tareas de artimética mental. Los EEG se registraron de forma monopolar usando el sistema internacional 10/20 de 23 cananles. Se utilizó un filtro paso alto con una frecuencia de corte de 30 Hz para obtener una señal sin artefactos de 60 segundos de duración. En la etapa de procesamiento, se utilizó el Análisis de Componentes Independientes (ICA) para eliminar artefactos (músculos, ojos, superposición cardíaca, ect.). La tarea aritmética constaba de realizar la resta en serie de dos números, en donde cada prueba comenzó con la comunicación oral de número de 4 dígitos y 2 dígitos. 

### 2.2. Análisis de componentes independientes (ICA)

Para el análisis de los datos de EEG, se utilizó el método de Análisis de Componentes Independientes (ICA) con el objetivo de identificar y eliminar componentes artefactuales. Inicialmente, se realizó una evaluación visual de los componentes ICA utilizando tres criterios principales: pendiente espectral, perifericidad y suavidad espacial, tal como se describe en la literatura [x].

- Pendiente Espectral: Este criterio mide la pendiente del espectro de potencia de un componente independiente en el rango de frecuencias de 7 a 75 Hz. Los componentes de origen muscular tienden a tener pendientes positivas debido a la alta potencia en frecuencias típicas de EMG, mientras que los componentes de origen neural muestran pendientes negativas.

- Perifericidad: Este criterio evalúa la fuerza de un componente en cada electrodo ponderada por la distancia desde el vértice de la cabeza. Los componentes que tienen origen cerca del borde del casco son más probables de ser artefactos musculares, mientras que los componentes de origen neural se encuentran más cerca del centro del casco.

- Suavidad Espacial: Este criterio calcula la diferencia relativa en magnitud entre pares de electrodos ponderados por la distancia entre ellos. Los componentes que representan una mezcla de varias fuentes tienden a tener grandes variaciones locales y, por lo tanto, altos valores de suavidad espacial.

Después de la evaluación visual, se implementó un proceso de detección automática de artefactos utilizando el método find_bads_muscle de la librería mne [y]. Este método proporciona una identificación automática de componentes contaminados por EMG, basándose en un análisis más robusto de las características espectrales y espaciales.

Finalmente, se decidió tomar en cuenta el método automático para la exclusión de componentes debido a su mayor precisión en la identificación de artefactos; además, se añadió uno de los identificados en la inspección visual. Los componentes identificados como artefactos fueron excluidos del conjunto de datos utilizando la función apply de mne, y los datos corregidos se almacenaron en un nuevo archivo en formato .edf para su posterior análisis.

### 2.3 Preprocesamiento: normalización y alineamiento de la señal

1. **Carga de Datos EEG**:
    - Los datos EEG fueron cargados desde un archivo en formato EDF utilizando la biblioteca MNE-Python. Este proceso involucró la lectura completa del archivo en memoria para facilitar su posterior manipulación y análisis.

2. **Filtrado de la Señal**:
    - Se aplicó un filtro de paso banda con frecuencias de corte en 1 Hz y 40 Hz. Este paso es crucial para limpiar la señal de EEG, eliminando componentes de baja frecuencia (como el ruido de desplazamiento de la línea base) y de alta frecuencia (como el ruido de la red eléctrica y otros artefactos no neuronales).

3. **Aplicación de ICA (Análisis de Componentes Independientes)**:
    - Se utilizó el Análisis de Componentes Independientes (ICA) para identificar y corregir artefactos presentes en la señal EEG. El número de componentes independientes se ajustó a 19, correspondiente al número de canales disponibles en los datos. Este ajuste es esencial para garantizar que el modelo ICA tenga una cantidad adecuada de componentes para trabajar.

4. **Exclusión de Componentes de Artefactos**:
    - Dado que no se encontraron canales específicos para la detección de movimientos oculares (EOG) ni puntos de digitización de electrodos en los datos, se optó por un enfoque manual. Se identificaron y excluyeron los componentes principales con mayor varianza, que generalmente están asociados a artefactos. En este caso, se excluyeron los primeros dos componentes.

5. **Aplicación de ICA a la Señal**:
    - Posteriormente, se aplicaron las correcciones derivadas del ICA a la señal original. Esto permitió limpiar la señal eliminando las contribuciones de los componentes de artefactos identificados.

6. **Normalización de la Señal**:
    - Se llevó a cabo una normalización de la señal mediante la técnica de normalización z-score. Este proceso consistió en restar la media y dividir por la desviación estándar de cada canal, lo que permite estandarizar los datos y hacer que tengan media cero y desviación estándar uno. Esta normalización facilita la comparación entre diferentes canales y sujetos.

7. **Alineación de la Señal**:
    - Se realizó un resampleo de la señal a una frecuencia de muestreo de 100 Hz. Este paso asegura que la señal tenga una tasa de muestreo uniforme, lo cual es importante para muchos métodos de análisis que asumen una temporalidad constante en los datos.

8. **Visualización y Guardado de los Datos Preprocesados**:
    - Finalmente, se visualizó la señal preprocesada para verificar la efectividad de los pasos anteriores y se dejó abierta la posibilidad de guardar los datos preprocesados en un nuevo archivo, ya sea en formato EDF o FIF, para su uso posterior.

Esta metodología proporciona una forma estructurada y detallada para el preprocesamiento de señales EEG, asegurando que los datos estén limpios y listos para el análisis posterior. Si necesitas más detalles o ajustes específicos, no dudes en pedírmelo.

### 2.4 Extracción de características

## 3. Resultados

### 3.1. Filtrado espacial


<table>
  <tr>
    <td><img src="resultados_ICA/ICA0.png" alt="Imagen 1" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA1.png" alt="Imagen 2" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA2.png" alt="Imagen 3" style="width:350px; height:250px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA3.png" alt="Imagen 4" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA4.png" alt="Imagen 5" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA5.png" alt="Imagen 6" style="width:350px; height:250px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA6.png" alt="Imagen 7" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA7.png" alt="Imagen 8" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA8.png" alt="Imagen 9" style="width:350px; height:250px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA9.png" alt="Imagen 10" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA10.png" alt="Imagen 11" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA11.png" alt="Imagen 12" style="width:350px; height:250px;"></td>
  </tr>
  <tr>
    <td><img src="resultados_ICA/ICA12.png" alt="Imagen 13" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA13.png" alt="Imagen 14" style="width:350px; height:250px;"></td>
    <td><img src="resultados_ICA/ICA14.png" alt="Imagen 15" style="width:350px; height:250px;"></td>
  </tr>
</table>

Siguiendo los 3 criterios establecidos en la metodología, se eligió las ICAs 6, 8, 9 y 14:
 - ICA006: debido a la posición muy cerca del contorno puede considerarse un artefacto o una combinación de esto y una señal.
 - ICA008: debido a su posición cerca del borde, la poca expansión del punto de fuente y el pulso en el espectro de poder dentro del rango de 7 a 75 Hz.
 - ICA009: debido a la poca expansión del punto de fuente.
 - ICA014: debido a la poca expansión del punto de fuente y el pico en el espectro de poder entre el rango de 7 a 75 Hz.

Además, se usó la función de find_band_muscles de la librería MNE para obtener de forma automática las ICAs a eliminar:

<img src="resultados_ICA/scores.png"> 

Finalmente, después de esto se decidió eliminar ICA006 y ICA014, ya que la primera coincide con la inspección visual y la determinación automática, y la segunda visualmente es la que más probailidad tiene de ser un artefacto.

### 3.2. Señal procesada

Según los resultados que se muestran en la imagen de las señales EEG después del preprocesamiento. Cada línea horizontal representa un canal de EEG diferente, etiquetado según el sistema internacional 10-20 (Fp1, Fp2, F3, F4, F7, F8, T7, T8, C3, C4).

#### Visualización de las Épocas (epochs.plot())
1. Eje Y (Vertical):
   * Representa los distintos canales de EEG (Fp1, Fp2, F3, F4, etc)
   * Cada línea corresponde a la señal registrada por un canal específico.
2. Eje X (Horizontal):
   * Reresenta el tiempo en segundos.
   * La escala va desde 0 hasta 50 segundos.
3. Señal EEG:
   * Las oscilaciones en las líneas muestran la actividad eléctrica cerebral registrada por los electrodos en el tiempo
   * Se observan patrones rítmicos y oscilaciones regulares, lo que es típico de las señales EEG 
4. Escala de Amplitud:
   *Indica por el valor en microvoltios (µV) en la parte superior izquierda del gráfico.

### 3.3 Extracción de características

## 4. Discusión

### 4.1. Análisis de filtrado espacial y procesamiento 



### 4.2 Análisis de características extraídas

* Actividad Cerebral: Las señales muestran una actividad continua y rítmica a lo largo del tiempo registrado.
* Diferencias entre los Canales: Se observan diferencias en la amplitud y la frecuencia de las oscilaciones entre los diferentes canales, lo que sugiere diferencias en la actividad cerebral subyacente en diferentes regiones.
* Patrones Temporales: Algunas señales, como Fp1 y Fp2, muestran una actividad más prominente en las frecuencias más bajas (ondas lentas), mientras que otras, como F7 y F8, exhiben oscilaciones más rápidas y de mayor frecuencias.

Dado que tus datos provienen de un estudio en PhysioNet sobre la actividad cerebral durante tareas de aritmética mental, cada época puede corresponder a un segmento donde los sujetos estaban realizando cálculos. El filtro paso alto y el uso de ICA para eliminar artefactos son técnicas estándar para limpiar los datos y asegurar que las señales que estás analizando representen la actividad cerebral relevante.

## 5. Conclusión



## 6. Bibliografía

[a] A. Hyvärinen, "Fast and robust fixed-point algorithms for independent component analysis," IEEE Transactions on Neural Networks, vol. 10, no. 3, pp. 626-634, 1999, doi: 10.1109/72.761722.

[x]  Dhani Dharmaprani, H. K. Nguyen, T. W. Lewis, D. DeLosAngeles, J. O. Willoughby, and K. J. Pope, “A comparison of independent component analysis algorithms and measures to discriminate between EEG and artifact components,” PubMed, Aug. 2016, doi: https://doi.org/10.1109/embc.2016.7590828.
‌

[y] “mne.preprocessing.ICA — MNE 1.8.0.dev67+g69f7d88f2 documentation,” Mne.tools, Jun. 13, 2024. https://mne.tools/dev/generated/mne.preprocessing.ICA.html#mne.preprocessing.ICA.find_bads_ecg (accessed Jun. 15, 2024).
‌
