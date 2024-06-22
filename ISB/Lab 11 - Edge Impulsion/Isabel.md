

#### Link del repositorio 
- (ECG): https://studio.edgeimpulse.com/public/431031/live
- (EMG): https://studio.edgeimpulse.com/public/431132/live
- (EEG): https://studio.edgeimpulse.com/public/431133/live

#### Señal EEG: 
| Señal EEG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Estado de reposo            | ![Imagen 15](EI%20-%20Isabel/EEG_Reposo.png)                                   |
| Preguntas de Matemática     | ![Imagen 15](EI%20-%20Isabel/EEG_Preguntas.png)                                         |
| Abrir y cerrar ojos         | ![Imagen 15](EI%20-%20Isabel/EEG_AbrirYCerrar.png)                                              |

#### Señal ECG: 
| Señal ECG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Estado Basal                | ![Imagen 15](EI%20-%20Isabel/ECG_EstadoBasal.png)                                      |
| Durante Ejercicio           | ![Imagen 15](EI%20-%20Isabel/ECG_DuranteEjercicio.png)                                 |
| Aguantando la Respiración     | ![Imagen 15](EI%20-%20Isabel/ECG_AguantarRespiracion.png)                               |

#### Señal EMG: 
| Señal EMG                   | Imagen                                                                                 |
|-----------------------------|----------------------------------------------------------------------------------------|
| Estado Basal                | ![Imagen 15](EI%20-%20Isabel/EMG_Reposo.png)                                      |
| Durante Extensión           | ![Imagen 15](EI%20-%20Isabel/EMG_Extension.png)                                 |
| Durante Extensión           | ![Imagen 15](EI%20-%20Isabel/EMG_Extension.png)                                 |
| Durante Oposición al movimiento     | ![Imagen 15](EI%20-%20Isabel/EMG_Oposicion.png)                               |

### Código EMG

```python
import requests
import os

api_key = 'ei_fdf44f1d476773aee6952540823535e7ce38d0d5e78a60de6f73165928ff836c'
# Add the files you want to upload to Edge Impulse
files = [
    'C:/Users/Joja/Documents/Reposo1.csv'
]
# # Replace the label with your own.
label = 'EMG'

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