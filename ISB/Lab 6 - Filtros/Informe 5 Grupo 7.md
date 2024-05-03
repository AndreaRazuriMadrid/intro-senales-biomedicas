# INFORME LABORATORIO 6
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


## 1. INTRODUCCIÓN 


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

</div>


## 4. Metodología



## 5. Resultados

**5.1. Análisis de Señales ECG:**
- Se analizaron las señales de electrocardiograma (ECG) con una frecuencia de muestreo de 1000 Hz. Utilizando Python, se extrajeron datos relevantes de la columna 6 de un archivo de texto. Estos datos, provenientes de un sistema de adquisición similar al biTalino, emplean una configuración bipolar para medir la diferencia amplificada entre dos puntos de medición.

- Los datos digitales se convirtieron a mV utilizando una fórmula basada en el voltaje de referencia (VCC) de 3.3V y una resolución de 10 bits. Luego, las señales se filtraron para reducir el ruido y mejorar la visibilidad de los componentes cardíacos significativos. Se utilizaron dos tipos de filtros: un filtro IIR Butterworth de orden 5 y un filtro FIR con ventana de Hamming, ambos con una frecuencia de corte de 20 Hz.

| Campos          | Señal cruda | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Basal | <img src="señales/ecgBasal.png" alt="Ejercicio" style="width:400px;"> |<img src="señales/ecgBasalButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgBasalHamming.png" alt="Ejercicio" style="width:400px;">|
| Respiración     |<img src="señales/ecgRespiracion.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiracionButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiraciónHamming.png" alt="Ejercicio" style="width:400px;">|
| Post ejercicio  |<img src="señales/ecgEjercicio.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioHamming.png" alt="Ejercicio" style="width:400px;">|






## 6. Discusión

**6.1. Análisis de Señales ECG:**
- asd

## 7. Conclusiones
- La inspección visual de las señales filtradas versus las señales crudas demostró claramente la efectividad de ambos tipos de filtros en la mejora de la calidad de la señal ECG. En particular, el filtro FIR, con sus características de fase lineal, mostró ser superior para aplicaciones donde la integridad de la fase es crucial.

 
## 8. Bibliografía
[1] 
