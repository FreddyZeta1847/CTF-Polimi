from socket import *
import threading
import json
import config

HOST = config.SERVER_HOST
PORT = config.TCP_PORT

CODE = "xxxxxxx"

N_CLIENTS = xx
TIMEOUT = 15.0

# Payload JSON costruito da config
payload_dict = config.AUTH_PAYLOAD.copy()
payload_dict["msg_code"] = CODE

payload = (json.dumps(payload_dict) + "\n").encode("utf-8")


def send_payload(client_id):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.settimeout(TIMEOUT)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[#] Client {client_id} connected")

        print(f"[>] Client {client_id} sending: {payload.decode().strip()}")

        client_socket.sendall(payload)

        response = client_socket.recv(4096).decode("utf-8", errors="replace")
        print(f"[<] Client {client_id}: {response}")

    except Exception as e:
        print(f"[!] Client {client_id} ERROR: {e}")

    finally:
        client_socket.close()
        print(f"[#] Client {client_id} closed")


threads = []

for i in range(N_CLIENTS):
    t = threading.Thread(target=send_payload, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()