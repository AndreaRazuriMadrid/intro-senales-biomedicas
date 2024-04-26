# INFORME LABORATORIO 5
## Lista de Participantes - Grupo 7

- Andrea Razuri Madrid
- Isabel Leon Luna
- Johanni Bohorquez Gutierrez
- Claudia Camacho Grimaldi
- Jaime Arista Cutipa 

## Tabla de Contenidos

- 


## 1. INTRODUCCIÓN A LA  (EEG)



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
  - Se consideró la polarización de los electrodos enfocándonos en la configuración bipolar. Se situó el electrodo negativo (negro) en la parte derecha de la frente, mientras que el electrodo positivo (rojo) se colocó en la parte izquierda de la frente. Adicionalmente, el electrodo de referencia (blanco) se posicionó en una área neutra, específicamente en el hueso detrás de la oreja [3].
<p align="center">
  <img src="videos_imagenes/PosicionElectrodos.jpeg" alt="Señales" style="width:430px;">
  <br>
  <strong>Fig.2. Posición de los electrodos para la adquisición de las señales EEG [3]</strong>
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
| Preguntas matemáticas | Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos y resuelve cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos. | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/e48396e2-c8de-45c2-9273-54a04c8cb4a1" width="50%" height="50%"></video> |













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

| Etapa                 | Toma               |
|-----------------------|--------------------|
| Reposo 1 (30 segundos)  | <<img src="resultados/reposo1.png" alt="reposo1" style="width:400px;">|
| Abrir y cerrar ojos   | <<img src="resultados/Ojos.png" alt="reposo1" style="width:400px;"> |
| Reposo (30 segundos)  | <<img src="resultados/reposo2.png" alt="reposo1" style="width:400px;">  |
| Preguntas matemáticas | <<img src="resultados/matemática.png" alt="reposo1" style="width:400px;">  |




## 6. Discusión
- 

## 7. Conclusiones
- 



## 9. Bibliografía
[1] 
