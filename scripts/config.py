"""Credenziali e parametri di connessione per la caccia alla flag."""

EMAIL = "xxxxxxx@xxxxxxx.xxx"
PERSON_CODE = "xxxxxxxxxxx"

SERVER_HOST = "52.233.88.199"
HTTP_PORT = 80
TCP_PORT = 12100
UDP_PORT = 13000

HTTP_BASE = f"http://{SERVER_HOST}:{HTTP_PORT}"

AUTH_PAYLOAD = {
    "email": EMAIL,
    "person_code": PERSON_CODE,
}
