from requests_futures.sessions import FuturesSession
import json
import csv

url = "https://8c8jirboi0.execute-api.eu-west-1.amazonaws.com/prod/"

headers = {
    'Content-Type': 'application/json'
}


def create_payload(row: list) -> str:
    return json.dumps({
        "model": "mul-en",
        "inputs": row[1]
    })

with FuturesSession() as session:
    with open('lug.csv') as sentences_file:
        reader = csv.reader(sentences_file, delimiter=',')
        payloads = map(create_payload, reader)
        futures = list(map(
            lambda payload: session.post(url, headers=headers, data=payload),
            payloads
        ))
        
        for future in futures:
            print(future.result().json()[0]["generated_text"])
