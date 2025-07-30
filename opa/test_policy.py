import requests
import json

url = "http://localhost:8181/v1/data/pipeline/allow"
headers = {"Content-Type": "application/json"}

data = {
    "input": {
        "role": "admin",
        "branch": "main"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print("Decision:", response.json())
