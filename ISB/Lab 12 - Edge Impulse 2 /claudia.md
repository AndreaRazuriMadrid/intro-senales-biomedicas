### EEG

```markdown
### Código para EEG - TRAINING

```python

import pandas as pd
import requests
import os
from io import StringIO

# Nueva API key
api_key = 'ei_bb18942ac6d4b5d8a5f040aa1ff1f0cdc6b9575a5f6a45c0b86c1c9d0c503957'

csv_files = [
    r'C:\Users\claro\Downloads\pandas_emg\Part_1_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_2_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_3_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_4_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_5_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_6_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_7_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_8_of_EMG_oposicion.csv',
]

label = 'emg_signal'

# Función para subir un solo archivo a Edge Impulse
def upload_file_from_dataframe(dataframe, label, api_key, file_name):
    try:
        # Convertir el DataFrame a CSV en memoria
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Realizar la solicitud para subir el archivo
        res = requests.post(
            url='https://ingestion.edgeimpulse.com/api/training/files',
            headers={
                'x-label': label,
                'x-api-key': api_key,
            },
            files={
                'data': (file_name, csv_buffer, 'text/csv')
            }
        )
        
        if res.status_code == 200:
            print(f'Successfully uploaded {file_name}\n', res.status_code, res.content)
        else:
            print(f'Failed to upload {file_name}\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_name}: {e}')

for file_path in csv_files:
    df = pd.read_csv(file_path)
    file_name = os.path.basename(file_path)
    upload_file_from_dataframe(df, label, api_key, file_name)

```
```markdown
### Código para EEG - TESTEO

```python
## TESTEO
import pandas as pd
import requests
import os
from io import StringIO

# Nueva API key
api_key = 'ei_bb18942ac6d4b5d8a5f040aa1ff1f0cdc6b9575a5f6a45c0b86c1c9d0c503957'

# Rutas de los archivos de pandas para la sección de test
test_csv_files = [
    r'C:\Users\claro\Downloads\pandas_emg\Part_9_of_EMG_oposicion.csv',
    r'C:\Users\claro\Downloads\pandas_emg\Part_10_of_EMG_oposicion.csv',
]

# Etiqueta para los datos de test
test_label = 'emg_signal_test'

# Función para subir un solo archivo a Edge Impulse
def upload_file_from_dataframe(dataframe, label, api_key, file_name):
    try:
        # Convertir el DataFrame a CSV en memoria
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Realizar la solicitud para subir el archivo
        res = requests.post(
            url='https://ingestion.edgeimpulse.com/api/testing/files',
            headers={
                'x-label': label,
                'x-api-key': api_key,
            },
            files={
                'data': (file_name, csv_buffer, 'text/csv')
            }
        )
        
        if res.status_code == 200:
            print(f'Successfully uploaded {file_name}\n', res.status_code, res.content)
        else:
            print(f'Failed to upload {file_name}\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_name}: {e}')

# Leer cada archivo CSV en un DataFrame y subirlo
for file_path in test_csv_files:
    df = pd.read_csv(file_path)
    file_name = os.path.basename(file_path)
    upload_file_from_dataframe(df, test_label, api_key, file_name)

```
#### Link del repositorio: https://studio.edgeimpulse.com/public/435749/live

#### Señal de Oposición - Training 

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2012%20-%20Edge%20Impulse%202%20/Archivos_Claudia/EMG_training_oposicion.jpg)

#### Señal de Oposición - Test 

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2012%20-%20Edge%20Impulse%202%20/Archivos_Claudia/EMG_test_oposicion.jpg)

