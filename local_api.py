#import json

import requests

BASE_URL = "http://127.0.0.1:8000"

get_response = requests.get(BASE_URL, timeout=10)
print("GET status code:", get_response.status_code)
print("GET response:", get_response.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

post_response = requests.post(
    f"{BASE_URL}/data/",
    json=data,
    timeout=10,
)
print("POST status code:", post_response.status_code)
print("POST response:", post_response.json())