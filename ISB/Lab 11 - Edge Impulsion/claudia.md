![image](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/127904104/270d22c1-0778-4482-81c5-72f0febf65da)![image](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/127904104/7eaaf719-88a1-405a-b313-5dce4dc9076b)![image](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/127904104/4022425f-4d1f-4bd9-bb99-35ca7342a3e7)![image](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/127904104/b88afcee-1f58-4c0a-af75-20ead6bf0066)### EEG

```markdown
### Código para EEG

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import requests
from scipy.io import loadmat
import csv
import os
import re
import json
import time, hmac, hashlib
import requests

input_csv_file_path = 'C:\\Users\\claro\\Downloads\\eeg_señal_intro\\EEG_REPOSO.csv'
output_csv_file_path = input_csv_file_path.replace('.csv', '_converted.csv')

with open(input_csv_file_path, 'r') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
    reader = csv.reader(input_csv_file, delimiter=';')
    writer = csv.writer(output_csv_file, delimiter=',')
    
    for row in reader:
        writer.writerow(row)

print(f'Archivo convertido y guardado en {output_csv_file_path}')

api_key = 'ei_b1e23dd418efa92456f8bcf1c9644d5d1c0918be2c4a6e7475e143964b2f6a0c'

csv_files = [
    'C:\\Users\\claro\\Downloads\\eeg_señal_intro\\EEG_REPOSO.csv',
]

# Reemplaza la etiqueta con la tuya propia.
label = 'eeg_signal'

# Función para subir un solo archivo a Edge Impulse
def upload_file(file_path, label, api_key):
    try:
        with open(file_path, 'rb') as f:
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files={
                    'data': (os.path.basename(file_path), f, 'text/csv')
                }
            )
        
        if res.status_code == 200:
            print(f'Successfully uploaded {file_path}\n', res.status_code, res.content)
        else:
            print(f'Failed to upload {file_path}\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_path}: {e}')

# Subir cada archivo de la lista
for file_path in csv_files:
    upload_file(file_path, label, api_key)
```

#### Link del repositorio: https://studio.edgeimpulse.com/public/431463/live

#### Señal de Ojo abriendo y Cerrandose

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EEG/EEG_OJO_CERRADO_ABIERTO.jpg?raw=true)

#### Señal de Ojo en reposo

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EEG/EEG_REPOSO.jpg?raw=true)

### EMG

```markdown
### Código para EMG

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import requests
from scipy.io import loadmat
import csv
import os
import re
import json
import time, hmac, hashlib
import requests

input_csv_file_path = 'C:\\Users\\claro\\Downloads\\emg_señal_intro\\EMG_reposo.csv'
output_csv_file_path = input_csv_file_path.replace('.csv', '_converted.csv')

with open(input_csv_file_path, 'r') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
    reader = csv.reader(input_csv_file, delimiter=';')
    writer = csv.writer(output_csv_file, delimiter=',')
    
    for row in reader:
        writer.writerow(row)

print(f'Archivo convertido y guardado en {output_csv_file_path}')

api_key = 'ei_d16c4a35cd824ba4c98f320f7231787c3a42fea93cecd06ffc1d5fbf29f41284'

csv_files = [
    'C:\\Users\\claro\\Downloads\\emg_señal_intro\\EMG_extension.csv',
    'C:\\Users\\claro\\Downloads\\emg_señal_intro\\EMG_flexion.csv',
    'C:\\Users\\claro\\Downloads\\emg_señal_intro\\EMG_oposicion.csv',
    'C:\\Users\\claro\\Downloads\\emg_señal_intro\\EMG_reposo.csv',

]

# Reemplaza la etiqueta con la tuya propia.
label = 'ecg_signal'

# Función para subir un solo archivo a Edge Impulse
def upload_file(file_path, label, api_key):
    try:
        with open(file_path, 'rb') as f:
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files={
                    'data': (os.path.basename(file_path), f, 'text/csv')
                }
            )
        
        if res.status_code == 200:
            print(f'Successfully uploaded {file_path}\n', res.status_code, res.content)
        else:
            print(f'Failed to upload {file_path}\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_path}: {e}')

# Subir cada archivo de la lista
for file_path in csv_files:
    upload_file(file_path, label, api_key)
```
#### Link del repositorio: https://studio.edgeimpulse.com/public/431483/live

#### Señal EMG en extensión

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EMG/EMG_extension.jpg?raw=true)

#### Señal EMG en flexión

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EMG/EMG_flexion.jpg?raw=true)

#### Señal EMG en oposición

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EMG/EMG_oposicion.jpg?raw=true)

#### Señal EMG en reposo

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/EMG/EMG_reposo.jpg?raw=true)


### ECG

```
```markdown
### Código para EMG

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import requests
from scipy.io import loadmat
import csv
import os
import re
import json
import time, hmac, hashlib
import requests

input_csv_file_path = 'C:\\Users\\claro\\Downloads\\dataset_intro\\ECG_Sentadillas.csv'
output_csv_file_path = input_csv_file_path.replace('.csv', '_converted.csv')

with open(input_csv_file_path, 'r') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
    reader = csv.reader(input_csv_file, delimiter=';')
    writer = csv.writer(output_csv_file, delimiter=',')
    
    for row in reader:
        writer.writerow(row)

print(f'Archivo convertido y guardado en {output_csv_file_path}')

api_key = 'ei_4b80dd93f009370d0dc3d2f882cd36ebf22decdf0e75320943d417674ba5d390'

csv_files = [
    'C:\\Users\\claro\\Downloads\\dataset_intro\\ECG_despuesdeactividad.csv',
    'C:\\Users\\claro\\Downloads\\dataset_intro\\ECG_hiperventilación.csv',
    'C:\\Users\\claro\\Downloads\\dataset_intro\\ECG_reposo.csv',
    'C:\\Users\\claro\\Downloads\\dataset_intro\\ECG_Sentadillas.csv',

]

# Reemplaza la etiqueta con la tuya propia.
label = 'ecg_signal'

# Función para subir un solo archivo a Edge Impulse
def upload_file(file_path, label, api_key):
    try:
        with open(file_path, 'rb') as f:
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files={
                    'data': (os.path.basename(file_path), f, 'text/csv')
                }
            )
        
        if res.status_code == 200:
            print(f'Successfully uploaded {file_path}\n', res.status_code, res.content)
        else:
            print(f'Failed to upload {file_path}\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_path}: {e}')

# Subir cada archivo de la lista
for file_path in csv_files:
    upload_file(file_path, label, api_key)
```
#### Link del repositorio: https://studio.edgeimpulse.com/public/431483/live

#### Señal ECG de Reposo

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/ECG/ECG_REPOSO.jpg?raw=true)

#### Señal ECG de Sentadillas

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/ECG/ECG_SENTADILLAS.jpg?raw=true)

#### Señal ECG de Hiperventilación

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/ECG/ECG_hiperventilaci%C3%B3n.jpg?raw=true)

#### Señal ECG después de Actividad 

![Descripción de la Imagen](https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/blob/main/ISB/Lab%2011%20-%20Edge%20Impulsion/Archivos_Claudia/ECG/ECG_despuesdeactividad.jpg?raw=true)
