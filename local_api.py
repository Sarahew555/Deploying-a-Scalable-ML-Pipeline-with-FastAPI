import json

import requests

url = http://127.0.0.1:8000
r = requests.get(url=url)

# TODO: print the status code
print(f'Status Code: {r.status_code}')
# TODO: print the welcome message
print(f'Results: {r.json()}')



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

# TODO: send a POST using the data above
r = requests.post(url=url+"/data/", json=data) # Your code here

# TODO: print the status code
 print(f'Status Code: {r.status_code}')
# TODO: print the result
print(f'Results: {r.json()}')
