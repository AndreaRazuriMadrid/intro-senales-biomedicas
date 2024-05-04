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

Los filtros IIR (Respuesta Impulsiva Infinita) son fundamentales en el procesamiento digital de señales debido a su eficiencia computacional y capacidad de implementación en tiempo real. Estos filtros utilizan una combinación de entradas pasadas y su propia salida pasada para calcular la señal de salida actual, característica que les permite tener una fase efectiva y rápida respuesta en aplicaciones críticas. Según Kuznetsov et al. (2020), los filtros IIR son especialmente valorados en aplicaciones de aprendizaje automático por su linealidad y estabilidad en sistemas dinámicos [1].

<p align="center">
  <img src="señales/IIRFILTERS.png" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig 1. Tipos de filtros IIR [2]</strong>
</p>

Por otro lado, los filtros FIR (Respuesta Impulsiva Finita) son igualmente prevalentes en el ámbito del procesamiento digital de señales. A diferencia de los filtros IIR, los FIR se basan únicamente en un número finito de entradas anteriores y no requieren retroalimentación. Esta propiedad los hace inherentemente estables y libres de oscilaciones, lo cual es crítico en aplicaciones donde la precisión y la predictibilidad son necesarias. Datta y Dutta (2021) destacan que los filtros FIR son ideales para implementaciones en FPGA debido a su estructura regular y predecible, lo que facilita su diseño y optimización [3].

<p align="center">
  <img src="señales/FIRFILTERS.png" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig 2. Ventanas para el diseño de filtros FIR. [4]</strong>
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

**4.2. Análisis de Señales EMG:**

**4.3. Análisis de Señales EEG:**
Lo que se desea obtener por medio del diseño de un filtro IIR es suprimir las interferencias en la toma de datos, debido a frecuencias altas y artefactos. Los filtros IIR utilizan los valores de entrada actuales de la señal como los valores de salida pasados para calcular la salida del filtro. Esto los hace más eficientes en términos de la complejidad computacional para una misma efectividad de filtrado. 

Para comprobar estos resultados, se diseño un filtro FIR, y se eligió una ventana Hamming. Con el propósito de extraer las bandas de frecuencias alfa, beta, delta, etc. Dentro de las especificaciones, se consideró una frecuencia de corte de [] para el filtro pasa banda.


## 5. Resultados

**5.1. Análisis de Señales ECG:**
- Se analizaron las señales de electrocardiograma (ECG) con una frecuencia de muestreo de 1000 Hz. Utilizando Python, se extrajeron datos relevantes de la columna 6 de un archivo de texto. Estos datos, provenientes delvsistema biTalino, emplean una configuración bipolar para medir la diferencia amplificada entre dos puntos de medición.

- Los datos digitales se convirtieron a mV utilizando una fórmula basada en el voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits. Luego, las señales se filtraron para reducir el ruido y mejorar la visibilidad de los componentes cardíacos significativos. Se utilizaron dos tipos de filtros: un filtro IIR Butterworth de orden 5 y un filtro FIR con ventana de Hamming, ambos con una frecuencia de corte de 20 Hz.

| Campos          | Señal cruda | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Basal | <img src="señales/ecgBasal.png" alt="Ejercicio" style="width:400px;"> |<img src="señales/ecgBasalButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgBasalHamming.png" alt="Ejercicio" style="width:400px;">|
| Respiración     |<img src="señales/ecgRespiracion.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiracionButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiraciónHamming.png" alt="Ejercicio" style="width:400px;">|
| Post ejercicio  |<img src="señales/ecgEjercicio.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioHamming.png" alt="Ejercicio" style="width:400px;">|

**5.3. Análisis de Señales EEG:**
  - En este estudio se procesaron señales EEG registradas a una frecuencia de muestreo de 1000 Hz, empleando el dispositivo BiTalino junto con la disposición estándar de electrodos según el sistema internacional 10-20, y aplicando un método monopolar con dos electrodos posicionados en una región cerebral específica más un electrodo de referencia. Para la conversión de las señales a milivoltios, se utilizó una ecuación que considera un voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits, permitiendo una cuantificación precisa de la señal EEG. Posteriormente, para mejorar la calidad de las señales eliminando ruidos no deseados, se implementaron filtros digitales. Se aplicaron dos tipos de filtros: un filtro IIR Butterworth de orden 9 y un filtro FIR diseñado con una ventana de Hanning, el primero configurados con una frecuencia de corte de 35 Hz y el segundo se trabajó por separado para analizar las frecuencias de las ondas alfa y beta. Estos filtros fueron esenciales para atenuar componentes de alta frecuencia y ruidos, facilitando así una mejor interpretación y análisis de las señales EEG.


## 6. Discusión

