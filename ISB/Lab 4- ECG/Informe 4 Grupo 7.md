# INFORME LABORATORIO 4
## Lista de Participantes - Grupo 7

- Andrea Razuri Madrid
- Isabel Leon Luna
- Johanni Bohorquez Gutierrez
- Claudia Camacho Grimaldi
- Jaime Arista Cutipa 

## Tabla de Contenidos

1. [Introducción a la Electrocardiografía (ECG)](#1-introducción-a-la-electrocardiografía-ecg)
2. [Objetivos](#2-objetivos)
3. [Materiales y Equipos](#3-materiales-y-equipos)
4. [Características de los Sujetos de Prueba](#4-características-de-los-sujetos-de-prueba)
5. [Metodología](#5-metodología)
   - [Empleo de OpenSignals](#empleo-de-opensignals)
   - [Uso de BITalino](#uso-de-bitalino)
   - [Posición de los Electrodos](#posición-de-los-electrodos)
   - [Sujeto 1- Jaime](#sujeto-1--jaime)
      - [Estado Basal](#estado-basal)
      - [Respiración Prolongada](#respiración-prolongada) 
      - [Ejercicio Intenso](#ejercicio-intenso) 
   - [Pro-sim](#pro-sim)
6. [Resultados](#6-resultados)
   - [Jaime](#jaime)
     - [Estado Basal](#estado-basal-1)
     - [Respiración Prolongada](#respiración-prolongada-1)
     - [Ejercicio Intenso](#ejercicio-intenso-1)
   - [Pro-sim](#pro-sim-1)
7. [Discusión](#7-discusión)
8. [Conclusiones](#8-conclusiones)
9. [Bibliografía](#9-bibliografía)



## 1. INTRODUCCIÓN A LA ELECTROCARDIOGRAFÍA (ECG)

La electrocardiografía (ECG) es una técnica esencial en el campo de la medicina que nos permite evaluar la actividad eléctrica del corazón de manera no invasiva. En nuestro laboratorio, empleamos electrodos para capturar y analizar estas señales eléctricas, proporcionando información vital sobre la salud cardiovascular de los pacientes.

### ¿Qué es un Electrocardiograma?

La ECG es un procedimiento que registra la actividad eléctrica del corazón a través de electrodos colocados en la piel. Estos registros ayudan a detectar irregularidades cardíacas, monitorizar la salud del corazón y diagnosticar diversas condiciones médicas. El corazón genera impulsos eléctricos que se propagan a través del tejido cardíaco y se detectan en la superficie de la piel. Cada latido produce un patrón característico en el electrocardiograma, que puede ser  analizado para evaluar el estado del corazón [1].

### ¿Cómo funciona el corazón?

El corazón es un órgano muscular que funciona como una bomba, enviando sangre oxigenada a todo el cuerpo y retornando la sangre desoxigenada en los pulmones para su oxigenación. La actividad eléctrica del corazón se inicia en el nodo sinoauricular, que actúa como marcapasos natural del corazón, y se propaga a través de las cámaras cardíacas, lo que resulta en su contracción y relajación rítmicas [1]. 

### Aplicaciones del ECG

El ECG es fundamental para detectar arritmias, infartos de miocardio, y otras condiciones patológicas del corazón. Además, es utilizado en chequeos rutinarios, en pruebas de esfuerzo o para monitorizar los efectos de ciertos medicamentos en el corazón. También puede proporcionar información sobre la variabilidad del ritmo cardíaco (HRV), que es un indicador importante de la salud cardiovascular y la respuesta autonómica del cuerpo [1].

### Decepción de la Señal de ECG

El electrocardiograma es una representación gráfica de la actividad eléctrica del corazón medida en el tiempo. Cada ciclo cardíaco produce una serie de ondas en el ECG que corresponden a diferentes fases de actividad cardíaca. A continuación, se describen los componentes principales de la señal de ECG:

<p align="center">
  <img src="videos_imagenes/senales.jpeg" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig 1. Señal ECG con diferentes intervalos que la componen [2]</strong>
</p>

   - **Onda P:** Representa la despolarización de las aurículas, es decir, el proceso eléctrico que precede a la contracción auricular. Esta onda es la primera deflexión positiva del ECG y es crucial para reevaluar la función auricular.
   - **Complejo QRS:** Sigue a la onda P y representa la despolarización de los ventrículos, que es el proceso eléctrico que precede a la contracción ventricular, la cual es responsable de bombear la sangre hacia los pulmones y el resto del cuerpo. Este complejo está compuesto por tres partes:
     - Onda Q: Primera deflexión negativa después de P
     - Onda R: Deflexión positiva prominente
     - Onda S: Deflexión negativa de después de la onda R
   - **Intervalo PR:** Es el período desde el inicio de la onda P hasta el inicio del complejo QRS. Este intervalo refleja el tiempo que el impulso eléctrico tarda en viajar desde las aurículas hasta los ventrículos. 
   - **Segmento ST:** Es el segmento desde el final complejo QRS hasta el inicio de la onda T. Este segmento es crucial para evaluar si hay un suministro de sangre adecuado al corazón o si existe alguna lesión miocárdica.
   - **Onda T:** Representa la repolarización ventricular, o el proceso de recuperación eléctrica que prepara a los ventrículos para el siguiente ciclo de contracción.
   - **Intervalo QT:** Es el tiempo desde el inicio del complejo QRS hasta el final de la onda T. Este intervalo es un indicador importante del estado de repolarización de los ventrículos y es ajustado según la frecuencia cardíaca.



## 2. Objetivos
- Obtener señales biomédicas de electrocardiografía (ECG).
- Configurar adecuadamente el dispositivo BiTalino.
- Extraer datos de las señales ECG utilizando el software OpenSignals (r)evolution.

## 3. Materiales y equipos

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| (R)EVOLUTION  | Kit BITalino  | 1        |
|       -       | Laptop o PC   | 1        |

## 4. Características de los sujetos de prueba

| Nombre  | Edad | Sexo | Frec. act. física | Intensidad act. | Condición Física | IMC  |
|---------|------|------|-------------------|-----------------|------------------|------|
| Jaime   | 23   | M    | 3                 | Media           | Sano             | 30.6 |

## 5. Metodología

- **Empleo de OpenSignals**: El software diseñado para la visualización de la señales del BITalino.

<img src="videos_imagenes/Opensignals.jpeg" alt="Opensignals" style="width:455px;">  <img src="videos_imagenes/MenúOS.jpeg" alt="MenúOS" style="width:430px;">

- **Uso de BITalino**: El dispositivo cuenta con un procesador ATMEGA328P, y funciona de manera inalámbrica gracias a su módulo Bluetooth.
<img src="videos_imagenes/bitalino1.jpeg" alt="bitalino1" style="width:440px;"> <img src="videos_imagenes/bitalino2.jpeg" alt="bitalino2" style="width:450px;">


- **Posición de los electrodos**:
  - Se consideró la polarización de los electrodos al enfocarnos en la primera derivación bipolar.
  - Se colocó el electrodo negativo en el brazo derecho, el electrodo positivo en el brazo izquierdo, y el electrodo de referencia cerca a la cresta ilíaca.
<p align="center">
  <img src="videos_imagenes/PosicionElectrodos .jpeg" alt="Señales" style="width:440px;">
  <br>
  <strong>Fig.2. Posición de los electrodos para la adquisición de las señales ECG [3]</strong>
</p>

<p align="center">
  <img src="videos_imagenes/PosElec.jpeg" alt="Señales" style="width:350px;">
  <br>
  <strong>Fig 3. Posicionamiento de los electrodos en el sujeto de prueba.</strong>
</p>

- **Sujeto 1- Jaime**:
  - Estado Basal
    - En la primera prueba se tomó la señal en reposo, los electrodos se colocaron en los antebrazos con un punto de referencia en la cresta ilíaca.

      [![](https://markdown-videos-api.jorgenkh.no/youtube/QS-2v3W504M )](https://youtu.be/QS-2v3W504M)

  - Respiración prolongada
    - La segunda prueba se realizó conteniendo la respiración por 30 segundos. La persona se encontraba sentada.
      - Jaime - Aguantar respiración (durante)

        [![](https://markdown-videos-api.jorgenkh.no/youtube/z_PpKdiaDY4 )](https://youtu.be/z_PpKdiaDY4)

      - Jaime - Aguantar respiración (después)

        [![](https://markdown-videos-api.jorgenkh.no/youtube/dTZBowwIjXA )](https://youtu.be/dTZBowwIjXA)

  - Haciendo ejercicio
    - En la tercera prueba se realizaron ejercicios aeróbicos durante 1 minuto para tomar las señales por el BiTalino.

      [![](https://markdown-videos-api.jorgenkh.no/youtube/Ik_4EM_qOgc )](https://youtu.be/Ik_4EM_qOgc)

- **Pro-sim**:
  ## Simulación de Pruebas Cardíacas

| Paso | Descripción | Foto | Enlace al Video |
|------|-------------|------|-----------------|
| 2 | Onda CVP (Contracciones ventriculares prematuras) | <img src="videos_imagenes/Paso2-CVP.jpeg" alt="Paso2-CVP" style="width:200px;"> |[![](https://markdown-videos-api.jorgenkh.no/youtube/29PwQj-pjZU)](https://www.youtube.com/watch?v=29PwQj-pjZU&ab_channel=ANDREARAZURIMADRID) |
| 3 | Taquicardia ventricular 160 lpm | <img src="videos_imagenes/Paso3-TaqVent.jpeg" alt="Paso3" style="width:200px;"> |[![](https://markdown-videos-api.jorgenkh.no/youtube/cv6lpsEO8ZQ)](https://youtu.be/cv6lpsEO8ZQ) |
| 4 | Fibrilación ventricular severa | <img src="videos_imagenes/Paso4-FibVent.jpeg" alt="Paso4" style="width:200px;">| [![](https://markdown-videos-api.jorgenkh.no/youtube/9j0LWFMWJuM )](https://youtu.be/9j0LWFMWJuM)  |
| 5 | Asistolia |<img src="videos_imagenes/Paso5-Asistolia.jpeg" alt="Paso5-Asistolia" style="width:200px;"> |  [![](https://markdown-videos-api.jorgenkh.no/youtube/bHxz2DLPJss)](https://youtu.be/bHxz2DLPJss) |

## 6. Resultados

En la gráfica de electromiografía (EMG), se optó por centrar el enfoque en el intervalo de tiempo de 6 a 7 segundos. Este ajuste se realizó para ampliar la imagen de la gráfica durante este periodo crítico, permitiendo una visualización detallada y clara de los datos. Este enfoque específico ayuda a analizar con mayor precisión las fluctuaciones y características de la señal EMG, facilitando así una interpretación más precisa de la actividad muscular registrada.

### Sujeto 1-Jaime

- Estado basal
- Respiración prolongada
  - Durante
  - Después
- Ejercicio intenso

### Pro sim
- Paso 2: Onda CVP (Contracciones ventriculares prematuras)
- Paso 3: Taquicardia ventricular 160 lpm
- Paso 4: Fibrilación ventricular severa
- Paso 5: Asistolia
  
## 7. Discusión
- El uso de métodos de reconocimiento de patrones para el análisis de señales ECG, el dispositivo BiTalino utiliza la configuración de Einthoven para evaluar diferentes estados de ritmos cardíacos y a una frecuencia de sampleo de 1000 Hz para su correcta conversión de ADC. Para el proceso de filtrado de la señal se suele utilizar un filtro Butterworth de paso de banda con frecuencias de corte de 10 y 450 Hz, la rectificación de la señal y la aplicación de otro filtro Butterworth de paso bajo con frecuencias de corte de 4 Hz, en donde estas mediciones cumplen con los Golden Standard [6]. 


## 8. Conclusiones
- Para la toma de muestras de señales ECG con el BiTalino, consiste en la amplificación de señales eléctricas detectadas por los electrodos, para su posterior conversión a señal digital. Con la obtención de estas señales podemos estudiar y analizar patrones en la formación de ondas de ECG por medio de su frecuencia en el tiempo y su amplitud en milivoltios.
- Durante la medición del estado basal, se obtuvo una amplitud máxima de 0.6 mV dentro del complejo QRS y con un intervalo R-R de 0.75 que equivalen a 80 latidos por minuto, lo cual está dentro de los rangos normales para señales ecg en reposo. Podemos observar que la amplitud del complejo QRS nos muestra la despolarización ventricular junto a la magnitud de la señal eléctrica generada por cada contracción [5]. 
- En la segunda medición, durante respiración prolongada, obtenemos un aumento en la amplitud de 0.8 mV dentro del complejo QRS y con un intervalo R-R de 0.83 que equivale a 72 latidos por minuto. Se muestra la disminución en la frecuencia cardíaca y en los intervalos R-R por el aumento progresivo del flujo sanguíneo.
- En la tercera medición, obtuvimos una amplitud de 0.8 mV dentro del complejo QRS y un intervalo R-R de 0.55, lo que implica 109 latidos por minuto. Cuando se ha realizado ejercicio por un minuto, se aumentó la frecuencia cardíaca lo que nos resulta en la disminución del intervalo R-R, ya que el organismo necesita suministrar más oxígeno y nutrientes por medio del sistema nervioso autónomo.
- Se debe considerar que las señales obtenidas están sujetas a interferencias y ruidos provocados por contacto de los electrodos. Por lo que, se deberá aplicar un filtro para la eliminación parcial o total de estas interferencias para la correcta detección de patrones o anomalías en las señales EKG [5]. 



## 9. Bibliografía
[1] M. Proença y K. Mrotzeck, "BITalino (r)evolution Lab Guide," PLUX – Wireless Biosignals, S.A., Lisboa, Portugal, OD.LB.03.04, 15 de febrero de 2021.  
[2] “(PDF) Avances en el Desarrollo de un Sistema de Espirometría con correlación ECGAR para la Detección Temprana de Enfermedades Cardiorrespiratorias,” ResearchGate, 2018. https://www.researchgate.net/publication/328080878_Avances_en_el_Desarrollo_de_un_Sistema_de_Espirometria_con_correlacion_ECGAR_para_la_Deteccion_Temprana_de_Enfermedades_Cardiorrespiratorias/figures (accessed Apr. 19, 2024).  
[3] BITalino (r)evolution Lab Guide. (2021, 15 de febrero). BITalino.  
https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf  
‌[4] PROCESAMIENTO DE SEÑALES DE ELECTROMIOGRAFÍA SUPERFICIAL PARA LA DETECCIÓN DE MOVIMIENTO DE DOS DEDOS DE LA MANO. (2012). UNIVERSIDAD RICARDO PALMA. https://repositorio.urp.edu.pe/bitstream/handle/20.500.14138/416/Alva_ca.pdf?sequence=1&isAllowed=y  
[5] Lorenzo Romero, J. (2015). Análisis De Señales Electrocardiográficas Usando Técnicas De Procesamiento Digital. Ingeniería Técnica De Telecomunicación. https://openaccess.uoc.edu/bitstream/10609/40186/6/jlorenzoroTFC0115memoria.pdf  
[6] Batista, D., Silva, H., & Fred, A. (2017). Experimental Characterization and Analysis of the BITalino Platforms Against a Reference Device. Instituto de Telecomunicações, Instituto Superior Técnico. https://pubmed.ncbi.nlm.nih.gov/29060386/

