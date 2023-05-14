import requests
import json

status = 'available'
info = {"id": 0, "category": {"id": 0, "name": "string"}, "name": "doggie", "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
new_info = {"id": 0, "category": {"id": 0, "name": "string"}, "name": "doggieRS", "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"}
id = 9223372036854775807

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                   headers={'accept': 'application/json'})

res = requests.post(f"https://petstore.swagger.io/v2/pet",
                    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=json.dumps(info, ensure_ascii=False))

res = requests.delete(f"https://petstore.swagger.io/v2/pet/id={id}", headers={'accept': 'application/json'})

res = requests.put(f"https://petstore.swagger.io/v2/pet",
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                   data=json.dumps(new_info, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
