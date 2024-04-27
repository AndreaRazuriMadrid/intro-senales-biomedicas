# INFORME LABORATORIO 5
## Lista de Participantes - Grupo 7

- Andrea Razuri Madrid
- Isabel Leon Luna
- Johanni Bohorquez Gutierrez
- Claudia Camacho Grimaldi
- Jaime Arista Cutipa 

## Tabla de Contenidos

1. [INTRODUCCIÓN A LA ELECTROENCEFALOGRAFÍA (EEG)](#1-introducción-a-la-electroencefalografía-eeg)
2. [Objetivos](#2-objetivos)
3. [Materiales y equipos](#3-materiales-y-equipos)
4. [Metodología](#4-metodología)
5. [Resultados](#5-resultados)
6. [Discusión](#6-discusión)
7. [Conclusiones](#7-conclusiones)
8. [Bibliografía](#8-bibliografía)


## 1. INTRODUCCIÓN A LA ELECTROENCEFALOGRAFÍA (EEG)

La electroencefalografía (EEG) es una técnica utilizada para registrar la actividad eléctrica del cerebro. Se realiza mediante la colocación de electrodos en el cuero cabelludo, los cuales detectan las señales eléctricas generadas por las neuronas cerebrales. Estas señales se representan en forma de ondas en un gráfico, permitiendo a los médicos estudiar la actividad cerebral del paciente​ [1].

**Contexto**

- El EEG fue desarrollado inicialmente por Hans Berger en 1924, quien registró la primera actividad eléctrica cerebral humana. Desde entonces, la EEG ha evolucionado significativamente en términos de la tecnología utilizada para capturar y analizar datos, así como su aplicación en diferentes campos médicos y de investigación [2].

**¿Cómo funciona el cerebro?**

- El cerebro está activo todo el tiempo, incluso durante el sueño. Esta actividad se manifiesta como ondas cerebrales que varían en frecuencia y amplitud, dependiendo del estado de conciencia y actividad del individuo. Las ondas alfa (8–13 Hz) son comunes en estados de relajación con los ojos cerrados, mientras que las ondas beta (13–30 Hz) son típicas en estados de alerta o actividad mental intensa. Otras ondas como las delta (0.5–4 Hz) y theta (4–7 Hz) son más comunes durante el sueño o en condiciones anormales​ [1].

**Aplicaciones del EEG**

- El EEG se utiliza ampliamente para diagnosticar y monitorear trastornos neurológicos como la epilepsia, trastornos del sueño y encefalopatías. Además, es útil para evaluar la profundidad de la anestesia, el coma y la posible muerte cerebral. También se emplea para investigar la actividad cerebral en estudios de ciencias cognitivas y psicológicas, mediante técnicas derivadas como los potenciales evocados y las respuestas relacionadas con eventos [1].

**Técnica y metodología**

- La colocación de los electrodos sigue un sistema estándar denominado "Sistema Internacional 10-20", que asegura una cobertura uniforme del cuero cabelludo para capturar la actividad eléctrica en diversas regiones cerebrales. Los electrodos captan señales eléctricas, que son luego amplificadas y registradas para su análisis. Las señales se categorizan en diversas bandas de frecuencia, como alfa, beta, delta y theta, cada una asociada con diferentes estados de conciencia y actividad neuronal​ [1].

<p align="center">
  <img src="videos_imagenes/Intro.jpeg" alt="Señales" style="width:430px;">
  <br>
  <strong>Fig.1. Adquisición de señal EEG [3]</strong>
</p>


## 2. Objetivos
- Obtener señales biomédicas de electroencefalografía (EEG).
- Configurar adecuadamente el dispositivo BiTalino.
- Extraer datos de las señales EEG utilizando el software OpenSignals (r)evolution.


## 3. Materiales y equipos

<div align="center">

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| (R)EVOLUTION  | Kit BITalino  | 1        |
|      -      |Electrodos con gel| 3|
|       -       | Laptop o PC   | 1        |
| OpenBCI |Ultracortex Mark IV EEG Headset |1|
| OpenBCI | OpenBCI Cyton 8-channel Board |1|
</div>


## 4. Metodología

- **Empleo de OpenSignals**: El software diseñado para la visualización de la señales del BITalino.

   <p align="center">
    <img src="videos_imagenes/Opensignals.jpeg" alt="Opensignals" style="width:320px;">
    <img src="videos_imagenes/MenúOS.jpeg" alt="MenúOS" style="width:300px;">
</p>


- **Uso de BITalino**: El dispositivo cuenta con un procesador ATMEGA328P, y funciona de manera inalámbrica gracias a su módulo Bluetooth.

 <p align="center">
    <img src="videos_imagenes/bitalino1.jpeg" alt="bitalino1" style="width:310px;">
    <img src="videos_imagenes/bitalino2.jpeg" alt="bitalino2" style="width:320px;">
</p>
  
- **Posición de los electrodos**:
  - Se consideró la polarización de los electrodos enfocándonos en la configuración bipolar. Se situó el electrodo negativo (negro) en la parte derecha de la frente, mientras que el electrodo positivo (rojo) se colocó en la parte izquierda de la frente. Adicionalmente, el electrodo de referencia (blanco) se posicionó en una área neutra, específicamente en el hueso detrás de la oreja **[4]**.
<p align="center">
  <img src="videos_imagenes/PosicionElectrodos.jpeg" alt="Señales" style="width:430px;">
  <br>
  <strong>Fig.2. Posición de los electrodos para la adquisición de las señales EEG [4]</strong>
</p>

<p align="center">
  <img src="videos_imagenes/P1.png" alt="Opensignals" style="width:300px;">  <img src="videos_imagenes\P2.png"alt="MenúOS" style="width:300px;">
  <br>
  <strong>Fig 3. Posicionamiento de los electrodos en el sujeto de prueba.</strong>
</p>

- **Procedimiento de registro EEG**:
  
| Etapa                 | Indicaciones                                                                                                       | Toma             |
|-----------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|
| Reposo (30 segundos)  | Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos. |<video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/82d554cf-76bf-4a84-bcb8-3286cde2dcd5" width="80%" height="80%"></video> |
| Abrir y cerrar ojos   | Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.       | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/8a0fa139-4ad7-46d0-9675-700ebbd0c155" width="50%" height="50%"></video> |
| Reposo (30 segundos)  | Registre otra fase de referencia de 30 segundos                                                              | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/ad29e4ad-b436-4184-9fb4-75859c0570c3" width="50%" height="50%"></video> |
| Preguntas matemáticas  | Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos (*) y resuelve cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos. | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/e48396e2-c8de-45c2-9273-54a04c8cb4a1" width="50%" height="50%"></video> |

**(*) Preguntas Realizadas:**

| Tipo de Pregunta           | Pregunta                                                                                           | Respuesta |
|----------------------------|---------------------------------------------------------------------------------------------------|-----------|
| Simples                    | Hay 3 pájaros en un árbol; llegan 7 más. ¿Cuántos pájaros hay ahora?                              | 10        |
|                            | Jonas tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tiene en total?                            | 9         |
|                            | Hanna tiene 9 dólares pero gasta 4. ¿Cuántos dólares le quedan?                                     | 5         |
| Complejas                  | Juan anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que Juan y José juntos. ¿Cuántos puntos anotaron en total? | 113       |


- **ULTRACORTEX**:
  
<div align="center">
 
| Etapa                 | Toma               |
|-----------------------|--------------------|
| Reposo (30 segundos)  | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/3dab45b9-6547-4d54-873f-d5b4080d903e" width="50%" height="50%"></video>                   |
| Abrir y cerrar ojos   | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/bd46b3f8-b6a9-45f1-b235-2544335b8c86" width="50%" height="50%"></video>                   |
| Reposo (30 segundos)  | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/420e8521-14c6-4189-82ad-57cb3a3a3ba6" width="50%" height="50%"></video>                   |
| Preguntas matemáticas |      <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/af04d08f-13e7-4b78-80a5-cb012320e098" width="50%" height="50%"></video>              |
</div>


## 5. Resultados

**Ploteo de la señal en Python**

Se usó una frecuencia de muestreo del bitalino de 1000Hz. Se usó el canal 8 para extraer la información de los archivos txt obtenidas del OpenSignal. El biTalino utiliza una configuración bipolar, en donde señal medida es la diferencia amplificada entre las dos señales de medición que se filtra por paso de banda por 0.8-48 Hz para eliminar señales no deseadas y una alta ganancia de amplificación de 41782, lo que lo hace sensible a artefactos como la luz y los movimientos.


| Etapa                 | Toma               |
|-----------------------|--------------------|
| Reposo 1 (30 segundos)  | <img src="resultados/reposo1.png" alt="reposo1" style="width:600px;">|
| Abrir y cerrar ojos   | <img src="resultados/Ojos.png" alt="reposo1" style="width:600px;"> |
| Reposo (30 segundos)  | <img src="resultados/reposo2.png" alt="reposo1" style="width:600px;">  |
| Preguntas matemáticas | <img src="resultados/matemática.png" alt="reposo1" style="width:600px;">  |


**Ploteo de FFT**

| Etapa                 | Toma               |
|-----------------------|--------------------|
| Reposo 1 (30 segundos)  | <img src="resultados/reposo1FFT.png" alt="reposo1" style="width:500px;">|
| Abrir y cerrar ojos entre 22-27 segundos | <img src="resultados/fftOJOS22_27seg.png" alt="reposo1" style="width:500px;"> |
| Abrir y cerrar ojos entre 27-32 segundos  | <img src="resultados/fftOJOS27_32seg.png" alt="reposo1" style="width:500px;">  |
| Preguntas matemáticas fáciles | <img src="resultados/fftMATEfacil.png" alt="reposo1" style="width:500px;">  |
| Preguntas matemáticas difíciles | <img src="resultados/fftMATEdif.png" alt="reposo1" style="width:500px;">  |


**Ploteo de la señal en Python - Ultracortex**

Para la adquisición de la señal se utilizó 16 canales; sin embargo para el ploteo solo se está graficando 13 de estos.


 <p align="center">
    <img src="resultados/ultracortex.png" alt="ultracortex" style="width:510px;">
</p>

## 6. Discusión
En nuestras pruebas usando el sensor eeg del bitalino, el arreglo utilizado en la frente nos permite leer la señal de lóbulo frontal del cerebro, se hizo siguiendo el sistema internacional 10-20, y se utilizó el método monopolar (dos electrodos en una área del cerebro y un electrodo de referencia). 
<p align="center">
  <img src="videos_imagenes/PosicionElectrodos.jpeg" alt="Señales" style="width:430px;">
  <br>
  <strong>Fig.4. Electrodos +/- se colocan en las posiciones azul y roja, y  la referencia detras de la oreja  [4]</strong>
</p>

- En la medición en Reposo 1, se observa un aumento de amplitud de hasta 1.5mV. Sin embargo, esto puede deberse a factores de ruido o al movimiento involuntario de los ojos. Una medida más precisa se encuentra entre los 28 a 40s, en donde la amplitud es alrededor de 1 mV aproximadamente, esto sugiere que la actividad eléctrica cerebral es más estable en ese intervalo de tiempo y que la amplitud medida allí es más confiable. Por otro lado, durante la medición de en reposo se pueden ver las ondas alfa de baja frecuencia pero contiene muchos artefactos y ruido. Con el análisis de frecuencia podemos ver que el ruido continua en las otras pruebas, haciendo más difícil poder leer la información. Este ruido se puede deber al posicionamiento de los electrodos y su referencia, además de que el sujeto se encontraba cerca de 2 laptops y tenía una joya de acero.

- En la medición de abrir y cerrar los ojos se observa los 5 ciclos realizados. Cuando se abren los ojos se obtiene una amplitud de hasta 1.5 mV, pero cuando se cierran los ojos se muestra una amplitud alrededor de 1 mV, lo cual es consistente con la activación cortical asociada con la percepción visual y el procesamiento de la información visual entrante **[5]**. Este ciclo de repetición se da por ejemplo entre 12 a 22s. Se podría considerar que se está encontrando ondas alfa, debido a que en este ejercicio la persona se encuentra en un estado mentalmente relajado pero despierto **[6]**. Además, de acuerdo a las gráficas de FFT, podemos observar que las ondas alfa (entre 8-13Hz) tienen actividad en cada ciclo.
  
-  En la medición de preguntas matemáticas, se observan picos con una amplitud mayor a 1.5 mV cuando se razona la pregunta formulada. Para el caso de las preguntas con mayor dificultad, se observa una señal con una mayor generación de picos de 1.5 mV, debido a que el cerebro realiza un mayor esfuerzo. Se podría considerar que se está visualizando onda beta, debido a que se está implicando actividades mentales que demandan mayor velocidad de transmisión **[6]**. Esto se puede confirmar con las gráficas de FFT obtenidas en los resultados, ya que se observa actividad alrededor de los 30Hz.


- Para el reconocimiento de señales en el Ultra Cortex, se toma en cuenta la posición de los electrodos según el International 10-20 system en el cuero cabelludo, el cual consta de la distancia total entre el frente y la parte posterior, así como de derecha a izquierda. El 10 y 20 describen las distancias entre cada electrodo adyacente en porcentaje. Cada posición tiene una letra y un número que describen la ubicación en el lóbulo (frontal, temporal, central y occipital), en donde los número impares se refiere a la izquierda y los número pares a la derecha.

<p align="center">
  <img src="videos_imagenes/Fig5.png" alt="Señales" style="width:430px;">
  <br>
  <strong>Figura 5: Vista superior de un cabezal con posicionamiento de electrodos según el sistema internacional 10-20.[4]</strong>
</p>

- En el caso de la prueba con el ultra cortex se debe tener en cuenta que no se logró una buena toma de la señal, se pudo deber a diferentes factores como no haber logrado una buena conexión con el cuero cabelludo, los electrodos se encontraban algo secos, todo esto causó que a pesar de nuestros intentos no se pudiera recolectar una señal útil. 
Esto se puede deber a una falta de experiencia de los usuarios tanto nosotros como las personas que lo probaron antes que nosotros.


## 7. Conclusiones
- En la medición en Reposo 1 y 2, se observa la adquisición de ruido en la señal al inicio, debido a interferencias por estar cerca a 2 laptops y tener un collar metálico durante la prueba.
- En la medición de abrir y cerrar los ojos, se obtuvieron 5 ciclos de repetición durante la prueba. Se muestra que al abrir los ojos se obtuvo una amplitud mayor de 1.5mV, y al cerrar los ojos se obtiene una medición de 1 mV.
- En la medición de preguntas matemáticas, se visualiza onda beta por el gráfico de FFT de la señal, en donde el rango de frecuencias es entre 12 a 30 Hz. Aquí se obtuvieron picos constantes con una amplitud mayor a 1.5mV, dependiendo de la complejidad de las preguntas.

 
## 8. Bibliografía
[1] "Mayo Clinic Staff, 'EEG (electroencephalogram) - Mayo Clinic,' Mayo Clinic, [Online]. Available: https://www.mayoclinic.org/tests-procedures/eeg/about/pac-20393875. [Accessed: 27-04-2024].

[2] Mark Freedman, 'Electroencefalografía (EEG) - Manual Merck versión para profesionales,' Merck Manuals, [Online]. Available: https://www.merckmanuals.com/es-us/professional/trastornos-neurol%C3%B3gicos/pruebas-y-procedimientos-neurol%C3%B3gicos/electroencefalograf%C3%ADa-eeg. [Accessed: 27-04-2024].

[3] L. J. Gomez Figueroa, "Título del trabajo de maestría," Tesis de Maestría, Nombre de la Universidad, Ciudad, País, año. [Online]. Available: https://oa.upm.es/44379/1/TFM_LEONARDO_JOSE_GOMEZ_FIGUEROA.pdf. [Accessed: 27-04-2024]

[4] “BITalino (r)evolution Lab Guide.” Accessed: Apr. 26, 2024. [Online]. Available: https://www.bitalino.com/storage/uploads/media/homeguide3-eeg.pdf

[5] Gómez, L.J. (2016) Departamento de Automática, Ingeniería Eléctrica y Electrónica e Informática Industrial. Available at: https://oa.upm.es/44379/1/TFM_LEONARDO_JOSE_GOMEZ_FIGUEROA.pdf (Accessed: 26 April 2024).  

[6] Ramos, R. (2020) Análisis de espectrogramas de señales EEG, Facultad de Ciencias de la Computación. Available at: https://repositorioinstitucional.buap.mx/server/api/core/bitstreams/92e27f78-4f9d-4d2e-9d69-9f90cd87c0b1/content (Accessed: 26 April 2024). 

