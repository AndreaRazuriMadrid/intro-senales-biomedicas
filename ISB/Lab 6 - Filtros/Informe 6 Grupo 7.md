# INFORME LABORATORIO 6
## Lista de Participantes - Grupo 7

- Andrea Razuri Madrid
- Isabel Leon Luna
- Johanni Bohorquez Gutierrez
- Claudia Camacho Grimaldi
- Jaime Arista Cutipa 

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Materiales y equipos](#3-materiales-y-equipos)
4. [Metodología](#4-metodología)
5. [Resultados](#5-resultados)
6. [Discusión](#6-discusión)
7. [Conclusiones](#7-conclusiones)
8. [Bibliografía](#8-bibliografía)


## 1. Introducción

Un filtro de señales es un dispositivo o método que se utiliza en el procesamiento de señales para permitir el paso de ciertas frecuencias mientras que otras son atenuadas o eliminadas. Los filtros son esenciales en una variedad de aplicaciones tecnológicas y científicas, incluyendo sistemas de audio, comunicaciones y procesamiento de imágenes [1]. 

Existen varios tipos de filtros de señales, clasificados generalmente según la naturaleza de las frecuencias que permiten pasar:

i. Filtro de paso bajo: Permite el paso de señales con frecuencias por debajo de un punto de un corte específico, y son comúnmente utilizados para eliminar ruidos de alta frecuencia [2].

ii. Filtro de paso alto: Operan de manera opuesta a los filtros de paso bajo, bloqueando señales de baja frecuencia y permitiendo el paso de señales de alta frecuencia. Son útiles en aplicaciones donde es necesario eliminar ruidos de fondo de baja frecuencia [2]. 

iii. Filtros de paso banda: Permiten el paso de un rango específico de frecuencias, bloqueando las frecuencias por debajo y por encima de este rango. Son ideales para aislar señales específicas dentro de un espectro más amplio [2].

iv. Filtro rechaza banda: Bloquean un rango específico de frecuencias mientras permiten el paso de todas las demás, utilizados para eliminar frecuencias específicas no deseadas [2].

Los filtros pueden ser analógicos o digitales. Los filtros analógicos utilizan circuitos electrónicos con resistencias, capacitores e inductores para procesar señales eléctricas continuas. Por otro lado, los filtros digitales utilizan algoritmos matemáticos para modificar señales digitales, que son representaciones discretas de las señales analógicas [4].

En términos de diseño, un filtro puede ser descrito por su orden, que indica el número de polos y ceros en su función de transferencia. Un orden mayor generalmente indica una mejor precisión en la conformación de la respuesta en frecuencia del filtro, aunque esto también puede incrementar la complejidad del diseño y los recursos computacionales necesarios para su implementación [3].

Cada tipo de filtro tiene aplicaciones específicas basadas en sus características, como la atenuación de señales no deseadas, la mejora de la calidad de señales en sistemas de comunicación, y la protección de dispositivos electrónicos sensibles a interferencias electromagnéticas [2].

### Filtro analógico 

|   Nombre del Filtro     | Descripción   | 
|---------------|---------------|
| Butterworth | Conocido por su respuesta en frecuencia plana dentro de la banda de paso, lo que significa que no introduce distorsiones en esa región. La transición hacia la banda de rechazo es suave, pero no tan abrupta como en otros tipos del filtro [5].   |
|     Chebyshev   |Este tipo de filtro permite ciertas ondulaciones (ripples) en las bandas de paso, lo que le permite tener una transición más abrupta entre la banda de paso y la banda de rechazo en comparación con el filtro Butterworth. Existen dos tipos: Tipo I, que tiene ripples solo en la banda de paso, y Tipo II, que tiene ripples en la banda de rechazo [5]. |
|   Bessel    | Ofrece la mejor respuesta de fase, preservando la forma de las señales de entrada a lo largo de la banda de paso, lo que lo hace ideal para aplicaciones donde la calidad de la señal temporal es crítica. Sin embargo, su pendiente de corte es menos pronunciada comparada con otros filtros [5].   |
| Elíptico   | Proporciona la transición más abrupta de todos los tipos de filtros entre la banda de paso y la banda de rechazo, pero a costa de ondulaciones tanto en la banda de paso como en la banda de rechazo y una respuesta de fase no lineal [5]  |

Los filtros IIR (Respuesta Impulsiva Infinita) son fundamentales en el procesamiento digital de señales debido a su eficiencia computacional y capacidad de implementación en tiempo real. Estos filtros utilizan una combinación de entradas pasadas y su propia salida pasada para calcular la señal de salida actual, característica que les permite tener una fase efectiva y rápida respuesta en aplicaciones críticas. Según Kuznetsov et al. (2020), los filtros IIR son especialmente valorados en aplicaciones de aprendizaje automático por su linealidad y estabilidad en sistemas dinámicos [6].

<p align="center">
  <img src="señales/IIRFILTERS.png" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig 1. Tipos de filtros IIR [7]</strong>
</p>

Por otro lado, los filtros FIR (Respuesta Impulsiva Finita) son igualmente prevalentes en el ámbito del procesamiento digital de señales. A diferencia de los filtros IIR, los FIR se basan únicamente en un número finito de entradas anteriores y no requieren retroalimentación. Esta propiedad los hace inherentemente estables y libres de oscilaciones, lo cual es crítico en aplicaciones donde la precisión y la predictibilidad son necesarias. Datta y Dutta (2021) destacan que los filtros FIR son ideales para implementaciones en FPGA debido a su estructura regular y predecible, lo que facilita su diseño y optimización [8].

<p align="center">
  <img src="señales/FIRFILTERS.png" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig 2. Ventanas para el diseño de filtros FIR. [9]</strong>
</p>

## 2. Objetivos
- Crear un filtro IIR, seleccionando uno de los siguientes tipos: Bessel, Butterworth, Chebyshev, o Elíptico.
- Diseñar un filtro FIR utilizando dos de las siguientes técnicas de ventaneo: Hanning, Hamming, Bartlett, rectangular, o Blackman.
- Implementar filtros IIR y FIR en el procesamiento de señales ECG, EMG y EEG.
## 3. Materiales y equipos

<div align="center">

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| (R)EVOLUTION  | Kit BITalino  | 1        |
|      -      |Electrodos con gel| 3|
|       -       | Laptop o PC   | 1        |

</div>


## 4. Metodología
**4.1. Análisis de Señales ECG:** 
- Las señales de electrocardiograma (ECG) se obtuvieron durante diferentes condiciones: en reposo basal, durante respiración controlada y después de ejercicio. Se almacenaron las señales en formato de texto y se muestrearon a una frecuencia de 1000 Hz, garantizando una captura adecuada de la dinámica cardíaca sin infracción del teorema de Nyquist.

- Para el análisis y reducción del ruido inherente en las mediciones de ECG, se aplicaron dos tipos de filtros digitales: un Filtro FIR (Respuesta Impulsiva Finita) y un filtro IIR (Respuesta Impulsiva Infinita).

  - Filtro FIR de Pasa-baja: Utilizando la función firwin de la biblioteca SciPy, se diseñó un filtro FIR con ventana de Hamming. Este filtro fue configurado con 101 taps y una frecuencia de corte de 20 Hz, seleccionada para preservar las componentes fundamentales de la señal de ECG mientras se reduce el ruido de alta frecuencia.
  - Filtro IIR Butterworth de Pasa-baja: Para obtener una respuesta de frecuencia más suave, se implementó un filtro IIR tipo Butterworth. Este filtro se configuró de orden 5 y con una frecuencia de corte también de 20 Hz. Se utilizó la función filtfilt para la aplicación del filtro, evitando cualquier desfase en la señal filtrada.

- Ambos filtros se aplicaron a las señales ECG para comparar los efectos del filtrado FIR e IIR en la calidad de las señales procesadas. El objetivo era evaluar cuál de los dos tipos de filtro era más efectivo en minimizar el ruido y mejorar la claridad de las señales para análisis posteriores.

- Las señales crudas y filtradas fueron visualizadas utilizando gráficos que mostraban segmentos de la señal en el tiempo. Esto permitió una comparación directa y visual de los efectos de cada filtro. Se prestó especial atención a la preservación de los picos y formas características del ECG, como los complejos QRS, los cuales son críticos para un diagnóstico clínico acertado.

**4.2. Análisis de Señales EMG:**

- Se obtuvieron las señales de EMG en diferentes actividades músculares: Oposición, Reposo, Extensión y Flexión. Las señales se almacenaron en formato de texto y se muestrearon a una frecuencia de 1000 Hz. Para analizar las señales y reducir el ruido inherente a las mediciones de EMG, se aplicaron dos tipos de filtros digitales: Filtro FIR (Respuesta Impulsiva Finita) y filtro IIR (Respuesta Impulsiva Infinita).
- Para esto se diseñaron los filtros FIR de alta-pasa utilizando la función 'firwin' de la biblioteca SciPY. La configuración del filtro se ajustó específicamente para cada tipo de actividad. Y luego el filtro IIR tipo butterworth de pasa-baja para obtener una respuesta de frecuencia más suave. El filtro se configuró de orden 5 y de frecuencia de corte de 200Hz. Se aplicó a las mismas señales para comparar los efectos del filtrado FIR e IIR en la calidad de las señales procesadas.

**4.3. Análisis de Señales EEG:**

- Lo que se desea obtener por medio del diseño de un filtro IIR es suprimir las interferencias en la toma de datos, debido a frecuencias altas y artefactos. Los filtros IIR utilizan los valores de entrada actuales de la señal como los valores de salida pasados para calcular la salida del filtro. Esto los hace más eficientes en términos de la complejidad computacional para una misma efectividad de filtrado. Para el diseño del filtro se eligió al filtro Butterworth de pasa banda, para el análisis de ondas alfa y beta. 
- Para comprobar estos resultados, se diseño un filtro FIR, y se eligió una ventana Hamming. Con el propósito de extraer las bandas de frecuencias alfa, beta, delta, etc. Dentro de las especificaciones, se consideró una frecuencia de corte entre los rangos de 8 a 30 Hz para el filtro pasa banda. Para el diseño del filtro se eligió al filtro Hamming de pasa banda, para la obtención de una mejora en la resolución en frecuencia, lo que permite una mejor discriminación entre diferentes frecuencias en la señal de EEG. Para el análisis de diferentes señales obtenidas, se aplicaron distintos filtros FIR adaptados a cada condición de medición. En la señal en reposo, se identificaron cuatro picos principales; por lo tanto, se utilizó un filtro con frecuencia de corte de 8 Hz para resaltar estas frecuencias. Durante la actividad de abrir y cerrar los ojos, se implementó un filtro pasabanda configurando un filtro paso bajo con una frecuencia de corte de 4 Hz seguido de un filtro paso alto, con el objetivo de aislar y analizar específicamente la onda alfa. Por último, en la condición donde el sujeto realizaba preguntas matemáticas y simultáneamente parpadeaba, se empleó un filtro paso bajo con una frecuencia de corte de 20 Hz, permitiendo el estudio combinado de las ondas alfa y beta.

Para ambos filtros Se utilizó de una frecuencia de sampleo de 1000 Hz y las frecuencias de corte fueron analizadas de acuerdo a los resultados obtenidos por el análisis espectral. 

## 5. Resultados

**5.1. Análisis de Señales ECG:**
- Se analizaron las señales de electrocardiograma (ECG) con una frecuencia de muestreo de 1000 Hz. Utilizando Python, se extrajeron datos relevantes de la columna 6 de un archivo de texto. Estos datos, provenientes delvsistema biTalino, emplean una configuración bipolar para medir la diferencia amplificada entre dos puntos de medición.

- Los datos digitales se convirtieron a mV utilizando una fórmula basada en el voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits. Luego, las señales se filtraron para reducir el ruido y mejorar la visibilidad de los componentes cardíacos significativos. Se utilizaron dos tipos de filtros: un filtro IIR Butterworth de orden 5 y un filtro FIR con ventana de Hamming, ambos con una frecuencia de corte de 20 Hz.

| Campos          | Señal cruda | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Basal | <img src="señales/ecgBasal.png" alt="Ejercicio" style="width:400px;"> |<img src="señales/ecgBasalButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgBasalHamming.png" alt="Ejercicio" style="width:400px;">|
| Respiración     |<img src="señales/ecgRespiracion.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiracionButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiraciónHamming.png" alt="Ejercicio" style="width:400px;">|
| Post ejercicio  |<img src="señales/ecgEjercicio.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioHamming.png" alt="Ejercicio" style="width:400px;">|

**5.2. Análisis de Señales EMG:**

En este estudio se trabajaron con dos compañeros. Se utilizó una frecuencia de muestreo de 1000 Hz. En el filtro FIR utilizamos 'firwin' para la creación del filtro pasa alta. La configuración se ajustó a cada actividad. 

- Oposición: 3 coeficientes, frecuencia de corte de 300 Hz.
- Reposo: 100 coeficientes, frecuencia de corte de 400 Hz para reservar la señal eliminando los componentes de baja frecuencia.
- Extensión: 3 coeficientes, frecuencia de corte de 10 Hz.
- Flexión: 3 coeficientes, frecuencia de corte de 300 Hz.

Sin embargo trans probar estas frecuencias de corte no se noto ninguna diferencia asi que para simplificar el codigo utilizado se uso solo la frecuencia de corte de 200 Hz.

Mientras el que filtro IIR se utilizó Butterworth de pasa baja para obtener una respuesta más suave. El filtro se configuró con un orden de 5 y una frecuencia de corte de 200 Hz. El filtro IIR se aplicó a las mismas señales para comparar los efectos del filtrado FIR e IIR en la calidad de las señales procesadas.


- El primer compañero tuvo estos resultados cuando se le aplicó el filtro FIR:

| Ejercicio   | Señal original | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Oposición |  <img src="señales/emg/emg_Jo_oposicion.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Jo_oposicion_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Jo_oposicion_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Reposo |   <img src="señales/emg/emg_Jo_reposo.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Jo_reposo_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Jo_reposo_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Extensión |  <img src="señales/emg/emg_Jo_extension.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Jo_extension_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Jo_extension_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Flexión |  <img src="señales/emg/emg_Jo_flexion.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Jo_flexion_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Jo_flexion_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |




i. Oposición: En la señal original, muestra viarabilidad constante a lo alrgo del tiempo con una amplitud que varía en un rango estrecho. Luego, con el filtro FIR parece haber suavizado algunos picos y valles de la señal, reduciendo el ruido y dejando uan representación más limpia de las fluctuaciones de la señal. La forma de la señal se mantiene en gran medida, lo que indica que el filtro ha sido efectivo sin ser demasiado agresivo. Luego, la señal filtrada por IIIR muestra una reducción notable en la amplitudd e las fluctuaciones. Esto indica que el filtro IIR ha suavizado efectivamente la señal, eliminando parte del ruido de alta frecuencia y posiblemente algunos componentes útiles, lo que puede ser indicativo de que la configuración del filtro necesita ajustes para preservar más características de la señal original. 

ii. Reposo: La señal original, es predonmianntemente plana con variaciones pequeñas pero notables en amplitud. Luego, la señal filtrada por el filtro FIR parece una línea plana, lo que indica que el filtro ha eliminado prácticamente toda la variabilidad. Esto sugiere que es filtro puede estar configurado con una frecuencia demasiado baja, eliminado así componentes escenciales de la señal. Luego, la señal filtrada por IIR aparece como una línea plana, indicando que el filtro IIR ha eliminado prácticamente todas las fluctuaciones. Este es un caso claro donde el filtro está siendo demasiado agresivo, sugiriendo la necesidad de ajustar la frecuencia de corte o reducir el orden del filtro para conservar más de la señal de baja amplitud.

iii. Extensión: Similar a la señal de Oposición, con una amplitud que varía dento de un rango entrescho pero con picos más definidos. El filtro FIR ha suavizado significativamente la señal. La señal retiene la forma general pero con menos vairabilidad y picos menos pronunciados. Por la parte del filtro IIR, la señal filtrada muestra una amplitud reducida y menos variabilidad. El filtro ha suavizado los picos y las caídas, pero al mismo tiempo podría estar atenuando detalles importantes de la señal.

iv. Flexión: La señal original presenta más variabilidad y rango de amplitud que las otras actividades. El efecto del filtro FIR es su suavizado, aunque la señal sigue mostrando variabilidad y picos, lo cual es positivo por que indica que el filtro no ha sido excesivamente restrictivo. Y el filtro IIR, hace que la señal filtrada sigue siendo reconocible pero con menor ruido y variabilidad. Aunque se conservan mejor las características generales que en otras señales, aún hay una notable reducción en la amplitud y los detalles finos.


- El segundo compañero tuvo estos resultados cuando se le aplicó el filtro FIR:

| Ejercicio   | Señal original | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Oposición |  <img src="señales/emg/emg_Ja_oposicion.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Ja_oposicion_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Ja_oposicion_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Reposo |   <img src="señales/emg/emg_Ja_reposo.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Ja_reposo_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Ja_reposo_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Extensión |  <img src="señales/emg/emg_Ja_extension.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Ja_extension_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Ja_extension_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |
| Flexión |  <img src="señales/emg/emg_Ja_flexion.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |<img src="señales/emg/emg_Ja_flexion_IIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> | <img src="señales/emg/emg_Ja_flexion_FIR.PNG" alt="Ejercicio" style="width:675px; height:125px;"> |

En todas las pruebas excepto la prueba de reposo el segundo participante muestro una mayor amplitud en la señal tomada
i. Oposición: La señal original muestra variabilidad constante a lo largo del tiempo con una amplitud que varía en un rango estrecho. Con el filtro FIR, algunos picos y valles de la señal parecen suavizarse, reduciendo el ruido y dejando una representación más limpia de las fluctuaciones. La forma de la señal se mantiene en gran medida, indicando que el filtro ha sido efectivo sin ser demasiado agresivo. Sin embargo, la señal filtrada por IIR muestra una reducción notable en la amplitud de las fluctuaciones, lo que sugiere que el filtro IIR ha sido efectivo en suavizar la señal, aunque posiblemente ha eliminado algunos componentes útiles. Sería necesario ajustar la configuración del filtro para preservar más características de la señal original.

ii. Reposo: La señal original es predominantemente plana con pequeñas pero notables variaciones en amplitud. La señal filtrada por el filtro FIR parece una línea plana, lo que indica una eliminación casi completa de la variabilidad. Esto sugiere que el filtro podría estar configurado con una frecuencia demasiado baja, eliminando componentes esenciales de la señal. Por otro lado, la señal filtrada por IIR también parece una línea plana, lo que indica un filtrado demasiado agresivo. Sería necesario ajustar la frecuencia de corte o reducir el orden del filtro para conservar más de la señal original.

iii. Extensión: Similar a la señal de Oposición, con variabilidad en un rango estrecho pero con picos más definidos. El filtro FIR ha suavizado la señal, aunque se conserva la forma general con menos variabilidad y picos menos pronunciados. La señal filtrada por IIR muestra una amplitud reducida y menos variabilidad. Si bien el filtro ha suavizado los picos y las caídas, podría estar atenuando detalles importantes de la señal.

iv. Flexión: La señal original presenta más variabilidad y amplitud que las otras actividades. El filtro FIR suaviza la señal sin eliminar completamente la variabilidad y los picos, lo cual es positivo ya que indica que el filtro no es demasiado restrictivo. La señal filtrada por IIR conserva las características generales pero con menos ruido y variabilidad. Aunque se conservan mejor las características generales que en otras señales, todavía hay una reducción notable en la amplitud y los detalles finos. Sería necesario ajustar la configuración del filtro para equilibrar la reducción de ruido con la preservación de detalles importantes.


**5.3. Análisis de Señales EEG:**
  - En este estudio se procesaron señales EEG registradas a una frecuencia de muestreo de 1000 Hz, empleando el dispositivo BiTalino junto con la disposición estándar de electrodos según el sistema internacional 10-20, y aplicando un método monopolar con dos electrodos posicionados en una región cerebral específica más un electrodo de referencia. Para la conversión de las señales a milivoltios, se utilizó una ecuación que considera un voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits, permitiendo una cuantificación precisa de la señal EEG. Posteriormente, para mejorar la calidad de las señales eliminando ruidos no deseados, se implementaron filtros digitales. Se aplicaron dos tipos de filtros: un filtro IIR Butterworth de orden 9 y un filtro FIR diseñado con una ventana de Hanning, el primero configurados con una frecuencia de corte de 35 Hz y el segundo se trabajó por separado para analizar las frecuencias de las ondas alfa y beta. Estos filtros fueron esenciales para atenuar componentes de alta frecuencia y ruidos, facilitando así una mejor interpretación y análisis de las señales EEG.


| Ejercicio   | Señal original | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Reposo |  <img src="señales/EEG/Reposo/SeñalSINFiltrar.png" alt="Reposo" style="width:675px; height:125px;"> |<img src="señales/EEG/Reposo/SeñalIIR.png" alt="ReposoIIR" style="width:675px; height:125px;"> | <img src="señales/EEG/Reposo/SeñalFIR.png" alt="ReposoFIR" style="width:675px; height:125px;"> |
| Abrir y Cerrar los ojos |   <img src="señales/EEG/AbrirYCerrar/señalSINFiltrar.png" alt="Ojos" style="width:675px; height:125px;"> |<img src="señales/EEG/AbrirYCerrar/SeñalIIR.png" alt="OjosIIR" style="width:675px; height:125px;"> | <img src="señales/EEG/AbrirYCerrar/SeñalFIR.png" alt="OjosFIR" style="width:675px; height:125px;"> |
| Preguntas matemáticas |   <img src="señales/EEG/Preguntas/señalSINFiltrar.png" alt="preguntas" style="width:675px; height:125px;"> |<img src="señales/EEG/Preguntas/señalIIR.png" alt="preguntasIIR" style="width:675px; height:125px;"> | <img src="señales/EEG/Preguntas/señalFIR.png" alt="preguntasFIR" style="width:675px; height:125px;"> |

## 6. Discusión

**6.1. Análisis de Señales ECG:**
- Elección del Filtro y Configuración:
  - Filtro IIR Butterworth: Se eligió un filtro Butterworth de orden 5 con una frecuencia de corte de 20 Hz, basado en su capacidad para ofrecer una respuesta de frecuencia plana en la banda de paso, lo que es crucial para no alterar las características esenciales de la señal de ECG. Este diseño se apoya en el estudio de S. Basu y S. Mamud, donde se examina cómo la variación del orden y la frecuencia de corte afecta la eliminación de ruido en las señales de ECG [10].
  - Filtro FIR con Ventana de Hamming: La elección de la ventana de Hamming para el diseño del filtro FIR se basa en su efectividad en la reducción de ruido mientras mantiene la integridad de la señal. Según un estudio reciente por M. Das, R. Kumar, y B. Sahana, el uso de una función de ventana híbrida que incorpora la ventana de Hamming en filtros FIR demuestra una mejora significativa en la desruidización de señales ECG, proporcionando una solución eficaz para aplicaciones clínicas donde la claridad de la señal es crucial [11].
- Análisis de las Señales Filtradas:
  - Las señales filtradas mostraron una notable reducción del ruido de alta frecuencia y los artefactos, validando la elección del orden del filtro y la frecuencia de corte. Y.A. Altay y A.S. Kremlev discuten en su estudio cómo los filtros polinomiales, incluidos los basados en Butterworth, mejoran la precisión del procesamiento de la señal de ECG, respaldando nuestras observaciones sobre la efectividad de los filtros elegidos [12].

**6.2. Análisis de Señales EMG:**
El uso de un filtro Hamming y un filtro Butterworth para una señal de EMG depende de varios factores, como las características de la señal y los requisitos de la aplicación. Aquí hay una breve explicación de por qué podrías optar por cada uno, junto con referencias para profundizar en cada tema:

-Filtro Hamming:
  Rendimiento en el dominio de la frecuencia: Los filtros Hamming son tipos de filtros de ventana que se utilizan comúnmente en el dominio de la frecuencia.   Tienen una respuesta en frecuencia más suave en comparación con otros filtros de ventana, lo que puede ayudar a preservar mejor las características de la    señal EMG.
-Reducción de la interferencia de frecuencia: Los filtros de ventana como el Hamming pueden ser útiles para reducir la interferencia de frecuencia no     deseada en la señal EMG, como el ruido de alta frecuencia.

Filtro Butterworth:
Características de diseño personalizables: Los filtros Butterworth son conocidos por su respuesta plana en la banda de paso y una caída rápida en la banda de parada. Esto los hace útiles cuando se necesita un filtro con características de diseño personalizables.

En particular al ser usado en combinacion, de highpass filter en 15 Hz y un notch para eliminar el ruido electrico a los 60 Hz. [15]
Ademas combinado con un filtro lowpass con frecuencia de corte alrededor de los 500Hz eliminatia la mayor parte del ruido blanco, sin afectar a la señal que tiene poca energia a esas frecuencias altas. [16]


**6.3. Análisis de Señales EEG:**
- Elección del Filtro y Configuración:
  - Filtro FIR Hamming: Se consideró un filtro Hamming ya que atenúa los artefactos de borde que pueden ocurrir al aplicar la transformada de Fourier a una señal de EEG, con mejores resultados. Para esto se consideró el análisis de las ondas alfa, por tanto, se eligió las frecuencias de corte dentro de los rangos de 8-13 Hz. Para el diseño del filtro se consideró un filtro pasa banda, en donde para su desarrollo se realizó el diseño de un filtro pasabaja de orden 200 y posteriormente de la aplicación de un filtro pasa alta de orden 101. Se tomó en consideración las frecuencias de corte también de acuerdo a estudios realizados por Bowman AD et all, ya que utilizaron una banda de frecuencia alfa de 8 a 13 Hz a través de los 4 canales bipolares usando una transformada rápida de Fourier con ventana de Hamming [14]. 
  - Filtro IIR Butterworth: Se seleccionó un filtro Butterworth IIR de orden 9 con una frecuencia de corte de 35 Hz para el procesamiento de señales EEG, basado en los picos identificados en el análisis espectral. Esta elección se fundamenta en datos de investigaciones anteriores y se alinea con los estudios realizados por Sabine L. y Sarang S., quienes recomendaron una frecuencia de corte entre 47 y 53 Hz, abarcando armónicos de hasta 500 Hz. En su investigación, utilizaron un filtro DFT calibrado a estos valores de frecuencia, logrando una eficacia notable en el filtrado de la señal [13]. Adicionalmente, considerando las bandas de frecuencia típicas en EEG, la elección de una frecuencia de corte de 35 Hz resulta adecuada para preservar las ondas alfa (8-12 Hz), beta (12-30 Hz) y theta (4-8 Hz), que son fundamentales en este estudio. Esto permite mantener la integridad de estas bandas esenciales, a la vez que se eliminan o atenúan las interferencias y ruidos de frecuencias más altas, asegurando así la calidad y la precisión de las señales EEG analizadas.

- Análisis de las Señales Filtradas - IIR:
  - Reposo:
    De acuerdo a las gráficas obtenidas, podemos ver que el filtro ha logrado atenuar las interferencias de la señal original. En la señal filtrada se han conservado las frecuencias más importantes, en este caso, en el tiempo 25 segundos en adelante, se observa que la amplitud de la señal alcanza hasta 0.6 mV. Lo cual es un resultado más certero, considerando que una señal eeg en reposo obtiene una magnitud en mV cercana a cero. En el caso de la señal antes del tiempo 25 segundos, se ha logrado también filtrar interferencias. Aquí se tomó en cuenta el parpadeo involuntario de los ojos como posible factor ante la obtención de picos con una amplitud superior a 1 mV, el cual en la señal original alcanza una amplitud superior a 1.5 mV.
  - Abrir y cerrar ojos:
    En las gráficas obtenidas en Abrir y Cerrar los ojos, vemos que el filtro ha logrado atenuar significativamente los ruidos e interferencias de la señal. En la señal original tenemos una amplitud superior a 1.5 mV; sin embargo, en la gráfica de la señal filtrada obtenemos una amplitud inferior a 1.5 mV. En ambas señales podemos ver los 5 ciclos de repetición que se dio al abrir y cerrar los ojos, en el mismo periodo de tiempo. Se va a considerar una señal filtrada a partir del tiempo 20 segundos, ya que se aprecia el aumento de la amplitud de la señal entre 0-10 segundos, lo cual se podría deber al diseño del filtro realizado, en cuanto a la delimitación del orden del filtro, las frecuencias de corte utilizadas, así como la elección del filtro.
  - Preguntas:
    En la señal filtrada de Preguntas y Respuestas, la señal alcanza una amplitud de hasta a 1.5 mV. Podemos observar que durante el tiempo de 20-40 segundos hemos atenuado la amplitud de la señal hasta 1 mV. De igual forma, se han conservado los picos en 10 a 20 segundos ya que fue en este tiempo que se realizaron las preguntas. Respecto al análsis espectral de la señal se encontraron las ondas alfa en 13 Hz y las ondas beta en 30 Hz aproximadamente. A partir del tiempo 40 segundos, se observan picos de mayor amplitud, lo cual se debe a que en este punto se realizaron preguntas de mayor complejidad en la obtensión de la señal. Aquí se utilizó frecuencia de corte entre los randos de 8 a 30 Hz para el análisis de las ondas eeg. 


- Análisis de las Señales Filtradas - FIR:
  - Reposo:
    Basándonos en las gráficas obtenidas, se puede observar que el filtro ha logrado reducir las interferencias presentes en la señal original. En la señal filtrada, se han conservado las frecuencias más relevantes. Por ejemplo, a partir de los 25 segundos, la amplitud de la señal alcanza hasta 0.6 mV, lo cual es un resultado más preciso, considerando que una señal EEG en reposo tiene una amplitud cercana a cero. Antes de los 25 segundos, también se han eliminado las interferencias. Se consideró el parpadeo involuntario de los ojos como un posible factor que contribuye a picos con una amplitud superior a 1 mV. En la señal original, estos picos alcanzan una amplitud superior a 1.5 mV.
  - Abrir y cerrar ojos:
    En la señal filtrada podemos observar una atenuación de los picos, alcanzando una amplitud de hasta 1 mV. Se logra visualizar los 5 ciclos de repetición entre los tiempos de 12 a 22s, por ejemplo. Cuando se cierran los ojos, se obtuvo una amplitud de 0.5 mV aproximadamente, esto se debe a que la persona se encuentra en ese momento en reposo. Para el diseño de este filtro se tomó en consideración las ondas alfa que se dan entre las frecuencias de 8 - 13 Hz, aquí se diseño primero un filtro pasa baja con un orden de 200; posteriormente, se diseño un filtro pasa alto con un orden de 101, esto enfocado en la creación de un filtro pasa banda. De acuerdo a los resultados, podemos decir que se ha logrado filtrar la señal eeg, al atenuar y eliminar artefactos en la toma de datos.
  - Preguntas:
    De acuerdo a la señal filtrada de Preguntas y Respuestas, podemos ver una atenuación de la amplitud también, aquí la amplitud alcanza hasta 1.5 mV. Aquí se conservan los picos representativos entre 10 y 20 segundos, ya que fue en el tiempo donde se realizaron las preguntas. Respecto al análsis espectral de la señal se encontraron las ondas alfa en 8 Hz y las ondas beta en 13 Hz aproximadamente. Lo cual corresponde al análsis realizado, en donde se está implicando actividades mentales que demandan mayor velocidad de transmisión.



## 7. Conclusiones
- La inspección visual de las señales filtradas versus las señales crudas demostró claramente la efectividad de ambos tipos de filtros en la mejora de la calidad de la señal ECG. En particular, el filtro FIR, con sus características de fase lineal, mostró ser superior para aplicaciones donde la integridad de la fase es crucial.

 
- En las señales EMG, ambos tipos de filtrado se mostraron efectivos. Ya depende de requerimientos especificos la decision de cual utilizar, entre estos destaca la combinacion de filtros highpass junto con un uno notch para eliminar rudio electrico y sus artefactos, ademas de uno low pass para el ruido blanco muestran buenos resultados.

## 8. Bibliografía
[1] Haily, 'Filtro digital - Definición y explicación,' TechEdu, 26 oct. 2022. [En línea]. Disponible: https://techlib.net/techedu/filtro-digital/. [Accedido: 03-may-2024]

[2] Electropreguntas, 'Los Filtros Electrónicos Más Comunes Y Su Funcionamiento,' Electropreguntas, 2023. [En línea]. Disponible: https://electropreguntas.com/los-10-tipos-de-filtros-electronicos-mas-utilizados/. [Accedido: 03-may-2024].

[3] Industriapedia, 'Filtro Butterworth: Optimiza tu señal de forma eficiente,' Industriapedia, 2023. [En línea]. Disponible: https://industriapedia.com/que-es-el-filtro-butterworth/. [Accedido: 03-may-2024]

[4] Learning About Electronics, 'Filtro Paso Alto- Explicado,' Learning About Electronics, [En línea]. Disponible: http://www.learningaboutelectronics.com/Articulos/Filtro-paso-alto.php. [Accedido: 03-may-2024].

[5] Electrositio, '¿Qué Es Un Filtro Analógico? - Diferentes Tipos De Filtros Analógicos,' Electrositio, 2023. [En línea]. Disponible: https://electrositio.com/que-es-un-filtro-analogico-diferentes-tipos-de-filtros-analogicos/. [Accedido: 03-may-2024].

[6] B. Kuznetsov, J.D. Parker et al., "Differentiable IIR filters for machine learning applications," in Proceedings of the International Conference on Digital Audio Effects (DAFx), 2020. [Acceso en línea]: https://dafx2020.mdw.ac.at/proceedings/papers/DAFx2020_paper_52.pdf

[7] “What Are High-Pass Filters? How & When To Use Them (+ Tips),” Unison.audio, May 06, 2023. https://unison.audio/high-pass-filters/ (accessed May 04, 2024).

[8] D. Datta, H.S. Dutta, "High performance IIR filter implementation on FPGA," Journal of Electrical Systems and Information Technology, 2021. [Acceso en línea]: https://link.springer.com/article/10.1186/s43067-020-00025-4

[9] “Perform Analysis and Design for the Spectral Analysis Case Study - dummies,” Dummies.com, 2016. https://www.dummies.com/article/business-careers-money/careers/trades-tech-engineering-careers/perform-analysis-and-design-for-the-spectral-analysis-case-study-165562/ (accessed May 04, 2024).
‌
[10] S. Basu and Samiul Mamud, “Comparative Study on the Effect of Order and Cut off Frequency of Butterworth Low Pass Filter for Removal of Noise in ECG Signal,” Sep. 2020, doi: https://doi.org/10.1109/icce50343.2020.9290646.

[11] M. Das, R. Kumar, y B. Sahana, "Implementation of effective hybrid window function for ECG signal denoising," Traitement du Signal, vol. 37, no. 2, pp. 305-312, 2020. [En línea]. Disponible: https://www.researchgate.net/publication/340100534_Implementation_of_Effective_Hybrid_Window_Function_for_ECG_Signal_Denoising

[12] Y. A. Altay y A. S. Kremlev, "Polynomial filtering of low-and high-frequency noise for improving the accuracy of ECG signal processing: new advancements," Cardiometry, 2020. [En línea]. Disponible: https://www.researchgate.net/publication/343295169_Polynomial_filtering_of_low-_and_high-_frequency_noise_for_improving_the_accuracy_of_ECG_signal_processing_new_advancements

[13] Sabine , L. and Sarang, S.D. (2019) Reducing power line noise in EEG and MEG data via spectrum interpolation, Neuroimage, 2019 Apr 1. Disponible: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6456018/ (Accessed: 03 May 2024). 

[14] Bowman AD, Griffis JC, Visscher KM, Dobbins AC, Gawne TJ, DiFrancesco MW, Szaflarski JP. Relationship Between Alpha Rhythm and the Default Mode Network: An EEG-fMRI Study. J Clin Neurophysiol. 2017 Nov;34(6):527-533. doi: 10.1097/WNP.0000000000000411. PMID: 28914659; PMCID: PMC8428580.

[15] Mello, R. G. T., Oliveira, L. F., & Nadal, J. (2007). "Digital Butterworth filter for subtracting noise from low magnitude surface electromyogram". Computer Methods and Programs in Biomedicine, 87(1), 28–35. https://doi.org/10.1016/j.cmpb.2007.04.004.
[16] M. Boyer, L. Bouyer, J.-S. Roy, and Alexandre Campeau-Lecours, “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review,” Sensors, vol. 23, no. 6, pp. 2927–2927, Mar. 2023, doi: https://doi.org/10.3390/s23062927.
‌
