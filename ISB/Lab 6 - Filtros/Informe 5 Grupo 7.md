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
  - Siguiendo la guía "BITalino (r)evolution Lab Guide" se consideró la polarización de los electrodos enfocándonos en la configuración bipolar. Se situó el electrodo negativo (negro) en la parte derecha de la frente, mientras que el electrodo positivo (rojo) se colocó en la parte izquierda de la frente. Adicionalmente, el electrodo de referencia (blanco) se posicionó en una área neutra, específicamente en el hueso detrás de la oreja **[4]**.
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

Para la adquisición de la señal se utilizó 16 canales; sin embargo para el ploteo solo se está graficando 13 de estos. Se utilizó una ganancia de 1 para la adquisición.


 <p align="center">
    <img src="resultados/ultracortex.png" alt="ultracortex" style="width:510px;">
</p>

## 6. Discusión
- 

## 7. Conclusiones
- 

 
## 8. Bibliografía
[1] 
