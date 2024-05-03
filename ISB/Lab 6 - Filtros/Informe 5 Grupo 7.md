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
| OpenBCI |Ultracortex Mark IV EEG Headset |1|
| OpenBCI | OpenBCI Cyton 8-channel Board |1|
</div>


## 4. Metodología



## 5. Resultados

**ECG:**

Se usó una frecuencia de muestreo del bitalino de 1000Hz. Se usó el canal 8 para extraer la información de los archivos txt obtenidas del OpenSignal. El biTalino utiliza una configuración bipolar, en donde señal medida es la diferencia amplificada entre las dos señales de medición que se filtra por paso de banda por 0.8-48 Hz para eliminar señales no deseadas y una alta ganancia de amplificación de 41782, lo que lo hace sensible a artefactos como la luz y los movimientos.

| Campos          | Señal cruda | Filtro IIR | Filtro FIR |
|-----------------|-------------|------------|------------|
| Basal | <img src="señales/ecgBasal.png" alt="Ejercicio" style="width:400px;"> |<img src="señales/ecgBasalButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgBasalHamming.png" alt="Ejercicio" style="width:400px;">|
| Respiración     |<img src="señales/ecgRespiracion.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiracionButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgRespiraciónHamming.png" alt="Ejercicio" style="width:400px;">|
| Post ejercicio  |<img src="señales/ecgEjercicio.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioButter.png" alt="Ejercicio" style="width:400px;">|<img src="señales/ecgEjercicioHamming.png" alt="Ejercicio" style="width:400px;">|






## 6. Discusión
- 

## 7. Conclusiones
- 

 
## 8. Bibliografía
[1] 
