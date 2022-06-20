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

luganda_translation = response.json()[0]["generated_text"]

print(f"Luganda translation: {luganda_translation}")

payload = json.dumps({
    "model": "mul-en",
    "inputs": "Oli otya?"
})

response = requests.request("POST", url, headers=headers, data=payload)
english_translation = response.json()[0]["generated_text"]

print(f"English translation: {english_translation}")
