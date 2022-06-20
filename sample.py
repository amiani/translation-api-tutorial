import requests
import json


url = "https://8c8jirboi0.execute-api.eu-west-1.amazonaws.com/prod/"

payload = json.dumps({
    "model": "en-mul",
    "inputs": ">>lug<<How are you?"
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)  # this will print out [{"generated_text":"Oli otya?"}]

payload = json.dumps({
    "model": "mul-en",
    "inputs": "Oli otya?"
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)  # [{"generated_text":"How are you?"}]
