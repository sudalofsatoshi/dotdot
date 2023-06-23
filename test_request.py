import requests
import json

url = 'http://localhost:8000/generate'  # Replace with your Flask app's URL

# JSON payload for the POST request
# Read data from file.json
with open('input_data.json', 'r') as f:
    f = json.load(f)

# Convert the data to JSON format
json_data = json.dumps(f)

# Set the request headers
headers = {'Content-Type': 'application/json'}

# Make the POST request
response = requests.post(url, data=json_data, headers=headers)
print (response)