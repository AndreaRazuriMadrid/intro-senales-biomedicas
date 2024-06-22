## Tabla de Contenidos

1. [Link de repositorios ](#link-de-repositorios)
2. [Edge Impulse](#edge-impulse)
3. [Código](#código)

## Link de repositorios 
- (ECG): [https://studio.edgeimpulse.com/public/431031/live](https://studio.edgeimpulse.com/public/431135/live)
- (EMG): [https://studio.edgeimpulse.com/public/431132/live](https://studio.edgeimpulse.com/public/429753/live)
- (EEG): [https://studio.edgeimpulse.com/public/431133/live](https://studio.edgeimpulse.com/public/431461/live)
## Edge Impulse

### Señal ECG: 
| Señal ECG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Estado Basal                | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/ECG/basal.PNG)                                      |
| Durante Ejercicio           | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/ECG/ejercicio.PNG)                                 |

### Señal EEG: 
| Señal EEG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Estado de reposo            | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/EEG/reposo.PNG)                                   |
| Abrir y cerrar ojos         | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/EEG/abrirycerrar.PNG)                                              |

### Señal EMG: 
| Señal EMG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Flexion                     | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/EMG/flexion.PNG)                                      |
| Durante Extensión           | ![Imagen 15](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/archivos_Jaime/EMG/oposicin.PNG)                                 |


## Código

```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'api_key'
# Add the files you want to upload to Edge Impulse
files = [
    'C:/Users/trabajo/Downloads/lab_ei/reposo.csv',
    
]
# # Replace the label with your own.
label = 'reposo'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'applications/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
