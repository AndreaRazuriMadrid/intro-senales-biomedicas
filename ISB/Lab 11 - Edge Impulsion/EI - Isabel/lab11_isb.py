# Install requests via: `pip3 install requests`
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