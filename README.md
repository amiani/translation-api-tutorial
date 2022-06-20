# Translation API tutorial/documentation
This repository shows how to use the Sunbird AI translation API endpoint.

## Running the sample file
To run the sample file you'll need python 3 installed. Then follow these steps:
- Clone this repository
- cd into this directory `cd translation-api-tutorial`
- Create a virtual environment and activate it: `python -m venv venv` `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Run the the sample file: `python sample.py`
- The output of this command should be:

```
Luganda translation: Oli otya?
English translation: How are you?
```


## What's the Sunbird AI translation endpoint?
The API endpoint provides an interface to the language translation model.

You can use it to translate from English to any of the 5 languages below and vice-versa:

|Language|Code|
|--------|----|
|Acholi|ach|
|Ateso|teo|
|Luganda|lug|
|Lugbara|lgg|
|Runyankole|nyn|

## Functionality
The API URL is:
```
https://8c8jirboi0.execute-api.eu-west-1.amazonaws.com/prod/
```

It's a post endpoint and you can make 2 types of queries to it:
- English to Multiple `en-mul`: Translate from English to a local language.
- Multiple to English `mul-en`: Translate from a local language to English.

**Note**: A local language here means one of the five languages above.

### English to Multiple query:
The format of the "English to Multiple" JSON query is as follows:
```
{
    "model": "en-mul",
    "inputs": ">>lang_code<<How are you?"
}
```

Replace `lang_code` with the language code for the language you're interested in. (refer above for the language codes).

**Params**
- `model`: use this to specify the model you want to use. For this query, use `en-mul` which means "English to Multiple"
- `inputs`: A string that starts with `>>lang_code<<` to represent the target language; along with the English text you want to translate.

**Example**

cURL:
```
curl --location --request POST 'https://8c8jirboi0.execute-api.eu-west-1.amazonaws.com/prod/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "en-mul",
    "inputs": ">>lug<<Hello?"
}'
```

See `sample.py` in this directory for a python example.

### Multiple to English query:
The format for the "Multiple to English" JSON query is as follows:
```
{
    "model": "mul-en",
    "inputs": "Oli otya?"
}
```

**Params**
- `model`: use this to specify the model you want to use. For this query, use `mul-en` which means "Multiple to English"
- `inputs`: A string with the local language text you want to translate. (Note that you don't have to specify the language).

**cURL**:
```
curl --location --request POST 'https://8c8jirboi0.execute-api.eu-west-1.amazonaws.com/prod/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "mul-en",
    "inputs": "Oli otya?"
}'
```

### Output format
Output is a JSON string in the following format: (The `generated_text` field contains the translation):
```
[
    {
        "generated_text": "How are you?"
    }
]
```

**Note**: The output is a **list**, which contains an **object** with a **field** `generated_text`. See the `sample.py` file to see how to extract the translated text.
