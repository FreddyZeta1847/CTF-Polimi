import requests
import config

url = "http://52.233.88.199:80/atajn/f9cc2/o55gb"

params = {
    "email": config.EMAIL,
    "person_code": config.PERSON_CODE,
    "msg_code": "xxxxxxxxx"
}

try:
    r = requests.get(url, params=params, timeout=10)
    print("Status:", r.status_code)
    print(r.text)
except Exception as e:
    print("Errore:", e)