**6.1. Análisis de Señales ECG:**
- Elección del Filtro y Configuración:
  - Filtro IIR Butterworth: Se eligió un filtro Butterworth de orden 5 con una frecuencia de corte de 20 Hz, basado en su capacidad para ofrecer una respuesta de frecuencia plana en la banda de paso, lo que es crucial para no alterar las características esenciales de la señal de ECG. Este diseño se apoya en el estudio de S. Basu y S. Mamud, donde se examina cómo la variación del orden y la frecuencia de corte afecta la eliminación de ruido en las señales de ECG [5].
  - Filtro FIR con Ventana de Hamming: La elección de la ventana de Hamming para el diseño del filtro FIR se basa en su efectividad en la reducción de ruido mientras mantiene la integridad de la señal. Según un estudio reciente por M. Das, R. Kumar, y B. Sahana, el uso de una función de ventana híbrida que incorpora la ventana de Hamming en filtros FIR demuestra una mejora significativa en la desruidización de señales ECG, proporcionando una solución eficaz para aplicaciones clínicas donde la claridad de la señal es crucial [6].
- Análisis de las Señales Filtradas:
  - Las señales filtradas mostraron una notable reducción del ruido de alta frecuencia y los artefactos, validando la elección del orden del filtro y la frecuencia de corte. Y.A. Altay y A.S. Kremlev discuten en su estudio cómo los filtros polinomiales, incluidos los basados en Butterworth, mejoran la precisión del procesamiento de la señal de ECG, respaldando nuestras observaciones sobre la efectividad de los filtros elegidos [7].

**6.3. Análisis de Señales EEG:**
- Elección del Filtro y Configuración:
  - Filtro FIR Hamming:
  - Filtro IIR Butterworth: Se seleccionó un filtro Butterworth IIR de orden 9 con una frecuencia de corte de 35 Hz para el procesamiento de señales EEG, basado en los picos identificados en el análisis espectral. Esta elección se fundamenta en datos de investigaciones anteriores y se alinea con los estudios realizados por Sabine L. y Sarang S., quienes recomendaron una frecuencia de corte entre 47 y 53 Hz, abarcando armónicos de hasta 500 Hz. En su investigación, utilizaron un filtro DFT calibrado a estos valores de frecuencia, logrando una eficacia notable en el filtrado de la señal [8]. Adicionalmente, considerando las bandas de frecuencia típicas en EEG, la elección de una frecuencia de corte de 35 Hz resulta adecuada para preservar las ondas alfa (8-12 Hz), beta (12-30 Hz) y theta (4-8 Hz), que son fundamentales en este estudio. Esto permite mantener la integridad de estas bandas esenciales, a la vez que se eliminan o atenúan las interferencias y ruidos de frecuencias más altas, asegurando así la calidad y la precisión de las señales EEG analizadas.


## 7. Conclusiones
- La inspección visual de las señales filtradas versus las señales crudas demostró claramente la efectividad de ambos tipos de filtros en la mejora de la calidad de la señal ECG. En particular, el filtro FIR, con sus características de fase lineal, mostró ser superior para aplicaciones donde la integridad de la fase es crucial.

 
## 8. Bibliografía
[1] B. Kuznetsov, J.D. Parker et al., "Differentiable IIR filters for machine learning applications," in Proceedings of the International Conference on Digital Audio Effects (DAFx), 2020. [Acceso en línea]: https://dafx2020.mdw.ac.at/proceedings/papers/DAFx2020_paper_52.pdf

[2] “What Are High-Pass Filters? How & When To Use Them (+ Tips),” Unison.audio, May 06, 2023. https://unison.audio/high-pass-filters/ (accessed May 04, 2024).

[3] D. Datta, H.S. Dutta, "High performance IIR filter implementation on FPGA," Journal of Electrical Systems and Information Technology, 2021. [Acceso en línea]: https://link.springer.com/article/10.1186/s43067-020-00025-4

[4] “Perform Analysis and Design for the Spectral Analysis Case Study - dummies,” Dummies.com, 2016. https://www.dummies.com/article/business-careers-money/careers/trades-tech-engineering-careers/perform-analysis-and-design-for-the-spectral-analysis-case-study-165562/ (accessed May 04, 2024).
‌
[5] S. Basu and Samiul Mamud, “Comparative Study on the Effect of Order and Cut off Frequency of Butterworth Low Pass Filter for Removal of Noise in ECG Signal,” Sep. 2020, doi: https://doi.org/10.1109/icce50343.2020.9290646.

[6] M. Das, R. Kumar, y B. Sahana, "Implementation of effective hybrid window function for ECG signal denoising," Traitement du Signal, vol. 37, no. 2, pp. 305-312, 2020. [En línea]. Disponible: https://www.researchgate.net/publication/340100534_Implementation_of_Effective_Hybrid_Window_Function_for_ECG_Signal_Denoising

[7] Y. A. Altay y A. S. Kremlev, "Polynomial filtering of low-and high-frequency noise for improving the accuracy of ECG signal processing: new advancements," Cardiometry, 2020. [En línea]. Disponible: https://www.researchgate.net/publication/343295169_Polynomial_filtering_of_low-_and_high-_frequency_noise_for_improving_the_accuracy_of_ECG_signal_processing_new_advancements

[8] Sabine , L. and Sarang, S.D. (2019) Reducing power line noise in EEG and MEG data via spectrum interpolation, Neuroimage, 2019 Apr 1. Disponible: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6456018/ (Accessed: 03 May 2024). 
