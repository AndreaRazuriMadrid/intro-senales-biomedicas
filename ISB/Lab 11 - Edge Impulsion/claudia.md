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
