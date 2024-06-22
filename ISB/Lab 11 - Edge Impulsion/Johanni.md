# Repossitorio Edge Impulse - Johanni

## Tabla de Contenidos

1. [Repositorio EMG](#1-RepositorioEMG)
2. [Repositorio ECG](#2-ReositorioECG)
3. [Repositorio EEG](#3-RepositorioEEG)


<img src="ArchivosJohanni/Proyectos.png"> 


## 1. Repositorio EMG

### 1.1 Código

```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_7c1bc6149d3e9151a694c1064b9bab7d7f5f5013e600c9b2fa63bedd51f67224'
# Add the files you want to upload to Edge Impulse
files = [
    'Flexion.csv',
]
# # Replace the label with your own.
label = 'EMG-Flexion'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'aplication/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)

```

### 1.2 Señales


| Señal   | Imagen                                                                                         |
|-------------|------------------------------------------------------------------------------------------------|
| Extensión   | <img src="ArchivosJohanni/EMG/Extensión.png" alt="Ejercicio" style="width:1000px; height:500px;">|
| Flexión     | <img src="ArchivosJohanni/EMG/Flexión.png" alt="Ejercicio" style="width:1000px; height:500px;">  |
| Oposición   | <img src="ArchivosJohanni/EMG/Oposición.png" alt="Ejercicio" style="width:1000px; height:500px;">|


## 2. Repositorio ECG

### 2.1 Código


### 2.2 Señales


## 3. Repositorio EEG

### 3.1 Código


### 3.2 Señales
