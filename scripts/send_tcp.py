from socket import *
import json
import config

HOST = config.SERVER_HOST
PORT = config.TCP_PORT

CODE = "0o8nocpqme"

# payload JSON coerente con gli step precedenti
payload = config.AUTH_PAYLOAD.copy()
payload["msg_code"] = CODE

message = (json.dumps(payload) + "\n").encode("utf-8")


s = socket(AF_INET, SOCK_STREAM)
s.settimeout(10)

try:
    s.connect((HOST, PORT))
    print("[#] Connesso al server TCP")

    print("[>] Invio:", message.decode().strip())
    s.sendall(message)

    response = b""
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk
    except timeout:
        pass

    print("[<] Risposta server:")
    print(response.decode(errors="replace"))

except Exception as e:
    print("[!] Errore:", e)

finally:
    s.close()
    print("[#] Connessione chiusa")