import requests

url = 'http://127.0.0.1:5000/process'
payload = {'key1': 'value1', 'key2': 'value2'}  # Replace with your data

response = requests.post(url, json=payload)  # Send the POST request

if response.status_code == 200:
    print("Request successful! Response content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
