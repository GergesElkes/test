import requests

api_key = '12345abcdAPIkey67890'
response = requests.get(f'https://api.example.com/data?key={api_key}')
print(response.json())
